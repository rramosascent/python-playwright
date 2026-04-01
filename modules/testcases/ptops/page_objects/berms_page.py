from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.utility_package import UtilityPackage


class BermsPageObjects(FrameWorkPWDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.menu_list = BermsPageMenuList(self.driver)
        self.application = BermsPageApplication(self.driver)
        self.company_info = BermsPageCompanyInfo(self.driver)
        self.company_proposed_project = BermsPageProposedProject(self.driver)
        self.existing_bus_reg = BermsPageExistingBusinessReg(self.driver)
        self.stock_holder_principal_officer = BermsPageStockHolderPrincipalOff(self.driver)
        self.manpower_timetable = BermsPageManpowerTimetable(self.driver)
        self.manufacturing_service_flow = BermsPageManufacturingServiceFlow(self.driver)
        self.machinery_raw_mat_prod_schedule = BermsPageMachineryRawMatProductionSched(self.driver)
        self.areas_utilities_waste_disposal = BermsPageAreasUtilitiesWasteDisposal(self.driver)
        self.market_aspect = BermsPageMarketAspect(self.driver)
        self.initial_project_cost = BermsPageInitialProjectCost(self.driver)
        self.supporting_documents = BermsPageSupportingDocuments(self.driver)
        self.application_submission = BermsPageSubmission(self.driver)

    def page_login_a_user(self, get_data):
        link_creds = {
            "url": "http://112.199.119.250:96/peza/login",
            "url_x": "http://192.168.20.25:82/peza/login",
            "url_1": "http://112.199.119.250:82/ECP/auth/login",
            "002": {"un": 'cgbc', "pw": 'Peza_123'},
            "001": {"un": 'amkortech', "pw": 'Password_123'},
            "examiner_1": {"un": 'balahibongpusa', "pw": 'Blitzkri3g!50088'},
        }
        return link_creds[get_data]


class BermsPageMenuList(FrameWorkPWDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.lnk_apps_accre = ["get_by_role_name", "link", " Applications & Accreditations"]
        self.new_berms_button = ["expect_by_role_name", "button", "+ New Ecozone Enterprise"]
        self.btn_new_berms_apps = ["get_by_role_name", "button", "+ New Ecozone Enterprise"]
        self.undertaking_link = ["expect_by_role_name", "link", "Undertaking"]
        self.chbx_agree_ut = ["get_by_role_name", "checkbox", "I Agree"]
        self.btn_proceed_e = ["get_by_location", "expect", "#btnSubmitUndertaking"]
        self.btn_proceed_c = ["get_by_location", "click", "#btnSubmitUndertaking"]

    def click_lnk_apps_accre(self):
        self.fw_execute_test_suites(self.lnk_apps_accre)

    def verify_new_berms_button(self):
        self.fw_execute_test_suites(self.new_berms_button)

    def click_btn_new_berms_apps(self):
        self.fw_execute_test_suites(self.btn_new_berms_apps)

    def verify_undertaking_link(self):
        self.fw_execute_test_suites(self.undertaking_link)

    def check_chbx_agree_ut(self):
        self.fw_execute_test_suites(self.chbx_agree_ut)

    def verify_btn_proceed_e(self):
        self.fw_execute_test_suites(self.btn_proceed_e)

    def click_btn_proceed_c(self):
        self.fw_execute_test_suites(self.btn_proceed_c)


class BermsPageApplication(FrameWorkPWDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.utility_f = UtilityPackage()
        self.opt_app_type = ["get_by_role_combox_select", "#select2-applicationTypeId-container", "xxx"]
        self.rbtn_type_ezone = ["get_by_role_name", "radio_b", "xxx"]
        self.opt_psic_classification = ["get_by_role_combox_select", "#select2-sectionCodeId-container", "xxx"]
        self.opt_psic_division = ["get_by_role_combox_select", "#select2-divisionCodeId-container", "xxx"]
        self.opt_psic_group = ["get_by_role_combox_select", "#select2-groupCodeId-container", "xxx"]
        self.opt_psic_class = ["get_by_role_combox_select", "#select2-classesCodeId-container", "xxx"]
        self.opt_psic_sub_class = ["get_by_role_combox_select", "#select2-subClassesCodeId-container", "xxx"]
        self.btn_proceed_app = ["get_by_role_name", "button", "Proceed"]

    def select_opt_app_type(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_app_type, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_rbtn_type_ezone(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.rbtn_type_ezone, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_opt_psic_classification(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_psic_classification, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_opt_psic_division(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_psic_division, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_opt_psic_div_group(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_psic_group, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_opt_psic_div_class(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_psic_class, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_opt_psic_div_subclass(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_psic_sub_class, get_data)
        self.fw_execute_test_suites(data_processed)

    def click_btn_proceed_app(self):
        self.fw_execute_test_suites(self.btn_proceed_app)


class BermsPageCompanyInfo(FrameWorkPWDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.utility_f = UtilityPackage()
        self.txt_company_name = ["get_by_role_name", "textbox_a", "Company Name", "xxx"]
        self.txt_nature_business = ["get_by_role_name", "textbox_a", "Nature of Business", "xxx"]
        self.txt_company_profile = ["get_by_role_name", "textbox_a", "Company Profile", "xxx"]
        self.btn_proceed = ["get_by_role_name", "button", "Save and Proceed"]

    def input_txt_company_name(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_company_name, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_nature_business(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_nature_business, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_company_profile(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_company_profile, get_data)
        self.fw_execute_test_suites(data_processed)

    def click_btn_proceed(self):
        self.fw_execute_test_suites(self.btn_proceed)


class BermsPageProposedProject(FrameWorkPWDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.utility_f = UtilityPackage()
        self.btn_proposed_project = ["get_by_location", "click", "#btnBusinessProduct"]
        self.txt_proposed_project = ["get_by_location_fill_b", "#newBusinessProductActivity", "xxx"]
        self.btn_proposed_project_add = ["get_by_role_name", "button", " Add"]
        self.txt_description = ["get_by_role_name", "textbox_b", "* Description:", "xxx"]
        self.txt_desc_uses = ["get_by_role_name", "textbox_b", "* Uses/Application:", "xxx"]
        self.add_permit = ["get_by_file_chooser", "#activity_product_img_documentsDropzone", "xxx"]
        self.btn_save_next = ["get_by_role_name", "button", "Save and Proceed"]

    def click_btn_proposed_project(self):
        self.fw_execute_test_suites(self.btn_proposed_project)

    def input_txt_proposed_project(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_proposed_project, get_data)
        self.fw_execute_test_suites(data_processed)

    def click_btn_proposed_project_add(self):
        self.fw_execute_test_suites(self.btn_proposed_project_add)

    def input_txt_description(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_description, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_desc_uses(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_desc_uses, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_permit(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_permit, get_data)
        self.fw_execute_test_suites(data_processed)

    def click_btn_save_next(self):
        self.fw_execute_test_suites(self.btn_save_next)


class BermsPageExistingBusinessReg(FrameWorkPWDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.utility_f = UtilityPackage()
        self.dp_registration_date = ["get_by_role_name", "row_dp", "Securities & Exchange", "DD-MMM-YYYY", "xxx"]
        self.txt_registration_no = ["get_by_location", "fill", "input[name=\"businessRegInfoAppsBean[0].reg_no\"]",
                                    "xxx"]
        self.txt_sec_primary_purpose = ["get_by_role_name", "textbox_b", "Sec Primary Purpose", "xxxx"]
        self.txt_authorized_amount = ["get_by_role_name", "textbox_b", "Authorized Amount (PHP)", "xxx"]
        self.txt_subscribed_amount = ["get_by_role_name", "textbox_b", "Subscribe Amount (PHP)", "xxx"]
        self.txt_paid_up_amount = ["get_by_role_name", "textbox_b", "* Paid-up Amount (PHP):", "xxx"]
        self.btn_save_next = ["get_by_role_name", "button", "Save and Proceed"]

    def pick_dp_registration_date(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.dp_registration_date, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_registration_no(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_registration_no, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_sec_primary_purpose(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_sec_primary_purpose, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_authorized_amount(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_authorized_amount, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_subscribed_amount(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_subscribed_amount, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_paid_up_amount(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_paid_up_amount, get_data)
        self.fw_execute_test_suites(data_processed)

    def click_btn_save_next(self):
        self.fw_execute_test_suites(self.btn_save_next)


class BermsPageStockHolderPrincipalOff(FrameWorkPWDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.utility_f = UtilityPackage()
        self.rb_stockholder_type = ["get_by_role_name", "radio_b", "xxx"]
        self.btn_stockholder_add = ["get_by_title_click", "Add Stockholder"]
        self.txt_stockholder_company_name = ["get_by_role_name", "textbox_b", "Company Name *", "xxx"]
        self.txt_stockholder_nationality = ["get_by_role_combox_select",
                                            "#select2-proposedStockholderNationalityId-container", "xxx"]
        self.txt_stockholder_no_shares = ["get_by_role_name", "textbox_b", "No. of Shares *", "xxx"]
        self.txt_amount_subscribed = ["get_by_role_name", "textbox_b", "Amount Subscribe (PHP) *", "xxx"]
        self.txt_amount_paid_up = ["get_by_role_name", "textbox_b", "Amount Paid-up (PHP) *", "xxx"]
        self.btn_stockholder_add_proceed = ["get_by_role_name", "button", " Add"]
        self.rb_proposed_stockholder_item = ["get_by_location", "click", "#isListedStockholder1"]
        self.rb_proposed_stockholder_item1 = ["get_by_location", "click", "#isListedStockholder2"]
        self.btn_principal_officer_add = ["get_by_title_click", "Add Principal Officer"]
        self.opt_officer_salutation = ["get_by_role_combox_select", "#select2-officerSalutationId-container", "xxx"]
        self.txt_officer_fname = ["get_by_role_name", "textbox_b", "* First Name", "xxx"]
        self.txt_officer_mname = ["get_by_role_name", "textbox_b", "Middle Name (Optional)", "xxx"]
        self.txt_officer_lname = ["get_by_role_name", "textbox_b", "* Last Name", "xxx"]
        self.txt_officer_position = ["get_by_location", "fill", "#officerPosition", "xxx"]
        self.btn_officer_add_proceed = ["get_by_role_name", "button", " Add"]
        self.btn_save_next = ["get_by_role_name", "button", "Save and Proceed"]

    def tick_rb_stockholder_type(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.rb_stockholder_type, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_stockholder_company_name(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_stockholder_company_name, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_stockholder_company_nationality(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_stockholder_nationality, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_stockholder_no_shares(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_stockholder_no_shares, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_amount_subscribed(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_amount_subscribed, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_amount_paid_up(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_amount_paid_up, get_data)
        self.fw_execute_test_suites(data_processed)

    def click_btn_stockholder_add(self):
        self.fw_execute_test_suites(self.btn_stockholder_add)

    def click_btn_stockholder_add_proceed(self):
        self.fw_execute_test_suites(self.btn_stockholder_add_proceed)

    def click_rb_proposed_stockholder_item(self):
        self.fw_execute_test_suites(self.rb_proposed_stockholder_item)

    def click_rb_proposed_stockholder_item_1(self):
        self.fw_execute_test_suites(self.rb_proposed_stockholder_item1)

    def click_btn_principal_officer_add(self):
        self.fw_execute_test_suites(self.btn_principal_officer_add)

    def select_opt_officer_salutation(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_officer_salutation, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_officer_fname(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_officer_fname, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_officer_mname(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_officer_mname, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_officer_lname(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_officer_lname, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_officer_position(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_officer_position, get_data)
        self.fw_execute_test_suites(data_processed)

    def click_btn_officer_add_proceed(self):
        self.fw_execute_test_suites(self.btn_officer_add_proceed)

    def click_btn_save_next(self):
        self.fw_execute_test_suites(self.btn_save_next)


class BermsPageManpowerTimetable(FrameWorkPWDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.utility_f = UtilityPackage()
        self.dp_bld_construction_fr = ["select_date_picker_v1",
                                       "xpath=(//div[@id=\"manpower-and-timetable\"]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/input[2])",
                                       "xxx"]
        self.dp_bld_construction_to = ["select_date_picker_v1",
                                       "xpath=(//div[@id=\"manpower-and-timetable\"]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/input[2])",
                                       "xxx"]
        self.dp_bld_procurement_fr = ["select_date_picker_v1",
                                      "xpath=(//div[@id=\"manpower-and-timetable\"]/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/input[2])",
                                      "xxx"]
        self.dp_bld_procurement_to = ["select_date_picker_v1",
                                      "xpath=(//div[@id=\"manpower-and-timetable\"]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/input[2])",
                                      "xxx"]
        self.dp_installation_fr = ["select_date_picker_v1",
                                   "xpath=(//div[@id=\"manpower-and-timetable\"]/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/input[2])",
                                   "xxx"]
        self.dp_installation_to = ["select_date_picker_v1",
                                   "xpath=(//div[@id=\"manpower-and-timetable\"]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/input[2])",
                                   "xxx"]
        self.dp_hiring_fr = ["select_date_picker_v1",
                             "xpath=(//div[@id=\"manpower-and-timetable\"]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/input[2])",
                             "xxx"]
        self.dp_hiring_to = ["select_date_picker_v1",
                             "xpath=(//div[@id=\"manpower-and-timetable\"]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/input[2])",
                             "xxx"]
        self.dp_commercial_start = ["select_date_picker_v1",
                                    "xpath=(//div[@id=\"manpower-and-timetable\"]/div[2]/div[3]/div/div/div/div[2]/div/input[2])",
                                    "xxx"]
        self.txt_manpower_01_service = ["get_by_location", "fill", "#servicePersonnelCount0", "xxx"]
        self.txt_manpower_01_indirect = ["get_by_location", "fill", "#indirectPersonnelCount0", "xxx"]
        self.txt_manpower_01_admin = ["get_by_location", "fill", "#adminPersonnelCount0", "xxx"]
        self.txt_manpower_02_service = ["get_by_location", "fill", "#servicePersonnelCount1", "xxx"]
        self.txt_manpower_02_indirect = ["get_by_location", "fill", "#indirectPersonnelCount1", "xxx"]
        self.txt_manpower_02_admin = ["get_by_location", "fill", "#adminPersonnelCount1", "xxx"]
        self.txt_manpower_03_service = ["get_by_location", "fill", "#servicePersonnelCount2", "xxx"]
        self.txt_manpower_03_indirect = ["get_by_location", "fill", "#indirectPersonnelCount2", "xxx"]
        self.txt_manpower_03_admin = ["get_by_location", "fill", "#adminPersonnelCount2", "xxx"]
        self.btn_save_proceed = ["get_by_role_name", "button", "Save and Proceed"]

    def pick_dp_bld_construction_fr(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.dp_bld_construction_fr, get_data)
        self.fw_execute_test_suites(data_processed)

    def pick_dp_bld_construction_to(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.dp_bld_construction_to, get_data)
        self.fw_execute_test_suites(data_processed)

    def pick_dp_bld_procurement_fr(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.dp_bld_procurement_fr, get_data)
        self.fw_execute_test_suites(data_processed)

    def pick_dp_bld_procurement_to(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.dp_bld_procurement_to, get_data)
        self.fw_execute_test_suites(data_processed)

    def pick_dp_installation_fr(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.dp_installation_fr, get_data)
        self.fw_execute_test_suites(data_processed)

    def pick_dp_installation_to(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.dp_installation_to, get_data)
        self.fw_execute_test_suites(data_processed)

    def pick_dp_hiring_fr(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.dp_hiring_fr, get_data)
        self.fw_execute_test_suites(data_processed)

    def pick_dp_hiring_to(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.dp_hiring_to, get_data)
        self.fw_execute_test_suites(data_processed)

    def pick_dp_commercial_start(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.dp_commercial_start, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_manpower_01_service(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_manpower_01_service, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_manpower_01_indirect(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_manpower_01_indirect, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_manpower_01_admin(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_manpower_01_admin, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_manpower_02_service(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_manpower_02_service, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_manpower_02_indirect(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_manpower_02_indirect, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_manpower_02_admin(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_manpower_02_admin, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_manpower_03_service(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_manpower_03_service, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_manpower_03_indirect(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_manpower_03_indirect, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_manpower_03_admin(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_manpower_03_admin, get_data)
        self.fw_execute_test_suites(data_processed)

    def click_btn_save_proceed(self):
        self.fw_execute_test_suites(self.btn_save_proceed)


class BermsPageManufacturingServiceFlow(FrameWorkPWDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.utility_f = UtilityPackage()
        self.txt_desrcibe_manufacturing_name = ["get_by_role_name", "textbox_a", "Describe the Manufacturing", "xxx"]
        self.add_diagram_process_flow = ["get_by_file_chooser", "#addtlInfo_supporting_documentsDropzone", r"xxx"]
        self.btn_save_proceed = ["get_by_role_name", "button", "Save and Proceed"]

    def input_txt_desrcibe_manufacturing_name(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_desrcibe_manufacturing_name, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_diagram_process_flow(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_diagram_process_flow, get_data)
        self.fw_execute_test_suites(data_processed)

    def click_btn_save_proceed(self):
        self.fw_execute_test_suites(self.btn_save_proceed)


class BermsPageMachineryRawMatProductionSched(FrameWorkPWDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.utility_f = UtilityPackage()
        self.btn_machinery_equipment_add = ["get_by_title_click", "Machinery/Equipments"]
        self.txt_machinery_equipment_description = ["get_by_role_name", "textbox_b", "* Item Description", "xxx"]
        self.txt_machinery_equipment_quantity = ["get_by_location", "fill", "#itemQty", "xx"]
        self.txt_machinery_equipment_cost = ["get_by_location", "fill", "#itemUnitCost", "xxx"]
        self.opt_machinery_equipment_source = ["get_by_role_combox_select", "#select2-itemSource-container", "xxx"]
        self.opt_machinery_equipment_origin = ["get_by_role_combox_select", "#select2-originId-container", "xxx"]
        self.btn_save_new = ["get_by_role_name", "button", " Save & Add New"]
        self.btn_cancel = ["get_by_role_name", "button", "Close"]
        self.btn_raw_mats_fin_products_add = ["get_by_title_click", "Raw Material/Semi Finished"]
        self.txt_raw_mats_fin_products_description = ["get_by_role_name", "textbox_b", "* Item Description","xxx"]
        self.opt_raw_mats_fin_products_source = ["get_by_role_combox_select", "#select2-productSource-container","xxx"]
        self.opt_raw_mats_fin_products_origin = ["get_by_role_combox_select", "#select2-productOriginId-container","xxx"]
        self.txt_schedule_shifts = ["get_by_location", "fill", "#prodSchedShifts0", "xxx"]
        self.txt_schedule_hours_per_shift = ["get_by_location", "fill", "#prodSchedHourShifts0", "xxx"]
        self.txt_schedule_days_per_month = ["get_by_location", "fill", "#prodSchedDaysMonth0", "xxx"]
        self.btn_save_proceed = ["get_by_role_name", "button", "Save and Proceed"]

    def click_btn_machinery_equipment_add(self):
        self.fw_execute_test_suites(self.btn_machinery_equipment_add)

    def input_txt_machinery_equipment_description(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_machinery_equipment_description, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_machinery_equipment_quantity(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_machinery_equipment_quantity, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_machinery_equipment_cost(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_machinery_equipment_cost, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_opt_machinery_equipment_source(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_machinery_equipment_source, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_opt_machinery_equipment_origin(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_machinery_equipment_origin, get_data)
        self.fw_execute_test_suites(data_processed)

    def click_btn_save_new(self):
        self.fw_execute_test_suites(self.btn_save_new)

    def click_btn_cancel(self):
        self.fw_execute_test_suites(self.btn_cancel)

    def click_btn_raw_mats_fin_products_add(self):
        self.fw_execute_test_suites(self.btn_raw_mats_fin_products_add)

    def input_txt_raw_mats_fin_products_description(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_raw_mats_fin_products_description, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_opt_raw_mats_fin_products_source(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_raw_mats_fin_products_source, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_opt_raw_mats_fin_products_origin(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_raw_mats_fin_products_origin, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_schedule_shifts(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_schedule_shifts, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_schedule_hours_per_shift(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_schedule_hours_per_shift, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_schedule_days_per_month(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_schedule_days_per_month, get_data)
        self.fw_execute_test_suites(data_processed)

    def click_btn_save_proceed(self):
        self.fw_execute_test_suites(self.btn_save_proceed)

class BermsPageAreasUtilitiesWasteDisposal(FrameWorkPWDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.utility_f = UtilityPackage()
        self.txt_owner_area = ["get_by_location", "fill", "#total_area_sqm", "xxx"]
        self.opt_location = ["get_by_role_combox_select", "#select2-zoneId-container","xxx"]
        self.opt_region = ["get_by_role_combox_select", "#select2-zone_addressRegionId-container","xxx"]
        self.opt_province = ["get_by_role_combox_select", "#select2-zone_addressProvinceId-container","xxx"]
        self.opt_city = ["get_by_role_combox_select", "#select2-zone_addressCityId-container","xxx"]
        self.opt_barangay = ["get_by_role_combox_select", "#select2-zone_addressBarangayId-container","xxx"]
        self.txt_street = ["get_by_role_name", "textbox_b", "Street Name", "xxx"]
        self.txt_unitowner_fname = ["get_by_location", "fill", "#unitOwnerFirstname","xxx"]
        self.txt_unitowner_lname = ["get_by_location", "fill", "#unitOwnerLastname","xxx"]
        self.txt_lotowner_fname = ["get_by_location", "fill", "#lotOwnerFirstname","xxx"]
        self.txt_lotowner_lname = ["get_by_location", "fill", "#lotOwnerLastname","xxx"]
        self.txt_lessor_fname = ["get_by_location", "fill", "#lessorFirstname", "xxx"]
        self.txt_lessor_lname = ["get_by_location", "fill", "#lessorLastname", "xxx"]
        self.txt_water_yr_req = ["get_by_location", "fill", "#water_yr_req", "xxx"]
        self.txt_electric_yr_req = ["get_by_location", "fill", "#electric_yr_req", "xxx"]
        self.txt_waste_d_desc = ["get_by_location", "fill", "#waste_disposal_desc","xxx"]
        self.txt_waste_d_method = ["get_by_location", "fill", "#waste_disposal_method_desc","xxx"]
        self.add_waste_products = ["get_by_file_chooser", "#activity_wasteproducts_supporting_documentsDropzone",r"xxx"]
        self.add_generated_waste = ["get_by_file_chooser","#activity_generatedwaste_supporting_documentsDropzone",r"xxx"]
        self.btn_save_proceed = ["get_by_role_name", "button", "Save and Proceed"]

    def input_txt_owner_area(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_owner_area, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_opt_location(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_location, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_opt_region(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_region, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_opt_province(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_province, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_opt_city(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_city, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_opt_barangay(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_barangay, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_street(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_street, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_unitowner_fname(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_unitowner_fname, get_data)
        self.fw_execute_test_suites(data_processed)
    def input_txt_unitowner_lname(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_unitowner_lname, get_data)
        self.fw_execute_test_suites(data_processed)
    def input_txt_lotowner_fname(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_lotowner_fname, get_data)
        self.fw_execute_test_suites(data_processed)
    def input_txt_lotowner_lname(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_lotowner_lname, get_data)
        self.fw_execute_test_suites(data_processed)
    def input_txt_lessor_fname(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_lessor_fname, get_data)
        self.fw_execute_test_suites(data_processed)
    def input_txt_lessor_lname(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_lessor_lname, get_data)
        self.fw_execute_test_suites(data_processed)

        self.txt_water_yr_req = ["get_by_location", "fill", "#water_yr_req", "xxx"],
        self.txt_electric_yr_req = ["get_by_location", "fill", "#electric_yr_req", "999456"],
        self.txt_waste_d_desc = ["get_by_location", "fill", "#waste_disposal_desc", "WASTE DISPOSAL DESCRIPTION"]
        self.txt_waste_d_method = ["get_by_location", "fill", "#waste_disposal_method_desc", "DISCUSSION OF METHODS"]
        self.add_waste_products = ["get_by_file_chooser", "#activity_wasteproducts_supporting_documentsDropzone",
                                   r"Testing_document.png"]
        self.add_generated_waste = ["get_by_file_chooser", "#activity_generatedwaste_supporting_documentsDropzone",
                                    r"Testing_document.png"]

    def input_txt_water_yr_req(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_water_yr_req, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_electric_yr_req(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_electric_yr_req, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_waste_d_desc(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_waste_d_desc, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_waste_d_method(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_waste_d_method, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_waste_products(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_waste_products, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_generated_waste(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_generated_waste, get_data)
        self.fw_execute_test_suites(data_processed)

    def click_btn_save_proceed(self):
        self.fw_execute_test_suites(self.btn_save_proceed)

class BermsPageMarketAspect(FrameWorkPWDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.utility_f = UtilityPackage()
        self.opt_export_rate = ["get_by_role_combox_select", "#select2-exportPercent-container","xxx"]
        self.opt_domestic_rate = ["get_by_role_combox_select", "#select2-importPercent-container","xxx"]
        self.opt_country_export = ["get_by_role_combox_multiple_select", "^$","xxx"]
        self.txt_country_domestic_clients = ["get_by_location_fill_d", "#domestic_clients", "xxx"]
        self.txt_country_x_selling_price = ["get_by_location", "fill", "#export_selling_price","xxx"]
        self.txt_country_d_selling_price = ["get_by_location", "fill", "#domestic_selling_price","xxxx"]
        self.opt_country_uom = ["get_by_role_combox_select", "#select2-projected_volume_sales_id-container","xxx"]
        self.btn_country_add_e_marketavv = ["get_by_title_click", "Add Export"]
        self.txt_country_add_e_marketavv0 = ["get_by_location", "fill", "#export_marketAspectVolumeValue0", "xxx"]
        self.txt_country_add_e_marketavv1 = ["get_by_location", "fill", "#export_marketAspectVolumeValue1", "xxx"]
        self.txt_country_add_e_marketavv2 = ["get_by_location", "fill", "#export_marketAspectVolumeValue2", "xxx"]
        self.btn_country_add_i_marketavv = ["get_by_title_click", "Add Local"]
        self.txt_country_add_i_marketavv0 = ["get_by_location", "fill","#import_marketAspectVolumeValue0", "xxx"]
        self.txt_country_add_i_marketavv1 = ["get_by_location", "fill","#import_marketAspectVolumeValue1", "xxx"]
        self.txt_country_add_i_marketavv2 = ["get_by_location", "fill","#import_marketAspectVolumeValue2", "xxx"]
        self.btn_save_proceed = ["get_by_role_name", "button", "Save and Proceed"]

    def select_opt_export_rate(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_export_rate, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_opt_domestic_rate(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_domestic_rate, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_opt_country_export(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_country_export, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_country_domestic_clients(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_country_domestic_clients, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_country_x_selling_price(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_country_x_selling_price, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_country_d_selling_price(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_country_d_selling_price, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_opt_country_uom(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_country_uom, get_data)
        self.fw_execute_test_suites(data_processed)

    def click_btn_country_add_e_marketavv(self):
        self.fw_execute_test_suites(self.btn_country_add_e_marketavv)

    def input_txt_country_add_e_marketavv0(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_country_add_e_marketavv0, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_country_add_e_marketavv1(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_country_add_e_marketavv1, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_country_add_e_marketavv2(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_country_add_e_marketavv2, get_data)
        self.fw_execute_test_suites(data_processed)

    def click_btn_country_add_i_marketavv(self):
        self.fw_execute_test_suites(self.btn_country_add_i_marketavv)

    def input_txt_country_add_i_marketavv0(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_country_add_i_marketavv0, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_country_add_i_marketavv1(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_country_add_i_marketavv1, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_country_add_i_marketavv2(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_country_add_i_marketavv2, get_data)
        self.fw_execute_test_suites(data_processed)

    def click_btn_save_proceed(self):
        self.fw_execute_test_suites(self.btn_save_proceed)

class BermsPageInitialProjectCost(FrameWorkPWDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.utility_f = UtilityPackage()
        self.txt_construction_renovation = ["get_by_location", "fill", "[name='projectCost[building_construction_renovation]']", "xxx"]
        self.txt_factory_tools = ["get_by_location", "fill", "[name='projectCost[factory_tools]']", "xxx"]
        self.txt_transportation_cost = ["get_by_location", "fill", "[name='projectCost[transporation]']", "xxx"]
        self.txt_office_equipment = ["get_by_location", "fill", "[name='projectCost[office_equipment]']", "xxx"]
        self.txt_other_assets = ["get_by_location", "fill", "[name='projectCost[other_assets]']", "xxxx"]
        self.txt_operating_expenses = ["get_by_location", "fill", "[name='projectCost[operating_expenses]']", "xxx"]
        self.txt_working_capital = ["get_by_location", "fill", "[name='projectCost[working_capital]']", "xxx"]
        self.txt_project_equity = ["get_by_location", "fill", "[name='fund_source[0][amount]']", "xxx"]
        self.opt_project_fund_source_1 = ["get_by_location_option_select", "#fundSource2", "xxx"]
        self.txt_project_add_equity = ["get_by_location", "fill", "[name='fund_source[1][amount]']", "xxx"]
        self.opt_project_fund_source_2 = ["get_by_location_option_select", "#fundSource3", "xxx"]
        self.txt_project_advances = ["get_by_location", "fill", "[name='fund_source[2][amount]']", "xxx"]
        self.txt_project_loans = ["get_by_location_fill_c", "[name='fund_source[3][amount]']", "xxx"]
        self.btn_save_proceed = ["get_by_role_name", "button", "Save and Proceed"]

    def input_txt_construction_renovation(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_construction_renovation, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_factory_tools(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_factory_tools, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_transportation_cost(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_transportation_cost, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_office_equipment(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_office_equipment, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_other_assets(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_other_assets, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_operating_expenses(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_operating_expenses, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_working_capital(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_working_capital, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_project_equity(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_project_equity, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_opt_project_fund_source_1(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_project_fund_source_1, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_project_add_equity(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_project_add_equity, get_data)
        self.fw_execute_test_suites(data_processed)

    def select_opt_project_fund_source_2(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.opt_project_fund_source_2, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_project_advances(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_project_advances, get_data)
        self.fw_execute_test_suites(data_processed)

    def input_txt_project_loans(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.txt_project_loans, get_data)
        self.fw_execute_test_suites(data_processed)

    def click_btn_save_proceed(self):
        self.fw_execute_test_suites(self.btn_save_proceed)

class BermsPageSupportingDocuments(FrameWorkPWDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.utility_f = UtilityPackage()
        self.add_notarized_affidavit_of_option = ["get_by_file_chooser", "#dropzoneInnernao10",r"xxx"]
        self.add_notarized_secretarys_certificate_anti_graft = ["get_by_file_chooser", "#dropzoneInnersc_agraft9",r"xxx"]
        self.add_notarized_applicants_undertaking = ["get_by_file_chooser", "#dropzoneInnerund8",r"xxx"]
        self.add_by_laws_indicating_purpose_etc = ["get_by_file_chooser", "#dropzoneInnerby_law7", r"xxx"]
        self.add_articles_of_incorporation= ["get_by_file_chooser", "#dropzoneInneraoi6", r"xxx"]
        self.add_general_information_sheet = ["get_by_file_chooser", "#dropzoneInnergis5", r"xxx"]
        self.add_20_year_projected_fin_statement = ["get_by_file_chooser", "#dropzoneInnerpfs4", r"xxx"]
        self.add_bir_form_2303 = ["get_by_file_chooser", "#dropzoneInnerbir3", r"xxx"]
        self.add_company_profile_of_parent_comp = ["get_by_file_chooser", "#dropzoneInnercppc2", r"xxx"]
        self.add_resume_of_principal_officers = ["get_by_file_chooser", "#dropzoneInnerrbpo1", r"xxx"]
        self.add_sec_certificate = ["get_by_file_chooser", "#dropzoneInnercrsec0", r"xxx"]
        self.add_site_development_plan_and_vicinity_map = ["get_by_file_chooser", "#dropzoneInnerSDPVM12", r"xxx"]
        self.add_notarized_affidavit_of_option_1 = ["get_by_file_chooser", "#dropzoneInnernao11", r"Txxx"]
        self.add_proof_of_land_ownership_or_any_document = ["get_by_file_chooser", "#dropzoneInnerplo10", r"xxx"]
        self.add_list_of_goods_handled = ["get_by_file_chooser", "#dropzoneInnerlgh10", r"xxx"]
        self.add_certification_from_the_national = ["get_by_file_chooser", "#dropzoneInnerCN18", r"xxx"]
        self.add_endorsement_from_doe = ["get_by_file_chooser", "#dropzoneInnerFEDOE17", r"xxx"]
        self.add_endorsement_from_local_water_district = ["get_by_file_chooser", "#dropzoneInnerFELWD16", r"xxx"]
        self.add_site_development_plan_and_vicinity_map_1 = ["get_by_file_chooser", "#dropzoneInnerSDPVM15", r"xxx"]
        self.add_operation_plan_including_capacity_plan = ["get_by_file_chooser", "#dropzoneInnerCOP14", r"xxx"]
        self.add_drawing_layout_support_structure_arrangement = ["get_by_file_chooser", "#dropzoneInnerSSA13", r"xxx"]
        self.add_notarized_affidavit_of_option_2 = ["get_by_file_chooser", "#dropzoneInnernao12", r"xxx"]
        self.add_certification_from_national_water_resources_board = ["get_by_file_chooser", "#dropzoneInnernwrc11", r"xxx"]
        self.add_endorsement_dot_and_doh= ["get_by_file_chooser", "#dropzoneInneredt_dh10", r"Testing_document.png"]
        self.btn_save_proceed = ["get_by_role_name", "button", "Save and Proceed"]

    def file_add_endorsement_dot_and_doh(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_endorsement_dot_and_doh, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_notarized_affidavit_of_option_2(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_notarized_affidavit_of_option_2, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_certification_from_national_water_resources_board(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_certification_from_national_water_resources_board, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_drawing_layout_support_structure_arrangement(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_drawing_layout_support_structure_arrangement, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_site_development_plan_and_vicinity_map_1(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_site_development_plan_and_vicinity_map_1, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_operation_plan_including_capacity_plan(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_operation_plan_including_capacity_plan, get_data)
        self.fw_execute_test_suites(data_processed)

    # def file_add_drawing_layout_support_structure_arrangement(self, get_data):
    #     data_processed = self.utility_f.add_data_in_array(self.add_drawing_layout_support_structure_arrangement, get_data)
    #     self.fw_execute_test_suites(data_processed)

    def file_add_certification_from_the_national(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_certification_from_the_national, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_endorsement_from_doe(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_endorsement_from_doe, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_endorsement_from_local_water_district(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_endorsement_from_local_water_district, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_list_of_goods_handled(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_list_of_goods_handled, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_site_development_plan_and_vicinity_map(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_site_development_plan_and_vicinity_map, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_notarized_affidavit_of_option_1(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_notarized_affidavit_of_option_1, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_proof_of_land_ownership_or_any_document(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_proof_of_land_ownership_or_any_document, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_notarized_affidavit_of_option(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_notarized_affidavit_of_option, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_notarized_secretarys_certificate_anti_graft(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_notarized_secretarys_certificate_anti_graft, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_notarized_applicants_undertaking(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_notarized_applicants_undertaking, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_by_laws_indicating_purpose_etc(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_by_laws_indicating_purpose_etc, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_articles_of_incorporation(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_articles_of_incorporation, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_general_information_sheet(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_general_information_sheet, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_20_year_projected_fin_statement(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_20_year_projected_fin_statement, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_bir_form_2303(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_bir_form_2303, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_company_profile_of_parent_comp(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_company_profile_of_parent_comp, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_resume_of_principal_officers(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_resume_of_principal_officers, get_data)
        self.fw_execute_test_suites(data_processed)

    def file_add_sec_certificate(self, get_data):
        data_processed = self.utility_f.add_data_in_array(self.add_sec_certificate, get_data)
        self.fw_execute_test_suites(data_processed)

    def click_btn_save_proceed(self):
        self.fw_execute_test_suites(self.btn_save_proceed)


class BermsPageSubmission(FrameWorkPWDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.utility_f = UtilityPackage()

        self.btn_application_submit = ["get_by_role_name", "button", "SUBMIT"]
        self.btn_submission_proceed = ["get_by_role_name", "button", "Proceed"]
        self.txt_application_number = ["expect_locator", "#swal2-html-container strong span"]
        self.save_application_number = ["expect_locator_inner_txt_save_to_file", "#swal2-html-container strong span"]
        self.btn_submission_proceed_confirm = ["get_by_role_name", "button", "OK"]

    def click_btn_application_submit(self):
        self.fw_execute_test_suites(self.btn_application_submit)

    def click_btn_submission_proceed(self):
        self.fw_execute_test_suites(self.btn_submission_proceed)

    def verify_txt_application_number(self):
        self.fw_execute_test_suites(self.txt_application_number)

    def verify_save_application_number(self):
        self.fw_execute_test_suites(self.save_application_number)

    def file_save_application_number(self):
        self.fw_execute_test_suites(self.save_application_number)

    def click_btn_submission_proceed_confirm(self):
        self.fw_execute_test_suites(self.btn_submission_proceed_confirm)