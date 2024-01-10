# Загрузка файла

from selenium import webdriver
from selenium.webdriver.common.by import By
import os # Обрати внимание 
import time 

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    browser.find_element(By. NAME, 'firstname').send_keys('SICK')
    browser.find_element(By. NAME, 'lastname').send_keys('POC')
    browser.find_element(By. NAME, 'email').send_keys('sickpoc122@yaya.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла 
    browser.find_element(By. ID, 'file').send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
     time.sleep(10)
     browser.quit()