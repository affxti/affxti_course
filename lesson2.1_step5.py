from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
 
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
 
try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, ".form-control").send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
     
finally:
    time.sleep(10)
    browser.quit()