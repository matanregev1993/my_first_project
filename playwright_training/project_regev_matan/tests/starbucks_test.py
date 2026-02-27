from playwright_training.project_regev_matan.pages.gift_card_page import GiftCardPage
from playwright_training.project_regev_matan.pages.main_page import MainPage
from playwright_training.project_regev_matan.pages.menu_page import MenuPage
from playwright_training.project_regev_matan.pages.reward_page import RewardPage
from playwright_training.project_regev_matan.pages.search_page import SearchPage

class TestStarbuck:

    def test_menu_page (self, setup_playwright_project):
        page = setup_playwright_project
        main = MainPage()
        menu = MenuPage()
        main.main_page(page)
        menu.menu_page(page)
        menu.featured_look(page)
        menu.rest_of_subbar(page)
        main.come_home(page)

    def test_reward_page(self, setup_playwright_project):
        page = setup_playwright_project
        reward = RewardPage()
        main = MainPage()
        main.main_page(page)
        reward.reward_nav(page)
        reward.reward_stars(page)
        reward.reward_slide(page)
        reward.reward_links(page)
        main.come_home(page)

    def test_gift_card(self, setup_playwright_project):
        page = setup_playwright_project
        main = MainPage()
        gift = GiftCardPage()
        main.main_page(page)
        gift.gift_card_basic(page)
        gift.gift_card_featured(page)
        gift.gift_card_extra(page)
        gift.gift_card_links(page)
        main.come_home(page)

    def test_main_page_nav(self, setup_playwright_project):
        page = setup_playwright_project
        main = MainPage()
        main.main_page(page)
        main.main_page_nav(page)

    def test_search_page(self, setup_playwright_project):
        page = setup_playwright_project
        main = MainPage()
        main.main_page(page)
        search = SearchPage()
        search.search_basic(page)
        search.search_delivery(page)
        search.search_links(page)
        main.come_home(page)