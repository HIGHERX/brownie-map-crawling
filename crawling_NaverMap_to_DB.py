import requests
import json
import time
import os, sys, argparse

from datetime import datetime
from urllib import parse

# my_module 디렉토리 추가
sys.path.append(os.path.join(os.path.dirname(__file__), 'prop'))

from properties import (
	baseUrl, baseOption, baseQuery, basePage, headerWithCookie, headerNoCookie
)

from db_connection import (
	init_db_pool, close_db_pool
	, fetch_data, insert_data
)

from crawling_keyword import (
	search_location_list, icecream_key_list, photoshop_key_list, selflaundry_key_list, studycafe_key_list
	, convenience_key_list, ramen_key_list, cafe_key_list, stationary_key_list, petshop_key_list
	, fruit_key_list, etc_search_key_list
	, get_category
)

## argument 설정
parser = argparse.ArgumentParser()
parser.add_argument('-crawldate', help=' : Please set the Crawling Date') 
args = parser.parse_args()

argv = sys.argv
crawlDate = args.crawldate
print("\nCrawling Date = ", crawlDate, flush=True)

today_date = datetime.today().strftime("%Y%m%d")

## 검색할 keyword 선택
whole_search_key = (
	icecream_key_list + photoshop_key_list + selflaundry_key_list + studycafe_key_list + convenience_key_list
	+ ramen_key_list + cafe_key_list + stationary_key_list + petshop_key_list + fruit_key_list
	+ etc_search_key_list
)
# whole_search_key = cafe_key_list

# DB 풀 초기화
init_db_pool()

# 기존에 저장되어 있는 store 인지 체크하는 쿼리
selectCrawlingStoreMap = "select * from crawling_store_map"

# 새로운 데이터 저장하는 쿼리
insertCrawlingStoreMap = (
	"insert into crawling_store_map "
	" (crawling_date, naver_store_id, store_name, created_at, search_key, address, si_address, goon_gu_address, latitude, longitude, contact_number, operation_time, brwnie_yn, naver_category, category) "
	" values (%s, %s, %s, now(), %s, %s, %s, %s, %s, %s, %s, %s, false, %s, %s); "
)

def logging(message: str):
	print(message, flush=True)

def callRequest(url: str, page: int):
	isIncludeCookie = True
	isFirstTry = True
	tryCount = 0
	
	while True:
		if isIncludeCookie == True:
			headerValue = headerWithCookie
		else:
			headerValue = headerNoCookie
		
		try:
			response = requests.get(url, headers=headerValue, allow_redirects=False)
			response.raise_for_status()  # 요청이 실패할 경우 예외 발생

			time.sleep(1)
			if page == 1:
				# print("\n", response, displaySearch)
				logging("\n" + str(response) + displaySearch)
			
			if isFirstTry == False:
				logging("  -> 재시도 #" + str(tryCount) + " :  Page= " + str(page))

			resultStr = response.text

			try:
				resultJson = json.loads(resultStr)
				break
			except Exception as inst:
				logging(type(inst))
				logging(inst.args)
				# logging(inst)
				isFirstTry = False
				tryCount += 1
				time.sleep(60)
		
		except requests.exceptions.RequestException as e:
			logging(f"Request 오류 발생  ->  {e}")
			isFirstTry = False
			tryCount += 1
			time.sleep(60)
	
	return resultJson


for location in search_location_list:

	for search_key in whole_search_key:
		search_category = get_category(search_key)
		displaySearch = " [" + location + "]  " + search_category + " / " + search_key

		schKeyword = location + " " + search_key
		urlQuery = baseQuery + parse.quote(schKeyword)
		url = baseUrl + baseOption + urlQuery + basePage + "1"
		# print(url)

		# 네이버 지도 api 호출
		resultJson = callRequest(url, 1)
		
		if resultJson.get("result").get("place") is not None:
			totalCount = resultJson["result"]["place"]["totalCount"]
			divResult = divmod(int(totalCount), 20)
			totalPage = divResult[0] + 1
			restCount = divResult[1]
			
			# print("totalCount= ", totalCount, ", totalPage= ", str(totalPage), ", restCount= ", str(restCount))
			logging("totalCount= " + str(totalCount) + ", totalPage= " + str(totalPage) + ", restCount= " + str(restCount))
			i = 1
			while i <= totalPage:
				# print("currentPage= ", str(i))
				logging("currentPage= " + str(i))

				if i > 1:
					displayCount = 20
					if i == totalPage:
						displayCount = restCount

					url = baseUrl + baseOption + urlQuery + basePage + str(i)
		
					# 네이버 지도 api 호출
					resultJson = callRequest(url, i)

				if resultJson.get("result") is not None and resultJson.get("result").get("place") is not None and resultJson.get("result").get("place").get("list") is not None:
					
					# print("resultJson[result][place][list]= ", resultJson["result"]["place"]["list"])
					for resultList in resultJson["result"]["place"]["list"]:
						eachNaverStoreId = resultList["id"]
						query = selectCrawlingStoreMap + " where crawling_date = %s and naver_store_id = %s ;"
						value = (crawlDate, eachNaverStoreId)

						rows = fetch_data(query, value)
						existCount = len(rows)

						# table에 존재하지 않는 매장은 저장 (저장된 매장은 pass)
						#   (existCount=0 이면, 저장되지 않은 매장)
						if existCount == 0:
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

							address = resultList["address"]

							addressArray = address.split()
							if len(addressArray) >= 2:
								resultSiAddress = addressArray[0]
								resultGoonGuAddress = addressArray[1]
							elif len(addressArray) == 1:
								resultSiAddress = addressArray[0]

							resultOperationTime = resultList["bizhourInfo"] + " (" + resultList["businessStatus"]["businessHours"].replace(today_date, "") + ")"
							resultNaverCategory = ','.join(str(e) for e in resultList["category"])

							# 테이블 저장
							query = insertCrawlingStoreMap
							# crawling_date, naver_store_id, store_name, search_key, address, si_address, goon_gu_address, latitude, longitude, contact_number, operation_time, naver_category, category
							value = (crawlDate, eachNaverStoreId, resultList["name"], search_key, address, resultSiAddress, resultGoonGuAddress, resultList["y"], resultList["x"], resultPhone, resultOperationTime, resultNaverCategory, search_category)

							insert_data(query, value)

						# else:
							# print("exist store")

				else:
					i = totalPage

				i += 1
		else:
			logging("totalCount= 0")

# DB 풀 종료
close_db_pool()
