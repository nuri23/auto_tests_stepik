from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
 browser = webdriver.Chrome()
 browser.get("http://suninjuly.github.io/cats.html")
 
 browser.implicitly_wait(5)
 
 button = browser.find_element(By.ID, "button")
  
finally:
    # успеваем скопировать код за 30 секунд

    # закрываем браузер после всех манипуляций
 browser.quit()
        
