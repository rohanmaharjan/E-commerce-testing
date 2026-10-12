import re

import pytest
from playwright.sync_api import expect

from automation.ui.pages.home_page import HomePage
from automation.ui.pages.login_page import LoginPage

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_login_with_valid_credentials(page, registered_user):  # TC-LOGIN-001
    LoginPage(page).open().login(registered_user["email"], registered_user["password"])
    expect(page).to_have_url(re.compile(r"/account"))
    expect(HomePage(page).nav_menu).to_be_visible()


def test_login_with_wrong_password_shows_error(page, registered_user):  # TC-LOGIN-002
    login = LoginPage(page).open()
    login.login(registered_user["email"], "wrong-password-123")
    expect(login.error).to_be_visible()
    expect(page).to_have_url(re.compile(r"/auth/login"))


def test_login_with_empty_form_stays_on_login_page(page):  # TC-LOGIN-004
    login = LoginPage(page).open()
    login.submit.click()
    expect(page).to_have_url(re.compile(r"/auth/login"))

def test_logout_ends_the_session(logged_in_page):  # TC-LOGIN-006
    page = logged_in_page
    HomePage(page).log_out()
    expect(page).to_have_url(re.compile(r"/auth/login"))

    # a logged-out user must not reach the account page
    page.goto("/account")
    expect(page).to_have_url(re.compile(r"/auth/login"))


def test_account_page_requires_login(page):  # TC-LOGIN-007
    page.goto("/account")
    expect(page).to_have_url(re.compile(r"/auth/login"))

def test_forgot_password_link_opens_reset_form(page):
    login = LoginPage(page).open()
    login.forgot_password_link.click()
    expect(page.get_by_test_id("forgot-password-submit")).to_be_visible()


def test_register_link_opens_registration_form(page):
    login = LoginPage(page).open()
    login.register_link.click()
    expect(page.get_by_test_id("register-submit")).to_be_visible()


def test_login_password_field_is_masked(page):  # TC-LOGIN-006
    login = LoginPage(page).open()
    login.password.fill("SomeSecret123!")
    expect(login.password).to_have_attribute("type", "password")