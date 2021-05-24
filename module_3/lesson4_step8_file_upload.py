# загрузка файла в форму
from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element_by_name("firstname")
    input_first_name.send_keys("Ivan")
    input_last_name = browser.find_element_by_name("lastname")
    input_last_name.send_keys("Petrov")
    input_email = browser.find_element_by_name("email")
    input_email.send_keys("test@mail.com")

    #отправляем файл
    chose_file = browser.find_element_by_css_selector('[type="file"]')
    chose_file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.close()
    time.sleep(2)
    browser.quit()