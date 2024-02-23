import time

import configparser
from multiprocessing import Pool

from selenium import webdriver
from selenium.webdriver.edge import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


# config.ini 읽기
config = configparser.ConfigParser()    
config.read('config.ini', encoding='utf-8') 

# 옵션 설정
options = webdriver.EdgeOptions()
options.use_chromium = True
# options.add_argument("-inprivate")
options.add_experimental_option('detach', True)

# Edge 파일 위치 설정
options.binary_location = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
s = service.Service(r'C:\Program Files (x86)\Microsoft\Edge\msedgedriver.exe')

# Edge 드라이버 생성
driver = webdriver.Edge(options=options, service = s)

# URL 설정
url = 'https://www.polyteru-store.com/'


# 로그인
print('폴리테루 로그인중...')

driver.get(url + 'login')
driver.find_element(By.ID, 'loginUid').send_keys(config['LOGIN']['ID'])
driver.find_element(By.ID, 'loginPassword').send_keys(config['LOGIN']['PASSWORD'])
driver.find_element(By.ID, 'loginPassword').send_keys(Keys.ENTER)
time.sleep(1)

print('로그인 완료!')

# 발매시간 대기


# 장바구니에 넣기
print('아이템 장바구니에 추가중...')

driver.get(url + 'product/' + 'PL23FWKNLS01PK')

select_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '선택하세요.')]"))
)
select_button.click()
time.sleep(0.5)

size_option = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='custom-select-option' and div[@class='custom-select-option-info'][text()='3(L)']]"))
)
size_option.click()

driver.find_element(By.ID, 'btn_addToCart').click()
time.sleep(0.5)

print('추가 완료!')

# 장바구니에서 구매버튼 클릭
driver.find_element(By.CLASS_NAME, 'ico-cart-border').click()
time.sleep(0.5)
driver.find_element(By.ID, 'btn_orderProducts').click()
time.sleep(0.5)

# 결제
print('결제중...')

time.sleep(1)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
driver.find_element(By.XPATH, '//button[contains(text(), "전액 사용")]').click()

driver.find_element(By.XPATH, '//span[contains(text(), "카카오페이")]').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[5]/div[2]/button').click()

# 카카오페이
time.sleep(2.5)
driver.find_element(By.CLASS_NAME, 'kakaotalk').click()
time.sleep(0.5)
driver.find_element(By.ID, 'userPhone').send_keys(config['KAKAOPAY']['PHONENUMBER'])
driver.find_element(By.ID, 'userBirth').send_keys(config['KAKAOPAY']['BIRTH'])
driver.find_element(By.CLASS_NAME, 'btn_payask').click()