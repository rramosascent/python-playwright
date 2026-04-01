import pytest, re
from modules.frame_work.utility.utility_package import UtilityPackage
from modules.testcases.ptops.page_objects.sign_up_page import SignUpPageClass
from modules.testcases.ptops.data_objects.ptops_data_sets import DataSetCompilation
from modules.testcases.ptops.data_objects.ptops_data_objects import DataObjectRegistration
@pytest.mark.usefixtures("setup")
class TestSignUpTestSuite0001:
    @pytest.fixture(scope="function", autouse=True)
    def before_each_after_each(self):
        print("before the test runs")
        # Go to the starting url before each test.
        global registration_data, application_counter, test_page_objects, reg_data_obj
        test_page_objects = SignUpPageClass(self.driver)
        application_counter = UtilityPackage().padd_zeroes_2(1)
        reg_data = DataSetCompilation().ds_test_sign_sp_ts002
        reg_data_obj = DataObjectRegistration(self.driver, reg_data)
        yield
        print("after the test runs")
        # self.driver.wait_for_timeout(10000)
    def test_open_ptops_url_link_create_account(self):
        test_page_objects.open_url_ptops("http://112.199.119.250:96/peza/login")
        test_page_objects.landing_link_create_account()

    def test_select_registration_type(self):
        test_page_objects.select_registration_type(reg_data_obj.select_registration_type)
        test_page_objects.select_registration_type_proceed(reg_data_obj.click_registration_proceed)

    def test_registration_data_privacy(self):
        test_page_objects.registration_data_privacy_agreement(reg_data_obj.accept_registration_data_privacy)
        test_page_objects.registration_data_privacy_agreement_proceed()

    def test_registration_company_info(self):
        test_page_objects.registration_company_info_type(reg_data_obj.select_comp_info_type)
        test_page_objects.registration_company_info_name(f"{reg_data_obj.select_comp_info_name}{application_counter}")
        test_page_objects.registration_company_info_tin(f"{reg_data_obj.select_comp_info_tin}{application_counter}")

    def test_registration_company_address(self):
        test_page_objects.registration_company_address_region(reg_data_obj.select_comp_add_region)
        test_page_objects.registration_company_address_province(reg_data_obj.select_comp_add_province)
        test_page_objects.registration_company_address_city(reg_data_obj.select_comp_add_city)
        test_page_objects.registration_company_address_barangay(reg_data_obj.select_comp_add_barangay)
        test_page_objects.registration_company_address_street(f"{reg_data_obj.select_comp_add_street}{application_counter}")

    def test_registration_contact(self):
        test_page_objects.registration_company_contact_mobile_no(reg_data_obj.input_contact_mobile)
        test_page_objects.registration_company_contact_landline(reg_data_obj.input_contact_landline)
        test_page_objects.registration_company_contact_email(f"{reg_data_obj.input_contact_email_p1}{application_counter}{reg_data_obj.input_contact_email_p2}")

    def test_registration_sup_docs_bir(self):
        test_page_objects.registration_supporting_documents_2(reg_data_obj.select_supporting_docs_1)
        test_page_objects.registration_supporting_upload_2()
        
    def test_registration_sup_docs_sec_certificate(self):
        test_page_objects.registration_supporting_documents(reg_data_obj.select_supporting_docs_2)
        test_page_objects.registration_supporting_upload()

    def test_registration_account_information(self):
        test_page_objects.registration_account_info_last_name(reg_data_obj.input_account_info_lname)
        test_page_objects.registration_account_info_first_name(reg_data_obj.input_account_info_fname)
        test_page_objects.registration_account_info_middle_name(reg_data_obj.input_account_info_mname)
        test_page_objects.registration_account_info_position(reg_data_obj.input_account_info_position)
        test_page_objects.registration_account_info_contact_no(reg_data_obj.get_registration_account_inf_contact_no())

    def test_registration_user_credentials(self):
        test_page_objects.registration_account_info_email(f"{reg_data_obj.input_user_creds_email_1}{application_counter}{reg_data_obj.input_user_creds_email_2}")
        test_page_objects.registration_account_info_uname(f"{reg_data_obj.input_user_creds_user_name}{application_counter}")
        test_page_objects.registration_account_info_pword(reg_data_obj.input_user_creds_pword)
        test_page_objects.registration_account_info_pword_c(reg_data_obj.input_user_creds_pword_c)

        page = self.driver
        page.wait_for_timeout(10000)

