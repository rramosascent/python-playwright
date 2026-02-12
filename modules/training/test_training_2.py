import pytest
from modules.testcases.ecp.data_processing import DataProcessingClass

# @pytest.mark.usefixtures("setup")
# # def test_ecp(playwright: Playwright) -> None:
# class TestSuite001a():
#     def initiate_test_data(self):
#         return TestExecutionClass(self.driver)
#
#     def execute_login_to_ptops(self) -> None:
#         print('test')
#         # self.initiate_test_data().login_to_ptops('url')

@pytest.mark.usefixtures("setup")
# def test_ecp(playwright: Playwright) -> None:
class TestSuite0001():
    # @pytest.fixture(autouse=True)
    def initiate_test_data(self):
        return DataProcessingClass(self.driver)

    def test_ecp_login(self) -> None:
        login_data = {
            "link_login": ["open_url", "url"],
            "user_name": ["get_by_role_name", "textbox_a", "Username", "001"],
            "password": ["get_by_role_name", "textbox_b", "Password", "001"],
            "btn_sign_in": ["get_by_role_name", "button", "Sign in"],
            "verify_login_success": ["expect_by_role_name", "link", " Applications & Accreditations"],
        }
        self.initiate_test_data().data_processing_func_peza(login_data)

    def test_create_new_berms(self) -> None:
        data_element_action = {
            "lnk_apps_accre": ["get_by_role_name", "link", " Applications & Accreditations"],
            "verify_new_bersm_button": ["expect_by_role_name", "button", "+ New Ecozone Enterprise"],
            "btn_new_berms_apps": ["get_by_role_name", "button", "+ New Ecozone Enterprise"],
            "verify_undertaking_link:": ["expect_by_role_name", "link", "Undertaking"],
            "chbx_agree_ut": ["get_by_role_name", "checkbox", "I Agree"],
            "verify_btn_proceed_ut:": ["get_by_location", "expect", "#btnSubmitUndertaking"],
            "btn_proceed_ut:": ["get_by_location", "click", "#btnSubmitUndertaking"]
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_application(self) -> None:
        data_element_action = {
            "opt_app_type": ["get_by_role_combox_select", "#select2-applicationTypeId-container","NEW ECOZONE ENTERPRISE"],
            "rbtn_type_ezone": ["get_by_role_name","radio_b", "Export Enterprise"],
            "opt_psic_classification": ["get_by_role_combox_select", "#select2-sectionCodeId-container","Accommodation and Food"],
            "opt_psic_division": ["get_by_role_combox_select", "#select2-divisionCodeId-container","[56] FOOD AND BEVERAGE SERVICE ACTIVITIES"],
            "opt_psic_group": ["get_by_role_combox_select", "#select2-groupCodeId-container","[563] Beverage serving activities"],
            "opt_psic_class": ["get_by_role_combox_select", "#select2-classesCodeId-container","[5630] Beverage serving activities"],
            "opt_psic_sub_class": ["get_by_role_combox_select", "#select2-subClassesCodeId-container","[56309] Other beverage serving activities, n.e.c."],
            "btn_proceed_app": ["get_by_role_name", "button", "Proceed"]
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_company_pesonal_info(self) -> None:
        data_element_action = {
            "txt_company_name": ["get_by_role_name", "textbox_a", "Company Name", "COMPANY NAME TESTING 001"],
            "txt_nature_business": ["get_by_role_name", "textbox_a", "Nature of Business", "NATURE OF BUSINESS TESTING 00"],
            "txt_company_profile": ["get_by_role_name", "textbox_a", "Company Profile", "COMPANY PROFILE TESTING 001"],
            "btn_san_company_person_info": ["get_by_role_name", "button", "Save and Proceed"]
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_company_proposed_project(self) -> None:
        data_element_action = {
            "btn_proposed_project": ["get_by_location", "click", "#btnBusinessProduct"],
            "txt_proposed_project": ["get_by_location_fill_b", "#newBusinessProductActivity", "NEW PROPOSES PRODUCT ACTIVITY 001"],
            "btn_proposed_project_add": ["get_by_role_name", "button", " Add"],
            "txt_proposed_project_desc": ["get_by_role_name", "textbox_b", "* Description:", "NEW PROPOSE PRODUCT ACTIVITY 001 DESCRIPTION"]
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

        page = self.driver
        page.wait_for_timeout(10000)

        # data_element_action = {
        #     "opt_app_type": ["get_by_location_option_select", "#applicationTypeId", "value:'2'"]
        # }
        # self.initiate_test_data().data_processing_func_peza(data_element_action)
        # page = self.driver
        # page.wait_for_timeout(10000)
        #
        # data_element_action = {
        #     "opt_app_type": ["get_by_location_option_select", "select#applicationTypeId", "EXPANSION PROJECT OF AN EXISTING ENTERPRISE"]
        # }
        # self.initiate_test_data().data_processing_func_peza(data_element_action)
        # page = self.driver
        # page.wait_for_timeout(10000)