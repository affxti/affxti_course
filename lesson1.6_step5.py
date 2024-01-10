# Поиск элемента по тексту в ссылке

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link1 = 'http://suninjuly.github.io/find_link_text'
try:
    browser = webdriver.Chrome()
    browser.get(link1)
    link_text = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link_text.click()
    first_name = browser.find_element(By.NAME, 'first_name')
    first_name.send_keys('SICK')
    last_name = browser.find_element(By.NAME, 'last_name')
    last_name.send_keys('POC')
    city = browser.find_element(By.CLASS_NAME, 'city')
    city.send_keys("TBILISI")  
    country = browser.find_element(By.ID, "country")
    country.send_keys('GEORGIA')
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()