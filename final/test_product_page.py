import time

import allure
import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

link_promo_new_year = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link_unavailable_item = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
link_available_item = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                             ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3",
                              "?promo=offer4", "?promo=offer5", "?promo=offer6",
                              pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8",
                              "?promo=offer9"])
    @allure.title("Гость может добавить товар в корзину со страницы продукта")
    def test_guest_can_add_product_to_basket_from_product_page(self, browser, promo_offer):
        # Arrange
        link = link_available_item+promo_offer
        page = ProductPage(browser, link)
        # Act
        page.open()
        page.add_to_basket_product_from_product_page()
        page.solve_quiz_and_get_code()
        # Assert
        page.should_be_message_adding_item_to_the_cart()
        page.should_be_message_about_the_price_in_the_basked()
        page.product_name_check()
        page.product_price_check()

    @pytest.mark.xfail
    @allure.title("Гость  не видит сообщение об успешном завершении добавления продукта в корзину")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link_available_item)
        # Act
        page.open()
        page.add_to_basket_product_from_product_page()
        # Assert
        page.should_not_be_success_message()

    @pytest.mark.xfail
    @allure.title("Сообщение пропадает после добавлените продукта в корзину")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link_available_item)
        # Act
        page.open()
        page.add_to_basket_product_from_product_page()
        # Assert
        page.should_be_disappeared()

    @allure.title("Гостю доступна кнопка авторизации на странице продукта")
    def test_guest_should_see_login_link_on_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, link_unavailable_item)
        # Act
        page.open()
        # Assert
        page.should_be_login_link()

    @allure.title("Гостю может перейти на страницу авторизации со страницы продукта")
    def test_guest_can_go_to_login_page_from_product_page(self, browser, language):
        # Arrange
        page = ProductPage(browser, link_unavailable_item)
        # Act
        page.open()
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url, language)  # переход на страницу LoginPage
        # Assert
        login_page.should_be_login_page()

    @allure.title("Гость не видит продукт в пустой корзине, открытой со страницы продукта")
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, link_unavailable_item)
        # Act
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        # Assert
        basket_page.should_not_be_messege_item_in_the_cart()
        basket_page.should_be_empty_cart_message()

    @allure.title("Гость не видит сообщение об успешном добавление продукта в корзину после перехода на стрницу продукта")
    def test_guest_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, link_available_item)
        # Act
        page.open()
        # Assert
        page.should_not_be_success_message()


class TestUserAddToBasketFromProductPage():
    link_login = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Arrange
        email = str(time.time()) + "@fakemail.org"
        password = "56345762497437865"
        page = LoginPage(browser, self.link_login)
        # Act
        page.open()
        page.register_new_user(email, password)
        # Assert
        page.should_be_authorized_user()

    @allure.title("Авторизованный пользователь не видит сообщение об успешном "
                  "добавление продукта в корзину, после перехода на стрницу продукта")
    def test_user_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, link_available_item)
        # Act
        page.open()
        # Assert
        page.should_not_be_success_message()

    @allure.title("Авторизованный пользователь добавить продукт в корзину")
    def test_user_can_add_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link_promo_new_year)
        # Act
        page.open()
        page.add_to_basket_product_from_product_page()
        page.solve_quiz_and_get_code()
        # Assert
        page.should_be_message_adding_item_to_the_cart()
        page.should_be_message_about_the_price_in_the_basked()
        page.product_name_check()
        page.product_price_check()
