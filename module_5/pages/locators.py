from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    INPUT_EMAIL_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_CONFIM_PASSWORD_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT_BUTTON_REGISTRATION = (By.CSS_SELECTOR, '[name="registration_submit"]')
    RESULT_MESSEGE_REGISTRATION = (By.CSS_SELECTOR, '.alertinner')
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

    INPUT_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[name="login_submit"]')
    RESULT_MESSEGE_ = (By.CSS_SELECTOR, "div.alertinner")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6 h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    MESSEGE_SUCCESSFUL_PRODUCT_ADDITION  = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1)")
    NAME_PRODUCT_ADDITION  = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > .alertinner > strong")
    PRICE_PRODUCT_ADDITION  = (By.CSS_SELECTOR, " div.alertinner > p:nth-child(1) > strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")













