import pytest
from playwright.sync_api import Playwright, expect

from automation.config.settings import BASE_URL
from automation.ui.pages.login_page import LoginPage
from automation.utils.helpers import create_user_via_api


@pytest.fixture(scope="session", autouse=True)
def use_data_test_attribute(playwright: Playwright):
    """This app marks elements with data-test, not Playwright's default data-testid."""
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture
def registered_user():
    """A brand-new user for each test, so tests never share or lock an account."""
    return create_user_via_api()


@pytest.fixture
def logged_in_page(page, registered_user):
    LoginPage(page).open().login(registered_user["email"], registered_user["password"])
    expect(page.get_by_test_id("nav-menu")).to_be_visible()
    return page