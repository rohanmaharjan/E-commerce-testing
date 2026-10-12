from automation.ui.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.form = page.get_by_test_id("login-form")
        self.email = page.get_by_test_id("email")
        self.password = page.get_by_test_id("password")
        self.submit = page.get_by_test_id("login-submit")
        self.forgot_password_link = page.get_by_test_id("forgot-password-link")
        self.register_link = page.get_by_test_id("register-link")
        self.error = page.get_by_test_id("login-error")    # VERIFY: not in your recording

    def open(self):
        self.goto("/auth/login")
        return self

    def login(self, email, password):
        self.email.fill(email)
        self.password.fill(password)
        self.submit.click()