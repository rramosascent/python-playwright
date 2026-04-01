import pytest
import os
import json
from faker import Faker
from pathlib import Path
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from modules.testcases.ptops.page_objects.login_page import LoginPage
from modules.testcases.ptops.page_objects.menu_item_page import MenuItemsPage
from modules.testcases.ptops.page_objects.berms_ee_pom.berms_dt_page import BermsDtPage
from modules.testcases.ptops.page_objects.berms_ee_pom.berms_undertaking_page import BermsUndertakingPage
from modules.testcases.ptops.page_objects.berms_ee_pom.berms_application_page import BermsApplicationPage
from modules.testcases.ptops.page_objects.berms_ee_pom.berms_information_page import BermsInformationPage
from modules.testcases.ptops.page_objects.berms_ee_pom.berms_business_activities_page import BermsBusinessActivitiesPage
from modules.testcases.ptops.page_objects.berms_ee_pom.berms_existing_business_page import BermsExistingBusinessPage
from modules.testcases.ptops.page_objects.berms_ee_pom.berms_stockholders_page import BermsStockholdersPage
from modules.testcases.ptops.page_objects.berms_ee_pom.berms_manpower_timetable_page import BermsManpowerTimetablePage
from modules.testcases.ptops.page_objects.berms_ee_pom.berms_manufacturing_flow_page import BermsManufacturingFlowPage
from modules.testcases.ptops.page_objects.berms_ee_pom.berms_machinery_schedule_page import BermsMachinerySchedulePage
from modules.testcases.ptops.page_objects.berms_ee_pom.berms_area_disposal_page import BermsAreaDisposalPage
from modules.testcases.ptops.page_objects.berms_ee_pom.berms_market_aspect_page import BermsMarketAspectPage
from modules.testcases.ptops.page_objects.berms_ee_pom.berms_project_page import BermsProjectPage
from modules.testcases.ptops.page_objects.berms_ee_pom.berms_supporting_docs import BermsSupportingDocsPage
from modules.frame_work.utility.custom_logger import log

load_dotenv() # Load variables from .env
BASE_URL = os.getenv("PEZA_URL")
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

    # Perform login
    login_page = LoginPage(page)
    login_page.login(os.getenv("TEST_USER"), os.getenv("TEST_PASS"))

    yield page

    # Closing the context also closes the page
    context.close()

# NEW ECOZONE ENTERPRISE > DOMESTIC MARKET > ZONE = [2CYV] [24]7 PLAZA

