from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self): # метод добавления в корзину
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def product_name_in_added_to_basket_message(self): # сверяем наименование товара в сообщении об успешном добавлении в корзину
        in_basket_name=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ADDED_TO_BASKET_ALERT)
        product_name=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert in_basket_name.text==product_name.text, "Wrong product name in basket message"

    def product_price_in_basket_total_message(self): # сверяем цену товара и сумму в сообщении об общей стоимости корзины
        in_basket_price=self.browser.find_element(*ProductPageLocators.SUM_IN_BASKET_TOTAL_ALERT)
        product_price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert in_basket_price.text==product_price.text, "Wrong product price in basket message"
