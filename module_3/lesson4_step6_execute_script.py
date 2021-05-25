import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    result = calc(x)
    input_result = browser.find_element_by_id("answer").send_keys(result)
    '''
       скролл нужно делать после ввода текста, ввод сбивает скролл
       '''
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)  # скролим страницу до кнопки
    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    radiobutton = browser.find_element_by_id("robotsRule").click()

    button.click()

finally:
    time.sleep(5)
    browser.quit()