def test_create_ee_berms_application(page):
    # Load JSON file from your project
    json_path = Path("modules/testcases/ptops/data_objects/berms_ee_new.json")

    with open(json_path, "r") as f:
        parsed = json.load(f)

    # Access the nested structure
    name = parsed["type_of_application"]["name"]
    ee_values = parsed["type_of_application"]["type_of_ee"]

    # Loop through ee_values while keeping the same name
    for ee in ee_values:
        menu_item_page = MenuItemsPage(page)
        menu_item_page.navigate_to_berms_application()
        berms_dt_page = BermsDtPage(page)
        berms_undertaking_page = BermsUndertakingPage(page)
        berms_application_page = BermsApplicationPage(page)
        berms_information_page = BermsInformationPage(page)
        berms_business_activities_page = BermsBusinessActivitiesPage(page)
        berms_existing_business_page = BermsExistingBusinessPage(page)
        berms_stockholders_page = BermsStockholdersPage(page)
        berms_manpower_timetable_page = BermsManpowerTimetablePage(page)
        berms_manufacturing_flow_page = BermsManufacturingFlowPage(page)
        berms_machinery_schedule_page = BermsMachinerySchedulePage(page)
        berms_area_disposal_page = BermsAreaDisposalPage(page)
        berms_market_aspect_page = BermsMarketAspectPage(page)
        berms_project_page = BermsProjectPage(page)
        berms_supporting_docs = BermsSupportingDocsPage(page)

        berms_dt_page.click_new_ecozone_enterprise()
        berms_undertaking_page.agree_applicants_undertaking()

        # Application
        berms_application_page.fillup_berms_application(
            type_of_application=name, #NEW ECOZONE ENTERPRISE
            market=ee,
            section_code="Accommodation and Food Service Activities",
            division_code="[55] ACCOMMODATION",
            groups_code="[559] Other accommodation",
            classes_code="[5590] Other accommodation",
            sub_classes_code="[55901] Dormitories/boarding houses"
        )

        #Company and Personal Information
        berms_information_page.fillup_berms_information(
            company_name=fake.company(),
            country="[PH] Philippines",
            business_nature="Test 101",
            business_profile="Test 101",
            landline="912312321"
        )

        # Business Product Activities
        berms_business_activities_page.fillup_berms_business_activities(
            proposed_product_activity="Proposed Product/Activity 001",
            description="Lorem ipsum dolor sit amet",
            uses_application="test 101",
            upload_image_product="modules/Testing_document.png"
        )

        # Existing Business Registration
        berms_existing_business_page.fillup_berms_existing_business(
            date="04262026",
            registration_number="13254",
            sec_primary_purpose="test 101",
            authorized_amount="1",
            subscribed_amount="1",
            paid_up_amount="1"
        )

        # Stockholders & Principal Officers
        berms_stockholders_page.fillup_berms_stockholders(
            stockholder_salutation="Mr.",
            stockholder_first_name="John",
            stockholder_last_name="Doe",
            stockholder_nationality="Filipino",
            stockholder_shares="10",
            stockholder_subscribe_amount="10",
            stockholder_paidup_amount="10",
            principal_officer_salutation="Mr.",
            principal_officer_first_name="John",
            principal_officer_last_name="Doe",
            principal_officer_nationality="Filipino",
            principal_officer_position="CEO"
        )

        # Manpower & Timetable
        berms_manpower_timetable_page.fillup_berms_manpower_timetable(
            service_personnel_1="10",
            service_personnel_2="10",
            service_personnel_3="10",
            indirect_personnel_1="10",
            indirect_personnel_2="10",
            indirect_personnel_3="10",
            admin_personnel_1="10",
            admin_personnel_2="10",
            admin_personnel_3="10"
        )

        # Manufacturing Process & Service Flow
        berms_manufacturing_flow_page.fillup_berms_manufacturing_flow(
            manufacturing_process_service_flow="test 101",
            upload_product_image="modules/Testing_document.png"
        )

        # Machinery, Raw Material Production Schedule
        berms_machinery_schedule_page.fillup_berms_machinery_schedule(
            machinery_description="test 101",
            machinery_quantity="1",
            machinery_unit_price="100",
            machinery_source="LOCAL (NEW)",
            raw_material_description="test 101",
            raw_material_source="LOCAL (NEW)",
            no_of_shifts="1",
            no_of_hours="1",
            no_of_operating_days="1"
        )

        # Areas, Utilities and waste Disposal
        berms_area_disposal_page.fillup_berms_area_disposal(
            area_sqm="100",
            location_zone="[1THH] 1 Nito Tower", # will be change this after
            zone_region="REGION I (ILOCOS REGION)",
            zone_province="ILOCOS SUR",
            zone_city_municipality="BANTAY",
            zone_barangay="AGGAY",
            zone_street_name="test 101",
            building_owner_first_name="test",
            building_owner_middle_name="test",
            building_owner_last_name="test",
            lot_owner_first_name="test",
            lot_owner_middle_name="test",
            lot_owner_last_name="test",
            lessor_first_name="test",
            lessor_middle_name="test",
            lessor_last_name="test",
            water="100",
            electricity="100",
            waste_products_description="test 101",
            waste_discussion_disposal="test 101",
            upload_waste_description_docs="modules/Testing_document.png",
            upload_waste_disposal_docs="modules/Testing_document.png"
        )

        # Market Aspect
        berms_market_aspect_page.fillup_berms_market_aspect(
            percent_export="10%",
            country_of_export_market="[PH] Philippines",
            domestic_client="test 101",
            export_selling_price="10",
            export_domestic_price="10",
            unit_of_measure="[BFT] Board foot",
            export_volume_1="10",
            export_volume_2="10",
            export_volume_3="10",
            local_market_volume_1="10",
            local_market_volume_2="10",
            local_market_volume_3="10"
        )

        # Project Cost & Source of Financing
        berms_project_page.fillup_berms_project(
            building_construction_amount="10",
            factory_tools_amount="10",
            transportation_amount="10",
            office_equipment_amount="10",
            other_assets_amount="10",
            assets_remarks="test",
            pre_operating_expenses_amount="10",
            working_capital_amount="10",
            equity_amount="10",
            advances_amount="0",
            loans_amount="0"
        )

        berms_supporting_docs.berms_ee_transaction(name, ee)

        berms_supporting_docs.click_proceed()

        # Confirmation
        berms_supporting_docs.application_confirmation()
