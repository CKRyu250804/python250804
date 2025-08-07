# 셀리니움_웹드라이버_네이버로그인.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import clipboard
import time

#selenium 4.6이상은 웹드라이버 설치 없이 사용 
driver = webdriver.Chrome()
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/')

# 로그인 창에 아이디/비밀번호 입력
loginID = "kim"
clipboard.copy(loginID)
#mac은 COMMAND, window는 CONTROL
driver.find_element(By.XPATH, '//*[@id="id"]').send_keys(
    Keys.CONTROL, 'v')
# find_element(By.XPATH, '//*[@id="id"]')
#   - By.XPATH : 요소를 찾는 방법(여기서는 XPath 사용)
#   - '//*[@id="id"]' : XPath 표현식, id가 "id"인 요소를 찾음

loginPW = "12345678"
clipboard.copy(loginPW)
driver.find_element(By.XPATH, '//*[@id="pw"]').send_keys(
    Keys.CONTROL, 'v')
# find_element(By.XPATH, '//*[@id="pw"]')
#   - By.XPATH : 요소를 찾는 방법(여기서는 XPath 사용)
#   - '//*[@id="pw"]' : XPath 표현식, id가 "pw"인 요소를 찾음

time.sleep(1)

# 로그인 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
# find_element(By.XPATH, '//*[@id="log.login"]')
#   - By.XPATH : 요소를 찾는 방법(여기서는 XPath 사용)
#   - '//*[@id="log.login"]' : XPath 표현식, id가 "log.login"인 요소를 찾음

while True:
    pass