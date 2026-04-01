import pytest
import os
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from modules.testcases.ptops.page_objects.login_page import LoginPage
from modules.testcases.ptops.page_objects.menu_item_page import MenuItemsPage
from modules.testcases.ptops.page_objects.vat_zero_ee_pom.vat_dt_page import VatDtPage
from modules.testcases.ptops.page_objects.vat_zero_ee_pom.vat_zero_application_page import VatApplicationPage

load_dotenv() # Load variables from .env
BASE_URL = os.getenv("PEZA_URL")

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # 'no_viewport=True' is required for '--start-maximized' to actually work
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def page(browser):
    # Contexts allow for clean state and viewport control
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    page.goto(BASE_URL, wait_until="domcontentloaded")

    # Perform login
    login_page = LoginPage(page)
    login_page.login(os.getenv("TEST_USER"), os.getenv("TEST_PASS"))

    yield page

    # Closing the context also closes the page
    context.close()

def test_create_new_ecai_application(page):
    menu_items_page = MenuItemsPage(page)
    vat_dt_page = VatDtPage(page)
    vat_application_page = VatApplicationPage(page)

    menu_items_page.navigate_to_vat_zero_application()
    vat_dt_page.click_new_application()
    vat_application_page.fillup_vat_application(
        application_type="NEW",
        responsible_officer="KELSIE HOFFMAN",
        tin="11",
        sales_summary="modules/Testing_document.png",
        notarized_undertaking="modules/Testing_document.png"
    )
