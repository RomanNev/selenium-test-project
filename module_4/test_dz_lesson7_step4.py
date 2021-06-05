import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def answer():
    return str(math.log(int(time.time() + 0.2)))


@pytest.fixture(scope="class")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('link',  # список параметров, они будут поочередно передаваться в test_chek_anser
                         ["https://stepik.org/lesson/236895/step/1",
                          "https://stepik.org/lesson/236896/step/1",
                          "https://stepik.org/lesson/236897/step/1",
                          "https://stepik.org/lesson/236898/step/1",
                          "https://stepik.org/lesson/236899/step/1",
                          "https://stepik.org/lesson/236903/step/1",
                          "https://stepik.org/lesson/236904/step/1",
                          "https://stepik.org/lesson/236905/step/1"
                          ]
                         )
class Test_link():
    def test_chek_anser(self, browser, link):
        link = f"{link}"  # передаем параметры из @pytest.mark.parametrize
        browser.get(link)
        browser.implicitly_wait(5)

        input_result = "textarea"
        submit_bt = "button.submit-submission"

        browser.find_element_by_tag_name(input_result).send_keys(answer())  # передаем ответ в поле ввода
        browser.find_element_by_css_selector(submit_bt).click()

        res_fild = WebDriverWait(browser, 5).until(  # проверяем, что поле с результатом появилось, ждем 5 сек
            EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )

        # res_fild_result = browser.find_element_by_css_selector("#ember122 pre")
        result = res_fild.text  # считываем результат / текст между тегами

        assert "Correct!" == result, "Введеннй результат некорректен"
