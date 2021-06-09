import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language ")


@pytest.fixture(scope="function")
def browser(language):
    print("\nstart chrome browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser

    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="session")
def language(request):
    return request.config.getoption("language")
