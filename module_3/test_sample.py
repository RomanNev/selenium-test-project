import time

from selenium import webdriver

page_link = "http://selenium1py.pythonanywhere.com/ru/"

login_button_link_locator = "#login_link"
login_input_name_locator = "#id_login-username"
login_input_password_locator = "#id_login-password"
login_summit_button_locator = '[name="login_submit"]'
result_messege_login_locator = "div.alertinner"


def test_login_old_user():
    search_text = "Рады видеть вас снова"
    user_login = "test_987@bail.com"
    user_passwoord = "passtest_987"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(page_link)

        # Act
        browser.find_element_by_css_selector(login_button_link_locator).click()
        browser.find_element_by_css_selector(login_input_name_locator).send_keys(user_login)
        browser.find_element_by_css_selector(login_input_password_locator).send_keys(user_passwoord)
        browser.find_element_by_css_selector(login_summit_button_locator).click()

        # Assert
        result_messege_login = browser.find_element_by_css_selector(result_messege_login_locator).text
        assert result_messege_login == search_text, "welcome message exists"

    finally:
        time.sleep(20)
        browser.quit()


test_login_old_user()
