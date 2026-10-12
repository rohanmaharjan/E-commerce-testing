from automation.ui.pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.proceed_to_billing = page.get_by_test_id("proceed-2")         # VERIFY
        self.proceed_to_payment = page.get_by_test_id("proceed-3")
        self.payment_method = page.get_by_test_id("payment-method")
        self.confirm = page.get_by_test_id("finish")
        self.success_message = page.get_by_test_id("payment-success-message")
        self.confirmation_text = page.locator("#order-confirmation")        # VERIFY: where is the invoice number shown?