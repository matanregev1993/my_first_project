
import re
from playwright.sync_api import expect
class GiftCardPage:

    def gift_card_basic(self, page):
        page.click('a[href="/gift"]')
        expect(page).to_have_url(re.compile("https://www.starbucks.com/gift"))        # 1. Featured carousel
        featured = page.get_by_label("Featured carousel").locator("a[data-product-name='MrBeast Smart']")
        expect(featured).to_be_visible()
        featured.click()
        expect(page).to_have_url(re.compile("/gift/00001129"))
        page.click('a[href="/gift"]')
        beast = page.get_by_label("MrBeast | Beast Games carousel").locator("a[data-product-name='MrBeast Smart']")
        expect(beast).to_be_visible()
        beast.click()
        expect(page).to_have_url(re.compile("/gift/00001129"))
        page.click('a[href="/gift"]')
        celebrate = page.locator("a[data-product-name=\"Let's Celebrate You \"]").nth(0)
        expect(celebrate).to_be_visible()
        celebrate.click()
        expect(page).to_have_url(re.compile("/gift/00001011"))
        page.click('a[href="/gift"]')
        big_thank = page.locator("a[data-product-name='Big Thank You']").nth(0)
        expect(big_thank).to_be_visible()
        big_thank.click()
        expect(page).to_have_url(re.compile("/gift/00000040"))
        page.click('a[href="/gift"]')
        yay = page.locator("a[data-product-name='Yay']").nth(0)
        expect(yay).to_be_visible()
        yay.click()
        expect(page).to_have_url(re.compile("/gift/00001059"))
        page.click('a[href="/gift"]')
        cheers = page.locator("a[data-product-name=\"Cheers To You \"]").nth(0)
        expect(cheers).to_be_visible()
        cheers.click()
        expect(page).to_have_url(re.compile("/gift/00001013"))
        page.click('a[href="/gift"]')
        perk = page.locator("a[data-product-name='A Little Perk']").nth(0)
        expect(perk).to_be_visible()
        perk.click()
        expect(page).to_have_url(re.compile("/gift/00001017"))
        page.click('a[href="/gift"]')
        above = page.locator("a[data-product-name='Above & Beyond']").nth(0)
        expect(above).to_be_visible()
        above.click()
        expect(page).to_have_url(re.compile("/gift/00001019"))
        page.click('a[href="/gift"]')
        cafe = page.locator("a[data-product-name='Café']").nth(0)
        expect(cafe).to_be_visible()
        cafe.click()
        expect(page).to_have_url(re.compile("/gift/00000651"))
        page.click('a[href="/gift"]')

    def gift_card_featured(self, page):
        see_all = page.locator("a[data-e2e='seeAll']")
        expect(see_all).to_be_visible()
        expect(see_all).to_have_text(re.compile("See all"))
        see_all.click()
        expect(page).to_have_url(re.compile("gift/category/featured"))
        thank_you = page.locator("a[data-product-name='Thank You ']")
        expect(thank_you).to_be_visible()
        expect(thank_you).to_have_attribute("data-product-type", "Gift Card")
        thank_you.click()
        expect(page).to_have_url(re.compile("/gift/00000648"))
        gift_cards = page.locator("a.sb-globalNav__desktopLink[data-e2e='dotComHamburgerNavMenuGift']")
        expect(gift_cards).to_be_visible()
        gift_cards.click()
        expect(page).to_have_url(re.compile("/gift$"))

    def gift_card_extra(self, page):
        page.click('a.sb-globalNav__desktopLink[href="/gift"]')
        expect(page).to_have_url(re.compile("/gift"))
        add_reload = page.get_by_role("link", name="Add or Reload")
        expect(add_reload).to_be_visible()
        expect(add_reload).to_have_attribute("href", "/account/cards")
        add_reload.click()
        expect(page).to_have_url(re.compile("/account/cards"))
        gift_cards = page.locator("a.sb-globalNav__desktopLink[href='/gift']")
        expect(gift_cards).to_be_visible()
        gift_cards.click()
        expect(page).to_have_url(re.compile("/gift"))

    def gift_card_links(self, page):
        shop_now = page.locator("a[data-e2e='shopNowButton']")
        expect(shop_now).to_be_visible()
        expect(shop_now).to_have_text(re.compile("Shop now"))
        expect(shop_now).to_have_attribute("href", "https://www.starbuckscardb2b.com/")
        shop_now.click()
        page.bring_to_front()
        terms = page.locator(
            "a.sb-external-link--button[href='https://www.starbucks.com/terms/manage-gift-cards/']"
        )
        expect(terms).to_be_visible()
        expect(terms).to_have_text(re.compile("Card Terms"))
        terms.click()
        page.bring_to_front()
        faqs = page.get_by_role("link", name="Card FAQs, opens in new window")
        expect(faqs).to_be_visible()
        expect(faqs).to_have_text(re.compile("Card FAQs"))
        faqs.click()
        page.bring_to_front()








