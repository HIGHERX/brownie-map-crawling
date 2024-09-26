import requests
import json
import time

from datetime import datetime
from urllib import parse
from var_types_240611 import InitialStoreData, search_location_list, icecream_key_list, photoshop_key_list, selflaundry_key_list, studycafe_key_list, convenience_key_list, ramen_key_list, cafe_key_list, stationary_key_list, petshop_key_list, fruit_key_list, etc_search_key_list

today_datetime = datetime.today().strftime("%Y%m%d%H%M%S")
today_date = datetime.today().strftime("%Y%m%d")
filename = './20240612/storeInfo_by_crawling_240612_'+ today_datetime + '.csv'

file = open(filename, 'w', encoding='utf-8')
file.write("location" + "●" + "search_key" + "●" + "category" + "●" + "naver_category"
	+ "●" + "store_name" + "●" + "address"
	+ "●" + "tel"
	+ "●" + "latitude" + "●" + "longitude" 
	+ "●" + "operation_time"
	# + "●" + "description"
	+ "\n")

baseUrl="https://map.naver.com/p/api/search/allSearch"
baseOption="?searchCoord=126.95943950000026%3B37.564414600000646&boundary=&"
baseQuery="&query="
basePage="&page="
baseDisplayCount="&displayCount="

baseDetailUrl="https://map.naver.com/v5/api/sites/summary/"
baseDetailOption="?lang=ko"

# search_location_list = busan_list
# search_location_list = gyeonggi_list
whole_search_key = icecream_key_list + photoshop_key_list + selflaundry_key_list + studycafe_key_list + convenience_key_list + ramen_key_list + cafe_key_list + stationary_key_list + petshop_key_list + fruit_key_list + etc_search_key_list
# whole_search_key = stationary_key_list + petshop_key_list + fruit_key_list + etc_search_key_list

isHeaderCookie = False

result_id_list = []

def get_category(search_key: str):
	returnValue = ''

	if search_key in icecream_key_list:
		returnValue = '아이스크림 할인점'
	
	elif search_key in photoshop_key_list:
		returnValue = '무인사진관'

	elif search_key in selflaundry_key_list:
		returnValue = '셀프빨래방'

	elif search_key in studycafe_key_list:
		returnValue = '스터디카페'

	elif search_key in convenience_key_list:
		returnValue = '무인편의점'

	elif search_key in ramen_key_list:
		returnValue = '무인라면'

	elif search_key in cafe_key_list:
		returnValue = '무인카페'

	elif search_key in stationary_key_list:
		returnValue = '무인문방구'

	elif search_key in petshop_key_list:
		returnValue = '무인펫샵'

	elif search_key in fruit_key_list:
		returnValue = '무인과일'

	elif search_key in etc_search_key_list:
		returnValue = '기타브랜드'

	else:
		returnValue = '??'

	return returnValue

for location in search_location_list:

	for search_key in whole_search_key:
		schKeyword = location + " " + search_key

		query = baseQuery + parse.quote(schKeyword)
		url = baseUrl + baseOption + query + basePage + "1"

		print(url)

		if isHeaderCookie == False:
			response = requests.get(url, headers={'cookie': 'NNB=LZKHOTW4IROWK; PUBLIC_PAGE=0; page_uid=iPlphlqpsECssmYzXdRssssss3o-113184; _ga=GA1.2.1911296213.1710217018; BUC=u2MaU0vN44LUAlxPkw7J3SOxIPIYu3AGBC1OXkDSXnY=', 'Cache-Control': 'no-cache', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}, allow_redirects=False)
		else:
			response = requests.get(url, headers={'Cache-Control': 'no-cache', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}, allow_redirects=False)
		
		time.sleep(1)
		
		print(response, schKeyword)
		# print(response.text)

		try:
			resultStr = response.text
			resultJson = json.loads(resultStr)
		except Exception as inst:
			# print(resultStr)
			# print(resultJson)
			print(type(inst))
			print(inst.args)
			print(inst)
			continue
			
		# print(type(resultJson))
		
		if resultJson.get("result").get("place") is not None:
			totalCount = resultJson["result"]["place"]["totalCount"]
			divResult = divmod(int(totalCount), 20)
			totalPage = divResult[0] + 1
			restCount = divResult[1]
			
			print("totalCount= ", totalCount, ", totalPage= ", str(totalPage), ", restCount= ", str(restCount))

			i = 1
			while i <= totalPage:
				print("currentPage= ", str(i))

				if i > 1:
					displayCount = 20
					if i == totalPage:
						displayCount = restCount

					url = baseUrl + baseOption + query + basePage + str(i)
		
					# print(url)
					if isHeaderCookie == False:
						response = requests.get(url, headers={'cookie': 'NNB=LZKHOTW4IROWK; PUBLIC_PAGE=0; page_uid=iPlphlqpsECssmYzXdRssssss3o-113184; _ga=GA1.2.1911296213.1710217018; BUC=u2MaU0vN44LUAlxPkw7J3SOxIPIYu3AGBC1OXkDSXnY=', 'Cache-Control': 'no-cache', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}, allow_redirects=False)
					else:
						response = requests.get(url, headers={'Cache-Control': 'no-cache', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}, allow_redirects=False)

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

							resultPhone = ''
							resultTel = ''
							resultTelDisplay = ''
							resultVirtualTel = ''
							resultVirtualTelDisplay = ''

							if resultList["tel"] != '':
								resultTel = resultList["tel"]
								resultPhone = resultTel
							
							if resultList["telDisplay"] != '' and resultList["telDisplay"] != resultTel:
								resultTelDisplay = resultList["telDisplay"]
								if resultPhone != '':
									resultPhone += ', ' + resultList["telDisplay"]
								else:
									resultPhone = resultList["telDisplay"]

							if resultList["virtualTel"] != '' and resultList["virtualTel"] != resultTel and resultList["virtualTel"] != resultTelDisplay:
								resultVirtualTel = resultList["virtualTel"]
								if resultPhone != '':
									resultPhone += ', ' + resultList["virtualTel"]
								else:
									resultPhone = resultList["virtualTel"]

							if resultList["virtualTelDisplay"] != '' and resultList["virtualTelDisplay"] != resultTel and resultList["virtualTelDisplay"] != resultTelDisplay and resultList["virtualTelDisplay"] != resultVirtualTel:
								resultVirtualTelDisplay = resultList["virtualTelDisplay"]
								if resultPhone != '':
									resultPhone += ', ' + resultList["virtualTelDisplay"]
								else:
									resultPhone = resultList["virtualTelDisplay"]

							file.write(location + "●" + search_key + "●" + get_category(search_key) + "●" + ','.join(str(e) for e in resultList["category"])
								+ "●" + resultList["name"]
								+ "●" + resultList["address"]
								+ "●" + resultPhone
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