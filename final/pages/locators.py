from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")


class LoginPageLocators():
    INPUT_EMAIL_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_MESSAGE_PASSWORD_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT_BUTTON_REGISTRATION = (By.CSS_SELECTOR, '[name="registration_submit"]')
    RESULT_MESSAGE_REGISTRATION = (By.CSS_SELECTOR, '.alertinner')
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

    INPUT_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[name="login_submit"]')
    SUCCESSFUL_AUTHORIZED_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6 h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    MESSAGE_SUCCESSFUL_PRODUCT_ADDITION = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1)")
    NAME_PRODUCT_ADDITION = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > .alertinner > strong")
    PRICE_PRODUCT_ADDITION = (By.CSS_SELECTOR, " div.alertinner > p:nth-child(1) > strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    MESSAGE_EMPTY_CART = (By.CSS_SELECTOR, "#content_inner p")
    MESSAGE_ITEM_IN_THE_CART = (By.CSS_SELECTOR, ".col-sm-6.h3")


class CatalogPageLocators():
    FIRST_ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "li.col-xs-6:nth-child(1) > article:nth-child(1) > "
                                                   "div:nth-child(4) > form:nth-child(3) > button")
    FIRST_PRICE_PRODUCT_IN_CATALOG = (By.CSS_SELECTOR, "li.col-xs-6:nth-child(1) > article:nth-child(1) > div:nth-child(4) > p.price_color")
    MESSAGE_SUCCESSFULLY_ADD_ITEM_TO_THE_CART = (By.CSS_SELECTOR, "div.alert:nth-child(1) > div")
    ALERT_PRODUCT_BASKET = (By.CSS_SELECTOR, ".alert-info")
    BUTTON_ALERT_PRODUCT_BASKET = (By.CSS_SELECTOR, "a.btn-info:nth-child(1)")
    ALERT_PRICE_PRODUCT = (By.CSS_SELECTOR, ".alert-info strong")
    PRICE_PRODUCT_IN_SITE_HEADER =(By.CSS_SELECTOR, ".basket-mini > strong")





