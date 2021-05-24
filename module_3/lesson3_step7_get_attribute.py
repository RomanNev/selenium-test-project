import math
import time
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    chest  = browser.find_element_by_id("treasure")
    chest_value = chest.get_attribute("valuex")
    result = calc(chest_value)

    input_result = browser.find_element_by_id("answer").send_keys(result)
    checkbox = browser.find_element_by_id("robotCheckbox").click()
    radiobutton = browser.find_element_by_id("robotsRule").click()
    button = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(5)
    browser.quit()