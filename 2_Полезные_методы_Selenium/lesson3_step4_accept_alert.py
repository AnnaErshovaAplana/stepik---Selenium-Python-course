from selenium import webdriver
import time
import os
import math

try:
    # Открыть страницу http://suninjuly.github.io/alert_accept.html
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    
    # Нажать на кнопку
    button = browser.find_element_by_tag_name("button[type='submit']")
    button.click()
    
    # Принять confirm
    confirm = browser.switch_to.alert
    time.sleep(3)
    confirm.accept()
    
    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    x = int(browser.find_element_by_id("input_value").text)
    answer = str(math.log(abs(12*math.sin(x))))
    print("answer: ", answer)
    
    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(answer)
    
    button = browser.find_element_by_tag_name("button[type='submit']")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()
