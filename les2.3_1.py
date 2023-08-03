from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
 link = "http://suninjuly.github.io/file_input.html"
 browser = webdriver.Chrome()
 browser.get(link)

 option1 = browser.find_element(By.NAME, "firstname")
 option1.send_keys("Ivan")
 option2 = browser.find_element(By.NAME, "lastname")
 option2.send_keys("Morozov")
 option3 = browser.find_element(By.NAME, "email")
 option3.send_keys("test@test.com")
 
 import os 
 current_dir = os.path.abspath(os.path.dirname(__file__))
 file_path = os.path.join(current_dir, 'file.txt')
 button = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
 button.send_keys(file_path)
 
 button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
 button1.click()
finally:
    # успеваем скопировать код за 30 секунд
 time.sleep(30)
    # закрываем браузер после всех манипуляций
 browser.quit()
        
