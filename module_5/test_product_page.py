import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

class TestProductPage:

    # def test_guest_can_add_product_to_basket(self, browser):
    #     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo="
    #     page = ProductPage(browser, link)
    #     page.open()
    #     page.add_to_basket_product()
    #     page.solve_quiz_and_get_code()
    #     page.should_be_message_adding_item_to_the_cart()
    #     page.should_be_message_about_the_price_in_the_basked()
    #     page.product_name_checed()
    #     page.product_price_checed()

    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                              pytest.param("offer7", marks=pytest.mark.xfail), "offer8",
                              "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo_offer}"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_product()
        page.solve_quiz_and_get_code()
        page.should_be_message_adding_item_to_the_cart()
        page.should_be_message_about_the_price_in_the_basked()
        page.product_name_checed()
        page.product_price_checed()






