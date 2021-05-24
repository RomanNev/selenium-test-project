from selenium.webdriver.support.ui import Select
import time
from selenium import webdriver

#link = "http://suninjuly.github.io/selects1.html"
links = ["http://suninjuly.github.io/selects1.html", "http://suninjuly.github.io/selects2.html"]

def selekt_tru_answer(link):
    browser = webdriver.Chrome()
    browser.get(link)
    select = Select(browser.find_element_by_tag_name("select"))
    button = browser.find_element_by_tag_name("button")

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    sum = int(num1) + int(num2)

    select.select_by_value(str(sum))
    button.click()

try:

    for link in links:
        selekt_tru_answer(link)
        time.sleep(5)

finally:
    time.sleep(10)
    browser.quit()