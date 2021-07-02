from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import openpyxl



############### 카페 연관검색어 크롤러 ###############################

print("검색어를 입력해주세요:")
keyword=input()

#Workbook 생성
wb = openpyxl.Workbook()

#Sheet 활성
sheet = wb.active

#sheet 이름 설정
wb.title="자동완성어"

#데이터 프레임 내 변수명 생성
sheet.append(["결과"])

# 크롬드라이버 옵션 설정
options = webdriver.ChromeOptions()
# options.add_argument('headless') # 헤드리스
options.add_argument("window-size=1920x1080")
options.add_argument("disable-gpu")

driver = webdriver.Chrome("chromedriver", chrome_options=options)

# 대기 설정
wait = WebDriverWait(driver, 3)
visible = EC.visibility_of_element_located  # DOM에 나타남, 웹에 보여야 조건 만족

# 카페 페이지 이동
driver.get("https://section.cafe.naver.com/")
htmlSource = driver.page_source

#검색창에 입력할 키워드 받고 입력
findelem = driver.find_element_by_css_selector("#header > div.snb_area > div > form > fieldset > div > div > input")
findelem.send_keys(keyword)

#검색 조회
driver.find_element_by_css_selector("#header > div.snb_area > div > form > fieldset > div > button > span.ico_search").click()
driver.implicitly_wait(1)

# 더보기 버튼 누르기
try:
    driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/div[1]/div[1]/div/a").click()
    driver.implicitly_wait(1)
except:
    driver.implicitly_wait(1)

soup = BeautifulSoup(htmlSource, "lxml")

#카페 연관검색 크롤링

try:
    CafeKeywords =driver.find_elements_by_class_name("relation_search_item")
    driver.implicitly_wait(1)
except AttributeError as e:
    print(" ")

words = []
for word in CafeKeywords:
    words.append(word.text.replace('\n',''))

print(words)

#엑셀에 저장
for i in words:
    sheet.append([i])
   
driver.quit()

#엑셀파일명 설정 및 저장
wb.save("카페검색어.xlsx")