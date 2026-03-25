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


class DataObjectBERMS:
    def __init__(self, driver, payload):
        self.driver = driver
        self.login = payload["Login"]
        self.link_reference = self.get_link_reference()
        self.username_reference = self.get_username_reference()
        self.password_reference = self.get_password_reference()
        self.app_det = payload["Application"]
        self.app_det_type = self.get_app_det_type()
        self.app_loc_type = self.get_app_locator_type()
        self.app_psic_class = self.get_app_psic_class()
        self.app_psic_division = self.get_app_psic_division()
        self.app_psic_div_group = self.get_app_psic_div_group()
        self.app_psic_div_class = self.get_app_psic_div_class()
        self.app_psic_div_subclass = self.get_app_psic_div_subclass()
        self.company_info = payload["Personal_information"]
        self.ci_company_name = self.get_comp_info_company_name()
        self.ci_nature_business = self.get_comp_info_nature_business()
        self.ci_company_profile = self.get_comp_info_company_profile()
        self.proposed_project = payload["Proposed_project"]
        self.propose_project = self.get_prop_proj_propose_project()
        self.proposed_project_desc = self.get_prop_proj_proposed_project_desc()
        self.project_desc_uses = self.get_prop_proj_proposed_project_desc_uses()
        self.proposed_project_permit = self.get_prop_proj_proposed_project_permit()
        self.existing_business_reg = payload["Existing_business_reg"]
        self.registration_date = self.get_exists_bus_reg_registration_date()
        self.registration_no = self.get_exists_bus_reg_registration_no()
        self.sec_primary_purpose = self.get_exists_bus_reg_sec_primary_purpose()
        self.authorized_amount = self.get_exists_bus_reg_authorized_amount()
        self.subscribed_amount = self.get_exists_bus_reg_subscribed_amount()
        self.reg_paid_up_amount = self.get_exists_bus_reg_paid_up_amount()
        self.stockholder_principal_officer = payload["Stockholder_principal_officer"]
        self.stockholder_type = self.get_stockholder_type()
        self.stockholder_name = self.get_stockholder_name()
        self.stockholder_nationality = self.get_stockholder_nationality()
        self.stockholder_no_shares = self.get_stockholder_no_shares()
        self.amount_subscribed = self.get_amount_subscribed()
        self.amount_paid_up = self.get_amount_paid_up()
        self.officer_salutation = self.get_officer_salutation()
        self.officer_fname = self.get_officer_fname()
        self.officer_mname = self.get_officer_mname()
        self.officer_lname = self.get_officer_lname()
        self.officer_position = self.get_officer_position()
        self.manpower_timetable = payload["Manpower_and_timetable"]
        self.construction_start = self.get_construction_start()
        self.construction_end = self.get_construction_end()
        self.procurement_start = self.get_procurement_start()
        self.procurement_end = self.get_procurement_end()
        self.installation_start = self.get_installation_start()
        self.installation_end = self.get_installation_end()
        self.hiring_start = self.get_hiring_start()
        self.hiring_end = self.get_hiring_end()
        self.commercial_start = self.get_commercial_start()
        self.manpower_01_service = self.get_manpower_01_service()
        self.manpower_01_indirect = self.get_manpower_01_indirect()
        self.manpower_01_admin = self.get_manpower_01_admin()
        self.manpower_02_service = self.get_manpower_02_service()
        self.manpower_02_indirect = self.get_manpower_02_indirect()
        self.manpower_02_admin = self.get_manpower_02_admin()
        self.manpower_03_service = self.get_manpower_03_service()
        self.manpower_03_indirect = self.get_manpower_03_indirect()
        self.manpower_03_admin = self.get_manpower_03_admin()
        self.manufacture_service_flow = payload["Manufacturing_service_flow"]
        self.manufacturing_pf_name = self.get_manufacturing_pf_name()
        self.process_flow_diagram = self.get_process_flow_diagram()
        self.raw_materials_machinery_prod = payload["Raw_materials_machinery_prod"]
        self.item_description_m1 = self.get_item_description_m1()
        self.item_quantity_m1 = self.get_item_quantity_m1()
        self.item_cost_m1 = self.get_item_cost_m1()
        self.item_source_m1 = self.get_item_source_m1()
        self.item_origin_m1 = self.get_item_origin_m1()
        self.item_description_r1 = self.get_item_description_r1()
        self.item_source_r1 = self.get_item_source_r1()
        self.item_origin_r1 = self.get_item_origin_r1()
        self.schedule_shifts = self.get_schedule_shifts()
        self.hours_shifts = self.get_hours_shifts()
        self.per_month = self.get_per_month()
        self.area_utilities_waste_disposal = payload["Areas_utilities_waste_disposal"]
        self.au_owner_area = self.get_au_owner_area()
        self.au_location = self.get_au_location()
        self.au_region = self.get_au_region()
        self.au_province = self.get_au_province()
        self.au_city = self.get_au_city()
        self.au_barangay = self.get_au_barangay()
        self.au_street = self.get_au_street()
        self.au_unitowner_fname = self.get_au_unitowner_fname()
        self.au_unitowner_lname = self.get_au_unitowner_lname()
        self.au_lotowner_fname = self.get_au_lotowner_fname()
        self.au_lotowner_lname = self.get_au_lotowner_lname()
        self.au_lessor_fname = self.get_au_lessor_fname()
        self.au_lessor_lname = self.get_au_lessor_lname()
        self.au_water_per_year = self.get_au_water_per_year()
        self.au_electricity_per_year = self.get_au_electricity_per_year()
        self.au_disposal_description = self.get_au_disposal_description()
        self.au_disposal_method = self.get_au_disposal_method()
        self.au_waste_products = self.get_au_waste_products()
        self.au_generated_waste = self.get_au_generated_waste()
        self.market_aspect = payload["Market_aspect"]
        self.ma_export_rate = self.get_ma_export_rate()
        self.ma_domestic_rate = self.get_ma_domestic_rate()
        self.ma_country_export = self.get_ma_country_export()
        self.ma_domestic_clients = self.get_ma_domestic_clients()
        self.ma_x_selling_price = self.get_ma_x_selling_price()
        self.ma_d_selling_price = self.get_ma_d_selling_price()
        self.ma_uom = self.get_ma_uom()
        self.ma_export_vv0 = self.get_ma_export_vv0()
        self.ma_export_vv1 = self.get_ma_export_vv1()
        self.ma_export_vv2 = self.get_ma_export_vv2()
        self.ma_local_vv0 = self.get_ma_local_vv0()
        self.ma_local_vv1 = self.get_ma_local_vv1()
        self.ma_local_vv2 = self.get_ma_local_vv2()
        # self.initial_project_cost_data_obj = payload["Initial_project_cost"]
        self.initial_project_cost = DataObjectBERMSIntialProjectCost(self.driver, payload["Initial_project_cost"])
        self.supporting_documents = DataObjectBERMSSupportingDocuments(self.driver, payload["Supporting_documents"])

    # def get_initial_project_cost(self):
    #     return DataObjectBERMSIntialProjectCost(self.driver, self.initial_project_cost_data_obj)

    def get_link_reference(self):
        set_data = self.login["Link"]
        return set_data

    def get_username_reference(self):
        set_data = self.login["Username"]
        return set_data

    def get_password_reference(self):
        set_data = self.login["Password"]
        return set_data

    def get_app_det_type(self):
        set_data = self.app_det["App_type"]
        return set_data

    def get_app_locator_type(self):
        set_data = self.app_det["Locator_type"]
        return set_data

    def get_app_psic_class(self):
        set_data = self.app_det["Psic_class"]
        return set_data

    def get_app_psic_division(self):
        set_data = self.app_det["Psic_division"]
        return set_data

    def get_app_psic_div_group(self):
        set_data = self.app_det["Psic_div_group"]
        return set_data

    def get_app_psic_div_class(self):
        set_data = self.app_det["Psic_div_class"]
        return set_data

    def get_app_psic_div_subclass(self):
        set_data = self.app_det["Psic_div_subclass"]
        return set_data

    def get_comp_info_company_name(self):
        set_data = self.company_info["Company_name"]
        return set_data

    def get_comp_info_nature_business(self):
        set_data = self.company_info["Nature_business"]
        return set_data

    def get_comp_info_company_profile(self):
        set_data = self.company_info["Company_profile"]
        return set_data

    def get_prop_proj_propose_project(self):
        set_data = self.proposed_project["Proposed_project"]
        return set_data

    def get_prop_proj_proposed_project_desc(self):
        set_data = self.proposed_project["Proposed_project_desc"]
        return set_data

    def get_prop_proj_proposed_project_desc_uses(self):
        set_data = self.proposed_project["Proposed_project_desc_uses"]
        return set_data

    def get_prop_proj_proposed_project_permit(self):
        set_data = self.proposed_project["Proposed_project_permit"]
        return set_data

    def get_exists_bus_reg_registration_date(self):
        set_data = self.existing_business_reg["Registration_date"]
        return set_data

    def get_exists_bus_reg_registration_no(self):
        set_data = self.existing_business_reg["Registration_no"]
        return set_data

    def get_exists_bus_reg_sec_primary_purpose(self):
        set_data = self.existing_business_reg["Sec_primary_purpose"]
        return set_data

    def get_exists_bus_reg_authorized_amount(self):
        set_data = self.existing_business_reg["Authorized_amount"]
        return set_data

    def get_exists_bus_reg_subscribed_amount(self):
        set_data = self.existing_business_reg["Subscribed_amount"]
        return set_data

    def get_exists_bus_reg_paid_up_amount(self):
        set_data = self.existing_business_reg["Paid_up_amount"]
        return set_data

    def get_stockholder_type(self):
        set_data = self.stockholder_principal_officer["Stockholder_type"]
        return set_data

    def get_stockholder_name(self):
        set_data = self.stockholder_principal_officer["Stockholder_name"]
        return set_data

    def get_stockholder_nationality(self):
        set_data = self.stockholder_principal_officer["Stockholder_nationality"]
        return set_data

    def get_stockholder_no_shares(self):
        set_data = self.stockholder_principal_officer["Stockholder_no_shares"]
        return set_data

    def get_amount_subscribed(self):
        set_data = self.stockholder_principal_officer["Amount_subscribe"]
        return set_data

    def get_amount_paid_up(self):
        set_data = self.stockholder_principal_officer["Amount_paid_up"]
        return set_data

    def get_officer_salutation(self):
        set_data = self.stockholder_principal_officer["Officer_salutation"]
        return set_data

    def get_officer_fname(self):
        set_data = self.stockholder_principal_officer["Officer_fname"]
        return set_data

    def get_officer_mname(self):
        set_data = self.stockholder_principal_officer["Officer_mname"]
        return set_data

    def get_officer_lname(self):
        set_data = self.stockholder_principal_officer["Officer_lname"]
        return set_data

    def get_officer_position(self):
        set_data = self.stockholder_principal_officer["Officer_position"]
        return set_data

    def get_construction_start(self):
        set_data = self.manpower_timetable["Construction_start"]
        return set_data

    def get_construction_end(self):
        set_data = self.manpower_timetable["Construction_end"]
        return set_data

    def get_procurement_start(self):
        set_data = self.manpower_timetable["Procurement_start"]
        return set_data

    def get_procurement_end(self):
        set_data = self.manpower_timetable["Procurement_end"]
        return set_data

    def get_installation_start(self):
        set_data = self.manpower_timetable["Installation_start"]
        return set_data

    def get_installation_end(self):
        set_data = self.manpower_timetable["Installation_end"]
        return set_data

    def get_hiring_start(self):
        set_data = self.manpower_timetable["Hiring_start"]
        return set_data

    def get_hiring_end(self):
        set_data = self.manpower_timetable["Hiring_end"]
        return set_data

    def get_commercial_start(self):
        set_data = self.manpower_timetable["Commercial_start"]
        return set_data

    def get_manpower_01_service(self):
        set_data = self.manpower_timetable["Manpower_01"]["Service"]
        return set_data

    def get_manpower_01_indirect(self):
        set_data = self.manpower_timetable["Manpower_01"]["Indirect"]
        return set_data

    def get_manpower_01_admin(self):
        set_data = self.manpower_timetable["Manpower_01"]["Admin"]
        return set_data

    def get_manpower_02_service(self):
        set_data = self.manpower_timetable["Manpower_02"]["Service"]
        return set_data

    def get_manpower_02_indirect(self):
        set_data = self.manpower_timetable["Manpower_02"]["Indirect"]
        return set_data

    def get_manpower_02_admin(self):
        set_data = self.manpower_timetable["Manpower_02"]["Admin"]
        return set_data

    def get_manpower_03_service(self):
        set_data = self.manpower_timetable["Manpower_03"]["Service"]
        return set_data

    def get_manpower_03_indirect(self):
        set_data = self.manpower_timetable["Manpower_03"]["Indirect"]
        return set_data

    def get_manpower_03_admin(self):
        set_data = self.manpower_timetable["Manpower_03"]["Admin"]
        return set_data

    def get_manufacturing_name(self):
        set_data = self.manufacture_service_flow["Manufacturing_name"]
        return set_data

    def get_manufacturing_pf_name(self):
        set_data = self.manufacture_service_flow["Manufacturing_name"]
        return set_data

    def get_process_flow_diagram(self):
        set_data = self.manufacture_service_flow["Process_flow_diagram"]
        return set_data

    def get_item_description_m1(self):
        set_data = self.raw_materials_machinery_prod["Machinery"]["Item_description"]
        return set_data

    def get_item_quantity_m1(self):
        set_data = self.raw_materials_machinery_prod["Machinery"]["Item_quantity"]
        return set_data

    def get_item_cost_m1(self):
        set_data = self.raw_materials_machinery_prod["Machinery"]["Item_cost"]
        return set_data

    def get_item_source_m1(self):
        set_data = self.raw_materials_machinery_prod["Machinery"]["Item_source"]
        return set_data

    def get_item_origin_m1(self):
        set_data = self.raw_materials_machinery_prod["Machinery"]["Item_origin"]
        return set_data

    def get_item_description_r1(self):
        set_data = self.raw_materials_machinery_prod["Raw_material"]["Item_description"]
        return set_data

    def get_item_source_r1(self):
        set_data = self.raw_materials_machinery_prod["Raw_material"]["Item_source"]
        return set_data

    def get_item_origin_r1(self):
        set_data = self.raw_materials_machinery_prod["Raw_material"]["Item_origin"]
        return set_data

    def get_schedule_shifts(self):
        set_data = self.raw_materials_machinery_prod["Schedule_shifts"]
        return set_data

    def get_hours_shifts(self):
        set_data = self.raw_materials_machinery_prod["Hours_shifts"]
        return set_data

    def get_per_month(self):
        set_data = self.raw_materials_machinery_prod["Per_month"]
        return set_data

    def get_au_owner_area(self):
        set_data = self.area_utilities_waste_disposal["Owner_area"]
        return set_data

    def get_au_location(self):
        set_data = self.area_utilities_waste_disposal["Location"]
        return set_data

    def get_au_region(self):
        set_data = self.area_utilities_waste_disposal["Region"]
        return set_data

    def get_au_province(self):
        set_data = self.area_utilities_waste_disposal["Province"]
        return set_data

    def get_au_city(self):
        set_data = self.area_utilities_waste_disposal["City"]
        return set_data

    def get_au_barangay(self):
        set_data = self.area_utilities_waste_disposal["Barangay"]
        return set_data

    def get_au_street(self):
        set_data = self.area_utilities_waste_disposal["Street"]
        return set_data

    def get_au_unitowner_fname(self):
        set_data = self.area_utilities_waste_disposal["Unitowner_fname"]
        return set_data

    def get_au_unitowner_lname(self):
        set_data = self.area_utilities_waste_disposal["Unitowner_lname"]
        return set_data

    def get_au_lotowner_fname(self):
        set_data = self.area_utilities_waste_disposal["Lotowner_fname"]
        return set_data

    def get_au_lotowner_lname(self):
        set_data = self.area_utilities_waste_disposal["Lotowner_lname"]
        return set_data

    def get_au_lessor_fname(self):
        set_data = self.area_utilities_waste_disposal["Lessor_fname"]
        return set_data

    def get_au_lessor_lname(self):
        set_data = self.area_utilities_waste_disposal["Lessor_lname"]
        return set_data

    def get_au_water_per_year(self):
        set_data = self.area_utilities_waste_disposal["Water_per_year"]
        return set_data

    def get_au_electricity_per_year(self):
        set_data = self.area_utilities_waste_disposal["Electricity_per_year"]
        return set_data

    def get_au_disposal_description(self):
        set_data = self.area_utilities_waste_disposal["Disposal_description"]
        return set_data

    def get_au_disposal_method(self):
        set_data = self.area_utilities_waste_disposal["Disposal_method"]
        return set_data

    def get_au_waste_products(self):
        set_data = self.area_utilities_waste_disposal["Waste_products"]
        return set_data

    def get_au_generated_waste(self):
        set_data = self.area_utilities_waste_disposal["Generated_waste"]
        return set_data

    def get_ma_export_rate(self):
        set_data = self.market_aspect["Export_rate"]
        return set_data

    def get_ma_domestic_rate(self):
        set_data = self.market_aspect["Domestic_rate"]
        return set_data

    def get_ma_country_export(self):
        set_data = self.market_aspect["Country_export"]
        return set_data

    def get_ma_domestic_clients(self):
        set_data = self.market_aspect["Domestic_clients"]
        return set_data

    def get_ma_x_selling_price(self):
        set_data = self.market_aspect["X_selling_price"]
        return set_data

    def get_ma_d_selling_price(self):
        set_data = self.market_aspect["D_selling_price"]
        return set_data

    def get_ma_uom(self):
        set_data = self.market_aspect["Uom"]
        return set_data

    def get_ma_export_vv0(self):
        set_data = self.market_aspect["Export_vv0"]
        return set_data

    def get_ma_export_vv1(self):
        set_data = self.market_aspect["Export_vv1"]
        return set_data

    def get_ma_export_vv2(self):
        set_data = self.market_aspect["Export_vv2"]
        return set_data

    def get_ma_local_vv0(self):
        set_data = self.market_aspect["Local_vv0"]
        return set_data

    def get_ma_local_vv1(self):
        set_data = self.market_aspect["Local_vv1"]
        return set_data

    def get_ma_local_vv2(self):
        set_data = self.market_aspect["Local_vv2"]
        return set_data


