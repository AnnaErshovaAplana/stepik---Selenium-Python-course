from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
try:
    link = "http://suninjuly.github.io/selects1.html"
    
    # Открыть страницу
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Посчитать сумму заданных чисел
    # записываем в переменные значения елементов через .text
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    sum = str(int(num1) + int(num2))
    print("sum calculated: ", sum)
    
    # Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)
    
    # Нажать кнопку "Submit
    #button = browser.find_element_by_css_selector(["type ='submit'"])
    browser.find_element_by_css_selector("[type ='submit']").click()
    
finally:
    time.sleep(10)
    browser.quit()
    