
class DataObjectRegistration:
    def __init__(self, driver, payload):
        self.driver = driver
        self.registration_hmp = payload["Registration"]
        self.registration_dp = payload["Data_privacy"]
        self.registration_ci = payload["Company_info"]
        self.registration_cadd = payload["Company_add"]
        self.registration_cntct = payload["Contact"]
        self.registration_suppd = payload["Supporting_docs"]
        self.registration_acnti = payload["Account_info"]
        self.registration_usrc = payload["User_creds"]
        self.select_registration_type = self.get_registration_type()
        self.click_registration_proceed = self.get_registration_proceed()
        self.accept_registration_data_privacy = self.get_registration_data_privacy()
        self.select_comp_info_type = self.get_registration_comp_info_type()
        self.select_comp_info_name = self.get_registration_comp_info_name()
        self.select_comp_info_tin = self.get_registration_comp_info_tin()
        self.select_comp_add_region = self.get_registration_comp_add_region()
        self.select_comp_add_province = self.get_registration_comp_add_province()
        self.select_comp_add_city = self.get_registration_comp_add_city()
        self.select_comp_add_barangay = self.get_registration_comp_add_barangay()
        self.select_comp_add_street = self.get_registration_comp_add_street()
        self.input_contact_mobile = self.get_registration_contact_mobile()
        self.input_contact_landline = self.get_registration_contact_landline()
        self.input_contact_email_p1 = self.get_registration_contact_email_p1()
        self.input_contact_email_p2 = self.get_registration_contact_email_p2()
        self.select_supporting_docs_1 = self.get_registration_supporting_docs_1()
        self.select_supporting_docs_2 = self.get_registration_supporting_docs_2()
        self.input_account_info_lname = self.get_registration_account_inf_lname()
        self.input_account_info_fname = self.get_registration_account_inf_fname()
        self.input_account_info_mname = self.get_registration_account_inf_mname()
        self.input_account_info_position = self.get_registration_account_inf_position()
        self.input_account_info_contact_no = self.get_registration_account_inf_contact_no()
        self.input_user_creds_email_1 = self.get_registration_user_creds_email_1()
        self.input_user_creds_email_2 = self.get_registration_user_creds_email_2()
        self.input_user_creds_user_name = self.get_registration_user_creds_user_name()
        self.input_user_creds_pword = self.get_registration_user_creds_pword()
        self.input_user_creds_pword_c = self.get_registration_user_creds_pword_c()

    def get_registration_type(self):
        set_data = self.registration_hmp["Type"]
        return set_data

    def get_registration_proceed(self):
        set_data = self.registration_hmp["Proceed"]
        return set_data

    def get_registration_data_privacy(self):
        return self.registration_dp

    def get_registration_comp_info_type(self):
        set_data = self.registration_ci["Type"]
        return set_data

    def get_registration_comp_info_name(self):
        set_data = self.registration_ci["Name"]
        return set_data

    def get_registration_comp_info_tin(self):
        set_data = self.registration_ci["Tin"]
        return set_data

    def get_registration_comp_add_region(self):
        set_data = self.registration_cadd["Region"]
        return set_data

    def get_registration_comp_add_province(self):
        set_data = self.registration_cadd["Province"]
        return set_data

    def get_registration_comp_add_city(self):
        set_data = self.registration_cadd["City"]
        return set_data

    def get_registration_comp_add_barangay(self):
        set_data = self.registration_cadd["Barangay"]
        return set_data

    def get_registration_comp_add_street(self):
        set_data = self.registration_cadd["Street"]
        return set_data

    def get_registration_contact_mobile(self):
        set_data = self.registration_cntct["Mobile"]
        return set_data

    def get_registration_contact_landline(self):
        set_data = self.registration_cntct["Landline"]
        return set_data
    def get_registration_contact_email_p1(self):
        set_data = self.registration_cntct["Email_p1"]
        return set_data

    def get_registration_contact_email_p2(self):
        set_data = self.registration_cntct["Email_p2"]
        return set_data

    def get_registration_supporting_docs_1(self):
        set_data = self.registration_suppd["Doc01"]
        return set_data

    def get_registration_supporting_docs_2(self):
        set_data = self.registration_suppd["Doc02"]
        return set_data
    def get_registration_account_inf_lname(self):
        set_data = self.registration_acnti["Last_name"]
        return set_data

    def get_registration_account_inf_fname(self):
        set_data = self.registration_acnti["First_name"]
        return set_data

    def get_registration_account_inf_mname(self):
        set_data = self.registration_acnti["Middle_name"]
        return set_data

    def get_registration_account_inf_position(self):
        set_data = self.registration_acnti["Position"]
        return set_data

    def get_registration_account_inf_contact_no(self):
        set_data = self.registration_acnti["Contact_no"]
        return set_data

    def get_registration_user_creds_email_1(self):
        set_data = self.registration_usrc["Email_p1"]
        return set_data

    def get_registration_user_creds_email_2(self):
        set_data = self.registration_usrc["Email_p2"]
        return set_data

    def get_registration_user_creds_user_name(self):
        set_data = self.registration_usrc["User_name"]
        return set_data

    def get_registration_user_creds_pword(self):
        set_data = self.registration_usrc["Pword"]
        return set_data

    def get_registration_user_creds_pword_c(self):
        set_data = self.registration_usrc["Pword_c"]
        return set_data