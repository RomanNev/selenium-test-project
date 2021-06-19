from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket_product(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def product_name_checed(self):
        #product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        # product_name_addition = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_ADDITION)
        product_name = self.get_text_element(ProductPageLocators.PRODUCT_NAME)
        product_name_addition = self.get_text_element(ProductPageLocators.NAME_PRODUCT_ADDITION)
        assert  product_name == product_name_addition, "name of the products did not match"

    def product_price_checed(self):
        # price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        # price_product_addition = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_ADDITION)
        price_product = self.get_text_element(ProductPageLocators.PRICE_PRODUCT)
        price_product_addition = self.get_text_element(ProductPageLocators.PRICE_PRODUCT_ADDITION)
        assert price_product == price_product_addition, "price of the products did not match"

    def should_be_message_adding_item_to_the_cart(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT_ADDITION)

    def should_be_message_about_the_price_in_the_basked(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT_ADDITION)








