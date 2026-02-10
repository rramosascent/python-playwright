import ast
import os
import json
import time

class DictionaryData:
    def get_data_for_test_a(self, test_case_data):
        with open(r"C:\Users\ASCENT\Documents\GitHub\python-playwright\pythonProject\testcases\ecp\file_uploads\ecp_test_data_1.txt",'r', encoding="utf-8") as file:
            dictionary_extraction = file.read()
        data_for_test = ast.literal_eval(dictionary_extraction)

        return data_for_test[test_case_data]

    def get_data_for_test(self, test_case_data, test_case_module):
        with open(r"C:\Users\ASCENT\Documents\GitHub\python-playwright\pythonProject\testcases\ecp\file_uploads\ecp_test_data_1.txt",'r', encoding="utf-8") as file:
            dictionary_extraction = file.read()
        data_for_test = ast.literal_eval(dictionary_extraction)

        get_element_map = self.ecp_address_data(test_case_module)

        if test_case_module in data_for_test[test_case_data]:
            for key, value in data_for_test[test_case_data][test_case_module].items():
                get_element_map[key][value[0]] = value[1]

        return get_element_map

    def get_data_for_test_all(self):
        with open(r"C:\Users\ASCENT\Documents\GitHub\python-playwright\pythonProject\testcases\ecp\file_uploads\ecp_test_data_1.txt",'r', encoding="utf-8") as file:
            dictionary_extraction = file.read()
        data_for_test = ast.literal_eval(dictionary_extraction)

        return data_for_test

    def get_entry_num_ref(self):
        with open(r"C:\Users\ASCENT\Documents\GitHub\python-playwright\pythonProject\testcases\ecp\file_uploads\entry_numbers.txt",'r', encoding="utf-8") as file:
            dictionary_extraction = file.read()

        data_for_test = ast.literal_eval(dictionary_extraction)

        return data_for_test

    def get_users_for_test(self, test_case_data):
        with open(r"C:\Users\ASCENT\Documents\GitHub\python-playwright\pythonProject\testcases\ecp\file_uploads\user_accounts.txt",'r', encoding="utf-8") as file:
            dictionary_extraction = file.read()
        data_for_test = ast.literal_eval(dictionary_extraction)

        return data_for_test[test_case_data]

    def update_entry_number(self, test_case_data):
        path = r'C:\Users\ASCENT\Documents\GitHub\python-playwright\pythonProject\testcases\ecp\file_uploads'
        file = r'\entry_numbers'
        extension = 'txt'
        iteration = int(time.time())

        orig_file = f"{path}{file}.{extension}"
        new_file = f"{path}{file}_{iteration}.{extension}"

        os.rename(orig_file,new_file)

        with open(orig_file, 'w', encoding="utf-8") as file:
            json.dump(test_case_data, file, indent=4)

    def update_ecp_test_data(self, test_case_data):
        path = r'C:\Users\ASCENT\Documents\GitHub\python-playwright\pythonProject\testcases\ecp\file_uploads'
        file = r'\ecp_test_data_1'
        extension = 'txt'
        iteration = int(time.time())

        orig_file = f"{path}{file}.{extension}"
        new_file = f"{path}{file}_{iteration}.{extension}"

        os.rename(orig_file,new_file)

        with open(orig_file, 'w', encoding="utf-8") as file:
            json.dump(test_case_data, file, indent=4)

    def ecp_address_data(self, test_case_module):
        ecp_action_map = {
            "login": {
                "link_login": ["open_url", "XXXXXX"],
                "privacy_policy": ["get_by_role_name", "checkbox", "I agree"],
                "privacy_pbutton": ["get_by_role_name", "button", "Proceed"],
                "user_name": ["get_by_role_name", "textbox_a", "Enter your email or username", "XXXXXX"],
                "password": ["get_by_role_name", "textbox_b", "Password", "XXXXXX"],
                "btn_sign_in": ["get_by_role_name", "button", "SIGN IN"]
            },
            "verify_land_page": {
                "verify_i_ecp_logo": ["get_by_role_name", "link","logo eCP"],
                "verify_i_ecp": ["get_by_location_con_text", "#layout-menu", "eCP"],
                "verify_i_loi": ["get_by_location_con_text", "#layout-menu", "List of Importer" ],
                "verify_i_myapps": ["get_by_location_con_text", "#layout-menu", "My Applications"],
                "verify_i_lofapps": ["get_by_location_con_text", "h3", "List of Applications"]
            },
            "create_ecp_consumption": {
                "link_ecp": ["get_by_role_name","link","\uea3c eCP"],
                "declaration": ["get_by_location_option_select", "#locatorType", "XXXXXXXXXX" ],
                "ecp_year": ["get_by_role_name", "textbox_a", "Entry Year", "XXXX"],
                "ecp_port_code": ["get_by_role_name", "textbox_b", "Port Code", "XXXX"],
                "ecp_e_number": ["get_by_role_name", "textbox_b", "Entry Number", "XXXXXX"],
                "registry_num": ["get_by_location_fill_a", "input[name=\"rg_number\"]", "XXXXXXX-XX"],
                "bl_number": ["get_by_location_fill_b", "input[name=\"bl_number\"]", "XXXXXXXXXX"],
                "consignee_rep": ["get_by_location_fill_b", "#representative", "XXXXXX XXXXXX"],
                "consignee_rep_des": ["get_by_location_fill_b", "#designation", "XXXXXX XXXXXX"],
                "consignee_rep_con": ["get_by_role_name", "textbox_b", "+63-", "XXX-XXXXXXXXXX"],
                "consignee_rep_tin": ["get_by_role_name", "textbox_b", "-000-000-000-000", "XXXXXXXXXXXX"],
                "transaction_type": ["get_by_location_option_select", "#transactionType", "XXXXXXXXXX"],
                "business_id": ["get_by_location_fill_b", "#business_id", "XXXX-XX-XXXXX"],
                "remarks": ["get_by_location_fill_b", "#remarks", "XXXXXX XXXXXX XXXXXX XXXXX"],
                "total_gross_weight": ["get_by_location_fill_b", "#total_gross_weight", "XXXXXX"],
                "total_net_weight": ["get_by_location_fill_b",  "#total_net_weight","XXXXXX"],
                "btn_save_ecp": ["get_by_role_name", "button", "Save eCP Info"],
                "btn_swal_confirm": ["get_by_role_name", "button", "Yes, submit it!"],
                "btn_swal_confirm_ok": ["get_by_role_name", "button", "OK"]
            },
            "verify_sub_sections": {
                "verify_btn_ecp_sub": ["expect_by_role_name", "button", "SUBMIT"],
                "verify_h3_ecp_det": ["expect_by_role_name", "heading", "eCP DETAILS"],
                "verify_h3_ecp_docs": ["expect_by_role_name", "heading", "eCP DOCUMENTS"]
            },
            "add_ecp_documents": {
                "btn_add_ecp_doc": ["get_by_role_name", "button", "\uf055 ADD NEW DOCUMENT"],
                "verify_modal_docu": ["get_by_location", "expect", "#modalDOCU"],
                "ecp_doc_desc": ["get_by_location_fill_a", "#itemGenDesc", "ECP DOCUMENTS TESTING /n/r ATTACH FILE AND SUBMIT"],
                "ecp_doc_file": ["get_by_role_name", "button_set_files", "Choose File", "XXXXXXXXXX"],
                "btn_add_ecp_doc_save": ["get_by_role_name", "button", "Save"],
                "verify_diaglog_confirm": ["expect_by_role_name", "dialog", "Confirmation"],
                "btn_add_ecp_doc_save_swal_confirm": ["get_by_role_name",  "button", "Yes"],
                "verify_diaglog_confirm_ok": ["expect_by_role_name", "dialog", "Great!"],
                "btn_add_ecp_doc_save_swal_confirm_ok": ["get_by_role_name", "button", "OK"]
            },
            "add_ecp_details": {
                "btn_add_ecp_det": ["get_by_role_name", "button", "\ue09a UPLOAD EXCEL FILE"],
                "verify_modal_docu": ["get_by_location", "expect", "#modalUPLOADDETAILS"],
                "ecp_det_file": ["get_by_role_name", "button_set_files", "Choose File", "XXXXXXXXXXXXX"],
                "btn_add_ecp_det_save": ["get_by_location", "click", "#btnUploadData"],
                "verify_diaglog_confirm": ["expect_by_role_name", "dialog", "Confirmation"],
                "btn_add_ecp_det_save_swal_confirm": ["get_by_role_name", "button", "Yes"],
                "verify_diaglog_confirm_ok": ["expect_by_role_name", "dialog", "Great!"],
                "btn_add_ecp_det_save_swal_confirm_ok": ["get_by_role_name", "button", "OK"]
            },
            "submit_ecp": {
                "btn_submit": ["get_by_role_name", "button", "SUBMIT"],
                "verify_diaglog_confirm": ["expect_locator_filter_has_txt", "div", "\u00d7!Are you sure you want to"],
                "btn_submit_swal": ["get_by_role_name", "button", "Yes, submit it!"],
                "verify_diaglog_confirm_ok": ["expect_locator_filter_has_txt", "div", "\u00d7 Application tagged as"],
                "btn_submit_swal_ok": ["get_by_role_name", "button", "OK"]
            },
            "logout": {
                "verify_link_profile": ["get_by_location", "expect", "xpath=//div[@id='navbar-collapse']/ul/li[3]/a/div/img"],
                "link_profile": ["get_by_location", "click", "xpath=//div[@id='navbar-collapse']/ul/li[3]/a/div/img"],
                "btn_logout": ["get_by_role_name","link"," Log Out"]
            },
            "examiner_verify_all": {
                "link_login": ["open_url", "XXXXXX"],
                # "privacy_policy": ["get_by_role_name", "checkbox", "I agree"],
                # "privacy_pbutton": ["get_by_role_name", "button", "Proceed"],
                "user_name": ["get_by_role_name", "textbox_a", "Enter your email or username", "XXXXXX"],
                "password": ["get_by_role_name", "textbox_b", "Password", "XXXXXX"],
                "btn_sign_in": ["get_by_role_name", "button", "SIGN IN"],
                "open_transaction": ["get_by_role_name","row_item","XXXXXXXXX"],
                "verify_check_all_details": ["get_by_location", "expect", "xpath=//input[@id='flowcheckall']"],
                "check_all_details": ["get_by_location","checkbox","#flowcheckall"],
                "btn_submit_verified": ["get_by_role_name", "button", "VERIFIED "],
                "verify_diaglog_confirm": ["expect_locator_filter_has_txt", "h2", "Confirmation"],
                "btn_dialog_confirm_yes": ["get_by_role_name", "button", "Yes"],
                "verify_diaglog_confirm_ok": ["expect_locator_filter_has_txt", "h2", "Great!"],
                "btn_dialog_confirm_ok": ["get_by_role_name", "button", "OK"]
            }
        }
        return ecp_action_map[test_case_module]


