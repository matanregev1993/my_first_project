import re
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # -----------------------------
    # בסיס: פעולות כלליות
    # -----------------------------
    def get(self, locator: str):
        return self.page.locator(locator)

    def click(self, locator: str):
        el = self.get(locator)
        el.wait_for(state="visible")
        el.click()

    def fill(self, locator: str, text: str):
        el = self.get(locator)
        el.wait_for(state="visible")
        el.fill(text)

    def navigate(self, url: str):
        self.page.goto(url)

    # -----------------------------
    # אימותים
    # -----------------------------
    def assert_url_contains(self, text: str):
        expect(self.page).to_have_url(re.compile(text))

    def assert_text(self, locator: str, text: str):
        expect(self.get(locator)).to_have_text(re.compile(text, re.I))

    def assert_attribute(self, locator: str, attr: str, value: str):
        expect(self.get(locator)).to_have_attribute(attr, re.compile(value))

    # -----------------------------
    # ניווט בטאבים חדשים
    # -----------------------------
    def open_in_new_tab(self, locator: str):
        with self.page.context.expect_page() as new_tab:
            self.click(locator)
        return new_tab.value

    # -----------------------------
    # גלילה חכמה
    # -----------------------------
    def scroll_if_needed(self, locator: str):
        self.get(locator).scroll_into_view_if_needed()

    # -----------------------------
    # פעולה משולבת: בדיקת לינק + ניווט
    # -----------------------------
    def verify_link(self, locator: str, expected_url_part: str):
        el = self.get(locator)
        el.wait_for(state="visible")
        el.click()
        self.assert_url_contains(expected_url_part)

    def click_if_exists(self, locator: str):
        el = self.page.locator(locator)
        if el.count() > 0:
            try:
                el.click(timeout=2000)
            except:
                pass
