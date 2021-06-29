from .base_page import BasePage
from .locators import BasketPageLocators, CatalogPageLocators


class BasketPage(BasePage):

    def delete_item_in_basket(self):
        delete_item_button = self.browser.find_element(*BasketPageLocators.DELETE_BUTTON_ITEM)
        delete_item_button.click()

    def should_be_empty_cart_message(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_CART), \
            "empty cart message does exist"

    def should_not_be_empty_cart_message(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE_EMPTY_CART), \
            "empty cart message does not exist"

    def should_not_be_message_item_in_the_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE_ITEM_IN_THE_CART), \
            "there should be no message about items in the cart"


    def should_be_message_item_in_the_cart(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ITEM_IN_THE_CART), \
            "there should be  message about items in the cart"

    def first_price_product_text(self):
        return self.get_text_element(*CatalogPageLocators.FIRST_PRICE_PRODUCT_IN_CATALOG)

    def check_price_added_item_basket_page(self, first_price_product):
        basket_price_product = self.get_text_element(*BasketPageLocators.PRICE_ITEM_IN_BASKET)
        assert first_price_product == basket_price_product, "the value in the cart is the same as " \
                                                          "the value of the item "

    def check_name_added_item_basket_page(self, first_name_product):
        basket_name_product = self.get_text_element(*BasketPageLocators.NAME_ITEM)
        assert first_name_product == basket_name_product, "the name in the cart not is the same as " \
                                                          "the name of the item "

    def should_be_no_deleted_item_in_the_cart(self):
        assert self.is_not_element_present(*CatalogPageLocators.FIRST_NAME_PRODUCT)