class DataObjectBERMSIntialProjectCost:
    def __init__(self, driver, payload):
        self.driver = driver
        self.data_object = payload
        self.construction_renovation = self.data_object["Construction_renovation"]
        self.factory_tools = self.data_object["Factory_tools"]
        self.transportation_cost = self.data_object["Transportation_cost"]
        self.office_equipment = self.data_object["Office_equipment"]
        self.other_assets = self.data_object["Other_assets"]
        self.operating_expenses = self.data_object["Operating_expenses"]
        self.working_capital = self.data_object["Working_capital"]
        self.project_equity = self.data_object["Project_equity"]
        self.project_fund_source_1 = self.data_object["Project_fund_source_1"]
        self.project_add_equity = self.data_object["Project_add_equity"]
        self.project_fund_source_2 = self.data_object["Project_fund_source_2"]
        self.project_advances = self.data_object["Project_advances"]
        self.project_loans = self.data_object["Project_loans"]

class DataObjectBERMSSupportingDocuments:
    def __init__(self, driver, payload):
        self.driver = driver
        self.data_object = payload
        self.affidavit_of_option = self.data_object["Notarized_affidavit_of_option"]
        self.secretary_certificate_anti_graft = self.data_object["Notarized_secretarys_certificate_anti_graft"]
        self.applicants_undertaking = self.data_object["Notarized_applicants_undertaking"]
        self.by_laws_indicating_purpose_etc = self.data_object["By_laws_indicating_purpose_etc"]
        self.articles_of_incorporation = self.data_object["Articles_of_incorporation"]
        self.general_info_sheet = self.data_object["General_information_sheet"]
        self.twenty_years_fin_statement = self.data_object["20_year_projected_fin_statement"]
        self.bir_form_2303 = self.data_object["BIR_form_2303"]
        self.company_profile_of_parent_comp = self.data_object["Company_profile_of_parent_comp"]
        self.resume_of_principal_officers = self.data_object["Resume_of_principal_officers"]
        self.sec_certificate = self.data_object["SEC_certificate"]
        self.site_development_plan_and_vicinity_map = self.data_object["Site_development_plan_and_vicinity_map"]
        self.affidavit_of_option_1 = self.data_object["Notarized_affidavit_of_option_1"]
        self.proof_of_land_ownership_or_any_document = self.data_object["Proof_of_land_ownership_or_any_document"]
        self.list_of_goods_handled = self.data_object["List_of_goods_handled"]
        self.certification_from_the_national = self.data_object["Certification_from_the_national"]
        self.endorsement_from_doe = self.data_object["Endorsement_from_doe"]
        self.endorsement_from_local_water_district = self.data_object["Endorsement_from_local_water_district"]
        self.site_development_plan_and_vicinity_map_1 = self.data_object["Site_development_plan_and_vicinity_map_1"]
        self.operation_plan_including_capacity_plan = self.data_object["Operation_plan_including_capacity_plan"]
        self.drawing_layout_support_structure_arrangement = self.data_object["Drawing_layout_support_structure_arrangement"]
        self.notarized_affidavit_of_option_2 = self.data_object["Notarized_affidavit_of_option_2"]
        self.certification_from_national_water_resources_board = self.data_object["Certification_from_national_water_resources_board"]

