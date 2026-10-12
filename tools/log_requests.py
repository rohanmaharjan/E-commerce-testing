import sys
from playwright.sync_api import sync_playwright

# usage: python tools/log_requests.py "<label of a category checkbox>"
label = sys.argv[1]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_load_state("networkidle")

    page.on("request", lambda r: print(r.method, r.url) if "api." in r.url else None)
    print("--- ticking the filter ---")
    page.get_by_label(label).check()
    page.wait_for_timeout(3000)   # fine in a scratch script; never in a real test
    browser.close()