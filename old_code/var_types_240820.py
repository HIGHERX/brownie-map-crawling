
from os import confstr

search_location_list = [
  '서울',
  '경기도 수원시',
  '경기도 성남시',
  '경기도 의정부시',
  '경기도 안양시',
  '경기도 부천시',
  '경기도 광명시',
  '경기도 평택시',
  '경기도 동두천시',
  '경기도 안산시',
  '경기도 고양시',
  '경기도 과천시',
  '경기도 구리시',
  '경기도 남양주시',
  '경기도 오산시',
  '경기도 시흥시',
  '경기도 군포시',
  '경기도 의왕시',
  '경기도 하남시',
  '경기도 용인시',
  '경기도 파주시',
  '경기도 이천시',
  '경기도 안성시',
  '경기도 김포시',
  '경기도 화성시',
  '경기도 광주시',
  '경기도 양주시',
  '경기도 포천시',
  '경기도 여주시',
  '경기도 연천군',
  '경기도 가평군',
  '경기도 양평군'
]

# 1. 아이스크림 할인점
icecream_key_list = [
  '아이스크림 할인점',
  '감동창고',
  '하하아이스365',
  '메리엘스',
  '아삭삭',
  '응응스크르',
  '노마진아이스크림',
  '달시',
  '아이스크림스토리',
  '더달달',
  '픽미픽미',
  '빙아이스크림',
  '아이스크림 나라',
  '아이스365',
  '아이스캔디',
  '아이스앤스낵창고',
  '빙고링고',
  '아이스헌터',
  '별난아이스',
  '빙고푸드',
  '도깨비냉장고'
]

# 2. 무인사진관
photoshop_key_list = [
  '무인사진관',
  '시현하다 프레임',
  '하이포토',
  '플레이인더박스',
  'RGB 포토 스튜디오',
  '3PIC STUDIO',
  '폴라스튜디오',
  '모노멘션',
  '인싸포토',
  '그믐달셀프스튜디오',
  '포토스트리트',
  '플랜비스튜디오',
  '포토아이브',
  '포토그레이',
  '하루필름',
  '셀픽스',
  '포토시그니처',
  '포토이즘 (박스)',
  '인생네컷',
  '하마필름',
  '픽닷',
  '포토스트리트웸앤쿨',
  '포토랩플러스',
  '지이포토',
  '스튜디오808',
  '스냅치즈',
  '세이치즈',
  'rgbphotostudio',
  'odtmode',
  '돈룩업'
]

# 3. 셀프빨래방
selflaundry_key_list = [
  '셀프빨래방',
  '워시엔조이',
  '월드클리닝',
  '크린에이드',
  '워시Q',
  '워시프렌즈',
  '화이트365',
  '더런드리',
  '크린위드',
  '워시테리아',
  '버블맨24',
  '위니아24',
  '이지워시',
  '런드리24',
  '런드리9',
  '에코런드렛',
  '크린시아',
  '위시피플',
  '화이트24',
  '탑크리닝업',
  '하얀크리닝',
  '베베드클린',
  '큐브위시',
  '런드리익스프레스',
  '런드리플립플랍',
  '위시쿱',
  '위시팡팡',
  '호텔런드리',
  '탑워시케어',
  '아쿠아워시'
]

# 4. 스터디카페
studycafe_key_list = [
  '스터디카페',
  '봄날의서재',
  '나인모드스터디카페',
  '두잇스터디카페',
  '다다르다',
  '더킹스터디카페',
  '프레쉬 스터디카페',
  '스터디카페포커스',
  '열공다방스터디카페',
  '기본스터디카페',
  'SIS 스터디카페',
  '지공스터디카페',
  '리게인스터디카페',
  '노벨스터디카페',
  '바짝스터디카페',
  '엘알마스터디카페',
  '랭스터디카페',
  '시너지플레이스',
  '위넌스터디카페',
  '공부인 스터디카페',
  '타임유스터디카페',
  '비허밍스터디카페',
  '공간샘스터디카페',
  '플랜A',
  '셀독24스터디카페',
  '커피랑도서관',
  '맨토즈',
  '시작스터디카페',
  '플랜트',
  '그루스터디센터',
  '화이트펜슬',
  '어라운드스터디카페',
  '하우스스터디카페',
  '초심',
  '토즈 스터디카페',
  '르하임스터디카페',
  '작심',
  '올탑스터디카페',
  '아토스터디'
]

# 5. 무인편의점
convenience_key_list = [
  '무인편의점',
  '신구멍가게24',
  '마켓무',
  '간식창고',
  '까까주까',
  '데이앤데이',
  '로그인편의점'
]

# 6. 무인라면
ramen_key_list = [
  '무인라면',
  '잉스커피&라면매니아',
  '한강라면',
  '월드면'
]

# 7. 무인카페
cafe_key_list = [
  '무인카페',
  '카페일분',
  '바리스타',
  '카페프리헷',
  '커피에반하다',
  '만월경',
  '비트코퍼레이션',
  '핑거커피',
  '패스트카페',
  '나우커피',
  '에그까페',
  '쏠제이커피',
  '데이롱카페',
  '더리터',
  '사람없는 커피어때',
  '커피보라'
]

# 8. 무인문방구
stationary_key_list = [
  '무인문방구',
  '빵꾸똥꾸 문구야',
  '문구방구',
  '말랑놀이터',
  '문구야 놀자',
  '방구대장',
  '빙구문구',
  '알사탕문방구',
  '우동방구',
  '문방구역',
  '문구잼',
  '오랜지팟',
  '픽미픽미문구야',
  '문구는 못말려'
]

# 9. 무인펫샵
petshop_key_list = [
  '무인팻샵',
  '무인펫샵',
  '펫프르트',
  '견생냥품',
  '도그마켓',
  '아무도없개',
  '펫싸롱',
  '슈가펫',
  '멍냥집사',
  '장보는 강아지와 고양이',
  '멍냥이편의점',
  '팻딜',
  '그냥가개?'
]

# 10. 무인과일
fruit_key_list = [
  '무인과일',
  '오롯',
  '이루팜',
  '옐로우팜',
  '아임프루트',
  '쥬시드봉',
  '달콤과일나무'
]

# 11. 무인프린트
print_key_list = [
  '무인 프린트',
  '프린트미니',
  '프린트잇',
  '클라피24',
  '프린트카페'
]

etc_search_key_list = [
  '태닝나우',
  '스위트99',
  '프린트미니',
  '클라피24',
  '집어가',
  '오밀당',
  '메고지고 떡창고',
  '떡마마',
  '케이크하우스아도르',
  '뻥튀기공작소',
  '꽃공작소',
  '금싸빠',
  '반찬톡톡'
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

