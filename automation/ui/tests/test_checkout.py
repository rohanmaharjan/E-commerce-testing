import re

import pytest
from playwright.sync_api import expect

from automation.ui.pages.cart_page import CartPage
from automation.ui.pages.checkout_page import CheckoutPage
from automation.ui.pages.home_page import HomePage
from automation.ui.pages.product_page import ProductPage
from automation.utils.helpers import get_invoices_via_api, parse_price

pytestmark = pytest.mark.ui


def place_cash_on_delivery_order(page):
    """Buy the first product. Returns (invoice_number, unit_price shown on the product page)."""
    HomePage(page).open().open_first_product()
    product = ProductPage(page)
    price = parse_price(product.price.inner_text())
    product.add_to_cart()

    CartPage(page).open().proceed.click()          # proceed-1
    checkout = CheckoutPage(page)
    checkout.proceed_after_sign_in.click()         # proceed-2
    checkout.enter_house_number("88")
    checkout.proceed_after_billing.click()         # proceed-3
    checkout.pay_with_cash_on_delivery()
    return checkout.invoice_number(), price


@pytest.mark.smoke
def test_complete_checkout_creates_a_matching_invoice(logged_in_page, registered_user):  # TC-CHECK-001
    invoice_number, price = place_cash_on_delivery_order(logged_in_page)
    assert re.fullmatch(r"INV-\d+", invoice_number)

    # cross-layer check: the API must know the same order, with the same total
    invoices = get_invoices_via_api(registered_user["email"], registered_user["password"])
    matching = [i for i in invoices if i["invoice_number"] == invoice_number]
    assert len(matching) == 1, f"{invoice_number} not found in API invoices"
    assert matching[0]["total"] == pytest.approx(price, abs=0.01)


def test_placed_order_appears_in_invoice_history(logged_in_page):  # TC-ACCT-002
    page = logged_in_page
    invoice_number, _ = place_cash_on_delivery_order(page)

    HomePage(page).open_my_invoices()
    expect(page).to_have_url(re.compile(r"/account/invoices"))
    expect(page.get_by_text(invoice_number)).to_be_visible()