import pytest
import os
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from modules.testcases.ptops.page_objects.login_page import LoginPage
from modules.testcases.ptops.page_objects.menu_item_page import MenuItemsPage
from modules.testcases.ptops.page_objects.ecai_ee_pom.ecai_application_page import EcaiApplicationPage
from modules.testcases.ptops.page_objects.ecai_ee_pom.ecai_status_change_page import EcaiStatusChangePage

load_dotenv() # Load variables from .env
BASE_URL = os.getenv("PEZA_URL")
application_id = "ANEC-6844285RK"

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
    login_page.login(os.getenv("USER_ZM"), os.getenv("PASS_ZM"))

    yield page

    # Closing the context also closes the page
    context.close()

def test_for_evaluation(page):
    menu_items_page = MenuItemsPage(page)
    ecai_status_change_page = EcaiStatusChangePage(page)
    login_page = LoginPage(page)

    menu_items_page.navigate_to_ecai_application()
    ecai_status_change_page.select_application_number(application_id)
    # Evaluate all importable
    ecai_status_change_page.change_status_to_evaluation()
    login_page.logout()

def test_for_pending_approval(page):
    menu_items_page = MenuItemsPage(page)
    ecai_status_change_page = EcaiStatusChangePage(page)
    login_page = LoginPage(page)

    login_page.login(os.getenv("USER_EOD_DM"), os.getenv("PASS_EOD_DM"))
    menu_items_page.navigate_to_ecai_application()
    ecai_status_change_page.select_application_number(application_id)
    ecai_status_change_page.change_status_to_approval()