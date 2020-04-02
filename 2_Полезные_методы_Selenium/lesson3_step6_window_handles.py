from selenium import webdriver
import os
import math
import time

try:
    # Открыть страницу http://suninjuly.github.io/redirect_accept.html
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    
    # Нажать на кнопку
    button = browser.find_element_by_tag_name("button[type = 'submit']")
    button.click()
    
    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    # Пройти капчу для робота и получить число-ответ
    x = int(browser.find_element_by_id("input_value").text)
    answer = str(math.log(abs(12*math.sin(x))))
    
    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(answer)
    
    button = browser.find_element_by_tag_name("button[type = 'submit']")
    button.click()
    
    
finally:
    time.sleep(10)
    browser.quit()