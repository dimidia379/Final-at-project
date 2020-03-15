from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty() #проверяем, что корзина пуста
    basket_page.should_be_empty_basket_message() #проверяем наличие сообщения о том, что корзина пуста
    #basket_page.basket_should_not_be_empty()  # проверяем, что корзина не пуста
    #basket_page.should_not_be_empty_basket_message()  # проверяем отсутсвие сообщения о том, что корзина пуста


#Давайте объединим в группу два теста в файле test_main_page.py и пометим его меткой login_guest.\
# Попробуйте запустить тесты в этом файле с меткой (нужно добавить "-m login_guest"). \
# Вы увидите, что запустились оба теста, хотя метка всего одна.
@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self
    def test_guest_can_go_to_login_page(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, self.link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
         self.link = "http://selenium1py.pythonanywhere.com/"
         page = MainPage(browser, self.link)
         page.open()
         page.should_be_login_link()