import pandas as pd
import time
import re
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from sqlalchemy import create_engine

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opts = Options()
# herder setting 변경
opts.add_argument("--headless=new")
opts.add_argument("--disable-gpu")
opts.add_argument("--disable-dev-shm-usage")
opts.add_argument("--no-sandbox")
opts.add_argument("--window-size=1920,1080")
# 프록시/언어 고정
opts.add_argument("--lang=ko-KR")

# 아래로 옮김

search_item = input("검색어를 입력하시오 :")
save_type = input("저장 방식을 입력하시오 ( csv / db ) :")

while True:
    if len(search_item) == 0:
        search_item = input("검색어를 입력하시오 :")
    else:
        break

while True:
    if save_type in ['csv', 'db'] :
        break
    else :
        save_type = input("저장 방식을 입력하시오 ( csv / db )")

driver = webdriver.Chrome( service=Service(
                ChromeDriverManager().install()
            ), options=opts
        )
driver = webdriver.Chrome()
# 딜레이
time.sleep(1)
# driver 에 네이버 요청을 보낸다
driver.get('http://www.naver.com')

time.sleep(1)
# id 가 query인 태그를 선택
search_element = driver.find_element(By.ID, 'query')
# 검색 하기
search_element.send_keys(search_item)
# 검색어 창에 ENTER 이벤트 발생
search_element.send_keys(Keys.ENTER)
time.sleep(1)
# 쇼핑 문구가 있는 하이퍼링크를 선택하여 클릭한다
driver.find_element(By.LINK_TEXT, '쇼핑').click()
time.sleep(1)

# driver에서 탭을 이동
driver.switch_to.window(driver.window_handles[1])


while True:
    # 현재 driver의 스크롤의 현재의 높이를 저장
    last_height = driver.execute_script("return window.pageYOffset")

    # driver에서 스크롤을 일정 간격으로 내린다
    driver.execute_script("window.scrollBy(0,800);")

    time.sleep(3)

    # 스크롤 이동 후 스크롤을 현재의 높이
    new_height = driver.execute_script("return window.pageYOffset")
    # 다 내려갔을때 반복문을 종료한다.
    if new_height == last_height:
        break
# driver에 있는 html데이터를 변수에 저장
html_data = driver.page_source
# selenium의 역할 끝 -> driver를 종료
driver.quit()

soup4 = bs(html_data, 'html.parser')
div_list = soup4.find_all(
    'div',
    attrs = {re.compile('product_item')}
)

values = []
for div_data in div_list :
    item_name = div_data.find(
        'div',
        attrs={
                'class' : re.compile('product_title')
            }
    ).get_text()
    # get_text() 로 상품의 이름추출
    item_price = div_data.find(
        'span',
        attrs={
            'class' : 'price'
    }
    ).get_text()

    item_url = div_data.find('a')['href']
    dict_data = {
        '상품명' : item_name,
        '가격' : item_price,
        'url' : item_url
    }
    values.append(dict_data)

df = pd.DataFrame(values)
if save_type == 'csv':
    df.to_csv(f'{search_item}.csv', index=False)
else:
    engine = create_engine(
    "mysql+pymysql://root:1234@localhost:3306/multicam"
    )
    df.to_sql(
        name = search_item,
        con=engine,
        if_exists= 'replace'
        )