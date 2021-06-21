from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", \
            "некорректная сслыка формы логина"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM)

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.INPUT_EMAIL_REGISTRATION).send_keys(email)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.INPUT_MESSAGE_PASSWORD_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON_REGISTRATION).click()
