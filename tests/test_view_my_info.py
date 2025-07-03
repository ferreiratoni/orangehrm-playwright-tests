from playwright.sync_api import sync_playwright


def test_user_can_view_my_info():
    """
    Scenario: User views personal information
    Given the user is logged into the OrangeHRM dashboard
    When the user clicks on 'My Info' in the side menu
    Then the employee's personal information page should be displayed
    And the full name of the employee should be visible
    """
    with sync_playwright() as p:
        # browser = p.chromium.launch(headless=False)
        browser = p.chromium.launch()
        page = browser.new_page()

        # Step 1: Login
        page.goto("https://opensource-demo.orangehrmlive.com/")
        page.fill('input[name="username"]', "Admin")
        page.fill('input[name="password"]', "admin123")
        page.click('button[type="submit"]')

        # Step 2: Wait for dashboard and click My Info
        page.wait_for_selector("text=Dashboard")
        page.click('a[href="/web/index.php/pim/viewMyDetails"]')

        # Step 3: Assert that employee info is visible
        # Step 3.1: Wait until the input has a non-empty value
        page.wait_for_function(
            """() => {
                const input = document.querySelector('input[name="firstName"]');
                return input && input.value && input.value.trim().length > 0;
            }"""
        )

        employee_name = page.eval_on_selector('input[name="firstName"]', 'el => el.value')
        print("Employee name found:", employee_name)
        assert employee_name is not None and len(employee_name.strip()) > 0
        page.wait_for_load_state("load")
        page.wait_for_timeout(6000)
        page.screenshot(path="test_view_my_info.png")

        browser.close()
