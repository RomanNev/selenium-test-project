import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text  # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента
    result = calc(x)

    input_result = browser.find_element_by_id("answer")
    input_result.send_keys(result)

    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
