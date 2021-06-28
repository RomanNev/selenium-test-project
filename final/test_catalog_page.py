import allure
import pytest
from final.pages.catalog_page import CatalogPage
from final.pages.product_page import ProductPage


class TestCatalogPage:
    catalog_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
    @pytest.mark.personal_tests
    @allure.title("Гость может добавить товар в корзину с главной страницы каталога")
    def test_guest_can_add_product_to_basket_from_catalog_page(self, browser):
        # Arrange
        page = CatalogPage(browser, self.catalog_link)
        # Act
        page.open()
        page.add_to_basket_product_from_catalog_page()
        #Assert
        page.should_successfully_message_add_item_to_the_cart()
        page.should_successfully_alert_add_item_to_the_cart()
        page.should_price_product_in_site_header()
        page.check_price_added_item()

    @pytest.mark.personal_tests
    @allure.title("Гость может перейти в корзину через  появивщееся уведомление, "
                  "кликнув по кнопке 'просмотреть корзину'")
    def test_guest_can_go_to_cart_via_notification_from_catalog_page(self, browser):
        # Arrange
        page = CatalogPage(browser, self.catalog_link)
        # Act
        page.open()
        page.add_to_basket_product_from_catalog_page()
        page.go_to_basket_via_alert_from_catalog_page()
        product_page = ProductPage(browser, browser.current_url)
        # Assert










