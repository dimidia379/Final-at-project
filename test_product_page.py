from pages.product_page import ProductPage
import pytest


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
