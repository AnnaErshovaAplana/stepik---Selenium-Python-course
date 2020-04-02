from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    button = browser.find_element_by_id("book")
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    
    # Нажать на кнопку "Book"
    button.click()
    
    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    x = int(browser.find_element_by_id("input_value").text)
    answer = str(math.log(abs(12*math.sin(x))))
    
    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(answer)
    
    button = browser.find_element_by_tag_name("button[type = 'submit']")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()


