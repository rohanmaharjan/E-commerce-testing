from automation.ui.pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.name = page.get_by_test_id("product-name")
        self.price = page.get_by_test_id("unit-price")
        self.add_to_cart_button = page.get_by_test_id("add-to-cart")

    def add_to_cart(self):
        self.add_to_cart_button.click()