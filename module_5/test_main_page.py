link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        browser.get(link)
        login_link = browser.find_element_by_css_selector("#login_link")
        login_link.click()

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")