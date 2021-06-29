import allure
import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


class TestMainPage:
    main_page_link = "http://selenium1py.pythonanywhere.com/"
    login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

    @allure.title("Гость не должен увидеть товар в пустой корзине, открытой с главной страницы")
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Arrange
        page = MainPage(browser, self.main_page_link)
        # Act
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        # Assert
        basket_page.should_not_be_message_item_in_the_cart()
        basket_page.should_be_empty_cart_message()


@pytest.mark.login_guest
class TestLoginFromMainPage():
    link = "http://selenium1py.pythonanywhere.com/"

    @allure.title("Гость может перейти на страницу авторизации")
    def test_guest_can_go_to_login_page(self, browser, language):
        # Arrange
        page = MainPage(browser,
                        self.link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        # Act
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url, language)  # переход на страницу LoginPage
        # Assert
        login_page.should_be_login_page()

    @allure.title("Гостю доступна кнопка авторизации")
    def test_guest_should_see_login_link(self, browser):
        # Arrange
        page = MainPage(browser, self.link)
        # Act
        page.open()
        # Assert
        page.should_be_login_link()
