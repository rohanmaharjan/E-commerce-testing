from automation.ui.pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.form = page.get_by_test_id("register-form")
        self.first_name = page.get_by_test_id("first-name")
        self.last_name = page.get_by_test_id("last-name")
        self.dob = page.get_by_test_id("dob")
        self.country = page.get_by_test_id("country")
        self.postal_code = page.get_by_test_id("postal_code")
        self.house_number = page.get_by_test_id("house_number")
        self.street = page.get_by_test_id("street")
        self.city = page.get_by_test_id("city")
        self.state = page.get_by_test_id("state")
        self.phone = page.get_by_test_id("phone")
        self.email = page.get_by_test_id("email")
        self.password = page.get_by_test_id("password")
        self.submit = page.get_by_test_id("register-submit")
        self.errors = page.locator("[data-test$='-error']")   # VERIFY: see below

    def open(self):
        self.goto("/auth/register")
        return self

    def register(self, user):
        address = user["address"]
        self.first_name.fill(user["first_name"])
        self.last_name.fill(user["last_name"])
        self.dob.fill(user["dob"])
        self.country.select_option(address["country"])
        self.postal_code.fill(address["postal_code"])
        self.house_number.fill(address.get("house_number", "10"))
        self.street.fill(address["street"])
        self.city.fill(address["city"])
        self.state.fill(address["state"])
        self.phone.fill(user["phone"])
        self.email.fill(user["email"])
        self.password.fill(user["password"])
        self.submit.click()