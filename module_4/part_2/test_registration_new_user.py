import random


link = "http://selenium1py.pythonanywhere.com/"

def random_data_for_registration():
    return random.randint(1,10000)

class TestLogin:
    def test_registration_new_user(self, browser):
        login_button_link_locator = "#login_link"
        input_email_locator = "#id_registration-email"
        input_password_locator = "#id_registration-password1"
        input_confim_password_locator = "#id_registration-password2"
        summit_button_locator = '[name="registration_submit"]'
        result_messege_registration = ".alertinner"

        data = random_data_for_registration()

        email = f"test{data}_user{data}@{data}.com"
        password = "56345762497437865"
        welcome_text = "Спасибо за регистрацию!"

        browser.get(link)
        browser.implicitly_wait(5)

        browser.find_element_by_css_selector(login_button_link_locator).click()
        browser.find_element_by_css_selector(input_email_locator).send_keys(email)
        browser.find_element_by_css_selector(input_password_locator).send_keys(password)
        browser.find_element_by_css_selector(input_confim_password_locator).send_keys(password)
        browser.find_element_by_css_selector(summit_button_locator).click()
        resul_messege = browser.find_element_by_css_selector(result_messege_registration).text



        assert resul_messege  == welcome_text, "welcome message exists"












