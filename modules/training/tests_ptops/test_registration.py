import pytest
import os
from faker import Faker
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from modules.testcases.ptops.page_objects.ptops_registration.ptops_registration_page import PtopsRegistrationPage

load_dotenv() # Load variables from .env
BASE_URL = os.getenv("PROD_MIRROR_URL")
fake = Faker()

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

    yield page

    # Closing the context also closes the page
    context.close()

def test_registration_page(page):
    ptops_registration_page = PtopsRegistrationPage(page)

    ptops_registration_page.goto_registration_form(type_of_registration="ee")
    # ptops_registration_page.test_connection()
    ptops_registration_page.fillup_company_registration(
        company_type="Sole Proprietorship",
        company_name=fake.company(),
        tin="737331377373",
        region="REGION I (ILOCOS REGION)",
        province="ILOCOS SUR",
        city="BANAYOYO",
        barangay="BISANGOL",
        street_name="test 101",
        company_mobile_number="323132132",
        company_landline="565656565",
        company_email=fake.email()
    )
    ptops_registration_page.fillup_account_information(
        last_name=fake.last_name(),
        first_name=fake.first_name(),
        middle_name="test",
        position="qa qc",
        contact_mobile_number="323132132",
        contact_email=fake.email(),
        contact_username="ee_qa_01",
        contact_password="Password_123",
        confirm_password="Password_123"
    )
    ptops_registration_page.fillup_otp_registration()



