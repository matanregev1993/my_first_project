

import re
from playwright.sync_api import expect
class MainPage:

    def main_page(self, page):
        page.goto("https://www.starbucks.com/")
        expect(page).to_have_url(re.compile("starbucks.com"))
        page.locator('[id="truste-consent-button"]').click()

    def come_home(self, page):
        page.click("a[aria-label='Home, Starbucks']")
        expect(page).to_have_url(re.compile("starbucks.com"))

    def main_page_nav(self, page):
        button = page.get_by_role("link", name="Start an order").first
        expect(button).to_be_visible()
        expect(button).to_have_text("Start an order")
        expect(button).to_have_attribute("href", re.compile("menu"))
        button.click()
        expect(page).to_have_url(re.compile("menu"))
        page.click("a[aria-label='Home, Starbucks']")
        assert "https://www.starbucks.com" in page.url
        button = page.get_by_role("link", name="Order from the matcha menu").first
        expect(button).to_be_visible()
        expect(button).to_have_attribute("href", re.compile("menu/drinks/matcha"))
        button.click()
        expect(page).to_have_url(re.compile("menu/drinks/matcha"))
        page.click("a[aria-label='Home, Starbucks']")
        assert "https://www.starbucks.com" in page.url
        button = page.get_by_role("link", name="Join now").first
        expect(button).to_be_visible()
        expect(button).to_have_attribute("href", re.compile("account/create"))
        button.click()
        expect(page).to_have_url(re.compile("account/create"))
        page.click("a[aria-label='Home, Starbucks']")
        assert "https://www.starbucks.com" in page.url
        button = page.get_by_role("link", name="Order now").first
        expect(button).to_be_visible()
        expect(button).to_have_attribute("href", re.compile("featured"))
        button.click()
        expect(page).to_have_url(re.compile("featured"))
        page.click("a[aria-label='Home, Starbucks']")
        assert "https://www.starbucks.com" in page.url
        button = page.get_by_role("link", name="Learn more").first
        expect(button).to_be_visible()
        expect(button).to_have_attribute("href", re.compile("stor"))
        button.click()
        expect(page).to_have_url(re.compile("stor"))





