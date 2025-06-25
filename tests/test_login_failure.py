from playwright.sync_api import sync_playwright

def test_user_login_fails_with_invalid_credentials():
    """
    Scenario: User fails to log in with wrong credentials
    Given the login page is open
    When the user enters invalid username or password
    And clicks the login button
    Then an error message should appear
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/")
        page.fill("input[name='username']", "WrongUser")
        page.fill("input[name='password']", "WrongPass")
        page.click("button[type='submit']")
        page.wait_for_selector("p:has-text('Invalid credentials')")
        assert page.locator("p:has-text('Invalid credentials')").is_visible()
        page.screenshot(path="login_failure.png")
        browser.close()