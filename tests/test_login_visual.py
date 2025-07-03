import os
from dotenv import load_dotenv
from applitools.playwright import Eyes, Target
from playwright.sync_api import sync_playwright

load_dotenv()

def test_visual_login():
    eyes = Eyes()
    eyes.api_key = os.getenv("APPLITOOLS_API_KEY")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Abrir Applitools Eyes
        eyes.open(page, "OrangeHRM", "Visual Login Test", {'width': 1024, 'height': 768})

        # Acessar a página
        page.goto("https://opensource-demo.orangehrmlive.com/")

        # Tirar o primeiro snapshot
        eyes.check("Login Page", Target.window().fully())

        # Fazer login
        page.fill('input[name="username"]', "Admin")
        page.fill('input[name="password"]', "admin123")
        page.click('button[type="submit"]')

        # Esperar e capturar a próxima tela
        page.wait_for_url("**/web/index.php/dashboard/**")
        eyes.check("Dashboard Page", Target.window().fully())

        # Fechar Eyes e navegador
        eyes.close()
        browser.close()
