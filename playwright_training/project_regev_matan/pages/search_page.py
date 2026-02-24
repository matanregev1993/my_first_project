import re
from playwright.sync_api import expect

class SearchPage:

    def search_basic(self, page):
        page.goto("https://www.starbucks.com/store-locator?place=")
        expect(page).to_have_url(re.compile("store-locator"))
        page.get_by_role("link", name="Find a store").click()
        search = page.locator("[data-e2e='searchTermInput']")
        expect(search).to_be_visible()
        search.fill("New York")
        expect(search).to_have_value("New York")
        search_button = page.locator("[data-e2e='submitSearchTermButton']")
        expect(search_button).to_be_visible()
        search_button.click()

    def search_delivery(self, page):
        delivery_radio = page.locator("input[name='orderType'][value='delivery']")
        expect(delivery_radio).to_be_visible()
        expect(delivery_radio).not_to_be_checked()
        delivery_radio.check()
        expect(delivery_radio).to_be_checked()
        faqs_link = page.get_by_role("link", name="Delivery FAQs")
        expect(faqs_link).to_be_visible()
        expect(faqs_link).to_have_attribute("href", re.compile("delivery"))
        with page.context.expect_page() as new_tab_info:
            faqs_link.click()
        new_tab = new_tab_info.value
        expect(new_tab).to_have_url(re.compile("delivery"))
        new_tab.close()
        pickup_radio = page.locator("input[name='orderType'][value='pickup']")
        expect(pickup_radio).to_be_visible()
        pickup_radio.check()
        expect(pickup_radio).to_be_checked()

    def search_links(self, page):
        privacy = page.locator("[data-e2e='privacy-notice-link']")
        expect(privacy).to_be_visible()
        expect(privacy).to_have_attribute("href", re.compile("privacy"))
        with page.context.expect_page() as new_tab_info:
            privacy.click()
        new_tab = new_tab_info.value
        expect(new_tab).to_have_url(re.compile("privacy"))
        new_tab.close()
        terms = page.locator("[data-e2e='terms-of-use-link']")
        expect(terms).to_be_visible()
        expect(terms).to_have_attribute("href", re.compile("terms"))
        with page.context.expect_page() as new_tab_info:
            terms.click()
        new_tab = new_tab_info.value
        expect(new_tab).to_have_url(re.compile("terms"))
        new_tab.close()
        do_not_share = page.get_by_role("link", name="Do Not Share My Personal Information")
        expect(do_not_share).to_be_visible()
        expect(do_not_share).to_have_attribute("href", re.compile("personal-information"))
        with page.context.expect_page() as new_tab_info:
            do_not_share.click()
        new_tab = new_tab_info.value
        expect(new_tab).to_have_url(re.compile("personal-information"))
        new_tab.close()


