import time
import os, sys, argparse

from datetime import datetime

# my_module 디렉토리 추가
sys.path.append(os.path.join(os.path.dirname(__file__), 'prop'))

from db_connection import (
	init_db_pool, close_db_pool
	, fetch_data, insert_data, delete_data, create_table, drop_table
)

## argument 설정
parser = argparse.ArgumentParser()
parser.add_argument('-crawldate', help=' : Please set the Crawling Date') 
parser.add_argument('-db', help=' : Please choose the DB (dev or prod)') 
args = parser.parse_args()

# argv = sys.argv
crawlDate = args.crawldate
db = args.db

if crawlDate is None or db is None:
	print("\nArgument 필요합니다. (-crawldate, -db)\n", flush=True)
	exit()

print("\n## 크롤링된 네이버 map 정보를 '브라우니 map' 정보로 복사합니다. ##\n", flush=True)
print("\nCrawling Date = ", crawlDate, ", db = ", db, flush=True)

today_date = datetime.today().strftime("%Y%m%d")


# DB 풀 초기화
init_db_pool(db, "brwnie")

# 기존 데이터 건 수 확인용 쿼리 (store_map, brwnie_yn is false)
selectCountStoreMapBrwnieYnisFalse = "select * from store_map where brwnie_yn is false;"

# 기존 store_map 데이터를 백업할 테이블 생성 쿼리
backTableName = f"public.store_map_backup_{today_date}"
dropBackupTable = f"DROP TABLE IF EXISTS public.store_map_backup_{today_date};"
createBackupTable = f"""
	CREATE TABLE {backTableName} (
		id serial4 NOT NULL,
		store_name varchar NOT NULL,
		created_at timestamptz NOT NULL,
		search_key varchar NOT NULL,
		address varchar NOT NULL,
		si_address varchar NOT NULL,
		goon_gu_address varchar NOT NULL,
		latitude float8 NULL,
		longitude float8 NULL,
		contact_number varchar NULL,
		operation_time varchar NULL,
		description varchar NULL,
		brwnie_yn bool NULL,
		naver_category varchar NULL,
		category varchar NULL,
		brwnie_yn_updated_at timestamptz NULL
	);
"""

# 기존 데이터 백업 쿼리 (store_map -> store_map_backup_{today_date})
backupStoreMap = f"""
	INSERT INTO {backTableName}
	(SELECT * FROM store_map);
"""

# 기존 데이터 삭제 쿼리 (store_map, brwnie_yn is false)
deleteStoreMapBrwnieYnIsFalse = "DELETE FROM store_map WHERE brwnie_yn is false;"

# 크롤링한 네이버 map 데이터를 브라우니 map 에 반영
copyNaverMapToBrwnieMap = f"""
	INSERT INTO store_map
	(	store_name, created_at, search_key, address, si_address
		, goon_gu_address, latitude, longitude, contact_number, operation_time
		, description, brwnie_yn, naver_category, category
	)
	(SELECT
		store_name, created_at, search_key, address, si_address
		, goon_gu_address, latitude, longitude, contact_number, operation_time
		, description, brwnie_yn, naver_category, category
	FROM
		crawling_store_map
	WHERE
		crawling_date = '{crawlDate}'
		and store_name not in (SELECT s.store_name FROM store_map s)
	);
"""

def logging(message: str):
	print(message, flush=True)


# 0. 기존 데이터 건 수 확인 (store_map, brwnie_yn is false)
logging("\n(Start #0) 0. 기존 데이터 건 수 확인 (store_map, brwnie_yn is false)")
rows = fetch_data(selectCountStoreMapBrwnieYnisFalse, None)
existCount = len(rows)
logging("   기존 데이터 건 수 = " + str(existCount))
logging("(__End #0) 0. 기존 데이터 건 수 확인 (store_map, brwnie_yn is false)")

## 기존 건 수가 1건 이상이면, 백업 및 삭제 수행
if existCount > 0:
	# 1. backup 테이블 생성
	logging("\n(Start #1) 1. backup 테이블 생성")
	drop_table(dropBackupTable)
	create_table(createBackupTable)
	logging("(__End #1) 1. backup 테이블 생성")

	# 2. backup (store_map)
	logging("\n(Start #2) 2. backup (store_map)")
	insert_data(backupStoreMap, None)
	logging("(__End #2) 2. backup (store_map)")

	# 3. 기존 데이터 삭제 (store_map, brwnie_yn is false)
	logging("\n(Start #3) 3. 기존 데이터 삭제 (store_map, brwnie_yn is false)")
	delete_data(deleteStoreMapBrwnieYnIsFalse, None)
	logging("(__End #3) 3. 기존 데이터 삭제 (store_map, brwnie_yn is false)")

## 복사는 무조건 수행
# 4. 네이버 map 데이터 복사 (crawling_store_map -> store_map)
logging("\n(Start #4) 4. 네이버 map 데이터 복사 (crawling_store_map -> store_map)")
insert_data(copyNaverMapToBrwnieMap, None)
logging("(__End #4) 4. 네이버 map 데이터 복사 (crawling_store_map -> store_map)")


# DB 풀 종료
close_db_pool(db, "brwnie")

logging("\n## '브라우니 map' 정보로 복사 완료되었습니다. ##\n")