from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    # находим radiobutton по умолчанию
    people_radio = browser.find_element_by_id("peopleRule")
    # проверяем что атрибут имеется
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    
    # находим radiobutton НЕ по умолчанию
    robots_radio = browser.find_element_by_id("robotsRule")
    # проверяем что атрибута НЕТ
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots checkbox: ", robots_checked)
    assert robots_checked is None, "People radio is selected by default"
    
    # находим кнопку отправки
    button = browser.find_element_by_css_selector("[type='submit']")
    # проверяем что кнопка заблокирована
    button_disabled = button.get_attribute("disabled")
    print("value of button before time is up: ", button_disabled)
    assert button_disabled is None, "Submit button is disabled"
    
    time.sleep(10)
    
    # находим кнопку отправки
    button = browser.find_element_by_css_selector("[type='submit']")
    # проверяем что кнопка заблокирована
    button_disabled = button.get_attribute("disabled")
    print("value of button when time is up: ", button_disabled)
    assert button_disabled == "true", "Submit button is not disabled"

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()