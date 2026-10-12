from automation.ui.pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.nav_cart = page.get_by_test_id("nav-cart")                    # VERIFY all of these
        self.rows = page.locator("tbody tr")
        self.titles = page.get_by_test_id("product-title")
        self.quantities = page.get_by_test_id("product-quantity")
        self.unit_prices = page.get_by_test_id("product-price")
        self.total = page.get_by_test_id("cart-total")
        self.delete_buttons = page.locator("a.btn-danger, [data-test='delete']")
        self.proceed = page.get_by_test_id("proceed-1")

    def open(self):
        self.nav_cart.click()
        return self