import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
import os
from bs4 import BeautifulSoup
import requests
import re
import time

path='C:\\Users\\Admin\\PycharmProjects\\BOBSINT\\crawler2'
keyword="inurl:or.kr filetype:xlsx"     #검색할 거 입력하면 됨

# driver
driver = webdriver.Chrome('/Users/Admin/Downloads/chromedriver') #크롬 웹드라이버 디렉토리 (각자 다름)


driver.get("https://cse.google.com/cse?cx=018411326708544098124:osxuozxkjot")                #구글 접속

#구글 검색
elem = driver.find_element_by_name("search")         #검색창에 커서 옮겨줌
elem.clear()

elem.send_keys(keyword)             #키워드 검색창에 입력
find=driver.find_element_by_xpath('''//*[@id="cse-search-form"]/form/table/tbody/tr/td[2]/button''')
find.click()

#.submit()                       #검색 실행

url_get=driver.current_url          #현재페이지 URL 얻어옴

page=1
time.sleep(5)
while True:
    for idx, element in enumerate(driver.find_elements_by_css_selector("a.gs-title")):  # 해당클래스 불러오고 클릭
        try:
            element.click() #해당 엘리먼트 클릭
            print(element.text) #클릭한 엘리먼트의 text 속성(파일명) 출력
            print(element.get_attribute('href')) #클릭한 엘리먼트의 URL = 파일 경로
            time.sleep(2)

        except:
            None

    try:
        page+=1
        driver.find_element_by_xpath('''//*[@id="___gcse_0"]/div/div/div/div[5]/div[2]/div/div/div[2]/div[10]/div/div[%s]''' % page).click()
        time.sleep(2)

    except:
        break