
from os import confstr

## Naver Map 관련 정보
baseUrl = "https://map.naver.com/p/api/search/allSearch"
baseOption = "?searchCoord=126.95943950000026%3B37.564414600000646&boundary=&"
baseQuery = "&query="
basePage = "&page="
headerWithCookie = {
  'Referer': 'https://map.naver.com/p/search/%EB%AC%B4%EC%9D%B8%EC%B9%B4%ED%8E%98?c=15.00,0,0,0,dh'
  , 'cookie': 'NNB=LZKHOTW4IROWK; PUBLIC_PAGE=0; page_uid=iPlphlqpsECssmYzXdRssssss3o-113184; _ga=GA1.2.1911296213.1710217018; BUC=u2MaU0vN44LUAlxPkw7J3SOxIPIYu3AGBC1OXkDSXnY='
  , 'Cache-Control': 'no-cache'
  , 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}
headerNoCookie = {
  'Referer': 'https://map.naver.com/p/search/%EB%AC%B4%EC%9D%B8%EC%B9%B4%ED%8E%98?c=15.00,0,0,0,dh'
  , 'Cache-Control': 'no-cache'
  , 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

## 브라우니 DB connection 정보
db_host = "db-dev-22-08-22.brwnie.kr"
db_name = "brownie"
db_user = "brwnie"
db_password = "v252544ChzLhc"
