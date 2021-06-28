import time

import allure
from final.pages.login_page import LoginPage


class TestLoginPage:
    login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
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
        page.should_be_messege_authorized_user()



