import requests
import json
import time

from urllib import parse
from var_types_busan import InitialStoreData, busan_list, category_list, base_search_key_list, brand_search_key_list, etc_search_key_list

filename = './storeInfo_by_crawling_busan.csv'

file = open(filename, 'w', encoding='utf-8')
file.write("search_key" + "●" + "category" + "●" + "naver_category"
	+ "●" + "store_name" + "●" + "address"
	+ "●" + "tel" + "●" + "telDisplay" + "●" + "virtualTel" + "●" + "virtualTelDisplay" + "●" + "phone"
	+ "●" + "latitude" + "●" + "longitude" 
	+ "●" + "operation_time"
	# + "●" + "description"
	+ "\n")

baseHeader = "headers={'cookie':'NNB=D6ZCMSTPJKFGI; NSCS=2; NV_WETR_LAST_ACCESS_RGN_M=\"MTQxMzAxMTY=\"; NV_WETR_LOCATION_RGN_M=\"MTQxMzAxMTY=\"; page_uid=i4wOEwp0JywssLdwm0Kssssstyl-291495; nx_ssl=2; page_uid=1944ade3-f33a-4c5d-96dd-c6c56f2927b5', 'Cache-Control': 'max-age=0', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}, allow_redirects=False"

baseUrl="https://map.naver.com/v5/api/search"
baseOption="?caller=pcweb&type=all&isPlaceRecommendationReplace=true&lang=ko"
baseQuery="&query="
basePage="&page="
baseDisplayCount="&displayCount="

baseDetailUrl="https://map.naver.com/v5/api/sites/summary/"
baseDetailOption="?lang=ko"

search_location_list = busan_list
# search_location_list = gyeonggi_list
whole_search_key = base_search_key_list + brand_search_key_list + etc_search_key_list

result_id_list = []

def get_category(search_key: str):
	returnValue = ''

	if search_key == '코인세탁소':
		returnValue = '셀프빨래방'
	
	elif search_key not in category_list:
		returnValue = '기타'
  
	else:
		find_category = category_list.index(search_key)
		returnValue = category_list[find_category]

	if returnValue == '기타':
		if search_key in brand_search_key_list:
			returnValue = '브랜드'
		elif search_key in etc_search_key_list:
			returnValue = '그외 기타'

	return returnValue

