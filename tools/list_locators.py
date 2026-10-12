import sys
from playwright.sync_api import sync_playwright

# usage: python tools/list_locators.py <url> [data-test to click] [another to click] ...
url = sys.argv[1]
clicks = sys.argv[2:]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)
    page.wait_for_load_state("networkidle")

    for test_id in clicks:
        page.locator(f"[data-test='{test_id}']").first.click()
        page.wait_for_load_state("networkidle")

    names = page.eval_on_selector_all(
        "[data-test]",
        "els => [...new Set(els.map(e => e.getAttribute('data-test')))]",
    )
    print("URL:", page.url)
    for name in sorted(names):
        print(name)
    browser.close()