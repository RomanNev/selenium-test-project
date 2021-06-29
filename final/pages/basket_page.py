from .base_page import BasePage
from .locators import BasketPageLocators, CatalogPageLocators


class BasketPage(BasePage):
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

    def  first_price_product_text(self):
        return self.get_text_element(*CatalogPageLocators.FIRST_PRICE_PRODUCT_IN_CATALOG)

    def check_price_added_item_basket_page(self, first_price_product):
        basket_price_product = self.get_text_element(*BasketPageLocators.PRICE_ITEM_IN_BASKET)
        assert first_price_product == basket_price_product, "the value in the cart is the same as " \
                                                          "the value of the item "