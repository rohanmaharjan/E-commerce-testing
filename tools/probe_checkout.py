import re
from playwright.sync_api import sync_playwright
from automation.api.clients.api_client import ApiClient
from automation.utils.helpers import create_user_via_api

BASE = "https://practicesoftwaretesting.com"
KEYWORDS = re.compile(r"success|invoice|thank|order|confirm|error|wrong|fail|empty", re.I)


def show(page, title):
    print(f"\n=== {title} | {page.url}")
    lines = [l.strip() for l in page.locator("body").inner_text().splitlines() if KEYWORDS.search(l)]
    print("matching text:", lines)
    print("finish buttons:", page.get_by_test_id("finish").count(),
          "| success message:", page.get_by_test_id("payment-success-message").count())
    return lines


user = create_user_via_api()
with sync_playwright() as p:
    p.selectors.set_test_id_attribute("data-test")
    browser = p.chromium.launch(headless=False, slow_mo=400)
    page = browser.new_page()
    page.goto(f"{BASE}/auth/login")
    page.get_by_test_id("email").fill(user["email"])
    page.get_by_test_id("password").fill(user["password"])
    page.get_by_test_id("login-submit").click()
    page.wait_for_url("**/account")

    page.get_by_test_id("nav-home").click()
    page.get_by_test_id("product-name").first.click()
    page.get_by_test_id("add-to-cart").click()
    page.get_by_test_id("nav-cart").click()
    page.get_by_test_id("proceed-1").click()
    page.get_by_test_id("proceed-2").click()

    page.get_by_test_id("house_number").fill("88")
    page.wait_for_timeout(2500)           # scratch script only: let the postcode lookup finish
    page.get_by_test_id("proceed-3").click()
    page.get_by_test_id("payment-method").select_option("cash-on-delivery")
    page.wait_for_timeout(1000)

    for attempt in (1, 2, 3):
        page.get_by_test_id("finish").click()
        page.wait_for_timeout(4000)
        lines = show(page, f"after Confirm click {attempt}")
        if any(re.search(r"invoice|thank", l, re.I) for l in lines):
            break

    page.get_by_test_id("nav-menu").click()
    page.get_by_test_id("nav-my-invoices").click()
    page.wait_for_timeout(2500)
    show(page, "invoices page")
    print("invoice rows on page:", page.locator("tbody tr").count())

    api = ApiClient()
    token = api.login(user["email"], user["password"]).json()["access_token"]
    api.set_token(token)
    r = api.get("/invoices")
    print("\nAPI /invoices:", r.status_code, r.text[:600])
    browser.close()