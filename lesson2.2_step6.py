# execute_script - прокрутка страницы 
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time 

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'https://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.CLASS_NAME, 'form-control').send_keys(calc(x))
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element(By.ID, "robotsRule"))
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    
    
finally:
    time.sleep(10)
    browser.quit()
    
