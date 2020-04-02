from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # содаем фукцию для просчитыания значения У
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    # находим элемент Х и записыаем значение в переменную Х
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    
    # создаем переменную У и просчитываем значение по методу
    y = calc(x)
    
    # Находим текстовое поле и вводим значение У
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    
    # отмечаем checkbox и выбираем radiobutton 
    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    
    # Отправляем заполненное поле
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()