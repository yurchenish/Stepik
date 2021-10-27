from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class BasketPageLocators():
    ADD_IN_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    ADD_COMMENT = (By.ID, "write_review")
    ALARM_BOOK_NAME = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ALARM_PRICE = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")
    PRICE = (By.CSS_SELECTOR, ".product_main p")
