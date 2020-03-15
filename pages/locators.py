from selenium.webdriver.common.by import By


class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
	REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
	REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
	PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
	ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
	PRODUCT_NAME_IN_ADDED_TO_BASKET_ALERT = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
	SUM_IN_BASKET_TOTAL_ALERT = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")


class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	BASKET_BUTTON = (By.CSS_SELECTOR, "header .basket-mini a")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
	BASKET_SUMMARY = (By.CSS_SELECTOR, ".content.basket_summary")
	EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
