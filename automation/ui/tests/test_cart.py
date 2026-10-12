import pytest
from playwright.sync_api import expect

from automation.ui.pages.home_page import HomePage
from automation.ui.pages.product_page import ProductPage

from automation.ui.pages.cart_page import CartPage
from automation.utils.helpers import parse_price

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_add_product_to_cart_updates_cart_count(page):  # TC-CART-001
    home = HomePage(page).open()
    home.open_first_product()
    ProductPage(page).add_to_cart()
    expect(home.cart_count).to_have_text("1")

def test_remove_item_from_cart(page):  # TC-CART-005
    home = HomePage(page).open()
    home.open_first_product()
    ProductPage(page).add_to_cart()

    cart = CartPage(page).open()
    expect(cart.rows).to_have_count(1)
    cart.delete_buttons.first.click()
    expect(cart.rows).to_have_count(0)


def test_cart_total_equals_price_times_quantity(page):  # TC-CART-004 / TC-CART-006
    home = HomePage(page).open()
    home.open_first_product()
    product = ProductPage(page)
    product.set_quantity(3)
    product.add_to_cart()

    cart = CartPage(page).open()
    expect(cart.quantities.first).to_have_value("3")
    unit = parse_price(cart.unit_prices.first.inner_text())
    total = parse_price(cart.total.inner_text())
    assert total == pytest.approx(unit * 4, abs=0.01)