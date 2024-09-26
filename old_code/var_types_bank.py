
from os import confstr

# 지역
search_location_list = [
  '서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주'
]
# 은행 종류
bank_search_key_list = [
  '국민은행',
  '신한은행',
  '기업은행',
  '하나은행',
  '우리은행'
]

# 네이버지도 url
naver_map_url = "https://map.naver.com/v5"

#크롤링 매장정보 class
class InitialStoreData:
  def __init__(self,store_name,address, tel, telDisplay, virtualTel, virtualTelDisplay, phone, operation_time,description,naver_category):
    self.store_name = '' if store_name == None else store_name
    self.address = '' if address == None else address
    self.tel = '' if tel == None else tel
    self.telDisplay = '' if telDisplay == None else telDisplay
    self.virtualTel = '' if virtualTel == None else virtualTel
    self.virtualTelDisplay = '' if virtualTelDisplay == None else virtualTelDisplay
    self.phone = '' if phone == None else phone
    self.operation_time = '' if operation_time == None else operation_time
    self.description = '' if description == None else description
    self.naver_category = '' if naver_category == None else naver_category
  
  def set_store_name(self, store_name):
    self.store_name = store_name

  def set_address(self, address):
    self.address = address

  def set_tel(self, tel):
    self.tel = tel

  def set_telDisplay(self, telDisplay):
    self.telDisplay = telDisplay

  def set_virtualTel(self, virtualTel):
    self.virtualTel = virtualTel

  def set_virtualTelDisplay(self, virtualTelDisplay):
    self.virtualTelDisplay = virtualTelDisplay

  def set_phone(self, phone):
    self.phone = phone
  
  def set_operation_time(self, operation_time):
    self.operation_time = operation_time
  
  def set_description(self,description):
    self.description = description

  def set_naver_category(self,naver_category):
    self.naver_category = naver_category


