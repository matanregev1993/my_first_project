import re
from playwright.sync_api import expect
class RewardPage:

    def reward_nav(self, page):
        rewards = page.locator(
            "a.sb-globalNav__desktopLink.inline-block.text-noUnderline.text-xxs.text-upper.text-bold[href='/rewards']"
        )
        expect(rewards).to_be_visible()
        expect(rewards).to_have_text("Rewards")
        rewards.click()
        expect(page).to_have_url(re.compile(r"https://www\.starbucks\.com/rewards/?$"))
        join_app_button = page.locator(
            "a.sb-button.sb-button--positive[href='https://starbucks.app.link/VLa2I3inh9']"
        ).first
        expect(join_app_button).to_be_visible()
        expect(join_app_button).to_have_text("Join in the app")
        join_app_button.click()
        rewards.click()
        expect(page).to_have_url(re.compile(r"/rewards/?$"))
        join_online = page.locator(
            "a.sb-textLink.color-textBlack[href='/account/create']"
        )
        expect(join_online).to_be_visible()
        expect(join_online).to_have_text("Or join online")
        join_online.click()
        rewards.click()
        expect(page).to_have_url(re.compile(r"/rewards/?$"))
        join_in_app_green = page.locator(
            "a.color-greenStarbucks[href='https://starbucks.app.link/VLa2I3inh9']"
        )
        expect(join_in_app_green).to_be_visible()
        expect(join_in_app_green).to_have_text("Join in the app")
        join_in_app_green.click()
        rewards.click()
        expect(page).to_have_url(re.compile(r"/rewards/?$"))
        join_online_green = page.locator(
            "a.color-greenStarbucks[href='/account/create']"
        )
        expect(join_online_green).to_be_visible()
        expect(join_online_green).to_have_text("join online")
        join_online_green.click()
        rewards.click()
        expect(page).to_have_url(re.compile(r"/rewards/?$"))
        learn_how = page.locator(
            "a.color-greenStarbucks[href='#waystopay']"
        )
        expect(learn_how).to_be_visible()
        expect(learn_how).to_have_text("Learn how")
        learn_how.click()

    def reward_stars(self, page):
        stars_100 = page.get_by_role("tab", name="100 Stars")
        expect(stars_100).to_be_visible()
        expect(stars_100).to_have_text(re.compile(r"100.*Stars"))
        stars_100.click()
        stars_200 = page.get_by_role("tab", name="200 Stars")
        expect(stars_200).to_be_visible()
        expect(stars_200).to_have_text(re.compile(r"200.*Stars"))
        stars_200.click()
        stars_300 = page.get_by_role("tab", name="300 Stars")
        expect(stars_300).to_be_visible()
        expect(stars_300).to_have_text(re.compile(r"300.*Stars"))
        stars_300.click()
        stars_400 = page.get_by_role("tab", name="400 Stars")
        expect(stars_400).to_be_visible()
        expect(stars_400).to_have_text(re.compile(r"400.*Stars"))
        stars_400.click()
        stars_25 = page.get_by_role("tab", name="25 Stars")
        expect(stars_25).to_be_visible()
        expect(stars_25).to_have_text(re.compile(r"25.*Stars"))
        stars_25.click()

    def reward_slide(self, page):
        fun_freebies = page.get_by_role("button", name=re.compile(r"Learn more.*fun freebies"))
        expect(fun_freebies).to_be_visible()
        fun_freebies.click()
        next_btn = page.get_by_role("button", name="Next slide")
        expect(next_btn).to_be_visible()
        next_btn.click()
        next_btn.click()
        close_btn = page.locator("button:has(path[d^='M13.06 12'])")
        expect(close_btn).to_be_visible()
        close_btn.click()
        ordering = page.get_by_role("button", name=re.compile(r"Learn more.*ordering and paying ahead"))
        expect(ordering).to_be_visible()
        ordering.click()
        next_btn = page.get_by_role("button", name="Next slide")
        expect(next_btn).to_be_visible()
        next_btn.click()
        confirm_btn = page.locator("button.sb-swipe-deck--confirmButton")
        expect(confirm_btn).to_be_visible()
        expect(confirm_btn).to_have_text("Ok")
        confirm_btn.click()
        faster_rewards = page.get_by_role("button", name=re.compile(r"Learn more.*free rewards faster"))
        expect(faster_rewards).to_be_visible()
        faster_rewards.click()
        next_btn = page.get_by_role("button", name="Next slide")
        expect(next_btn).to_be_visible()
        next_btn.click()
        next_btn.click()
        prev_btn = page.get_by_role("button", name="Previous slide")
        expect(prev_btn).to_be_visible()
        prev_btn.click()
        prev_btn.click()
        close_btn = page.locator("button:has(path[d^='M13.06 12'])")
        expect(close_btn).to_be_visible()
        close_btn.click()

    def reward_links(self, page):
        delta_link = page.get_by_role(
            "link",
            name=re.compile(r"Link your Delta SkyMiles", re.I)
        )
        expect(delta_link).to_be_visible()
        delta_link.click()
        page.bring_to_front()
        marriott_link = page.get_by_role(
            "link",
            name=re.compile(r"Link your Marriott Bonvoy", re.I)
        )
        expect(marriott_link).to_be_visible()
        marriott_link.click()
        page.bring_to_front()
        join_rewards = page.get_by_role(
            "link",
            name=re.compile(r"Join Starbucks.*Rewards", re.I)
        )
        expect(join_rewards).to_be_visible()
        join_rewards.click()
        rewards_home = page.locator('a[href="/rewards"]')
        expect(rewards_home).to_be_visible()
        rewards_home.click()
        right_here = page.get_by_role(
            "link",
            name=re.compile(r"right over here", re.I)
        )
        expect(right_here).to_be_visible()
        right_here.click()
        page.bring_to_front()
        delta_terms = page.get_by_role(
            "link",
            name=re.compile(r"deltastarbucks\.com/terms", re.I)
        )
        expect(delta_terms).to_be_visible()
        delta_terms.click()
        page.bring_to_front()
        marriott_page = page.get_by_role(
            "link",
            name=re.compile(r"Starbucks\.com/MarriottBonvoy", re.I)
        )
        expect(marriott_page).to_be_visible()
        marriott_page.click()
        page.bring_to_front()
        rewards_terms = page.get_by_role(
            "link",
            name=re.compile(r"starbucks\.com/rewards/terms", re.I)
        )
        expect(rewards_terms).to_be_visible()
        rewards_terms.click()
        page.bring_to_front()
        store_locator = page.get_by_role(
            "link",
            name=re.compile(r"Starbucks Store Locator", re.I)
        )
        expect(store_locator).to_be_visible()
        store_locator.click()
        page.bring_to_front()

