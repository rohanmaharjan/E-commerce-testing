import pytest
from playwright.sync_api import expect

from automation.ui.pages.home_page import HomePage
from automation.ui.pages.product_page import ProductPage

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_add_product_to_cart_updates_cart_count(page):  # TC-CART-001
    home = HomePage(page).open()
    home.open_first_product()
    ProductPage(page).add_to_cart()
    expect(home.cart_count).to_have_text("1")