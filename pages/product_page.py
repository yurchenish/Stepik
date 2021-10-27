from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def add_in_basket(self):
        link = self.browser.find_element(*BasketPageLocators.ADD_IN_BASKET)
        link.click()

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

    def should_be_message_name_book(self):
        assert self.browser.find_element(*BasketPageLocators.ALARM_BOOK_NAME).text == \
            self.browser.find_element(*BasketPageLocators.BOOK_NAME).text, "В корзину попала не та книга"

    def should_be_message_price_book(self):
        assert self.browser.find_element(*BasketPageLocators.ALARM_PRICE).text == \
            self.browser.find_element(*BasketPageLocators.PRICE).text, "Цена товара не совпадает с суммой корзины"

    # messages > div:nth-child(1) > div > strong
    # //*[@id="messages"]/div[1]/div/strong
    # /html/body/div[2]/div/div[1]/div[1]/div/strong
