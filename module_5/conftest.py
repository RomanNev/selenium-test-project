from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):  # метод для передачи параметров командной строке
    parser.addoption('--browser_name',  # принимаем браузер
                     action='store',
                     default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language',  # принимаем язык
                     action='store',
                     default='en',
                     help="Choose language : ru, en ...")


@pytest.fixture(scope="function")
def browser(request):  # принимаем  реквест от pytest_addoption  с введенным языком из командной строки
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")  # запрос значения языка
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})  # задаем нужный язык
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)  # запускаем выбранный браузер с нужным языком
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")

    # получаем переменную с текущей датой и временем в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # делаем скриншот с помощью команды Selenium'а и сохраняем его с именем "screenshot-ГГГГ-ММ-ДД_ЧЧ-ММ-СС"
    browser.save_screenshot('screenshot-%s.png' % now)

    browser.quit()
