import re
from playwright.sync_api import expect
class MenuPage:

    def menu_page(self, page):
        menu = page.locator("a.sb-globalNav__desktopLink[href='/menu']")
        expect(menu).to_be_visible()
        expect(menu).to_have_text("Menu")
        menu.click()
        expect(page).to_have_url("https://www.starbucks.com/menu")
        trending = page.locator(
            "a.text-noUnderline.color-textBlackSoft.block.flex.justify-between[href='/menu/fan-favorites/trending']"
        )
        expect(trending).to_be_visible()
        expect(trending).to_have_text("Trending")
        trending.click()
        expect(page).to_have_url("https://www.starbucks.com/menu/fan-favorites/trending")
        matcha = page.locator(
            "a.text-noUnderline.color-textBlackSoft.block.flex.justify-between[href='/menu/drinks/matcha']"
        )
        expect(matcha).to_be_visible()
        expect(matcha).to_have_text("Matcha")
        matcha.click()
        expect(page).to_have_url("https://www.starbucks.com/menu/drinks/matcha")
        bakery = page.locator(
            "a.text-noUnderline.color-textBlackSoft.block.flex.justify-between[href='/menu/food/bakery']"
        )
        expect(bakery).to_be_visible()
        expect(bakery).to_have_text("Bakery")
        bakery.click()
        expect(page).to_have_url("https://www.starbucks.com/menu/food/bakery")
        whole_bean = page.locator(
            "a.text-noUnderline.color-textBlackSoft.block.flex.justify-between[href='/menu/at-home-coffee/whole-bean']"
        )
        expect(whole_bean).to_be_visible()
        expect(whole_bean).to_have_text("Whole Bean")
        whole_bean.click()
        expect(page).to_have_url("https://www.starbucks.com/menu/at-home-coffee/whole-bean")

    def featured_look(self, page):
        menu = page.locator("a.sb-global-subnav-item[href='/menu']")
        expect(menu).to_be_visible()
        expect(menu).to_have_text("Menu")
        menu.click()
        expect(page).to_have_url(re.compile(r"https://www\.starbucks\.com/menu/?$"))
        featured = page.locator("a.sb-global-subnav-item[href='https://www.starbucks.com/menu/featured']")
        expect(featured).to_be_visible()
        expect(featured).to_have_text("Featured")
        featured.click()
        expect(page).to_have_url(re.compile(r"https://www\.starbucks\.com/menu/featured/?$"))
        order_now = page.get_by_role("link", name="Order now").first
        expect(order_now).to_be_visible()
        expect(order_now).to_have_attribute("href", "https://www.starbucks.com/menu/product/34829/iced")
        order_now.click()
        expect(page).to_have_url(re.compile(r"/menu/product/34829/iced/?$"))

    def rest_of_subbar(self, page):
        menu = page.locator("a.sb-globalNav__desktopLink[href='/menu']")
        expect(menu).to_be_visible()
        expect(menu).to_have_text("Menu")
        menu.click()
        expect(page).to_have_url("https://www.starbucks.com/menu")
        previous = page.locator("a.sb-global-subnav-item[href='/menu/previous']")
        expect(previous).to_be_visible()
        expect(previous).to_have_text("Previous")
        previous.click()
        expect(page).to_have_url("https://www.starbucks.com/menu/previous")
        favorites = page.locator("a.sb-global-subnav-item[href='/menu/favorites']")
        expect(favorites).to_be_visible()
        expect(favorites).to_have_text("Favorites")
        favorites.click()
        expect(page).to_have_url("https://www.starbucks.com/menu/favorites")