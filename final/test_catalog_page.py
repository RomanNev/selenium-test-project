import allure
import pytest

from final.pages.basket_page import BasketPage
from final.pages.catalog_page import CatalogPage


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
        page.check_price_added_item()
        page.should_be_button_alert_product_basket()
        page.should_price_product_in_site_header()

    @pytest.mark.personal_tests
    @allure.title("Гость может перейти в корзину через  появивщееся уведомление, "
                  "кликнув по кнопке 'просмотреть корзину'")
    def test_guest_can_go_to_cart_via_notification_from_catalog_page(self, browser):
        # Arrange
        page = CatalogPage(browser, self.catalog_link)
        # Act
        page.open()
        first_price_product = page.first_price_product_text()
        first_name_product = page.first_name_product_text()
        page.add_to_basket_product_from_catalog_page()
        page.go_to_basket_via_alert_from_catalog_page()
        basket_page = BasketPage(browser, browser.current_url)

        # Assert
        basket_page.should_be_message_item_in_the_cart()
        basket_page.check_price_added_item_basket_page(first_price_product)
        basket_page.check_name_added_item_basket_page(first_name_product)

    @pytest.mark.xfail
    @pytest.mark.personal_tests
    @allure.title("Гость может удалить добавленный в корзину товар'")
    def test_guest_can_delete_the_item_added_to_the_carte(self, browser):
        # Arrange
        page = CatalogPage(browser, self.catalog_link)
        page.open()
        first_name_product = page.first_name_product_text()
        page.add_to_basket_product_from_catalog_page()
        page.go_to_basket_via_alert_from_catalog_page()
        basket_page = BasketPage(browser, browser.current_url)
        # Act
        basket_page.delete_item_in_basket()
        # Assert
        basket_page.should_not_be_message_item_in_the_cart()
        basket_page.should_be_no_deleted_item_in_the_cart()

    @pytest.mark.personal_tests
    @allure.title("Поиск товара по каталогу'")
    def test_product_catalog_search(self, browser):
        # Arrange
        search_data = "Learning Python"

        page = CatalogPage(browser, self.catalog_link)
        page.open()
        # Act
        page.search_product(search_data)
        page.should_be_item_expected_in_the_search_results(search_data)






























