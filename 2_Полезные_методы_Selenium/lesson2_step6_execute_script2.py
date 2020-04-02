from selenium import webdriver
import math
import time
import os

try:
    # Открыть страницу http://SunInJuly.github.io/execute_script.html
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    
   # весь путь с указанием имени файла
    print(os.path.abspath(__file__))
    # путь до папки с указанным файлом
    print(os.path.abspath(os.path.dirname(__file__)))
    
    # Считать значение для переменной x.
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    print(type(x_element))
    
    # Посчитать математическую функцию от x.
    answer = str(math.log(abs(12*math.sin(int(x)))))
    print("answer is:", answer)
    
    # Проскроллить страницу вниз.
    answer_field = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_field)
    
    # Ввести ответ в текстовое поле.
    answer_field.send_keys(answer)
    
    # Выбрать checkbox "I'm the robot".
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    # Переключить radiobutton "Robots rule!".
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    
    # Нажать на кнопку "Submit".
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    assert True
    
finally:
    time.sleep(10)
    browser.quit()
    