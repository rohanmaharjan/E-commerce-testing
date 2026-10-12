import re

from playwright.sync_api import expect

from automation.ui.pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.proceed_after_sign_in = page.get_by_test_id("proceed-2")
        self.house_number = page.get_by_test_id("house_number")
        self.street = page.get_by_test_id("street")
        self.proceed_after_billing = page.get_by_test_id("proceed-3")
        self.payment_method = page.get_by_test_id("payment-method")
        self.confirm = page.get_by_test_id("finish")
        self.payment_success = page.get_by_test_id("payment-success-message")
        self.order_confirmation = page.get_by_text(re.compile(r"Your invoice number is INV-\d+"))

    def enter_house_number(self, value):
        street_before = self.street.input_value()
        self.house_number.fill(value)
        # the app runs a postcode lookup that rewrites the address: wait for it
        expect(self.street).not_to_have_value(street_before)

    def pay_with_cash_on_delivery(self):
        self.payment_method.select_option("cash-on-delivery")
        expect(self.payment_method).to_have_value("cash-on-delivery")
        self.confirm.click()
        expect(self.payment_success).to_be_visible()   # step 1: payment accepted
        self.confirm.click()
        expect(self.order_confirmation).to_be_visible()  # step 2: order created

    def invoice_number(self):
        return re.search(r"INV-\d+", self.order_confirmation.inner_text()).group(0)