# Переод на новую вкладку 

from selenium import webdriver
from selenium.webdriver.common.by import By 
import time, math 

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    time.sleep(2)
    browser.find_element(By. CSS_SELECTOR, 'button.trollface').click()
    new_window = browser.window_handles[1] # обратить внимание 
    browser.switch_to.window(new_window)
    x = browser.find_element(By. ID, 'input_value').text
    browser.find_element(By. NAME, 'text').send_keys(calc(x))
    browser.find_element(By. CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(5)
    browser.quit()