from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
	def should_be_login_page(self):
		self.should_be_login_url()  # проверка на корректный url адрес
		self.should_be_login_form()  # проверка, что есть форма логина на странице
		self.should_be_register_form()  # проверка, что есть форма регистрации на странице

	def should_be_login_url(self):
		assert "login" in self.browser.current_url, "It's not login-page-URL"

	def should_be_login_form(self):
		assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

	def should_be_register_form(self):
		assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

	def register_new_user(self, email, password):  # регистрация нового пользователя
		self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
		self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
		self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
		self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
