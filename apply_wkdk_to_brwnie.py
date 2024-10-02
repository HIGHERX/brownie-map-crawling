import time
import os, sys, argparse

from datetime import datetime
import pytz

# my_module 디렉토리 추가
sys.path.append(os.path.join(os.path.dirname(__file__), 'prop'))

from db_connection import (
	init_db_pool, close_db_pool
	, fetch_data, insert_data, update_data, delete_data
)

## argument 설정
parser = argparse.ArgumentParser()
parser.add_argument('-db', help=' : Please choose the DB (dev or prod)') 
args = parser.parse_args()

# argv = sys.argv
db = args.db

if db is None:
	print("\nArgument 필요합니다. (-db)\n", flush=True)
	exit()

today_date = datetime.today().strftime("%Y-%m-%d")

print("\n## 워키도키의 브라우니 매장을 '브라우니 map' 에 반영합니다. ##\n", flush=True)
print("\nBase Date = ", today_date, ", db = ", db, flush=True)

def logging(message: str):
	print(message, flush=True)


##### 워키도키 DB 풀 초기화
init_db_pool(db, "wkdk")

# 워키도키의 브라우니 매장 가져오는 쿼리
selectWkdkBrwnieStore = (
	" SELECT "
	" 	id, name, coalesce(address, ''), lat, lng, brwnie_store_id "
    " FROM "
	"	account_store "
	" WHERE "
	"	brwnie_store_id is not null "
	"	and brand_id = 16 "
	" 	and name not like '%테스트%' "
    " ORDER BY "
	"	id; "
)

# 1. 워키도키의 브라우니 매장 가져오기
logging("\n(Start #1) 1. 워키도키의 브라우니 매장 가져오기")
rows = fetch_data(selectWkdkBrwnieStore, None)
existCount = len(rows)
logging("  * 워키도키의 브라우니 매장 수 = " + str(existCount))
logging("(__End #1) 1. 워키도키의 브라우니 매장 가져오기")

##### 워키도키 DB 풀 종료
# close_db_pool(db, "wkdk")
close_db_pool("prod", "wkdk")


##### 브라우니 DB 풀 초기화
init_db_pool(db, "brwnie")

# 브라우니의 워키도키 매장에 저장하는 쿼리
insertBrwnieStoreFromWkdk = (
	" INSERT INTO store_from_wkdk "
	" 	(base_date, wkdk_store_id, store_name, address, latitude, longitude, brwnie_store_id) "
	" VALUES "
	" 	(%s, %s, %s, %s, %s, %s, %s); "
)

# 브라우니의 워키도키 매장 테이블 초기화 쿼리
deleteBrwnieStoreFromWkdk = "DELETE FROM store_from_wkdk WHERE base_date = %s; "

# 브라우니 map 테이블에 존재하는 워키도키의 브라우니 매장은 brwnie_yn = true 처리하는 쿼리
updateStoreMapBrwnieIsTrue = (
	" UPDATE store_map "
	" SET brwnie_yn = true, brwnie_yn_updated_at = %s "
	" WHERE "
	" 	brwnie_yn is false "
	" 	and store_name in (SELECT store_name FROM store_from_wkdk WHERE base_date = %s); "
)

# 브라우니 map 테이블에 없는 워키도키의 브라우니 매장 추가 (매장 이름으로 검색)
insertStoreMapNewBrwnieIsTrue = (
	" INSERT INTO store_map "
	" (	store_name, created_at, search_key, address, si_address "
	" 	, goon_gu_address, latitude, longitude, contact_number, operation_time "
	" 	, description, brwnie_yn, naver_category, category, brwnie_yn_updated_at) "
	" (SELECT "
	" 	a.store_name, now(), coalesce(c.search_key, '기타'), a.address, split_part(a.address, ' ', 1) "
	" 	, split_part(a.address, ' ', 2), a.latitude, a.longitude, '', '' "
	" 	, '', true, coalesce(c.naver_category , '기타'), coalesce(c.category, '기타'), %s "
	"  FROM "
	" 	store_from_wkdk a "
	" 	join store b 	on a.brwnie_store_id = b.id "
	" 	left outer join code_master c 		on b.type = c.code_value and c.code_kind = 'C03' "
	" WHERE "
	"   a.base_date = %s "
	" 	and a.store_name not in (SELECT sa.store_name FROM store_map sa) "
	" ); "
)

todayValue = datetime.today().date()
nowDatetime = datetime.utcnow()
logging("\n# Now DateTime (UTC) : " + str(nowDatetime))

## 워키도키의 브라우니 매장 수가 1건 이상이면, 복사 수행
if existCount > 0:
	# 2. '브라우니의 워키도키 매장' 초기화 (base_date 기준)
	logging("\n(Start #2) 2. '브라우니의 워키도키 매장' 초기화 (base_date 기준)")
	delete_data(deleteBrwnieStoreFromWkdk, (todayValue, ))
	logging("(__End #2) 2. '브라우니의 워키도키 매장' 초기화 (base_date 기준)")

	# 3. 워키도키에서 추출한 브라우니 매장을 '브라우니의 워키도키 매장' 에 저장
	logging("\n(Start #3) 3. 워키도키에서 추출한 브라우니 매장을 '브라우니의 워키도키 매장' 에 저장")
	for eachResult in rows:
		value = (today_date, eachResult[0], eachResult[1], eachResult[2], eachResult[3], eachResult[4], eachResult[5])
		insert_data(insertBrwnieStoreFromWkdk, value)
	logging("(__End #3) 3. 워키도키에서 추출한 브라우니 매장을 '브라우니의 워키도키 매장' 에 저장")

	# 4. '브라우니의 워키도키 매장' 이 현재의 브라우니 map 테이블에 존재하면, brwnie_yn = true 처리
	logging("\n(Start #4) 4. '브라우니의 워키도키 매장' 이 현재의 브라우니 map 테이블에 존재하면, brwnie_yn = true 처리")
	update_data(updateStoreMapBrwnieIsTrue, (nowDatetime, todayValue))
	logging("(__End #4) 4. '브라우니의 워키도키 매장' 이 현재의 브라우니 map 테이블에 존재하면, brwnie_yn = true 처리")

	# 5. 브라우니 map 에 없는 '브라우니의 워키도키 매장' 을 추가
	logging("\n(Start #5) 5.  브라우니 map 에 없는 '브라우니의 워키도키 매장' 을 추가")
	insert_data(insertStoreMapNewBrwnieIsTrue, (nowDatetime, todayValue))
	logging("(__End #5) 5.  브라우니 map 에 없는 '브라우니의 워키도키 매장' 을 추가")


##### 브라우니 DB 풀 종료
close_db_pool(db, "brwnie")

logging("\n## '브라우니 map' 에 반영 완료되었습니다. ##\n")