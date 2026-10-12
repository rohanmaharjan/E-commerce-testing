import pytest
from playwright.sync_api import expect

from automation.ui.pages.home_page import HomePage
from automation.ui.pages.product_page import ProductPage
from automation.utils.helpers import parse_price

pytestmark = pytest.mark.ui


def test_sort_by_price_low_to_high(page):  # TC-BROWSE-002
    home = HomePage(page).open()
    first_price_before = home.product_prices.first.inner_text()
    home.sort_by("Price (Low - High)")             # VERIFY the exact option text
    # wait until the list actually changed
    expect(home.product_prices.first).not_to_have_text(first_price_before)

    prices = [parse_price(t) for t in home.product_prices.all_inner_texts()]
    assert prices == sorted(prices)


def test_filter_by_category_matches_api_results(page):  # TC-BROWSE-004
    home = HomePage(page).open()
    with page.expect_response(lambda r: "by_category" in r.url) as response_info:
        home.filter_by_category("Hammer")          # VERIFY: use a category you saw
    api_names = [p["name"] for p in response_info.value.json()["data"]]

    assert api_names, "category returned no products"
    expect(home.product_names).to_have_count(len(api_names))
    assert sorted(n.strip() for n in home.product_names.all_inner_texts()) == sorted(api_names)


def test_product_page_matches_listing(page):  # TC-DETAIL-001
    home = HomePage(page).open()
    name = home.product_names.first.inner_text().strip()
    price = parse_price(home.product_prices.first.inner_text())

    home.open_first_product()
    product = ProductPage(page)
    expect(product.name).to_contain_text(name)
    assert parse_price(product.price.inner_text()) == price