from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

 # содаем фукцию для просчитыания значения У
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
    # Найти элемент-картинку, который является изображением сундука с сокровищами.
    picture = browser.find_element_by_id("treasure")
    
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = picture.get_attribute("valuex")
    
    # Посчитать математическую функцию от x.
    y = calc(x)
    
    # Ввести ответ в текстовое поле.
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    
    # Отметить checkbox "I'm the robot".
    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()
    
    # Выбрать radiobutton "Robots rule!".
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    
    # Нажать на кнопку "Submit".
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()