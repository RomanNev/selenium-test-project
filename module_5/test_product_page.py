import time

import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

link_promo_new_year = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link_unavailable_item = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
link_available_item = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestProductPage:
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link_promo_new_year)
        page.open()
        page.add_to_basket_product()
        page.solve_quiz_and_get_code()
        page.should_be_message_adding_item_to_the_cart()
        page.should_be_message_about_the_price_in_the_basked()
        page.product_name_check()
        page.product_price_check()


    @pytest.mark.parametrize('promo_offer',
                             ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3",
                              "?promo=offer4", "?promo=offer5", "?promo=offer6",
                              pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8",
                              "?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        link = link_available_item+promo_offer
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_product()
        page.solve_quiz_and_get_code()
        page.should_be_message_adding_item_to_the_cart()
        page.should_be_message_about_the_price_in_the_basked()
        page.product_name_check()
        page.product_price_check()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link_available_item)
        page.open()
        page.add_to_basket_product()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link_available_item)
        page.open()
        page.add_to_basket_product()
        page.should_be_disappeared()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link_unavailable_item)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link_unavailable_item)
        page.open()
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)  # переход на страницу LoginPage
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, link_unavailable_item)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_messege_item_in_the_cart()
        basket_page.should_be_empty_cart_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_available_item)
        page.open()
        page.should_not_be_success_message()


class TestUserAddToBasketFromProductPage():
    link_login = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "56345762497437865"
        page = LoginPage(browser, self.link_login)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_available_item)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link_promo_new_year)
        page.open()
        page.add_to_basket_product()
        page.solve_quiz_and_get_code()
        page.should_be_message_adding_item_to_the_cart()
        page.should_be_message_about_the_price_in_the_basked()
        page.product_name_check()
        page.product_price_check()
