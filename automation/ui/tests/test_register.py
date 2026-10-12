import re

import pytest
from playwright.sync_api import expect

from automation.ui.pages.register_page import RegisterPage
from automation.utils.data_factory import new_user_payload

pytestmark = pytest.mark.ui


def test_register_new_user(page):  # TC-REG-001
    RegisterPage(page).open().register(new_user_payload())
    expect(page).to_have_url(re.compile(r"/auth/login"))


def test_register_empty_form_shows_validation_errors(page):  # TC-REG-003
    register = RegisterPage(page).open()
    register.submit.click()
    expect(page).to_have_url(re.compile(r"/auth/register"))
    expect(register.errors.first).to_be_visible()