for location in search_location_list:
	for search_key in whole_search_key:
		schKeyword = location + " " + search_key

		query = baseQuery + parse.quote(schKeyword)
		url = baseUrl + baseOption + query + basePage + "1" + baseDisplayCount + "100"
		
		print(url)
		response = requests.get(url, headers={'cookie':'NNB=ZBZP6NYKLBVWG; page_uid=icQB2sprvh8ssvLxUMhssssssQw-187203; page_uid=59d6ffc8-d8ca-438b-adc5-b096e055a950', 'Cache-Control': 'no-cache', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}, allow_redirects=False)
		
		time.sleep(1)
		
		print(response, schKeyword)
		# print(response.text)

		try:
			resultStr = response.text
			resultJson = json.loads(resultStr)
		except Exception as inst:
			print(type(inst))
			print(inst.args)
			print(inst)
			continue
			
		# print(type(resultJson))
		
		if resultJson.get("result").get("place") is not None:
			totalCount = resultJson["result"]["place"]["totalCount"]
			divResult = divmod(int(totalCount), 100)
			totalPage = divResult[0] + 1
			restCount = divResult[1]
			
			print("totalCount= ", totalCount, ", totalPage= ", str(totalPage), ", restCount= ", str(restCount))

			i = 1
			while i <= totalPage:
				print("currentPage= ", str(i))

				if i > 1:
					displayCount = 100
					if i == totalPage:
						displayCount = restCount

					url = baseUrl + baseOption + query + basePage + str(i) + baseDisplayCount + str(displayCount)
		
					# print(url)
					response = requests.get(url, headers={'cookie':'NNB=ZBZP6NYKLBVWG; page_uid=icQB2sprvh8ssvLxUMhssssssQw-187203; page_uid=59d6ffc8-d8ca-438b-adc5-b096e055a950', 'Cache-Control': 'no-cache', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}, allow_redirects=False)
					time.sleep(1)

					resultStr = response.text

					try:
						resultJson = json.loads(resultStr)
					except Exception as inst:
						i += 1
						print('url : ' + url)
						print(inst)
						continue

				if resultJson.get("result") is not None:
					
					for resultList in resultJson["result"]["place"]["list"]:
						if resultList["id"] in result_id_list:
							# print('exist ID : ', resultList["id"])
							exist = 'exist'

						else:
							result_id_list.append(resultList["id"])

							row_data = InitialStoreData(resultList["name"], resultList["address"], resultList["tel"], resultList["telDisplay"], resultList["virtualTel"], resultList["virtualTelDisplay"], resultList["tel"], resultList["bizhourInfo"], "", "")
							# print("resultList['name'] : ", resultList["name"])
							file.write(search_key + "●" + get_category(search_key) + "●" + row_data.naver_category
								+ "●" + row_data.store_name
								+ "●" + row_data.address
								+ "●" + row_data.tel + "●" + row_data.telDisplay + "●" + row_data.virtualTel + "●" + row_data.virtualTelDisplay + "●" + row_data.phone
								+ "●" + resultList["y"] + "●" + resultList["x"]
								+ "●" + row_data.operation_time
								# + "●" + " "
								+ "\n")

							# detailUrl = baseDetailUrl + resultList["id"] + baseDetailOption
							# detailResponse = requests.get(detailUrl, headers={'cookie':'NNB=D6ZCMSTPJKFGI; NSCS=2; NV_WETR_LAST_ACCESS_RGN_M="MTQxMzAxMTY="; NV_WETR_LOCATION_RGN_M="MTQxMzAxMTY="; page_uid=i4wOEwp0JywssLdwm0Kssssstyl-291495; nx_ssl=2; page_uid=1944ade3-f33a-4c5d-96dd-c6c56f2927b5', 'Cache-Control': 'no-cache', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}, allow_redirects=False)

							# detailResultStr = detailResponse.text

							# if "Moved" in detailResultStr:
							# 	time.sleep(1)
							# 	detailResponse = requests.get(detailUrl, headers={'cookie':'NNB=D6ZCMSTPJKFGI; NSCS=2; NV_WETR_LAST_ACCESS_RGN_M="MTQxMzAxMTY="; NV_WETR_LOCATION_RGN_M="MTQxMzAxMTY="; page_uid=i4wOEwp0JywssLdwm0Kssssstyl-291495; nx_ssl=2; page_uid=1944ade3-f33a-4c5d-96dd-c6c56f2927b5', 'Cache-Control': 'no-cache', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}, allow_redirects=False)
							# 	detailResultStr = detailResponse.text

							# if "Moved" in detailResultStr:
							# 	time.sleep(1)
							# 	detailResponse = requests.get(detailUrl, headers={'cookie':'NNB=D6ZCMSTPJKFGI; NSCS=2; NV_WETR_LAST_ACCESS_RGN_M="MTQxMzAxMTY="; NV_WETR_LOCATION_RGN_M="MTQxMzAxMTY="; page_uid=i4wOEwp0JywssLdwm0Kssssstyl-291495; nx_ssl=2; page_uid=1944ade3-f33a-4c5d-96dd-c6c56f2927b5', 'Cache-Control': 'no-cache', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}, allow_redirects=False)
							# 	detailResultStr = detailResponse.text

							# if "Moved" in detailResultStr:
							# 	time.sleep(1)
							# 	detailResponse = requests.get(detailUrl, headers={'cookie':'NNB=D6ZCMSTPJKFGI; NSCS=2; NV_WETR_LAST_ACCESS_RGN_M="MTQxMzAxMTY="; NV_WETR_LOCATION_RGN_M="MTQxMzAxMTY="; page_uid=i4wOEwp0JywssLdwm0Kssssstyl-291495; nx_ssl=2; page_uid=1944ade3-f33a-4c5d-96dd-c6c56f2927b5', 'Cache-Control': 'no-cache', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}, allow_redirects=False)
							# 	detailResultStr = detailResponse.text

							# if "Moved" in detailResultStr:
							# 	row_data = InitialStoreData(resultList["name"], resultList["address"], resultList["tel"], resultList["telDisplay"], resultList["virtualTel"], resultList["virtualTelDisplay"], resultList["tel"], resultList["bizhourInfo"], "", "")
							# 	print("resultList['name'] : ", resultList["name"])
							# 	file.write(search_key + "●" + get_category(search_key) + "●" + row_data.naver_category
							# 		+ "●" + row_data.store_name
							# 		+ "●" + row_data.address
							# 		+ "●" + row_data.tel + "●" + row_data.telDisplay + "●" + row_data.virtualTel + "●" + row_data.virtualTelDisplay + "●" + row_data.phone
							# 		+ "●" + resultList["y"] + "●" + resultList["x"]
							# 		+ "●" + row_data.operation_time
							# 		# + "●" + " "
							# 		+ "\n")
							
							# else:
							# 	try:
							# 		detailResultJson = json.loads(detailResultStr)

							# 		# print(search_key + "●" + get_category(search_key) + "●" + resultList["name"])
							# 		# print("resultList[category].length", len(resultList["category"]), resultList["category"][len(resultList["category"])-1])
							# 		# , detailResultJson["fullRoadAddress"], resultList["virtualTelDisplay"], detailResultJson["bizhourInfo"], detailResultJson["description"], detailResultJson["category"])
							# 		# print(str(detailResultJson["y"]), str(detailResultJson["x"]))

							# 		if resultList.get("name") is not None:
							# 			name = resultList["name"]
							# 		else:
							# 			name = ""
										
							# 		if detailResultJson.get("address") is not None:
							# 			fullRoadAddress = detailResultJson["address"]
							# 		else:
							# 			fullRoadAddress = ""

							# 		if fullRoadAddress.strip() == "" and detailResultJson.get("fullAddress") is not None:
							# 			fullRoadAddress = detailResultJson["fullAddress"]

							# 		if resultList.get("tel") is not None:
							# 			tel = resultList["tel"]
							# 		else:
							# 			tel = ""

							# 		if resultList.get("telDisplay") is not None:
							# 			telDisplay = resultList["telDisplay"]
							# 		else:
							# 			telDisplay = ""

							# 		if resultList.get("virtualTel") is not None:
							# 			virtualTel = resultList["virtualTel"]
							# 		else:
							# 			virtualTel = ""

							# 		if resultList.get("virtualTelDisplay") is not None:
							# 			virtualTelDisplay = resultList["virtualTelDisplay"]
							# 		else:
							# 			virtualTelDisplay = ""

							# 		if detailResultJson.get("phone") is not None:
							# 			phone = detailResultJson["phone"]
							# 		else:
							# 			phone = ""

							# 		if detailResultJson.get("bizhourInfo") is not None:
							# 			bizhourInfo = detailResultJson["bizhourInfo"].replace("\t", "  ").replace("\n", "  ")
							# 		else:
							# 			bizhourInfo = ""

							# 		if detailResultJson.get("description") is not None:
							# 			description = detailResultJson["description"].replace("\t", "  ").replace("\n", "  ")
							# 		else:
							# 			description = ""

							# 		if detailResultJson.get("categories") is not None:
							# 			naver_category = detailResultJson["categories"][len(detailResultJson["categories"])-1]
							# 		else:
							# 			naver_category = ""
							# 		# naver_category = detailResultJson["category"]

							# 		if detailResultJson.get("y") is not None:
							# 			latitude = detailResultJson["y"]
							# 		else:
							# 			latitude = ""

							# 		if detailResultJson.get("x") is not None:
							# 			longitude = detailResultJson["x"]
							# 		else:
							# 			longitude = ""

							# 		row_data = InitialStoreData(name, fullRoadAddress, tel, telDisplay, virtualTel, virtualTelDisplay, phone, bizhourInfo, description, naver_category)
									
							# 		file.write(search_key + "●" + get_category(search_key) + "●" + row_data.naver_category
							# 			+ "●" + row_data.store_name
							# 			+ "●" + row_data.address
							# 			+ "●" + row_data.tel + "●" + row_data.telDisplay + "●" + row_data.virtualTel + "●" + row_data.virtualTelDisplay + "●" + row_data.phone
							# 			+ "●" + str(latitude) + "●" + str(longitude)
							# 			+ "●" + row_data.operation_time
							# 			# + "●" + " "
							# 			+ "\n")
									
							# 	except Exception as inst:
							# 		print('except : ' + detailUrl)
							# 		print('resultList["name"] : ' + resultList["name"])
							# 		print(type(inst))
							# 		print(inst.args)
							# 		print(inst)
							# 		continue

				else:
					i = totalPage

				i += 1
file.close() 			

# print('end of search --------')
# for result_id in result_id_list:
# 	print('result_id : ', result_id)