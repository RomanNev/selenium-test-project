import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser(request):
     print("\nstart chrome browser for test..")
     browser = webdriver.Chrome()
     yield browser

     print("\nquit browser..")
     browser.quit()