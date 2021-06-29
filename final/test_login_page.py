import time

import allure
import pytest

from final.pages.login_page import LoginPage


class TestLoginPage:
    login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

    @pytest.mark.personal_tests
    @allure.title("Гость может зарегистрироваться")
    def test_quest_can_register(self, browser):
        # Arrange
        email = str(time.time()) + "@fakeemail.org"
        password = "943523487566378223445"
        page = LoginPage(browser, self.login_page_link)
        # Act
        page.open()
        page.register_new_user(email,password)
        # Assert
        page.should_be_authorized_user()
        page.should_be_message_authorized_new_user()

    @pytest.mark.personal_tests
    @allure.title("Существующий пользователь может авторизоваться")
    def test_old_user_can_be_authorized(self, browser):
        #Arrange
        user_login = "test_987@bail.com"
        user_passwoord = "passtest_987"
        page = LoginPage(browser, self.login_page_link)
        # Act
        page.open()
        page.authorized_old_user(user_login,user_passwoord)
        #Assert
        page.should_be_message_authorized_old_user()








