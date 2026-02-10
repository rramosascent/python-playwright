from testcases.ecp.data import DictionaryData
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.testcases.ptops.berms_page import TestExecutionClass
from modules.frame_work.utility.utility_package import UtilityPackage
from testcases.ecp.api_processing import EcoConsumptionApi
class DataProcessingClass(FrameWorkPWDriver):
    def __init__(self, driver):
        self.driver = driver

    def data_processing_func(self, data_file, data_module):

        test_data = DictionaryData()

        for data_key, data_value in test_data.get_data_for_test(data_file, data_module).items():
            # print(f"{key}: {value}")
            if data_key == "user_name":
                account_update = data_value[3]
                data_value[3] = test_data.get_users_for_test(account_update)["un"]
            elif data_key == "password":
                account_update = data_value[3]
                data_value[3] = test_data.get_users_for_test(account_update)["pw"]
            elif data_key == "link_login":
                account_update = data_value[1]
                data_value[1] = test_data.get_users_for_test(account_update)[0]

            self.fw_execute_test_suites(data_value)

    def data_processing_func_peza(self, data_file):

        test_data = TestExecutionClass(self.driver)

        for data_key, data_value in data_file.items():

            if data_key == "user_name":
                account_update = data_value[3]
                data_value[3] = test_data.page_login_a_user(account_update)["un"]
            elif data_key == "password":
                account_update = data_value[3]
                data_value[3] = test_data.page_login_a_user(account_update)["pw"]
            elif data_key == "link_login":
                account_update = data_value[1]
                data_value[1] = test_data.page_login_a_user(account_update)

            # print(f"{data_key}: {data_value}")
            self.fw_execute_test_suites(data_value)

    def update_test_data_iterate(self) -> None:
        utility_package = UtilityPackage()
        test_data = DictionaryData()
        ecp_test_data = test_data.get_data_for_test_all()
        ecp_entry_num_ref = test_data.get_entry_num_ref()
        for data_key_1, data_value_1 in ecp_test_data.items():
            for data_key_2, data_value_2 in ecp_entry_num_ref.items():
                port = ecp_test_data[data_key_1]["create_ecp_consumption"]["ecp_port_code"][1]
                if data_key_2 == port:
                    updated_counter = ecp_entry_num_ref[port]["counter"] + 1
                    padded_entry_num = utility_package.padd_zeroes(updated_counter)
                    ecp_entry_num_ref[port]["counter"] = updated_counter
                    ecp_test_data[data_key_1]["create_ecp_consumption"]["ecp_e_number"][1] = padded_entry_num
                    ecp_test_data[data_key_1]["create_ecp_consumption"]["declaration"][2] = f'{ecp_entry_num_ref[port]["dec_ref"]}{padded_entry_num}'
                    ecp_test_data[data_key_1]["create_ecp_consumption"]["ecp_e_number"][2] = f'{ecp_entry_num_ref[port]["receipt"]}{padded_entry_num}'
                    ecp_test_data[data_key_1]["create_ecp_consumption"]["registry_num"][1] = ecp_entry_num_ref[port]["registry_num"]
                    ecp_test_data[data_key_1]["create_ecp_consumption"]["bl_number"][1] = f'{ecp_entry_num_ref[port]["bl"]}{padded_entry_num}'
                    ecp_test_data[data_key_1]["examiner_verify_all"]["open_transaction"][1] = f'{ecp_entry_num_ref[port]["year"]}{port}C{padded_entry_num}'
        test_data.update_entry_number(ecp_entry_num_ref)
        test_data.update_ecp_test_data(ecp_test_data)

    def update_cbu_excel_file(self) -> None:
        test_data = DictionaryData()
        utility_package = UtilityPackage()

        for data_key_1 in test_data.get_data_for_test_all().keys():
            data_value_2 = test_data.get_data_for_test_a(data_key_1)
            port = data_value_2["create_ecp_consumption"]["ecp_port_code"][1]
            data_entry_num = test_data.get_entry_num_ref()[port]
            data_ecp_information = data_value_2["create_ecp_consumption"]["ecp_e_number"][1]
            data_path = data_value_2["add_ecp_details"]["ecp_det_file"][1]
            utility_package.cbu_excel(data_path, data_entry_num, data_ecp_information)

    def execute_port_api_consumption(self) -> None:
        test_data = DictionaryData()
        post_api = EcoConsumptionApi()

        for data_key in test_data.get_data_for_test_all().keys():
            # print(data_key)
            assert post_api.processing_consumption_api(data_key) == 200



