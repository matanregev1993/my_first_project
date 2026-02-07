class MainPage:

    def test_main(self, setup_playwright_project):
       page = setup_playwright_project
       page.goto("https://www.nike.com/")
