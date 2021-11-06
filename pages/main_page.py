from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
