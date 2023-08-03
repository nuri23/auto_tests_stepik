from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
 browser = webdriver.Chrome()
 browser.implicitly_wait(5)
 browser.get("http://suninjuly.github.io/wait2.html")

 button = browser.find_element(By.ID, "verify")
 button.click()
 message = browser.find_element(By.ID, "verify_message")

 assert "successful" in message.text
 
finally:
    # успеваем скопировать код за 30 секунд

    # закрываем браузер после всех манипуляций
 browser.quit()
        
