from selenium import webdriver
import time
import os

try:
    # Открыть страницу http://suninjuly.github.io/file_input.html
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    
    # Заполнить текстовые поля: имя, фамилия, email
    name_field = browser.find_element_by_css_selector("[name='firstname']")
    name_field.send_keys("name")
    
    surname_field = browser.find_element_by_css_selector("[name='lastname']")
    surname_field.send_keys("surname")
    
    email_field = browser.find_element_by_css_selector("[name='email']")
    email_field.send_keys("email")

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_path,'new_file.txt')
    load_file_button = browser.find_element_by_id("file")
    load_file_button.send_keys(file_path)
    
    # Нажать кнопку "Submit"
    submit =  browser.find_element_by_tag_name("button[type='submit']")
    submit.click()
    
finally:
    time.sleep(10)
    browser.quit()