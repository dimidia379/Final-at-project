from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

	def basket_should_be_empty(self):  # проверяем, что корзина пуста
		assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), "Basket is not empty."

	def basket_should_not_be_empty(self):  # проверяем, что корзина не пуста
		assert self.is_element_present(*BasketPageLocators.BASKET_SUMMARY), "Basket is empty."

	def should_be_empty_basket_message(self):  # проверяем, что присутствует сообщение о том, что корзина пуста
		assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text, \
			"There is no message about empty basket."

	def should_not_be_empty_basket_message(self):  # проверяем, что отсутствует сообщение о том, что корзина пуста
		assert "Your basket is empty." not in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text, \
			"There is a message about empty basket."
