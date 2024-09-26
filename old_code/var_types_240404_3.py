
from os import confstr

search_location_list = [
  '서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주'
]

# 0. 카페인 24
cafein_list = [
  '카페인24'
]

# 0. 캠핑장
campling_list = [
  '캠핑장'
]

# 1. 아이스크림 할인점
icecream_key_list = [
  '아이스크림 할인점',
  '감동창고',
  '노마진아이스크림',
  '달시',
  '더달달',
  '메리엘스',
  '별난아이스',
  '빙고링고',
  '빙아이스크림',
  '아삭삭',
  '아이스365',
  '아이스앤스낵창고',
  '아이스캔디',
  '아이스크림 나라',
  '아이스크림스토리',
  '아이스헌터',
  '응응스크르',
  '잡사바24',
  '픽미픽미',
  '하하아이스365'
]

# 2. 무인사진관
photoshop_key_list = [
  '무인사진관',
  '셀프사진관',
  '셀픽스',
  '포토스트리트',
  '플레이인더박스',
  '하마필름',
  '인싸포토',
  '포토이즘 (박스)',
  '포토아이브',
  '포토시그니처',
  '3PIC STUDIO',
  '버블스튜디오',
  '플랜비스튜디오',
  '그믐달셀프스튜디오',
  'rgbphotostudio',
  'odtmode',
  '모노멘션',
  '픽닷',
  '하이포토',
  '폴라스튜디오',
  '포토그레이',
  'RGB 포토 스튜디오',
  '포토스트리트웸앤쿨',
  '지이포토',
  '포토랩플러스',
  '하루필름',
  '포토드링크',
  '스냅치즈',
  '시현하다 프레임',
  '인생네컷',
  '세이치즈',
  '스튜디오808'
]

# 3. 셀프빨래방
selflaundry_key_list = [
  '셀프빨래방',
  '위니아24',
  '런드리익스프레스',
  '워시프렌즈',
  '더런드리',
  '탑크리닝업',
  '크린위드',
  '이지워시',
  '워시테리아',
  '런드리9',
  '큐브위시',
  '코인워시365',
  '화이트365',
  '크린에이드',
  '위시팡팡',
  '런드리24',
  '버블맨24',
  '월드클리닝',
  '위시피플',
  '화이트24',
  '에코런드렛',
  '탑 워시케어',
  '워시엔조이',
  '하얀크리닝',
  '워시쿱',
  '베베드클린',
  '워시Q',
  '크린시아',
  '런드리플립플랍',
  '셀런드리',
  '코스모런드리'
]

# 4. 스터디카페
studycafe_key_list = [
  '스터디카페',
  '리게인스터디카페',
  '다다르다',
  '타임유스터디카페',
  '나인모드스터디카페',
  '셀독24스터디카페',
  '스터디카페포커스',
  '작심',
  '기본스터디카페',
  '플랜트',
  '그루스터디센터',
  '더킹스터디카페',
  '공간샘스터디카페',
  '바짝스터디카페',
  '노벨스터디카페',
  '맨토즈',
  '랭스터디카페',
  '르하임스터디카페',
  '두잇스터디카페',
  '봄날의서재',
  '프레쉬 스터디카페',
  '시너지플레이스',
  '시작스터디카페',
  '아토스터디',
  '공부인 스터디카페',
  '비허밍스터디카페',
  '어라운드스터디카페',
  '엘알마스터디카페',
  '열공다방스터디카페',
  '올탑스터디카페',
  '위넌스터디카페',
  '지공스터디카페',
  '초심',
  '커피랑도서관',
  '토즈 스터디카페',
  '플랜A',
  '하우스스터디카페',
  '화이트펜슬',
  'SIS 스터디카페'
]

# 5. 무인편의점
convenience_key_list = [
  '무인편의점',
  '온앤오프',
  '신구멍가게24',
  '데이앤데이',
  '마켓무',
  '봉봉24',
  '월드면',
  '간식창고',
  '로그인편의점',
  '까까주까'
]

# 6. 무인라면
ramen_key_list = [
  '무인라면',
  '월드면',
  '잉스커피&라면매니아',
  '한강라면'
]

# 7. 무인카페
cafe_key_list = [
  '무인카페',
  '바리스타',
  '비트코퍼레이션',
  '만월경',
  '에그까페',
  '커피에반하다',
  '카페일분',
  '핑거커피',
  '패스트카페',
  '나우커피',
  '카페프리헷',
  '쏠제이커피',
  '데이롱카페'
]

# 8. 무인문방구
stationary_key_list = [
  '무인문방구',
  '빵꾸똥꾸 문구야',
  '알사탕문방구',
  '빙구문구',
  '픽미픽미문구야',
  '문구잼',
  '방구대장',
  '문구방구',
  '라임이네 문구점',
  '말랑놀이터',
  '우동방구',
  '문방구역',
  '문구야 놀자',
  '오랜지팟'
]

# 9. 무인펫샵
petshop_key_list = [
  '무인팻샵',
  '그냥가개?',
  '장보는 강아지와 고양이',
  '견생냥품',
  '펫싸롱',
  '팻딜',
  '멍냥집사',
  '폴리파크',
  '도그마켓',
  '아무도없개',
  '펫프르트',
  '슈가펫'
]

# 10. 무인과일
fruit_key_list = [
  '무인과일',
  '오롯',
  '달콤과일나무',
  '쥬시드봉',
  '이루팜',
  '옐로우팜',
  '아임프루트'
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
  '뻥튀기공작소',
  '집어가',
  '스위트99',
  '오밀당',
  '태닝나우',
  '금싸빠',
  '클라피24',
  '꽃공작소',
  '떡마마',
  '케이크하우스아도르',
  '메고지고 떡창고',
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


