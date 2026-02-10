import pytest
from modules.testcases.ecp.data_processing import DataProcessingClass

# @pytest.mark.usefixtures("setup")
# def test_ecp(playwright: Playwright) -> None:
# class TestSuite0000():
#     def initiate_test_data(self):
#         return DataProcessingClass(self.driver)
#
#     def test_data_preparation(self) -> None:
#         self.initiate_test_data().update_test_data_iterate()
#
#     def test_api_processing(self) -> None:
#         self.initiate_test_data().execute_port_api_consumption()
#
#     def test_cbu_xl_update(self) -> None:
#         self.initiate_test_data().update_cbu_excel_file()




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
            "verify_undertaking_link:": ["expect_by_role_name", "link", "Undertaking"]

        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)
        page = self.driver
        page.wait_for_timeout(10000)

# @pytest.mark.usefixtures("setup")
# # def test_ecp(playwright: Playwright) -> None:
# class TestSuite0001():
#     # @pytest.fixture(autouse=True)
#     def initiate_test(self):
#         return "test_data_01"
#     def initiate_test_data(self):
#         return DataProcessingClass(self.driver)
#
#     def test_ecp_login(self) -> None:
#         test_data_set = self.initiate_test()
#         self.initiate_test_data().data_processing_func(test_data_set,"login")
#
#     def test_ecp_verify_land_page(self) -> None:
#         test_data_set = self.initiate_test()
#         self.initiate_test_data().data_processing_func(test_data_set,"verify_land_page")
#
#     def test_create_ecp_consumption(self) -> None:
#         test_data_set = self.initiate_test()
#         self.initiate_test_data().data_processing_func(test_data_set, "create_ecp_consumption")
#
#     def test_verify_sub_sections(self) -> None:
#         test_data_set = self.initiate_test()
#         self.initiate_test_data().data_processing_func(test_data_set, "verify_sub_sections")
#
#     def test_add_ecp_documents(self) -> None:
#         test_data_set = self.initiate_test()
#         self.initiate_test_data().data_processing_func(test_data_set, "add_ecp_documents")
#
#     def test_add_ecp_details(self) -> None:
#         test_data_set = self.initiate_test()
#         self.initiate_test_data().data_processing_func(test_data_set, "add_ecp_details")
#
#     def test_submit_ecp(self) -> None:
#         test_data_set = self.initiate_test()
#         self.initiate_test_data().data_processing_func(test_data_set, "submit_ecp")
#
#     def test_logout(self) -> None:
#         test_data_set = self.initiate_test()
#         self.initiate_test_data().data_processing_func(test_data_set, "logout")
#
#
#     def test_examiner_verify_all(self) -> None:
#         page = self.driver
#         test_data_set = self.initiate_test()
#         self.initiate_test_data().data_processing_func(test_data_set, "examiner_verify_all")
#         page.wait_for_timeout(10000)

# @pytest.mark.usefixtures("setup")
# class TestSuite0002():
#     def initiate_test(self):
#         return "test_data_02"
#     def initiate_test_data(self):
#         return DataProcessingClass(self.driver)
#
#
#     def test_ecp_login(self) -> None:
#         test_data_set = self.initiate_test()
#         self.initiate_test_data().data_processing_func(test_data_set, "login")
#
#
#     def test_ecp_verify_land_page(self) -> None:
#         test_data_set = self.initiate_test()
#         self.initiate_test_data().data_processing_func(test_data_set, "verify_land_page")
#
#
#     def test_create_ecp_consumption(self) -> None:
#         test_data_set = self.initiate_test()
#         self.initiate_test_data().data_processing_func(test_data_set, "create_ecp_consumption")
#
#
#     def test_verify_sub_sections(self) -> None:
#         test_data_set = self.initiate_test()
#         self.initiate_test_data().data_processing_func(test_data_set, "verify_sub_sections")
#
#
#     def test_add_ecp_documents(self) -> None:
#         test_data_set = self.initiate_test()
#         self.initiate_test_data().data_processing_func(test_data_set, "add_ecp_documents")
#
#
#     def test_add_ecp_details(self) -> None:
#         page = self.driver
#         test_data_set = self.initiate_test()
#         self.initiate_test_data().data_processing_func(test_data_set, "add_ecp_details")
#         page.wait_for_timeout(10000)




