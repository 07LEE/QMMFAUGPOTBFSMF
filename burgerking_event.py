import time                    # time 모듈 불러오기
from selenium.webdriver.common.keys import Keys     # Keys 모듈 불러오기
from selenium import webdriver                     # webdriver 모듈 불러오기
from webdriver_manager.chrome import ChromeDriverManager

time.sleep(2)                    # 2초 대기

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options) # Chrome 브라우저 열기
url = 'https://www.burgerkingevent.com/?utm_medium=kakao_da&utm_source=cpc&utm_campaign=quattromaximum'   # 버거킹 이벤트 페이지 URL
driver.get(url)                  # 해당 URL로 브라우저 이동
time.sleep(5)                    # 5초 대기

# '터치하고 시작하기' 버튼 클릭
driver.find_element_by_xpath('//*[@id="main_btn_touch"]').click()
time.sleep(3)                    # 3초 대기

# 이름 입력 칸 찾기
box = driver.find_element_by_xpath('//*[@id="input_typing"]')

# 이름
name = '콰트로 맥시멈 미트 포커스드 어메이징 얼티밋 그릴드 패티 오브 더 비기스트 포 슈퍼 미트 프릭'

# 입력한 이름을 한 글자씩 입력
for i in name:
    box.send_keys(i)

# 엔터키 입력
box.send_keys(Keys.RETURN)