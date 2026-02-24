import time
class RewardPage:

    def reward_page(self, page):
        page.click('a[href="/rewards"]')
        assert "https://www.starbucks.com/rewards" in page.url
        time.sleep(4)

    def reward_nav(self, page):
        page.locator("a.sb-button.sb-button--positive").first.click()
        page.click('a[href="/rewards"]')
        page.get_by_role("link", name="with the app").click()
        page.click('a[href="/rewards"]')
        page.get_by_role("link", name="join in the app").click()
        page.click('a[href="/rewards"]')
        page.get_by_role("link", name="join now", exact=True).click()
        page.click('a[href="/rewards"]')
        page.get_by_role("link", name="learn how").click()

    def reward_stars(self, page):
        var = page.get_by_role("tab", name="100 Stars")
        var.click()
        var = page.get_by_role("tab", name="200 Stars")
        var.click()
        var = page.get_by_role("tab", name="300 Stars")
        var.click()
        var = page.get_by_role("tab", name="400 Stars")
        var.click()
        var = page.get_by_role("tab", name="25 Stars")
        var.click()

    def reward_slide(self, page):
        page.get_by_role("button", name="Learn more about fun freebies").click()
        page.get_by_role("button", name="Next slide").click()
        page.get_by_role("button", name="Next slide").click()
        page.locator("button:has(path[d^='M13.06 12'])").click()
        page.get_by_role("button", name="Learn more about ordering and paying ahead").click()
        page.get_by_role("button", name="Next slide").click()
        page.locator("button.sb-swipe-deck--confirmButton").click()
        page.get_by_role("button", name="Learn more about getting free rewards faster").click()
        page.get_by_role("button", name="Next slide").click()
        page.get_by_role("button", name="Next slide").click()
        page.get_by_role("button", name="Previous slide").click()
        page.get_by_role("button", name="Previous slide").click()
        page.locator("button:has(path[d^='M13.06 12'])").click()

    def reward_links(self, page):
        page.get_by_role("link", name="Link your Delta SkyMiles®, opens in new window").click()
        page.bring_to_front()
        page.get_by_role("link", name="Link your Marriott Bonvoy®, opens in new window").click()
        page.bring_to_front()
        page.get_by_role("link", name="Join Starbucks® Rewards").click()
        page.click('a[href="/rewards"]')
        page.get_by_role("link", name="right over here, opens in new window").click()
        page.bring_to_front()
        page.get_by_role("link", name="deltastarbucks.com/terms, opens in new window").click()
        page.bring_to_front()
        page.get_by_role("link", name="Starbucks.com/MarriottBonvoy, opens in new window").click()
        page.bring_to_front()
        page.get_by_role("link", name="starbucks.com/rewards/terms, opens in new window").click()
        page.bring_to_front()
        page.get_by_role("link", name="Starbucks Store Locator, opens in new window").click()
        page.bring_to_front()
