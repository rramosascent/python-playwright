from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver


class SignUpPageClass(FrameWorkPWDriver):

    def __init__(self, driver):
        self.driver = driver

    def open_url_ptops(self, get_data):
        open_url_complete = ["open_url", "XXX"]
        print(open_url_complete)
        open_url_complete[1] = get_data
        print(open_url_complete)

        self.fw_execute_test_suites(open_url_complete)

    def landing_link_create_account(self):
        data_link = ["get_by_role_name", "link", "Create an account"]
        self.fw_execute_test_suites(data_link)

    def select_registration_type(self, get_data):
        data_link = ["get_by_location", "label_has_txt_click", "XXX"]
        data_link[2] = get_data
        self.fw_execute_test_suites(data_link)

    def select_registration_type_proceed(self, get_data):
        data_link = ["get_by_role_name", "button", "XXX"]
        data_link[2] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_data_privacy_agreement(self, get_data):
        data_link = ["get_by_role_name", "checkbox", "XXX"]
        data_link[2] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_data_privacy_agreement_proceed(self):
        data_link = ["get_by_role_name", "button", "Submit"]
        self.fw_execute_test_suites(data_link)

    def registration_company_info_type(self,get_data):
        data_link = ["get_by_role_name", "radio_b", "XXX"]
        data_link[2] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_company_info_name(self,get_data):
        data_link = ["get_by_role_name", "textbox_b", "* Company Name:", "XXX"]
        data_link[3] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_company_info_tin(self,get_data):
        data_link = ["get_by_role_name", "textbox_b", "* TAX IDENTIFICATION NUMBER:", "XXX"]
        data_link[3] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_company_address_region(self, get_data):
        data_link = ["get_by_role_combox_select", "#select2-companyRegionId-container", "XXX"]
        data_link[2] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_company_address_province(self, get_data):
        data_link = ["get_by_role_combox_select", "#select2-companyProvinceId-container", "XXX"]
        data_link[2] = get_data
        self.fw_execute_test_suites(data_link)


    def registration_company_address_city(self, get_data):
        data_link = ["get_by_role_combox_select", "#select2-companyCityId-container", "XXX"]
        data_link[2] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_company_address_barangay(self, get_data):
        data_link = ["get_by_role_combox_select", "#select2-companyBarangayId-container", "XXX"]
        data_link[2] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_company_address_street(self,get_data):
        data_link = ["get_by_role_name", "textbox_b", "* Street Name:", "XXX"]
        data_link[3] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_company_contact_mobile_no(self,get_data):
        data_link = ["get_by_role_name", "textbox_b", "* Mobile No.", "XXX"]
        data_link[3] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_company_contact_landline(self,get_data):
        data_link = ["get_by_role_name", "textbox_b", "Landline No.", "XXX"]
        data_link[3] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_company_contact_email(self,get_data):
        data_link = ["get_by_role_name", "textbox_b", "username@gmail.com", "XXX"]
        data_link[3] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_supporting_documents(self,get_data):
        data_link = ["get_by_file_chooser", "#supportingDocumentFilename", "XXX"]
        data_link[2] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_supporting_upload(self):
        data_link = ["get_by_location", "click", "#btnAddSupportingDocument"]
        self.fw_execute_test_suites(data_link)

    def registration_supporting_documents_2(self,get_data):
        data_link = ["get_by_file_chooser", "#supportingDocumentFilename2", "XXX"]
        data_link[2] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_supporting_upload_2(self):
        data_link = ["get_by_location", "click", "#btnAddSupportingDocument2"]
        self.fw_execute_test_suites(data_link)

    def registration_account_info_last_name(self,get_data):
        data_link = ["get_by_role_name", "textbox_b", "* LAST NAME:", "XXX"]
        data_link[3] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_account_info_first_name(self,get_data):
        data_link = ["get_by_role_name", "textbox_b", "* FIRST NAME:", "XXX"]
        data_link[3] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_account_info_middle_name(self,get_data):
        data_link = ["get_by_role_name", "textbox_b", "MIDDLE NAME:", "XXX"]
        data_link[3] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_account_info_position(self,get_data):
        data_link = ["get_by_role_name", "textbox_b", "Enter Company Position", "XXX"]
        data_link[3] = get_data
        self.fw_execute_test_suites(data_link)
    def registration_account_info_contact_no(self,get_data):
        data_link = ["get_by_role_name", "textbox_b", "* CONTACT NO:", "XXX"]
        data_link[3] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_account_info_email(self,get_data):
        data_link = ["get_by_role_name", "textbox_b", "* EMAIL ADDRESS:", "XXX"]
        data_link[3] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_account_info_uname(self,get_data):
        data_link = ["get_by_role_name", "textbox_b", "* USERNAME: USERNAME:", "XXX"]
        data_link[3] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_account_info_pword(self,get_data):
        data_link = ["get_by_role_name", "textbox_b", "* PASSWORD: PASSWORD", "XXX"]
        data_link[3] = get_data
        self.fw_execute_test_suites(data_link)

    def registration_account_info_pword_c(self,get_data):
        data_link = ["get_by_role_name", "textbox_b", "* CONFIRM PASSWORD:", "XXX"]
        data_link[3] = get_data
        self.fw_execute_test_suites(data_link)