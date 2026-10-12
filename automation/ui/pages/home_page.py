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
        self.sign_out = page.get_by_test_id("nav-sign-out")      # VERIFY
        self.sort = page.get_by_test_id("sort")                  # VERIFY
        self.product_prices = page.get_by_test_id("product-price")  # VERIFY

    def sort_by(self, label):
        self.sort.select_option(label=label)

    def filter_by_category(self, name):
        self.page.get_by_label(name).check()                     # VERIFY: how are checkboxes labelled?
    
    def log_out(self):
        self.nav_menu.click()
        self.sign_out.click()

    def open(self):
        self.goto("/")
        return self

    def search(self, term):
        self.search_input.fill(term)
        self.search_button.click()

    def open_first_product(self):
        self.product_names.first.click()