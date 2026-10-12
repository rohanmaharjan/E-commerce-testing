import re

import pytest
from playwright.sync_api import expect

from automation.ui.pages.cart_page import CartPage
from automation.ui.pages.checkout_page import CheckoutPage
from automation.ui.pages.home_page import HomePage
from automation.ui.pages.product_page import ProductPage

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_complete_checkout_with_cash_on_delivery(logged_in_page):  # TC-CHECK-001
    page = logged_in_page
    HomePage(page).open().open_first_product()
    ProductPage(page).add_to_cart()

    cart = CartPage(page).open()
    cart.proceed.click()                                  # cart -> sign-in step (already logged in)

    checkout = CheckoutPage(page)
    checkout.proceed_to_billing.click()                   # sign-in -> billing address
    checkout.proceed_to_payment.click()                   # billing -> payment
    checkout.payment_method.select_option("cash-on-delivery")   # VERIFY the option value
    checkout.confirm.click()

    expect(checkout.success_message).to_be_visible()
    # keep the order reference: Step 6 will verify it through the API and database
    print("ORDER CONFIRMATION:", checkout.confirmation_text.inner_text())