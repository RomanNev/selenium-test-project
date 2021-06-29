import math

from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .locators import BasePageLocators, CatalogPageLocators
from .locators import LoginPageLocators

class BasePage():
    def __init__(self, browser, url, language = None , timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.language = language

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_basket(self):
        basket_btn = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        basket_btn.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_text_element(self, how, what):
        return self.browser.find_element(how, what).text

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_price_product_in_site_header(self):
        assert self.is_element_present(*CatalogPageLocators.PRICE_PRODUCT_IN_SITE_HEADER), \
            "expected product price in the header of the site "

    def should_be_message_authorized_new_user(self):
        assert self.is_element_present(*LoginPageLocators.RESULT_MESSAGE_REGISTRATION), "Successful register message is not presented, " \
                                                                           "probably unauthorised user"

    def should_be_message_authorized_old_user(self):
        assert self.is_element_present(*LoginPageLocators.SUCCESSFUL_AUTHORIZED_MESSAGE), "Successful register message is not presented, " \
                                                                           "probably unauthorised user"