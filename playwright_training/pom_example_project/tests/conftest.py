import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def setup_playwright_project():
    print("Starting Playwright...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        page.close()
        browser.close()
        print("### Test session ended ###")

        print("####Test end###")