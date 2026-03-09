from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.utility_package import UtilityPackage


class SignUpPageClass(FrameWorkPWDriver):

    def __init__(self, driver):
        self.driver = driver
        self.utility_f = UtilityPackage()
        self.open_url_data = ["open_url", "XXX"]
        self.data_link = ["get_by_role_name", "link", "Create an account"]
        self.registration_type = ["get_by_location", "label_has_txt_click", "XXX"]
        self.registration_type_proceed = ["get_by_role_name", "button", "XXX"]
        self.data_privacy_agreement = ["get_by_role_name", "checkbox", "XXX"]
        self.data_privacy_agreement_proceed = ["get_by_role_name", "button", "Submit"]
        self.company_info_type = ["get_by_role_name", "radio_b", "XXX"]
        self.company_info_name = ["get_by_role_name", "textbox_b", "* Company Name:", "XXX"]
        self.company_info_tin = ["get_by_role_name", "textbox_b", "* TAX IDENTIFICATION NUMBER:", "XXX"]
        self.company_address_region = ["get_by_role_combox_select", "#select2-companyRegionId-container", "XXX"]
        self.company_address_province = ["get_by_role_combox_select", "#select2-companyProvinceId-container", "XXX"]
        self.company_address_city = ["get_by_role_combox_select", "#select2-companyCityId-container", "XXX"]
        self.company_address_barangay = ["get_by_role_combox_select", "#select2-companyBarangayId-container", "XXX"]
        self.company_address_street = ["get_by_role_name", "textbox_b", "* Street Name:", "XXX"]
        self.company_contact_mobile_no = ["get_by_role_name", "textbox_b", "* Mobile No.", "XXX"]
        self.company_contact_landline = ["get_by_role_name", "textbox_b", "Landline No.", "XXX"]
        self.company_contact_email = ["get_by_role_name", "textbox_b", "username@gmail.com", "XXX"]
        self.supporting_documents = ["get_by_file_chooser", "#supportingDocumentFilename", "XXX"]
        self.supporting_upload = ["get_by_location", "click", "#btnAddSupportingDocument"]
        self.supporting_documents_2 = ["get_by_file_chooser", "#supportingDocumentFilename2", "XXX"]
        self.supporting_upload_2 = ["get_by_location", "click", "#btnAddSupportingDocument2"]
        self.account_info_last_name = ["get_by_role_name", "textbox_b", "* LAST NAME:", "XXX"]
        self.account_info_first_name = ["get_by_role_name", "textbox_b", "* FIRST NAME:", "XXX"]
        self.account_info_middle_name = ["get_by_role_name", "textbox_b", "MIDDLE NAME:", "XXX"]
        self.account_info_position = ["get_by_role_name", "textbox_b", "Enter Company Position", "XXX"]
        self.account_info_contact_no = ["get_by_role_name", "textbox_b", "* CONTACT NO:", "XXX"]
        self.account_info_email = ["get_by_role_name", "textbox_b", "* EMAIL ADDRESS:", "XXX"]
        self.account_info_uname = ["get_by_role_name", "textbox_b", "* USERNAME: USERNAME:", "XXX"]
        self.account_info_pword = ["get_by_role_name", "textbox_b", "* PASSWORD: PASSWORD", "XXX"]
        self.account_info_pword_c = ["get_by_role_name", "textbox_b", "* CONFIRM PASSWORD:", "XXX"]
        self.confirm_registration = ["get_by_role_name", "button", "Details Confirmed "]
        self.confirm_registration_submit = ["get_by_location", "click", "#btnSubmitRegistration"]
        self.confirm_registration = ["get_by_role_name", "button", "Proceed"]


    def open_url_ptops(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.open_url_data, get_data)
        self.fw_execute_test_suites(data_processed)

    def landing_link_create_account(self):
        self.fw_execute_test_suites(self.data_link)

    def select_registration_type(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.registration_type, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_registration_type_proceed(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.registration_type_proceed, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_data_privacy_agreement(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.data_privacy_agreement, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_data_privacy_agreement_proceed(self):
        self.fw_execute_test_suites(self.data_privacy_agreement_proceed)

    def registration_company_info_type(self,get_data):
        data_processed = self.utility_f.add_data_in_array(self.company_info_type, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_company_info_name(self,get_data):
        data_processed = self.utility_f.add_data_in_array(self.company_info_name, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_company_info_tin(self,get_data):
        data_processed = self.utility_f.add_data_in_array(self.company_info_tin, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_company_address_region(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.company_address_region, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_company_address_province(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.company_address_province, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_company_address_city(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.company_address_city, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_company_address_barangay(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.company_address_barangay, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_company_address_street(self,get_data):
        data_processed = self.utility_f.add_data_in_array(self.company_address_street, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_company_contact_mobile_no(self,get_data):
        data_processed = self.utility_f.add_data_in_array(self.company_contact_mobile_no, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_company_contact_landline(self,get_data):
        data_processed = self.utility_f.add_data_in_array(self.company_contact_landline, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_company_contact_email(self,get_data):
        data_processed = self.utility_f.add_data_in_array(self.company_contact_email, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_supporting_documents(self,get_data):
        data_processed = self.utility_f.add_data_in_array(self.supporting_documents, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_supporting_upload(self):
        self.fw_execute_test_suites(self.supporting_upload)

    def registration_supporting_documents_2(self,get_data):
        data_processed = self.utility_f.add_data_in_array(self.supporting_documents_2, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_supporting_upload_2(self):
        self.fw_execute_test_suites(self.supporting_upload_2)

    def registration_account_info_last_name(self,get_data):
        data_processed = self.utility_f.add_data_in_array(self.account_info_last_name, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_account_info_first_name(self,get_data):
        data_processed = self.utility_f.add_data_in_array(self.account_info_first_name, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_account_info_middle_name(self,get_data):
        data_processed = self.utility_f.add_data_in_array(self.account_info_middle_name, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_account_info_position(self,get_data):
        data_processed = self.utility_f.add_data_in_array(self.account_info_position, get_data)
        self.fw_execute_test_suites(data_processed)
    def registration_account_info_contact_no(self,get_data):
        data_processed = self.utility_f.add_data_in_array(self.account_info_contact_no, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_account_info_email(self,get_data):
        data_processed = self.utility_f.add_data_in_array(self.account_info_email, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_account_info_uname(self,get_data):
        data_processed = self.utility_f.add_data_in_array(self.account_info_uname, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_account_info_pword(self,get_data):
        data_processed = self.utility_f.add_data_in_array(self.account_info_pword, get_data)
        self.fw_execute_test_suites(data_processed)

    def registration_account_info_pword_c(self,get_data):
        data_processed = self.utility_f.add_data_in_array(self.account_info_pword_c, get_data)
        self.fw_execute_test_suites(data_processed)