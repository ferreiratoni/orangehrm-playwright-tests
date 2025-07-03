import os
from dotenv import load_dotenv
from applitools.playwright import Eyes, Target
from playwright.sync_api import sync_playwright

# Load environment variables from .env file
load_dotenv()

def test_visual_login():
    eyes = Eyes()
    eyes.api_key = os.getenv("APPLITOOLS_API_KEY")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Start Applitools Eyes session
        eyes.open(page, "OrangeHRM", "Visual Login Test", {'width': 1024, 'height': 768})

        # Navigate to the login page
        page.goto("https://opensource-demo.orangehrmlive.com/")

        # Take snapshot of the login page
        eyes.check("Login Page", Target.window().fully())

        # Perform login
        page.fill('input[name="username"]', "Admin")
        page.fill('input[name="password"]', "admin123")
        page.click('button[type="submit"]')

        # Wait for dashboard page and take snapshot
        page.wait_for_url("**/web/index.php/dashboard/**")
        eyes.check("Dashboard Page", Target.window().fully())

        # Close Applitools session and browser
        eyes.close()
        browser.close()
