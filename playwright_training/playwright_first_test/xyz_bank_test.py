class Testglobalqa():

    def test_manager_login(self, setup_playwright):
        page = setup_playwright
        page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        elements = page.query_selector_all("[class*='primary btn-lg]")
        elements[1].click()






