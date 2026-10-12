from automation.ui.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_input = page.get_by_test_id("search-query")
        self.search_button = page.get_by_test_id("search-submit")
        self.product_names = page.get_by_test_id("product-name")
        self.no_results = page.get_by_test_id("no-results")
        self.nav_menu = page.get_by_test_id("nav-menu")
        self.cart_count = page.get_by_test_id("cart-quantity")

    def open(self):
        self.goto("/")
        return self

    def search(self, term):
        self.search_input.fill(term)
        self.search_button.click()

    def open_first_product(self):
        self.product_names.first.click()