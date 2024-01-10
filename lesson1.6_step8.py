 # Поиск элемента по XPath

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, 'first_name')
    input1.send_keys("Dart")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Weider")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Village")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Tatuin")
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click() # Обратить внимание🧜‍♂️🧜‍♂️🧜‍♂️

finally:
    time.sleep(30)
    browser.quit()
    
    