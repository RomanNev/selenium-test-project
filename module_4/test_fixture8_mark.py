"""
 Для выборочного запуска таких тестов в PyTest используется маркировка тестов или метки (marks).
Для маркировки теста нужно написать декоратор вида @pytest.mark.mark_name, где mark_name - произвольная строка.
"""

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.smoke
def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

@pytest.mark.skip # чтобы пропустить тест, его отмечают в коде как @pytest.mark.skip
def test_guest_should_see_login_link_skip(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

@pytest.mark.regression
@pytest.mark.win10
def test_guest_should_see_basket_link_on_the_main_page(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".basket-mini .btn-group > a")

@pytest.mark.xfail(reason="fixing this bug right now") # XFail: помечать тест как ожидаемо падающий
def test_guest_should_see_search_button_on_the_main_page(browser):
    browser.get(link)
    #browser.find_element_by_css_selector("button.favorite")
    browser.find_element_by_css_selector("input.btn.btn-default")

