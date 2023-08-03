from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


try:
    browser = webdriver.Chrome()
    
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    button = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, 'price'),'100')
        )
    browser.find_element(By.ID, "book").click()
  
    
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    """
    x = browser.find_element(By.ID, "input_value")
    y = calc(x)
    """
    browser.find_element(By.ID, "answer").send_keys(calc(browser.find_element(By.ID, "input_value").text))
    browser.find_element(By.ID, "solve").click()
    print(browser.switch_to.alert.text)


finally:
    # успеваем скопировать код за 30 секунд
 time.sleep(5)
    # закрываем браузер после всех манипуляций
 browser.quit()
   
