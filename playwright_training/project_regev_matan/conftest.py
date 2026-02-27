import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def setup_playwright_project():
    print("Starting Playwright...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        context.close()
        browser.close()
        print("### Test session ended ###")
        print("####Test end###")