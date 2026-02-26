import pytest, re
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
            "rbtn_type_ezone": ["get_by_role_name","radio_b", "Facilities"],
            "opt_psic_classification": ["get_by_role_combox_select", "#select2-sectionCodeId-container","Accommodation and Food Service Activities"],
            "opt_psic_division": ["get_by_role_combox_select", "#select2-divisionCodeId-container","[56] FOOD AND BEVERAGE SERVICE ACTIVITIES"],
            "opt_psic_group": ["get_by_role_combox_select", "#select2-groupCodeId-container","[563] Beverage serving activities"],
            "opt_psic_class": ["get_by_role_combox_select", "#select2-classesCodeId-container","[5630] Beverage serving activities"],
            "opt_psic_sub_class": ["get_by_role_combox_select", "#select2-subClassesCodeId-container","[56309] Other beverage serving activities, n.e.c."],
            "btn_proceed_app": ["get_by_role_name", "button", "Proceed"]
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_company_pesonal_info(self) -> None:
        data_element_action = {
            "txt_company_name": ["get_by_role_name", "textbox_a", "Company Name", "FACILITIES COMPANY NAME TESTING 017"],
            "txt_nature_business": ["get_by_role_name", "textbox_a", "Nature of Business", "NATURE OF BUSINESS TESTING 017"],
            "txt_company_profile": ["get_by_role_name", "textbox_a", "Company Profile", "COMPANY PROFILE TESTING 017"],
            "btn_san_company_person_info": ["get_by_role_name", "button", "Save and Proceed"]
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_company_proposed_project(self) -> None:
        data_element_action = {
            "btn_proposed_project": ["get_by_location", "click", "#btnBusinessProduct"],
            "txt_proposed_project": ["get_by_location_fill_b", "#newBusinessProductActivity", "NEW PRODUCT ACTIVITY FACILITIES COMPANY 017"],
            "btn_proposed_project_add": ["get_by_role_name", "button", " Add"],
            "txt_proposed_project_desc": ["get_by_role_name", "textbox_b", "* Description:", "NEW PRODUCT ACTIVITY FACILITIES COMPANY 017 DESCRIPTION"],
            "txt_proposed_project_desc_uses": ["get_by_role_name", "textbox_b", "* Uses/Application:", "USES AND APPLICATION NEW PRODUCT ACTIVITY FACILITIES COMPANY 017"],
            # "add_proposed_project_permit": ["get_by_file_chooser", "choose a file", r"Testing_document.png"],
            "add_proposed_project_permit": ["get_by_file_chooser", "#activity_product_img_documentsDropzone", r"Testing_document.png"],
            "btn_proposed_project_save_next": ["get_by_role_name", "button", "Save and Proceed"]

        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_existing_business_reg(self) -> None:
        data_element_action = {
            "date_proposed_registration_date": ["get_by_role_name", "row_dp", "Securities & Exchange","DD-MMM-YYYY","2016-01-11"],
            "txt_proposed_registration_no": ["get_by_location", "fill", "input[name=\"businessRegInfoAppsBean[0].reg_no\"]","REG-2025-002"],
            "txt_proposed_sec_primary_purpose": ["get_by_role_name", "textbox_b", "Sec Primary Purpose","SEC PRIMARY PURPOSE 002"],
            "txt_proposed_authorized_amount": ["get_by_role_name", "textbox_b", "Authorized Amount (PHP)","99999999999"],
            "txt_proposed_subscribed_amount": ["get_by_role_name", "textbox_b", "Subscribe Amount (PHP)","99999999999"],
            "txt_proposed_paid-up_amount": ["get_by_role_name", "textbox_b", "* Paid-up Amount (PHP):","99999999999"],
            "btn_proposed_existing_registration_next": ["get_by_role_name", "button", "Save and Proceed"]
            # "add_proposed_project_permit": ["get_by_file_chooser", "choose a file", r"Testing_document.png"],
            # "btn_proposed_project_save_next": ["get_by_role_name", "button", "Save and Proceed"]

        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_stockholder_reg(self) -> None:
        data_element_action = {
            "txt_proposed_stockholder_type": ["get_by_role_name", "radio_b", "Corporate"],
            # "txt_proposed_stockholder_type1": ["get_by_role_name", "radio_b", "Person"],
            "btn_proposed_stockholder_add": ["get_by_title_click", "Add Stockholder"],
            "txt_proposed_stockholder_company_name": ["get_by_role_name", "textbox_b", "Company Name *", "COMPANY NAME CORP"],
            "txt_proposed_stockholder_nationality": ["get_by_role_combox_select","#select2-proposedStockholderNationalityId-container","Finnish"],
            "txt_proposed_stockholder_no_shares": ["get_by_role_name", "textbox_b", "No. of Shares *","1280"],
            "txt_proposed_stockholder_subscribed": ["get_by_role_name", "textbox_b", "Amount Subscribe (PHP) *","1281"],
            "txt_proposed_stockholder_amount_paid": ["get_by_role_name", "textbox_b", "Amount Paid-up (PHP) *","1282"],
            "txt_proposed_stockholder_amount_add_proceed": ["get_by_role_name", "button", " Add"],
            "txt_proposed_stockholder_item": ["get_by_location","click","#isListedStockholder1"],
            "txt_proposed_stockholder_item1": ["get_by_location","click","#isListedStockholder2"],
            # "txt_proposed_stockholder_item1": ["get_by_location","filter_th_click","#stockholderWrapper div","Not Applicable","1"],
            "btn_proposed_principal_officer_add": ["get_by_title_click","Add Principal Officer"],
            "opt_proporse_principal_officer_salutation": ["get_by_role_combox_select","#select2-officerSalutationId-container","Mr."],
            "txt_proporse_principal_officer_fname": ["get_by_role_name", "textbox_b", "* First Name","PRNCIPAL FNAME"],
            "txt_proporse_principal_officer_mname": ["get_by_role_name", "textbox_b", "Middle Name (Optional)",""],
            "txt_proporse_principal_officer_lname": ["get_by_role_name", "textbox_b", "* Last Name", "PRINCIPAL LNAME"],
            "txt_proporse_principal_officer_position": ["get_by_location", "fill", "#officerPosition","PRESIDENT"],
            "btn_proposed_principal_officer_add_proceed": ["get_by_role_name", "button"," Add"],
            "btn_proposed_principal_officer_save_next": ["get_by_role_name", "button", "Save and Proceed"]
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_manpower_timetable(self) -> None:
        data_element_action = {
            "dp_timetable_bld_construction_fr": ["select_date_picker_v1", "xpath=(//div[@id=\"manpower-and-timetable\"]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/input[2])","11/1/2028"],
            "dp_timetable_bld_construction_to": ["select_date_picker_v1", "xpath=(//div[@id=\"manpower-and-timetable\"]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/input[2])","9/1/2030"],
            "dp_timetable_bld_procurement_fr": ["select_date_picker_v1", "xpath=(//div[@id=\"manpower-and-timetable\"]/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/input[2])","2/1/2028"],
            "dp_timetable_bld_procurement_to": ["select_date_picker_v1", "xpath=(//div[@id=\"manpower-and-timetable\"]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/input[2])","1/1/2030"],
            "dp_timetable_bld_installation_fr": ["select_date_picker_v1", "xpath=(//div[@id=\"manpower-and-timetable\"]/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/input[2])","10/1/2028"],
            "dp_timetable_bld_installation_to": ["select_date_picker_v1", "xpath=(//div[@id=\"manpower-and-timetable\"]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/input[2])","8/1/2030"],
            "dp_timetable_bld_hiring_fr": ["select_date_picker_v1", "xpath=(//div[@id=\"manpower-and-timetable\"]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/input[2])","12/1/2028"],
            "dp_timetable_bld_hiring_to": ["select_date_picker_v1", "xpath=(//div[@id=\"manpower-and-timetable\"]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/input[2])","11/1/2030"],
            "dp_timetable_bld_start_commercial": ["select_date_picker_v1", "xpath=(//div[@id=\"manpower-and-timetable\"]/div[2]/div[3]/div/div/div/div[2]/div/input[2])","2/1/2031"],
            "txt_timetable_bld_service0": ["get_by_location", "fill", "#servicePersonnelCount0", "10"],
            "txt_timetable_bld_service1": ["get_by_location", "fill", "#servicePersonnelCount1", "20"],
            "txt_timetable_bld_service2": ["get_by_location", "fill", "#servicePersonnelCount2", "100"],
            "txt_timetable_bld_indirect0": ["get_by_location", "fill", "#indirectPersonnelCount0", "10"],
            "txt_timetable_bld_indirect1": ["get_by_location", "fill", "#indirectPersonnelCount1", "20"],
            "txt_timetable_bld_indirect2": ["get_by_location", "fill", "#indirectPersonnelCount2", "100"],
            "txt_timetable_bld_admin0": ["get_by_location", "fill", "#adminPersonnelCount0", "100"],
            "txt_timetable_bld_admin1": ["get_by_location", "fill", "#adminPersonnelCount1", "100"],
            "txt_timetable_bld_admin2": ["get_by_location", "fill", "#adminPersonnelCount2", "100"],
            "btn_timetable_bld_save_proceed": ["get_by_role_name", "button", "Save and Proceed"]

        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_manu_servi_flow(self) -> None:
        data_element_action = {
            "txt_desrcibe_manufacturing_name": ["get_by_role_name", "textbox_a", "Describe the Manufacturing","MANUFACTURING PROCESS SERVICE FLOW TESTING 001"],
            # "add_diagram_process_flow": ["get_by_file_chooser", "Click Here", r"Testing_document.png"],
            "add_diagram_process_flow": ["get_by_file_chooser", "#addtlInfo_supporting_documentsDropzone", r"Testing_document.png"],
            "btn_manu_servi_flow_proceed": ["get_by_role_name", "button", "Save and Proceed"]
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_m_rp_p_schedule_add_machinery_equipment(self) -> None:
        data_element_action = {
            "btn_machinery_equipment_add": ["get_by_title_click", "Machinery/Equipments"],
            "txt_machinery_equipment_description": ["get_by_role_name", "textbox_b", "* Item Description", "DESCRIPTION 001"],
            "txt_machinery_equipment_quantity": ["get_by_location", "fill", "#itemQty", "100000"],
            "txt_machinery_equipment_cost": ["get_by_location", "fill", "#itemUnitCost", "100"],
            "opt_machinery_equipment_source": ["get_by_role_combox_select", "#select2-itemSource-container","IMPORTED"],
            "opt_machinery_equipment_origin": ["get_by_role_combox_select", "#select2-originId-container","[DE] Germany"],
            "btn_machinery_equipment_save_new": ["get_by_role_name", "button", " Save & Add New"],
            "btn_machinery_equipment_cancel": ["get_by_role_name", "button", "Close"]
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_m_rp_p_schedule_add_materials(self) -> None:
        data_element_action = {
            "btn_raw_mats_fin_products_add": ["get_by_title_click", "Raw Material/Semi Finished"],
            "txt_raw_mats_fin_products_description": ["get_by_role_name", "textbox_b", "* Item Description","ITEM DESCRIPTION 001"],
            "opt_raw_mats_fin_products_source": ["get_by_role_combox_select", "#select2-productSource-container","IMPORTED"],
            "opt_raw_mats_fin_products_origin": ["get_by_role_combox_select", "#select2-productOriginId-container","[DE] Germany"],
            "btn_raw_mats_fin_products_save_new": ["get_by_role_name", "button", " Save & Add New"],
            "btn_raw_mats_fin_products_cancel": ["get_by_role_name", "button", "Close"]
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_m_rp_p_schedule_add_schedule(self) -> None:
        data_element_action = {
            "txt_scheudle_shifts": ["get_by_location", "fill", "#prodSchedShifts0", "3"],
            "txt_schedule_hours_per_shift": ["get_by_location", "fill", "#prodSchedHourShifts0", "8"],
            "txt_schedule_days_per_monthj": ["get_by_location", "fill", "#prodSchedDaysMonth0", "21"],
            "btn_m_rp_p_schedule_add_proceed": ["get_by_role_name", "button", "Save and Proceed"]
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_areas_utilities_w_disposal(self) -> None:
        data_element_action = {
            "txt_areas_utilities_w_disposal_owner_area": ["get_by_location", "fill", "#total_area_sqm", "5765"],
            "opt_areas_utilities_w_disposal_location": ["get_by_role_combox_select", "#select2-zoneId-container","[2CYV] [24]7 PLAZA"],
            "opt_areas_utilities_w_disposal_region": ["get_by_role_combox_select", "#select2-zone_addressRegionId-container","NATIONAL CAPITAL REGION (NCR)"],
            "opt_areas_utilities_w_disposal_province": ["get_by_role_combox_select", "#select2-zone_addressProvinceId-container","METRO MANILA"],
            "opt_areas_utilities_w_disposal_city": ["get_by_role_combox_select", "#select2-zone_addressCityId-container","CALOOCAN CITY"],
            "opt_areas_utilities_w_disposal_barangay": ["get_by_role_combox_select", "#select2-zone_addressBarangayId-container","BARANGAY 1"],
            "txt_areas_utilities_w_disposal_street": ["get_by_role_name", "textbox_b", "Street Name","STREET NAME TEST INPUT 001"],
            "txt_areas_utilities_w_disposal_unitowner_Fname": ["get_by_location", "fill", "#unitOwnerFirstname", "UNIT OWNER FNAME"],
            "txt_areas_utilities_w_disposal_unitowner_lname": ["get_by_location", "fill", "#unitOwnerLastname", "UNIT OWNER LNAME"],
            "txt_areas_utilities_w_disposal_lotowner_fname": ["get_by_location", "fill", "#lotOwnerFirstname", "LOT OWNER LNAME"],
            "txt_areas_utilities_w_disposal_lotowner_lname": ["get_by_location", "fill", "#lotOwnerLastname", "LOT OWNER LNAME"],
            "txt_areas_utilities_w_disposal_lessor_fname": ["get_by_location", "fill", "#lessorFirstname", "LESSOR LNAME"],
            "txt_areas_utilities_w_disposal_lessor_lname": ["get_by_location", "fill", "#lessorLastname", "LESSOR LNAME"],
            "txt_areas_utilities_w_disposal_water_yr_req": ["get_by_location", "fill", "#water_yr_req", "100"],
            "txt_areas_utilities_w_disposal_electric_yr_req": ["get_by_location", "fill", "#electric_yr_req", "999456"],
            "txt_areas_utilities_w_disposal_waste_d_desc": ["get_by_location", "fill", "#waste_disposal_desc", "WASTE DISPOSAL DESCRIPTION"],
            "txt_areas_utilities_w_disposal_waste_d_method": ["get_by_location", "fill", "#waste_disposal_method_desc", "DISCUSSION OF METHODS"],
            "add_areas_utilities_w_disposal_waste_products": ["get_by_file_chooser", "#activity_wasteproducts_supporting_documentsDropzone",r"Testing_document.png"],
            "add_areas_utilities_w_disposal_generated_waste": ["get_by_file_chooser", "#activity_generatedwaste_supporting_documentsDropzone",r"Testing_document.png"],
            "btn_areas_utilities_w_disposal_add_proceed": ["get_by_role_name", "button", "Save and Proceed"]
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_market_aspec(self) -> None:
        data_element_action = {
            "opt_market_aspect_export_rate": ["get_by_role_combox_select", "#select2-exportPercent-container","50%"],
            "opt_market_aspect_domestic_rate": ["get_by_role_combox_select", "#select2-importPercent-container","50%"],
            "opt_market_aspect_country_export": ["get_by_role_combox_multiple_select", "^$","[HM] Heard Island and McDonald Islands"],
            "txt_market_aspect_country_domestic_clients": ["get_by_location_fill_d", "#domestic_clients", "DOMESTIC CLIENTS"],
            "txt_market_aspect_country_x_selling_price": ["get_by_location", "fill", "#export_selling_price","2354"],
            "txt_market_aspect_country_d_selling_price": ["get_by_location", "fill", "#domestic_selling_price","4532"],
            "opt_market_aspect_country_uom": ["get_by_role_combox_select", "#select2-projected_volume_sales_id-container","[KGM] Kilogram"],
            # "btn_market_aspect_country_add_e_marketavv": ["get_by_title_click", "Add Export"],
            "txt_market_aspect_country_add_e_marketavv0": ["get_by_location", "fill", "#export_marketAspectVolumeValue0", "8888"],
            "txt_market_aspect_country_add_e_marketavv1": ["get_by_location", "fill", "#export_marketAspectVolumeValue1", "8888"],
            "txt_market_aspect_country_add_e_marketavv2": ["get_by_location", "fill", "#export_marketAspectVolumeValue2", "8888"],
            # "btn_market_aspect_country_add_i_marketavv": ["get_by_title_click", "Add Local"],
            "txt_market_aspect_country_add_i_marketavv0": ["get_by_location", "fill","#import_marketAspectVolumeValue0", "7777"],
            "txt_market_aspect_country_add_i_marketavv1": ["get_by_location", "fill","#import_marketAspectVolumeValue1", "7777"],
            "txt_market_aspect_country_add_i_marketavv2": ["get_by_location", "fill","#import_marketAspectVolumeValue2", "7777"],
            "btn_market_aspect_country_add_proceed": ["get_by_role_name", "button", "Save and Proceed"]
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_initial_project_cost(self) -> None:
        data_element_action = {
            "txt_initial_project_cost_construc_renov": ["get_by_location", "fill", "[name='projectCost[building_construction_renovation]']", "10"],
            "txt_initial_project_cost_factory_tools": ["get_by_location", "fill", "[name='projectCost[factory_tools]']", "25"],
            "txt_initial_project_cost_transportation": ["get_by_location", "fill", "[name='projectCost[transporation]']", "25"],
            "txt_initial_project_cost_office_equipment": ["get_by_location", "fill", "[name='projectCost[office_equipment]']", "37"],
            "txt_initial_project_cost_other_assets": ["get_by_location", "fill", "[name='projectCost[other_assets]']", "1000"],
            "txt_initial_project_cost_operating_expenses": ["get_by_location", "fill", "[name='projectCost[operating_expenses]']", "28"],
            "txt_initial_project_cost_working_capital": ["get_by_location", "fill", "[name='projectCost[working_capital]']", "100"],
            "txt_initial_project_cost_equity": ["get_by_location", "fill", "[name='fund_source[0][amount]']", "10001000"],
            "opt_initial_project_cost_fund_source_1": ["get_by_location_option_select", "#fundSource2", "Foreign Loan"],
            "txt_initial_project_cost_add_equity": ["get_by_location", "fill", "[name='fund_source[1][amount]']", "100"],
            "opt_initial_project_cost_fund_source_2": ["get_by_location_option_select", "#fundSource3", "Local Loan"],
            "txt_initial_project_cost_advances": ["get_by_location", "fill", "[name='fund_source[2][amount]']", "100"],
            "txt_initial_project_cost_loans": ["get_by_location_fill_c", "[name='fund_source[3][amount]']", "25"],
            "btn_initial_project_cost_add_proceed": ["get_by_role_name", "button", "Save and Proceed"]
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_supporting_documents_0(self) -> None:
        data_element_action = {
            "add_supporing_documents": ["get_by_file_chooser", "#dropzoneInnerSDPVM12",r"Testing_document.png"],
            "add_supporing_documents1": ["get_by_file_chooser", "#dropzoneInnernao11",r"Testing_document.png"],
            "add_supporing_documents2": ["get_by_file_chooser", "#dropzoneInnerplo10",r"Testing_document.png"]
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)



    def test_create_new_berms_supporting_documents_1(self) -> None:
        data_element_action = {
            "add_supporing_documents": ["get_by_file_chooser", "#dropzoneInnersc_agraft9",r"Testing_document.png"],
            "add_supporing_documents1": ["get_by_file_chooser", "#dropzoneInnerund8",r"Testing_document.png"],
            "add_supporing_documents2": ["get_by_file_chooser", "#dropzoneInnerby_law7",r"Testing_document.png"]
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_supporting_documents_2(self) -> None:
        data_element_action = {
            "add_supporing_documents": ["get_by_file_chooser", "#dropzoneInneraoi6",r"Testing_document.png"],
            "add_supporing_documents1": ["get_by_file_chooser", "#dropzoneInnergis5",r"Testing_document.png"],
            "add_supporing_documents2": ["get_by_file_chooser", "#dropzoneInnerpfs4", r"Testing_document.xlsx"]
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_supporting_documents_3(self) -> None:
        data_element_action = {
            "add_supporing_documents": ["get_by_file_chooser", "#dropzoneInnerbir3",r"Testing_document.png"],
            "add_supporing_documents1": ["get_by_file_chooser", "#dropzoneInnercppc2",r"Testing_document.png"],
            "add_supporing_documents2": ["get_by_file_chooser", "#dropzoneInnerrbpo1", r"Testing_document.png"],
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_supporting_documents_4(self) -> None:
        data_element_action = {
            "add_supporing_documents": ["get_by_file_chooser", "#dropzoneInnercrsec0", r"Testing_document.png"],
            "btn_add_proceed": ["get_by_role_name", "button", "Save and Proceed"]
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

    def test_create_new_berms_submit(self) -> None:
        data_element_action = {
            "btn_add_submit": ["get_by_role_name", "button", "SUBMIT"],
            "btn_add_proceed": ["get_by_role_name", "button", "Proceed"],
            "verify_application_number": ["expect_locator","#swal2-html-container strong span"],
            "btn_add_proceed_confirm": ["get_by_role_name", "button", "OK"]
        }
        self.initiate_test_data().data_processing_func_peza(data_element_action)

        # page = self.driver
        # page.wait_for_timeout(120000)

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