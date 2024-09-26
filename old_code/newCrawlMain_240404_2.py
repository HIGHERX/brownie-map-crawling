import requests
import json
import time

from datetime import datetime
from urllib import parse
from var_types_240404_2 import InitialStoreData, search_location_list, selflaundry_key_list

today_datetime = datetime.today().strftime("%Y%m%d%H%M%S")
today_date = datetime.today().strftime("%Y%m%d")
filename = './selflaundry_storeInfo_by_crawling_240404_'+ today_datetime + '.csv'

file = open(filename, 'w', encoding='utf-8')
file.write("location" + "●" + "search_key" + "●" + "category" + "●" + "naver_category"
	+ "●" + "store_name" + "●" + "address"
	+ "●" + "tel" + "●" + "telDisplay" + "●" + "virtualTel" + "●" + "virtualTelDisplay" + "●" + "phone"
	+ "●" + "latitude" + "●" + "longitude" 
	+ "●" + "operation_time"
	# + "●" + "description"
	+ "\n")

baseHeader = "headers={'cookie':'NNB=D6ZCMSTPJKFGI; NSCS=2; NV_WETR_LAST_ACCESS_RGN_M=\"MTQxMzAxMTY=\"; NV_WETR_LOCATION_RGN_M=\"MTQxMzAxMTY=\"; page_uid=i4wOEwp0JywssLdwm0Kssssstyl-291495; nx_ssl=2; page_uid=1944ade3-f33a-4c5d-96dd-c6c56f2927b5', 'Cache-Control': 'max-age=0', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}, allow_redirects=False"

baseUrl="https://map.naver.com/p/api/search/allSearch"
baseOption="?caller=pcweb&type=all&isPlaceRecommendationReplace=true&lang=ko"
baseOption2="?type=all&searchCoord=126.87787299999331%3B37.484281200002485&boundary="
baseQuery="&query="
basePage="&page="
baseDisplayCount="&displayCount="
countPerPage=20

baseDetailUrl="https://map.naver.com/v5/api/sites/summary/"
baseDetailOption="?lang=ko"

# search_location_list = busan_list
# search_location_list = gyeonggi_list
whole_search_key = selflaundry_key_list
# whole_search_key = photoshop_key_list

result_id_list = []

def get_category(search_key: str):
	returnValue = ''

	# if search_key in icecream_key_list:
	# 	returnValue = '아이스크림 할인점'
	
	# elif search_key in photoshop_key_list:
	# 	returnValue = '무인사진관'

	# elif search_key in selflaundry_key_list:
	# 	returnValue = '셀프빨래방'

	# elif search_key in studycafe_key_list:
	# 	returnValue = '스터디카페'

	# elif search_key in convenience_key_list:
	# 	returnValue = '무인편의점'

	# elif search_key in ramen_key_list:
	# 	returnValue = '무인라면'

	# elif search_key in cafe_key_list:
	# 	returnValue = '무인카페'

	# elif search_key in stationary_key_list:
	# 	returnValue = '무인문방구'

	# elif search_key in petshop_key_list:
	# 	returnValue = '무인펫샵'

	# elif search_key in fruit_key_list:
	# 	returnValue = '무인과일'

	# elif search_key in print_key_list:
	# 	returnValue = '무인프린트'

	# elif search_key in etc_search_key_list:
	# 	returnValue = '기타브랜드'

	# else:
	# 	returnValue = '??'

	returnValue = '셀프빨래방'

	return returnValue

for location in search_location_list:
	for search_key in whole_search_key:
		schKeyword = location + "+" + search_key

		query = baseQuery + parse.quote(schKeyword)
		# url = baseUrl + baseOption + query + basePage + "1" + baseDisplayCount + "100"
		url = baseUrl + baseOption2 + query + basePage + "1" + baseDisplayCount + str(countPerPage)

		print(url)
		response = requests.get(url, headers={'cookie':'NNB=3S6UTB5CEP5GK; page_uid=ili3Wwqo15VssbCYmLNssssst+l-021573', 'Cache-Control': 'no-cache', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}, allow_redirects=False)
		
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
			divResult = divmod(int(totalCount), countPerPage)
			totalPage = divResult[0] + 1
			restCount = divResult[1]
			
			print("totalCount= ", totalCount, ", totalPage= ", str(totalPage), ", restCount= ", str(restCount))

			i = 1
			while i <= totalPage:
				print("currentPage= ", str(i))

				if i > 1:
					displayCount = countPerPage
					if i == totalPage:
						displayCount = restCount

					# url = baseUrl + baseOption + query + basePage + str(i) + baseDisplayCount + str(displayCount)
					url = baseUrl + baseOption2 + query + basePage + str(i) + baseDisplayCount + str(displayCount)
		
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

				if resultJson.get("result") is not None and resultJson.get("result").get("place") is not None and resultJson.get("result").get("place").get("list") is not None:
					# print("resultJson[result][place][list]= ", resultJson["result"]["place"]["list"])
					for resultList in resultJson["result"]["place"]["list"]:
						if resultList["id"] in result_id_list:
							# print('exist ID : ', resultList["id"])
							exist = 'exist'

						else:
							result_id_list.append(resultList["id"])

							# row_data = InitialStoreData(resultList["name"], resultList["address"], resultList["tel"], resultList["telDisplay"], resultList["virtualTel"], resultList["virtualTelDisplay"], resultList["tel"], resultList["bizhourInfo"], "", "")
							# print("resultList['name'] : ", resultList["name"])

							file.write(location + "●" + search_key + "●" + get_category(search_key) + "●" + ','.join(str(e) for e in resultList["category"])
								+ "●" + resultList["name"]
								+ "●" + resultList["address"]
								+ "●" + resultList["tel"] + "●" + resultList["telDisplay"] + "●" + resultList["virtualTel"] + "●" + resultList["virtualTelDisplay"] + "●" + resultList["tel"]
								+ "●" + resultList["y"] + "●" + resultList["x"]
								+ "●" + resultList["bizhourInfo"] + " (" + resultList["businessStatus"]["businessHours"].replace(today_date, "") + ")"
								# + "●" + " "
								+ "\n")

				else:
					i = totalPage

				i += 1
file.close() 			

# print('end of search --------')
# for result_id in result_id_list:
# 	print('result_id : ', result_id)