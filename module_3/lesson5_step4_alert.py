import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name("button").click()
    alert = browser.switch_to.alert  # переключаемся на алерт
    alert.accept()  # принимаем

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text  # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента
    result = calc(x)

    input_result = browser.find_element_by_id("answer")
    input_result.send_keys(result)
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
