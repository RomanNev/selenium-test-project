import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    new_window = browser.window_handles[1] # выбираем вторую вкладку в массиве вкладок
    browser.switch_to.window(new_window) #переключаемся на новую вкладку

    #дальше скрипт работает в новой вкладке
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    result = calc(x)
    input_result = browser.find_element_by_id("answer")
    input_result.send_keys(result)
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(5)
    browser.quit()