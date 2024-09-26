
from os import confstr

# 서울특별시 구 리스트
seoul_gu_list = [
            '마포구','서대문구','은평구','종로구','중구','용산구',
            '성동구','광진구',
            '동대문구','성북구','강북구','도봉구','노원구','중랑구','강동구','송파구',
            '강남구','서초구','관악구','동작구','영등포구','금천구','구로구','양천구','강서구'
            ]


# 경기도 구/군 리스트
gyeonggi_list = [
            '수원시','용인시','성남시','부천시','화성시','안산시','안양시',
            '평택시','시흥시','김포시','광주시','광명시','군포시','하남시','오산시',
            '이천시','안성시','의왕시','양평군','여주시','과천시','고양시','남양주시',
            '파주시','의정부시','양주시','구리시','포천시','동두천시','가평군','연천군'
            ]

category_list = [
  '스터디카페',
  '셀프빨래방',
  '무인편의점',
  '아이스크림할인점',
  '셀프스튜디오',
  '프린트카페',
  '무인카페',
  '스마트자판기',
  '밀키트'
]

# 무인매장 업종
base_search_key_list = [
  '스터디카페',
  '셀프빨래방',
  '코인세탁소',
  '무인편의점',
  '아이스크림할인점',
  '셀프스튜디오',
  '프린트카페'
]

brand_search_key_list = [
  '워시프렌즈',
  '크린위드',
  '워시엔조이',
  '런드리24',
  '위니아24크린샵',
  '워시테리아',
  '크린업24',
  '르하임스터디카페',
  '위넌스터디카페',
  '초심스터디카페',
  '열공다방스터디카페',
  '셀독24스터디카페',
  '어라운드스터디카페',
  '그루스터디센터',
  '리게인스터디카페',
  '시작스터디카페',
  '플랜A스터디카페',
  '초월스터디카페',
  '하우스터디스터디카페',
  '토즈스터디카페',
  '타임유스터디카페',
  '공간샘스터디카페',
  '플랜트 스터디카페',
  '잇올 스터디카페',
  '공부인 스터디카페',
  '커피랑도서관',
  '작심스터디카페',
  '화이트펜슬',
  '비에이블스터디카페',
  '하우스터디',
  '멘토즈 스터디카페',
  '디플레이스',
  '데이앤데이',
  '까까주까',
  '노마진아이스크림',
  'the달달',
  '아무도없개',
  '쏘플 파티룸',
  '인생네컷',
  '포토이즘박스',
  '셀픽스',
  '포토매틱',
  '포토드링크'
]

etc_search_key_list = [
  '홍루이젠',
  '무인카페',
  '패스트카페',
  '비트박스카페',
  '집밥뚝딱',
  '오늘쉐프',
  '진이찬방',
  '더팜홈쿡',
  '밀땅',
  '홈즈앤쿡',
  '쿡쿡쿡',
  '미미쿡',
  '옐로우스푼',
  '더잇24',
  '담꾹',
  '빵꾸똥꾸문구야',
  '펫클럽',
  '달콤과일나무',
  '문구야놀자',
  '견생냥품',
  '씨유펫',
  '오렌지팟'
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


