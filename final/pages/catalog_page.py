from final.pages.base_page import BasePage
from final.pages.locators import CatalogPageLocators

class CatalogPage(BasePage):
    def add_to_basket_product_from_catalog_page(self):
        first_to_basket_button = self.browser.find_element(*CatalogPageLocators.FIRST_ADD_TO_BASKET_BUTTON)
        first_to_basket_button.click()

    def go_to_basket_via_alert_from_catalog_page(self):
        button_alert_product_basket = self.browser.find_element(*CatalogPageLocators.BUTTON_ALERT_PRODUCT_BASKET)
        button_alert_product_basket.click()

    def should_successfully_message_add_item_to_the_cart(self):
        assert self.is_element_present(*CatalogPageLocators.MESSAGE_SUCCESSFULLY_ADD_ITEM_TO_THE_CART), \
            "there should be message successfully adding a product to the cart from the catalog page "

    def should_successfully_alert_add_item_to_the_cart(self):
        assert self.is_element_present(*CatalogPageLocators.ALERT_PRODUCT_BASKET), \
            "there should be alert successfully adding a product to the cart from the catalog page" \
            " with the price of the goods  "

    def should_price_product_in_site_header(self):
        assert self.is_element_present(*CatalogPageLocators.PRICE_PRODUCT_IN_SITE_HEADER), \
            "expected product price in the header of the site "

    def check_price_added_item(self):
        first_price_product = self.get_text_element(*CatalogPageLocators.FIRST_PRICE_PRODUCT_IN_CATALOG)
        alert_price_product = self.get_text_element(*CatalogPageLocators.ALERT_PRICE_PRODUCT)
        assert first_price_product == alert_price_product, "the value in the cart is the same as " \
                                                          "the value of the item "

    def should_be_button_alert_product_basket(self):
        assert self.is_element_present(*CatalogPageLocators.BUTTON_ALERT_PRODUCT_BASKET), \
            "there should be button alert product basket"

    def  first_price_product_text(self):
        return self.get_text_element(*CatalogPageLocators.FIRST_PRICE_PRODUCT_IN_CATALOG)

    def  first_name_product_text(self):
        return self.get_text_element(*CatalogPageLocators.FIRST_NAME_PRODUCT)






