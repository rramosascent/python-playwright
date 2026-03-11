import pytest, re
from modules.frame_work.utility.utility_package import UtilityPackage
from modules.testcases.ptops.page_objects.sign_up_page import SignUpPageClass
@pytest.mark.usefixtures("setup")
class TestSignUpTestSuite0001:
    @pytest.fixture(scope="function", autouse=True)
    def before_each_after_each(self):
        print("before the test runs")
        # Go to the starting url before each test.
        global test_page_objects
        test_page_objects = SignUpPageClass(self.driver)
        global application_counter
        application_counter = UtilityPackage().padd_zeroes_2(1)
        yield
        print("after the test runs")
        # self.driver.wait_for_timeout(10000)
    def test_open_ptops_url_link_create_account(self):
        test_page_objects.open_url_ptops("http://192.168.20.25:82/peza/login")
        test_page_objects.landing_link_create_account()

    def test_select_registration_type(self):
        test_page_objects.select_registration_type("Ecozone/Business Enterprise")
        test_page_objects.select_registration_type_proceed("Proceed to Registration Form ")

    def test_registration_data_privacy(self):
        test_page_objects.registration_data_privacy_agreement("I have read and agree to the")
        test_page_objects.registration_data_privacy_agreement_proceed()

    def test_registration_company_info(self):
        test_page_objects.registration_company_info_type("Corporation")
        test_page_objects.registration_company_info_name(f"COMPANY EE CORPORATION C{application_counter}")
        test_page_objects.registration_company_info_tin(f"999-999-200-{application_counter}")

    def test_registration_company_address(self):
        test_page_objects.registration_company_address_region("NATIONAL CAPITAL REGION (NCR)")
        test_page_objects.registration_company_address_province("METRO MANILA")
        test_page_objects.registration_company_address_city("CALOOCAN CITY")
        test_page_objects.registration_company_address_barangay("BARANGAY 1")
        test_page_objects.registration_company_address_street("COMPANY NAME A001 STREET NAME TESTING")

    def test_registration_contact(self):
        test_page_objects.registration_company_contact_mobile_no("+63-9999999999")
        test_page_objects.registration_company_contact_landline("+6399-9999999")
        test_page_objects.registration_company_contact_email(f"rramos.ascent+c{application_counter}@gmail.com")

    def test_registration_sup_docs_bir(self):
        test_page_objects.registration_supporting_documents_2("Testing_document.png")
        test_page_objects.registration_supporting_upload_2()

    def test_registration_sup_docs_sec_certificate(self):
        test_page_objects.registration_supporting_documents("Testing_document.png")
        test_page_objects.registration_supporting_upload()

    def test_registration_account_information(self):
        test_page_objects.registration_account_info_last_name("LNAME")
        test_page_objects.registration_account_info_first_name("FNAME")
        test_page_objects.registration_account_info_middle_name("")
        test_page_objects.registration_account_info_position("POSITION")
        test_page_objects.registration_account_info_contact_no("+63-9999999999")

    def test_registration_user_credentials(self):
        test_page_objects.registration_account_info_email(f"rramos.ascent+c{application_counter}@gmail.com")
        test_page_objects.registration_account_info_uname(f"TESTCT{application_counter}")
        test_page_objects.registration_account_info_pword("Password123!")
        test_page_objects.registration_account_info_pword_c("Password123!")

        page = self.driver
        page.wait_for_timeout(10000)

