import unittest

from selenium import webdriver


class TestRegistration(unittest.TestCase):
    def test_registration_page1(self):
        first_name_input = '.first_block .form-control.first'
        last_name_input = '.first_block .form-control.second'
        email_input = '//input[@placeholder="Input your email"]'
        btn_submit = 'button.btn'
        welcome_text_elt = "h1"

        try:
            browser = webdriver.Chrome()
            browser.get("http://suninjuly.github.io/registration1.html")

            browser.find_element_by_css_selector(first_name_input).send_keys("Ivan")
            browser.find_element_by_css_selector(last_name_input).send_keys("Petrov")
            browser.find_element_by_xpath(email_input).send_keys("ivan_petrov@gmail.com")
            browser.find_element_by_css_selector(btn_submit).click()
            welcome_text = browser.find_element_by_tag_name(welcome_text_elt).text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                             "не найдена сторока успешной регистрации")
        finally:
            browser.quit()

    def test_registration_page2(self):
        first_name_input = '.first_block .form-control.first'
        last_name_input = '.first_block .form-control.second'
        email_input = '//input[@placeholder="Input your email"]'
        btn_submit = 'button.btn'
        welcome_text_elt = "h1"

        try:
            browser = webdriver.Chrome()
            browser.get("http://suninjuly.github.io/registration2.html")

            browser.find_element_by_css_selector(first_name_input).send_keys("Ivan")
            browser.find_element_by_css_selector(last_name_input).send_keys("Petrov")
            browser.find_element_by_xpath(email_input).send_keys("ivan_petrov@gmail.com")
            browser.find_element_by_css_selector(btn_submit).click()
            welcome_text = browser.find_element_by_tag_name(welcome_text_elt).text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                             "не найдена сторока успешной регистрации")

        finally:
            browser.quit()


if __name__ == "__main__":
    unittest.main()
