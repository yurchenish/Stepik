from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        # * - указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
