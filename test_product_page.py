from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest
import time


@pytest.mark.parametrize('promo_offer', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, promo_offer):
	product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
	link = f"{product_base_link}/?promo=offer{promo_offer}"
	page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
	page.open()  # открываем страницу
	page.add_to_basket()  # выполняем метод страницы - добавляем товар в корзину
	page.solve_quiz_and_get_code() # решаем задачку во всплывающем окне
	page.product_name_in_added_to_basket_message() # сверяем наименование товара в сообщении об успешном добавлении в корзину
	page.product_price_in_basket_total_message() # сверяем цену товара и сумму в сообщении об общей стоимости корзины

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208"
	page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
	page.open()  # открываем страницу
	page.add_to_basket()  # добавляем товар в корзину
	page.should_not_be_success_message() # проверяем, что после добавления товара в корзину не видно сообщение об успешном добавлении в корзину

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208"
	page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
	page.open()  # открываем страницу
	page.add_to_basket()  # добавляем товар в корзину
	page.success_message_is_disappeared() # проверяем, что при добавлении товара в корзину сообщение об успехе исчезает после появления

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()

def test_guest_cant_see_success_message(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208"
	page = ProductPage(browser,
		              link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
	page.open()  # открываем страницу
	page.should_not_be_success_message()  # проверяем, что не видно сообщение об успешном добалении в корзину, если мы не добавили в нее товар

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_basket()
	basket_page = BasketPage(browser, browser.current_url)
	basket_page.basket_should_be_empty()  # проверяем, что корзина пуста
	basket_page.should_be_empty_basket_message()  # проверяем наличие сообщения о том, что корзина пуста
	# basket_page.basket_should_not_be_empty()  # проверяем, что корзина не пуста
	# basket_page.should_not_be_empty_basket_message()  # проверяем отсутсвие сообщения о том, что корзина пуста

class TestUserAddToBasketFromProductPage():

	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
		self.page = LoginPage(browser, login_link)
		self.page.open()
		email = str(time.time()) + "@fakemail.org"  # генерация email с помощью time
		password = "testpassword" # пароль для любого email
		self.page.register_new_user(email, password) #регистрируем нового пользователя
		self.page.should_be_authorized_user() # проверяем, что пользователь залогинен

	def test_user_cant_see_success_message(self, browser):
		link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208"
		page = ProductPage(browser, link)
		page.open()
		page.should_not_be_success_message()  # проверяем, что не видно сообщение об успешном добалении в корзину, если мы не добавили в нее товар

	def test_user_can_add_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208"
		page = ProductPage(browser, link)
		page.open()
		page.add_to_basket()
		page.product_name_in_added_to_basket_message()  # сверяем наименование товара в сообщении об успешном добавлении в корзину
		page.product_price_in_basket_total_message()  # сверяем цену товара и сумму в сообщении об общей стоимости корзины




