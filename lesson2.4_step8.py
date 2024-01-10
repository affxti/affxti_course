# Ждем нужный текст на странице

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time, math 

def calc(x): 
    return str(math.log(abs(12*math.sin(int(x))))) 

try: 
    browser = webdriver.Chrome() 
    browser.get('http://suninjuly.github.io/explicit_wait2.html') 
        # ждем до тех пор, пока цена не снизится до $100
    expectation = WebDriverWait(browser, 12).until( 
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    ) 
    browser.find_element(By.ID, 'book').click() 
         # скроллим страницу вниз
    browser.execute_script("window.scrollBy(0, 100);")
    x = browser.find_element(By.ID, 'input_value').text 
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.ID, "solve").click()


finally: 
    time.sleep(20) 
    browser.quit()
    

