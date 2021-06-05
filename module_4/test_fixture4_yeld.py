import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function") # Допустимые значения: “function”, “class”, “module”, “session”.
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    # Когда программа доходит до yield, то функция переходит в состояние ожидания и продолжает работу с того же места при повторном вызове.
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(autouse=True)  #фикстуру нужно запустить для каждого теста даже без явного вызова
def prepare_data():
    print()
    print("preparing some critical data for every test")


# вызываем фикстуру в тесте, передав ее как параметр
def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")


def test_guest_should_see_basket_link_on_the_main_page(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".basket-mini .btn-group > a")
