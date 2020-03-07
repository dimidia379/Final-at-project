from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_ADDED_TO_BASKET_ALERT = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong") # исправить селектор
    SUM_IN_BASKET_TOTAL_ALERT = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong") # исправить селектор
