from automation.ui.pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_name = page.get_by_test_id("first-name")      # VERIFY all of these
        self.last_name = page.get_by_test_id("last-name")
        self.dob = page.get_by_test_id("dob")
        self.street = page.get_by_test_id("street")
        self.postal_code = page.get_by_test_id("postal_code")
        self.city = page.get_by_test_id("city")
        self.state = page.get_by_test_id("state")
        self.country = page.get_by_test_id("country")
        self.phone = page.get_by_test_id("phone")
        self.email = page.get_by_test_id("email")
        self.password = page.get_by_test_id("password")
        self.submit = page.get_by_test_id("register-submit")
        self.errors = page.locator("[data-test$='-error']")      # any element whose data-test ends in -error

    def open(self):
        self.goto("/auth/register")
        return self

    def register(self, user):
        self.first_name.fill(user["first_name"])
        self.last_name.fill(user["last_name"])
        self.dob.fill(user["dob"])
        self.street.fill(user["address"]["street"])
        self.postal_code.fill(user["address"]["postal_code"])
        self.city.fill(user["address"]["city"])
        self.state.fill(user["address"]["state"])
        self.country.select_option(user["address"]["country"])
        self.phone.fill(user["phone"])
        self.email.fill(user["email"])
        self.password.fill(user["password"])
        self.submit.click()