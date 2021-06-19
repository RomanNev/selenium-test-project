from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_cart_message(self):
        assert self.is_element_present(*BasketPageLocators.MESSEGE_EMPTY_CART),\
            "empty cart message does not exist"

    def should_not_be_messege_item_in_the_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSEGE_ITEM_IN_THE_CART),\
            "there should be no message about items in the cart "

