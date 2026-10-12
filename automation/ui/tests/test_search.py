import pytest
from playwright.sync_api import expect

from automation.ui.pages.home_page import HomePage

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_search_returns_matching_products(page):  # TC-SEARCH-001
    home = HomePage(page).open()
    home.search("hammer")
    # wait until the list has actually been filtered, then check every result
    expect(home.product_names.first).to_contain_text("hammer", ignore_case=True)
    for name in home.product_names.all_inner_texts():
        assert "hammer" in name.lower()


def test_search_with_no_match_shows_message(page):  # TC-SEARCH-002
    home = HomePage(page).open()
    home.search("xyzabc123nomatch")
    expect(home.no_results).to_be_visible()