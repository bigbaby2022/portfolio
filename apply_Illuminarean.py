# 개발환경
# Visual Studio Code 1.81.1
# Python 3.11.5
# Sellenium 4.12.0

#<수행과제>
#- 다음 조건을 만족시키는 자동화 코드를 작성해주세요
#- 이동 경로 : 일루미나리안 사이트(https://illuminarean.com/) > [Work] > [GOODVIBE WORKS 바로가기] > [무료체험신청] > 내용 입력 > 신청 취소
#- 담당 업무 리스트에서 클릭으로 1개, 검색으로 1개 선택해주세요.
#- 그 외 내용은 자유롭게 채워 넣어주세요.
#- 무료 이용 신청 버튼은 클릭하지 않으셔도 됩니다.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()

# Chrome 자동종료되는 현상 제거
chrome_options.add_experimental_option("detach", True)

# Chrome WebDriver 경로 설정 및 크기 설정
chrome_options.add_argument("executable_path=/usr/bin/chromedriver")
chrome_options.add_argument("--window-size=1920,1080") 

# Chrome WebDriver 생성
driver = webdriver.Chrome(options=chrome_options)

# 1.일루미나리안 사이트 이동
driver.get("https://illuminarean.com/")

# 팝업이 떠나오길 기다림 
popup_locator = (By.XPATH, "Modal")  
try:
    WebDriverWait(driver, 7).until(
        EC.invisibility_of_element_located(popup_locator)
    )

    # 팝업종료
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

except Exception as e:
    print("팝업이 나타나지 않거나 사라지지 않았습니다.", e)

# 2.[Work] 메뉴로 이동
menu_locator = (By.LINK_TEXT, "Work")  
try:
    # 메뉴가 나타날 때까지 기다림 
    menu_element = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located(menu_locator)
    )
    
    menu_element.click()
except Exception as e:
    print("[Work]메뉴를 찾을 수 없거나 클릭할 수 없습니다.", e)

# 3.[GOODVIBE WORKS 바로가기] 메뉴로 이동
menu_locator = (By.LINK_TEXT, "GOODVIBE WORKS 바로가기")  
try:
    # 메뉴가 나타날 때까지 기다림 
    menu_element = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located(menu_locator)
    )
    
    menu_element.click()
except Exception as e:
    print("[GOODVIBE WORKS 바로가기]메뉴를 찾을 수 없거나 클릭할 수 없습니다.", e)

# 새 탭으로 전환
last_tab = driver.window_handles[-1]
driver.switch_to.window(window_name=last_tab)

try:
    # 무료 체험 신청 버튼 클릭
    option_to_select_emp = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='fullpage']/div[1]/div/div/div[2]/button[text()='무료 체험 신청']"))
    )
    option_to_select_emp.click()
        
except Exception as e:
    print("[무료 체험 신청]메뉴를 찾을 수 없거나 클릭할 수 없습니다.", e)


# 5.내용 입력
#   담당 업무 리스트에서 클릭으로 1개, 검색으로 1개 선택해주세요. 
#   그 외 내용은 자유롭게 채워 넣어주세요. 
#   무료 이용 신청 버튼은 클릭하지 않으셔도 됩니다.
try:
    # 회사명 입력
    input_element = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.ID, "companyName"))  
    )
    
    input_element.send_keys("세상을밝히는사람들")  

except Exception as e:
    print("회사명 입력 중 오류가 발생했습니다.", e)

try:
    # 대표자명 입력
    input_element = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.ID, "ceoName"))  
    )
    
    input_element.send_keys("김대표님")  

except Exception as e:
    print("회사명 입력 중 오류가 발생했습니다.", e)

try:
    # 사업자유형 선택
    dropdown_value = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.ID, "businessType"))
    )

    dropdown_value.click()

    option_to_select = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()='개인']"))
    )
    option_to_select.click()

except Exception as e:
    print("사업자 유형 메뉴를 선택하는 중 오류가 발생했습니다.", e)

try:
    # 직원수 선택
    dropdown_value_emp = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.ID, "scale"))
    )

    dropdown_value_emp.click()

    option_to_select_emp = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()='6-20 명']"))
    )
    option_to_select_emp.click()

except Exception as e:
    print("직원수 메뉴를 선택하는 중 오류가 발생했습니다.", e)

try:
    # 담당자명 입력
    input_element = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.ID, "name"))  
    )
    
    input_element.send_keys("밝은사람")  

except Exception as e:
    print("담당자명 입력 중 오류가 발생했습니다.", e)

try:
    # 이메일 입력
    input_element = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.ID, "email"))  
    )
    
    input_element.send_keys("sunshine@sunshine.com")  

except Exception as e:
    print("이메일 입력 중 오류가 발생했습니다.", e)

try:
    # 휴대폰 입력
    input_element = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.ID, "mobile"))  
    )
    
    input_element.send_keys("01011112222")  

except Exception as e:
    print("휴대폰 입력 중 오류가 발생했습니다.", e)

try:    
    # 담당업무 선택 :담당 업무 리스트에서 클릭으로 1개, 검색으로 1개 선택
    dropdown_duty = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.CLASS_NAME, "css-l5eay4.el0tj993"))
    )
    
    dropdown_duty.click()

    option_to_select_duty = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div/div/div/div/div[2]/dl[8]/dd/div/div[2]/div/div[1]/button[32]"))
    )
    
    option_to_select_duty.click()
    
    # 스크롤하여 요소가 보이도록 함
    driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_duty)
    
    # '등록' 버튼을 클래스 이름으로 찾기
    option_to_select_done = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='등록']"))
    )

    # 클릭 가능한 상태 확인 후 클릭
    WebDriverWait(driver, 7).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='등록']"))
    ).click()

    # 검색으로 1건 더 선택하기 위해 다시 클릭
    dropdown_duty = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.CLASS_NAME, "css-l5eay4.el0tj993"))
    )
    
    dropdown_duty.click()

    # 입력 필드 클릭
    input_field = driver.find_element(By.XPATH, "//input[@placeholder='업무명 검색']")
    input_field.click()

    # "임원" 입력
    input_field.send_keys("임원")

    # 검색 결과 목록에서 입력값 선택
    search_result = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div/div/div/div[2]/dl[8]/dd/div/div[2]/div/div[1]/button[4]")
    search_result.click()

    # '등록' 버튼을 클래스 이름으로 찾기
    option_to_select_done = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='등록']"))
    )

    # 클릭 가능한 상태 확인 후 클릭
    WebDriverWait(driver, 7).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='등록']"))
    ).click()
    
except Exception as e:
    print("담당업무 메뉴를 선택하는 중 오류가 발생했습니다.", e)

try:    
    # "서비스 이용약관 동의" 레이블을 클릭
    agree_label = driver.find_element(By.XPATH, "//label[contains(., '서비스 이용약관 동의')]")
    agree_label.click()

    # "개인정보 취급방침 동의" 레이블을 클릭
    agree_label = driver.find_element(By.XPATH, "//label[contains(., '개인정보 취급방침 동의')]")
    agree_label.click()

    # 무료 이용 신청을 누르지 않고 '신청취소' 선택
    apply_cancel = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.CLASS_NAME, "css-jqp98p.e1oaq22c7"))
    )
    
    apply_cancel.click()

except Exception as e:    
    print("체크박스 선택시 또는 취소선택 중 오류가 발생했습니다", e)

time.sleep(7)

# 웹 드라이버 종료
driver.quit()