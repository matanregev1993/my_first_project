from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    user = page.locator("[id='user-name']")
    user.fill("standard_user")
    password = page.locator("[id='password']")
    password.fill("secret_sauce")
    login_button = page.locator("[name='login-button']")
    login_button.click()

    page.close()
    browser.close()
    print ("Test end****")