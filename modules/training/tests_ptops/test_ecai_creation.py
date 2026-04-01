import pytest
import os
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from modules.testcases.ptops.page_objects.login_page import LoginPage
from modules.testcases.ptops.page_objects.menu_item_page import MenuItemsPage
from modules.testcases.ptops.page_objects.ecai_ee_pom.ecai_dt_page import EcaiDtPage
from modules.testcases.ptops.page_objects.ecai_ee_pom.ecai_application_page import EcaiApplicationPage

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
    ecai_dt_page = EcaiDtPage(page)
    ecai_application_page = EcaiApplicationPage(page)

    menu_items_page.navigate_to_ecai_application()
    ecai_dt_page.click_new_application()
    ecai_application_page.fillup_ecai_application(
        application_type="PRIMARY",
        zone_location="[1THH] 1 Nito Tower",
        enterprise_type="Export Enterprise"
    )

def test_create_ecai_item(page):
    ecai_application_page = EcaiApplicationPage(page)
    ecai_application_page.fillup_item(
        item_code="qc001",
        item_description="description 001",
        search_box_ahtn_code="123",
        loa_number="123456",
        loa_validity_date="2027-03-22",
        generic_category="test 101",
        opt_nature_of_import="[ADH] Adhesive"
    )

# def test_upload_multiple_items(page):
#     ecai_application_page = EcaiApplicationPage(page)
#     ecai_application_page.upload_multiple_items()

def test_af_payment(page):
    ecai_application_page = EcaiApplicationPage(page)
    ecai_application_page.proceed_to_payment()
    ecai_application_page.get_value_application_id()

# Scenarios for ecai creation
# 1. Primary > one item > one registered activity
# 2. Primary > more than two item (500 items) > one registered activity
# 3. Supplementary > one item > one registered activity
# 4. Supplementary > more than two item (500 items) > one registered activity

# 5. Primary > one item > two or more registered activity
# 6. Primary > more than two item (500 items) > two or more registered activity
# 7. Supplementary > one item > two or more registered activity
# 8. Supplementary > more than two item (500 items) > two or more registered activity


# Scenarios for ecai approval
# 1. Primary > one item > evaluate importable > approved
# 2. Primary > one item > evaluate importable > disapprove
# 3. Primary > one item > reject importable > approved
# 4. Primary > one item > reject importable > disapprove

# 5. Primary > more than two items > evaluate all importable > approved
# 6. Primary > more than two items > evaluate all importable > disapprove
# 7. Primary > more than two items > reject all importable > approved
# 8. Primary > more than two items > reject all importable > disapprove

# 9. Primary > more than two items > evaluate two or more importable > (dont update the others) > approved
# 10. Primary > more than two items > evaluate two or more importable > (dont update the others) > disapprove
# 11. Primary > more than two items > reject two or more importable > (dont update the others) > approved
# 12. Primary > more than two items > reject two or more importable > (dont update the others) > disapprove

# 13. Primary > more than two items > evaluate two or more importable > reject the rest of importable > approved
# 14. Primary > more than two items > evaluate two or more importable > reject the rest of importable > disapprove

# 15. Primary > more than two items > evaluate two or more importable > reject two or more importable > (dont update the others) > approved
# 16. Primary > more than two items > evaluate two or more importable > reject two or more importable > (dont update the others) > disapprove
