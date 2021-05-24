# явные ожидания конкретных элементов Explicit Waits
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from time import sleep

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )

    book_btn = browser.find_element_by_id("book")
    book_btn.click()

    # решаем капчу для роботов
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text  # получает текст между тегами
    y = calc(x)
    input_result = browser.find_element_by_id("answer")
    input_result.send_keys(y)
    # подтверждаем отправку решения
    submit_btn = browser.find_element_by_id("solve")
    submit_btn.click()

finally:
    sleep(10)
    browser.quit()
    sleep(2)
    browser.close()