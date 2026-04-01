import os
import pytest
import csv

from piglet.parsers.semicolonseparated import value
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from modules.testcases.ptops.page_objects.login_page import LoginPage
from modules.testcases.ptops.page_objects.menu_item_page import MenuItemsPage
from modules.testcases.ptops.page_objects.berms_ee_pom.berms_status_change_page import BermsStatusChangePage
from modules.training.tests_ptops.test_ecai_approval import application_id
from modules.frame_work.utility.custom_logger import log

load_dotenv()

BASE_URL = os.getenv("PEZA_URL")

# Step 1: Read the CSV file
with open("berms_ee_id.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    values = [row["id_value"] for row in reader]

# Step 2: Select the second row (index 1, since Python is zero-based)
    application_id = values[4]

# application_number = "AN-1346132HE"

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
    login_page.login(os.getenv("USER_PRESCREENER"), os.getenv("PASS_PRESCREENER"))

    yield page

    # Closing the context also closes the page
    context.close()


# @pytest.mark.skip
def test_for_screening(page): #1
    menu_items_page = MenuItemsPage(page)
    berms_status_change_page = BermsStatusChangePage(page)
    login_page = LoginPage(page)

    menu_items_page.navigate_to_berms_application()
    berms_status_change_page.select_application_number(application_id)
    berms_status_change_page.change_status_to_prescreened()
    login_page.logout()

# @pytest.mark.skip
def test_for_af_payment(page): #2
    menu_items_page = MenuItemsPage(page)
    berms_status_change_page = BermsStatusChangePage(page)
    login_page = LoginPage(page)

    login_page.login(os.getenv("TEST_USER"), os.getenv("TEST_PASS"))
    menu_items_page.navigate_to_berms_application()
    berms_status_change_page.select_application_number(application_id)
    berms_status_change_page.do_af_payment()
    login_page.logout()
# @pytest.mark.skip
def test_for_eso_assignment(page): #3
    menu_items_page = MenuItemsPage(page)
    berms_status_change_page = BermsStatusChangePage(page)
    login_page = LoginPage(page)

    login_page.login(os.getenv("USER_DC"), os.getenv("PASS_DC"))
    menu_items_page.navigate_to_berms_application()
    berms_status_change_page.select_application_number(application_id)
    berms_status_change_page.do_eso_assignment()
    login_page.logout()
# @pytest.mark.skip
def test_for_evaluation_report_approval(page): #4
    menu_items_page = MenuItemsPage(page)
    berms_status_change_page = BermsStatusChangePage(page)
    login_page = LoginPage(page)

    login_page.login(os.getenv("USER_EVALUATOR"), os.getenv("PASS_EVALUATOR"))
    menu_items_page.navigate_to_berms_application()
    berms_status_change_page.select_application_number(application_id)
    berms_status_change_page.do_evaluation_report_approval()
    login_page.logout()
# @pytest.mark.skip
def test_for_evaluation_report(page): #5
    berms_status_change_page = BermsStatusChangePage(page)
    menu_items_page = MenuItemsPage(page)
    login_page = LoginPage(page)

    login_page.login(os.getenv("USER_EVALUATOR"), os.getenv("PASS_EVALUATOR"))# delete this
    menu_items_page.navigate_to_berms_application()# delete this

    berms_status_change_page.select_application_number(application_id)
    berms_status_change_page.do_evaluation_report()
    login_page.logout()
# @pytest.mark.skip
def test_for_endorsement_of_DC(page): #6
    menu_items_page = MenuItemsPage(page)
    berms_status_change_page = BermsStatusChangePage(page)
    login_page = LoginPage(page)

    login_page.login(os.getenv("USER_DC"), os.getenv("PASS_DC"))
    menu_items_page.navigate_to_berms_application()
    berms_status_change_page.select_application_number(application_id)
    berms_status_change_page.do_endorsement_of_dc()
    login_page.logout()
# @pytest.mark.skip
def test_for_endorsement_of_DM(page): #7
    menu_items_page = MenuItemsPage(page)
    berms_status_change_page = BermsStatusChangePage(page)
    login_page = LoginPage(page)

    login_page.login(os.getenv("USER_DM"), os.getenv("PASS_DM"))
    menu_items_page.navigate_to_berms_application()
    berms_status_change_page.select_application_number(application_id)
    berms_status_change_page.do_endorsement_of_dm()
    login_page.logout()
# @pytest.mark.skip
def test_for_endorsement_of_GM(page): #8
    menu_items_page = MenuItemsPage(page)
    berms_status_change_page = BermsStatusChangePage(page)
    login_page = LoginPage(page)

    login_page.login(os.getenv("USER_GM"), os.getenv("PASS_GM"))
    menu_items_page.navigate_to_berms_application()
    berms_status_change_page.select_application_number(application_id)
    berms_status_change_page.do_endorsement_of_gm()
    login_page.logout()
# @pytest.mark.skip
def test_for_endorsement_of_DDG(page): #9
    menu_items_page = MenuItemsPage(page)
    berms_status_change_page = BermsStatusChangePage(page)
    login_page = LoginPage(page)

    login_page.login(os.getenv("USER_DDG"), os.getenv("PASS_DDG"))
    menu_items_page.navigate_to_berms_application()
    berms_status_change_page.select_application_number(application_id)
    berms_status_change_page.do_endorsement_of_ddg()
    login_page.logout()
# @pytest.mark.skip
def test_for_board_consideration(page): #10
    menu_items_page = MenuItemsPage(page)
    berms_status_change_page = BermsStatusChangePage(page)
    login_page = LoginPage(page)

    login_page.login(os.getenv("USER_DG"), os.getenv("PASS_DG"))
    menu_items_page.navigate_to_berms_application()
    berms_status_change_page.select_application_number(application_id)
    berms_status_change_page.do_board_consideration()
    login_page.logout()
# @pytest.mark.skip
def test_for_pb_approval(page): #11
    menu_items_page = MenuItemsPage(page)
    berms_status_change_page = BermsStatusChangePage(page)
    login_page = LoginPage(page)

    login_page.login(os.getenv("USER_ODG"), os.getenv("PASS_ODG"))
    menu_items_page.navigate_to_berms_application()
    berms_status_change_page.select_application_number(application_id)
    berms_status_change_page.do_pb_approval()
    login_page.logout()
# @pytest.mark.skip
def test_for_issuance_of_board_consideration(page): #12
    menu_items_page = MenuItemsPage(page)
    berms_status_change_page = BermsStatusChangePage(page)
    login_page = LoginPage(page)

    login_page.login(os.getenv("USER_ODG"), os.getenv("PASS_ODG"))
    menu_items_page.navigate_to_berms_application()
    berms_status_change_page.select_application_number(application_id)
    berms_status_change_page.do_issuance_of_board_consideration()
    login_page.logout()
# @pytest.mark.skip
def test_for_registration_payment(page): #13
    menu_items_page = MenuItemsPage(page)
    berms_status_change_page = BermsStatusChangePage(page)
    login_page = LoginPage(page)

    login_page.login(os.getenv("TEST_USER"), os.getenv("TEST_PASS"))
    menu_items_page.navigate_to_berms_application()
    berms_status_change_page.select_application_number(application_id)
    berms_status_change_page.do_registration_payment()
    login_page.logout()

def test_for_ra_uploading(page): #14
    menu_items_page = MenuItemsPage(page)
    berms_status_change_page = BermsStatusChangePage(page)
    login_page = LoginPage(page)

    login_page.login(os.getenv("USER_RMU"), os.getenv("PASS_RMU"))
    menu_items_page.navigate_to_berms_application()
    berms_status_change_page.select_application_number(application_id)
    berms_status_change_page.do_ra_uploading()
    login_page.logout()

def test_for_preparation_of_cor(page): #15
    menu_items_page = MenuItemsPage(page)
    berms_status_change_page = BermsStatusChangePage(page)
    login_page = LoginPage(page)

    login_page.login(os.getenv("USER_RMU"), os.getenv("PASS_RMU"))
    menu_items_page.navigate_to_berms_application()
    berms_status_change_page.select_application_number(application_id)
    berms_status_change_page.do_preparation_of_cor()
    login_page.logout()