from playwright.sync_api import sync_playwright

def test_user_can_login_successfully():
    """
    Scenario: User logs in with valid credentials
    Given the login page is open
    When the user enters valid username and password
    And clicks the login button
    Then the user should be redirected to the dashboard
    And the word 'Dashboard' should be visible
    """
    with sync_playwright() as p:
        # browser = p.chromium.launch(headless=False)
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/")
        page.fill("input[name='username']", "Admin")
        page.fill("input[name='password']", "admin123")
        page.click("button[type='submit']")
        page.wait_for_selector("h6:has-text('Dashboard')")
        assert page.locator("h6:has-text('Dashboard')").is_visible()
        page.screenshot(path="login_success.png")
        browser.close()