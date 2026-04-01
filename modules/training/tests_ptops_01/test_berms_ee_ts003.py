import pytest, re
from modules.testcases.ecp.data_processing import DataProcessingClass
from modules.frame_work.utility.utility_package import UtilityPackage
from modules.testcases.ptops.page_objects.login import LoginPage
from modules.testcases.ptops.page_objects.berms_page import BermsPageObjects
from modules.testcases.ptops.data_objects.ptops_data_sets import DataSetCompilationBERMS
from modules.testcases.ptops.data_objects.ptops_data_objects import DataObjectBERMS

@pytest.mark.usefixtures("setup")
# def test_ecp(playwright: Playwright) -> None:
class TestSuiteBERMS001():
    # @pytest.fixture(autouse=True)
    @pytest.fixture(scope="function", autouse=True)
    def before_each_after_each(self):
        print("before the test runs")
        # Go to the starting url before each test.
        global data_set, application_counter, pg, data_obj, berms
        pg = LoginPage(self.driver)
        berms = BermsPageObjects(self.driver)
        application_counter = UtilityPackage().padd_zeroes_2(1)
        data_set = DataSetCompilationBERMS().ds_test_berms_ts003
        data_obj = DataObjectBERMS(self.driver, data_set)
        yield
        print("after the test runs")
        # self.driver.wait_for_timeout(10000)

    def initiate_test_data(self):
        return DataProcessingClass(self.driver)

    def test_ptops_login(self) -> None:
        pg.get_ptops_url(data_obj.link_reference)
        pg.get_user_name(data_obj.username_reference)
        pg.get_pass_word(data_obj.password_reference)
        pg.proceed_ptops_login()
        pg.verify_link_berms()

    def test_create_new_berms(self) -> None:
        berms.menu_list.click_lnk_apps_accre()
        berms.menu_list.verify_new_berms_button()
        berms.menu_list.click_btn_new_berms_apps()
        berms.menu_list.verify_undertaking_link()
        berms.menu_list.check_chbx_agree_ut()
        berms.menu_list.verify_btn_proceed_e()
        berms.menu_list.click_btn_proceed_c()

    def test_create_new_berms_application_1(self) -> None:
        berms.application.select_opt_app_type(data_obj.app_det_type)
        berms.application.select_rbtn_type_ezone(data_obj.app_loc_type)
        berms.application.select_opt_psic_classification(data_obj.app_psic_class)

    def test_create_new_berms_application_2(self) -> None:
        berms.application.select_opt_psic_division(data_obj.app_psic_division)
        berms.application.select_opt_psic_div_group(data_obj.app_psic_div_group)
        berms.application.select_opt_psic_div_class(data_obj.app_psic_div_class)
        berms.application.select_opt_psic_div_subclass(data_obj.app_psic_div_subclass)
        berms.application.click_btn_proceed_app()

    def test_create_new_berms_company_personal_info(self) -> None:
        berms.company_info.input_txt_company_name(f"{data_obj.ci_company_name}{application_counter}")
        berms.company_info.input_txt_nature_business(f"{data_obj.ci_nature_business}{application_counter}")
        berms.company_info.input_txt_company_profile(f"{data_obj.ci_company_profile}{application_counter}")
        berms.company_info.click_btn_proceed()

    def test_create_new_berms_company_proposed_project_1(self) -> None:
        berms.company_proposed_project.click_btn_proposed_project()
        berms.company_proposed_project.input_txt_proposed_project(f"{data_obj.propose_project}{application_counter}")
        berms.company_proposed_project.click_btn_proposed_project_add()

    def test_create_new_berms_company_proposed_project_2(self) -> None:
        berms.company_proposed_project.input_txt_description(f"{data_obj.proposed_project_desc}{application_counter}")
        berms.company_proposed_project.input_txt_desc_uses(f"{data_obj.project_desc_uses}{application_counter}")
        berms.company_proposed_project.file_add_permit(data_obj.proposed_project_permit)
        berms.company_proposed_project.click_btn_save_next()

    def test_create_new_berms_existing_business_reg_1(self) -> None:

        berms.existing_bus_reg.pick_dp_registration_date(data_obj.registration_date)
        berms.existing_bus_reg.input_txt_registration_no(f"{data_obj.registration_no}{application_counter}")
        berms.existing_bus_reg.input_txt_sec_primary_purpose(f"{data_obj.sec_primary_purpose}{application_counter}")

    def test_create_new_berms_existing_business_reg_2(self) -> None:
        berms.existing_bus_reg.input_txt_authorized_amount(data_obj.authorized_amount)
        berms.existing_bus_reg.input_txt_subscribed_amount(data_obj.subscribed_amount)
        berms.existing_bus_reg.input_txt_paid_up_amount(data_obj.reg_paid_up_amount)
        berms.existing_bus_reg.click_btn_save_next()

    def test_create_new_berms_stockholder_reg_1(self) -> None:
        berms.stock_holder_principal_officer.tick_rb_stockholder_type(data_obj.stockholder_type)
        berms.stock_holder_principal_officer.click_btn_stockholder_add()
        berms.stock_holder_principal_officer.input_txt_stockholder_company_name(data_obj.stockholder_name)
        berms.stock_holder_principal_officer.input_txt_stockholder_company_nationality(data_obj.stockholder_nationality)
        berms.stock_holder_principal_officer.input_txt_stockholder_no_shares(data_obj.stockholder_no_shares)
        berms.stock_holder_principal_officer.input_txt_amount_subscribed(data_obj.amount_subscribed)
        berms.stock_holder_principal_officer.input_txt_amount_paid_up(data_obj.amount_paid_up)
        berms.stock_holder_principal_officer.click_btn_stockholder_add_proceed()


    def test_create_new_berms_stockholder_reg_2(self) -> None:
        berms.stock_holder_principal_officer.click_rb_proposed_stockholder_item()
        berms.stock_holder_principal_officer.click_rb_proposed_stockholder_item_1()
        berms.stock_holder_principal_officer.click_btn_principal_officer_add()
        berms.stock_holder_principal_officer.select_opt_officer_salutation(data_obj.officer_salutation)
        berms.stock_holder_principal_officer.input_txt_officer_fname(data_obj.officer_fname)
        berms.stock_holder_principal_officer.input_txt_officer_mname(data_obj.officer_mname)
        berms.stock_holder_principal_officer.input_txt_officer_lname(data_obj.officer_lname)
        berms.stock_holder_principal_officer.input_txt_officer_position(data_obj.officer_position)
        berms.stock_holder_principal_officer.click_btn_officer_add_proceed()
        berms.stock_holder_principal_officer.click_btn_save_next()

    def test_create_new_berms_manpower_timetable_1(self) -> None:
        berms.manpower_timetable.pick_dp_bld_construction_fr(data_obj.construction_start)
        berms.manpower_timetable.pick_dp_bld_construction_to(data_obj.construction_end)
        berms.manpower_timetable.pick_dp_bld_procurement_fr(data_obj.procurement_start)
        berms.manpower_timetable.pick_dp_bld_procurement_to(data_obj.procurement_end)

    def test_create_new_berms_manpower_timetable_2(self) -> None:
        berms.manpower_timetable.pick_dp_installation_fr(data_obj.installation_start)
        berms.manpower_timetable.pick_dp_installation_to(data_obj.installation_end)
        berms.manpower_timetable.pick_dp_hiring_fr(data_obj.hiring_start)
        berms.manpower_timetable.pick_dp_hiring_to(data_obj.hiring_end)
        berms.manpower_timetable.pick_dp_commercial_start(data_obj.commercial_start)

    def test_create_new_berms_manpower_timetable_3(self) -> None:
        berms.manpower_timetable.input_txt_manpower_01_service(data_obj.manpower_01_service)
        berms.manpower_timetable.input_txt_manpower_01_indirect(data_obj.manpower_01_indirect)
        berms.manpower_timetable.input_txt_manpower_01_admin(data_obj.manpower_01_admin)

    def test_create_new_berms_manpower_timetable_4(self) -> None:

        berms.manpower_timetable.input_txt_manpower_02_service(data_obj.manpower_02_service)
        berms.manpower_timetable.input_txt_manpower_02_indirect(data_obj.manpower_02_indirect)
        berms.manpower_timetable.input_txt_manpower_02_admin(data_obj.manpower_02_admin)

    def test_create_new_berms_manpower_timetable_5(self) -> None:
        berms.manpower_timetable.input_txt_manpower_03_service(data_obj.manpower_03_service)
        berms.manpower_timetable.input_txt_manpower_03_indirect(data_obj.manpower_03_indirect)
        berms.manpower_timetable.input_txt_manpower_03_admin(data_obj.manpower_03_admin)
        berms.manpower_timetable.click_btn_save_proceed()

    def test_create_new_berms_manu_servi_flow(self) -> None:

        berms.manufacturing_service_flow.input_txt_desrcibe_manufacturing_name(data_obj.manufacturing_pf_name)
        berms.manufacturing_service_flow.file_add_diagram_process_flow(data_obj.process_flow_diagram)
        berms.manufacturing_service_flow.click_btn_save_proceed()

    def test_create_new_berms_m_rp_p_schedule_add_machinery_equipment(self) -> None:

        berms.machinery_raw_mat_prod_schedule.click_btn_machinery_equipment_add()
        berms.machinery_raw_mat_prod_schedule.input_txt_machinery_equipment_description(data_obj.item_description_m1)
        berms.machinery_raw_mat_prod_schedule.input_txt_machinery_equipment_quantity(data_obj.item_quantity_m1)
        berms.machinery_raw_mat_prod_schedule.input_txt_machinery_equipment_cost(data_obj.item_cost_m1)
        berms.machinery_raw_mat_prod_schedule.select_opt_machinery_equipment_source(data_obj.item_source_m1)
        berms.machinery_raw_mat_prod_schedule.select_opt_machinery_equipment_origin(data_obj.item_origin_m1)
        berms.machinery_raw_mat_prod_schedule.click_btn_save_new()
        berms.machinery_raw_mat_prod_schedule.click_btn_cancel()



    def test_create_new_berms_m_rp_p_schedule_add_materials(self) -> None:
        berms.machinery_raw_mat_prod_schedule.click_btn_raw_mats_fin_products_add()
        berms.machinery_raw_mat_prod_schedule.input_txt_raw_mats_fin_products_description(data_obj.item_description_r1)
        berms.machinery_raw_mat_prod_schedule.select_opt_raw_mats_fin_products_source(data_obj.item_source_r1)
        berms.machinery_raw_mat_prod_schedule.select_opt_raw_mats_fin_products_origin(data_obj.item_origin_r1)
        berms.machinery_raw_mat_prod_schedule.click_btn_save_new()
        berms.machinery_raw_mat_prod_schedule.click_btn_cancel()

        # page = self.driver
        # page.wait_for_timeout(120000)

    def test_create_new_berms_m_rp_p_schedule_add_schedule(self) -> None:

        berms.machinery_raw_mat_prod_schedule.input_txt_schedule_shifts(data_obj.schedule_shifts)
        berms.machinery_raw_mat_prod_schedule.input_txt_schedule_hours_per_shift(data_obj.hours_shifts)
        berms.machinery_raw_mat_prod_schedule.input_txt_schedule_days_per_month(data_obj.per_month)
        berms.machinery_raw_mat_prod_schedule.click_btn_save_proceed()


    def test_create_new_berms_areas_utilities_w_disposal_1(self) -> None:
        berms.areas_utilities_waste_disposal.input_txt_owner_area(data_obj.au_owner_area)
        berms.areas_utilities_waste_disposal.select_opt_location(data_obj.au_location)
        berms.areas_utilities_waste_disposal.select_opt_region(data_obj.au_region)
        berms.areas_utilities_waste_disposal.select_opt_province(data_obj.au_province)
        berms.areas_utilities_waste_disposal.select_opt_city(data_obj.au_city)
        berms.areas_utilities_waste_disposal.select_opt_barangay(data_obj.au_barangay)
        berms.areas_utilities_waste_disposal.input_txt_street(data_obj.au_street)

    def test_create_new_berms_areas_utilities_w_disposal_2(self) -> None:
        berms.areas_utilities_waste_disposal.input_txt_unitowner_fname(data_obj.au_unitowner_fname)
        berms.areas_utilities_waste_disposal.input_txt_unitowner_lname(data_obj.au_unitowner_lname)
        berms.areas_utilities_waste_disposal.input_txt_lotowner_fname(data_obj.au_lotowner_fname)
        berms.areas_utilities_waste_disposal.input_txt_lotowner_lname(data_obj.au_lotowner_lname)
        berms.areas_utilities_waste_disposal.input_txt_lessor_fname(data_obj.au_lessor_fname)
        berms.areas_utilities_waste_disposal.input_txt_lessor_lname(data_obj.au_lessor_lname)


    def test_create_new_berms_areas_utilities_w_disposal_3(self) -> None:

        berms.areas_utilities_waste_disposal.input_txt_water_yr_req(data_obj.au_water_per_year)
        berms.areas_utilities_waste_disposal.input_txt_electric_yr_req(data_obj.au_electricity_per_year)
        berms.areas_utilities_waste_disposal.input_txt_waste_d_desc(data_obj.au_disposal_description)
        berms.areas_utilities_waste_disposal.input_txt_waste_d_method(data_obj.au_disposal_method)
        berms.areas_utilities_waste_disposal.file_add_waste_products(data_obj.au_waste_products)
        berms.areas_utilities_waste_disposal.file_add_generated_waste(data_obj.au_generated_waste)
        berms.areas_utilities_waste_disposal.click_btn_save_proceed()


    def test_create_new_berms_market_aspec_1(self) -> None:

        berms.market_aspect.select_opt_export_rate(data_obj.ma_export_rate)
        berms.market_aspect.select_opt_domestic_rate(data_obj.ma_domestic_rate)
        berms.market_aspect.select_opt_country_export(data_obj.ma_country_export)
        berms.market_aspect.input_txt_country_domestic_clients(data_obj.ma_domestic_clients)
        berms.market_aspect.input_txt_country_x_selling_price(data_obj.ma_x_selling_price)
        berms.market_aspect.input_txt_country_d_selling_price(data_obj.ma_d_selling_price)
        berms.market_aspect.select_opt_country_uom(data_obj.ma_uom)

    def test_create_new_berms_market_aspec_2(self) -> None:

        berms.market_aspect.input_txt_country_add_e_marketavv0(data_obj.ma_export_vv0)
        berms.market_aspect.input_txt_country_add_e_marketavv1(data_obj.ma_export_vv1)
        berms.market_aspect.input_txt_country_add_e_marketavv2(data_obj.ma_export_vv2)
        berms.market_aspect.input_txt_country_add_i_marketavv0(data_obj.ma_local_vv0)
        berms.market_aspect.input_txt_country_add_i_marketavv1(data_obj.ma_local_vv1)
        berms.market_aspect.input_txt_country_add_i_marketavv2(data_obj.ma_local_vv2)
        berms.market_aspect.click_btn_save_proceed()


    def test_create_new_berms_initial_project_cost_1(self) -> None:

        berms.initial_project_cost.input_txt_construction_renovation(data_obj.initial_project_cost.construction_renovation)
        berms.initial_project_cost.input_txt_factory_tools(data_obj.initial_project_cost.factory_tools)
        berms.initial_project_cost.input_txt_transportation_cost(data_obj.initial_project_cost.transportation_cost)
        berms.initial_project_cost.input_txt_office_equipment(data_obj.initial_project_cost.office_equipment)
        berms.initial_project_cost.input_txt_other_assets(data_obj.initial_project_cost.other_assets)
        berms.initial_project_cost.input_txt_operating_expenses(data_obj.initial_project_cost.operating_expenses)
        berms.initial_project_cost.input_txt_working_capital(data_obj.initial_project_cost.working_capital)

    def test_create_new_berms_initial_project_cost_2(self) -> None:

        berms.initial_project_cost.input_txt_project_equity(data_obj.initial_project_cost.project_equity)
        berms.initial_project_cost.select_opt_project_fund_source_1(data_obj.initial_project_cost.project_fund_source_1)
        berms.initial_project_cost.input_txt_project_add_equity(data_obj.initial_project_cost.project_add_equity)
        berms.initial_project_cost.select_opt_project_fund_source_2(data_obj.initial_project_cost.project_fund_source_2)
        berms.initial_project_cost.input_txt_project_advances(data_obj.initial_project_cost.project_advances)
        berms.initial_project_cost.input_txt_project_loans(data_obj.initial_project_cost.project_loans)
        berms.initial_project_cost.click_btn_save_proceed()


    def test_create_new_berms_supporting_documents_1(self) -> None:
        berms.supporting_documents.file_add_site_development_plan_and_vicinity_map(data_obj.supporting_documents.site_development_plan_and_vicinity_map)
        berms.supporting_documents.file_add_notarized_affidavit_of_option_1(data_obj.supporting_documents.affidavit_of_option_1)
        berms.supporting_documents.file_add_proof_of_land_ownership_or_any_document(data_obj.supporting_documents.proof_of_land_ownership_or_any_document)

    def test_create_new_berms_supporting_documents_2(self) -> None:
        berms.supporting_documents.file_add_notarized_secretarys_certificate_anti_graft(data_obj.supporting_documents.secretary_certificate_anti_graft)
        berms.supporting_documents.file_add_notarized_applicants_undertaking(data_obj.supporting_documents.applicants_undertaking)
        berms.supporting_documents.file_add_by_laws_indicating_purpose_etc(data_obj.supporting_documents.by_laws_indicating_purpose_etc)

    def test_create_new_berms_supporting_documents_3(self) -> None:

        berms.supporting_documents.file_add_articles_of_incorporation(data_obj.supporting_documents.articles_of_incorporation)
        berms.supporting_documents.file_add_general_information_sheet(data_obj.supporting_documents.general_info_sheet)
        berms.supporting_documents.file_add_20_year_projected_fin_statement(data_obj.supporting_documents.twenty_years_fin_statement)

    def test_create_new_berms_supporting_documents_4(self) -> None:

        berms.supporting_documents.file_add_bir_form_2303(data_obj.supporting_documents.bir_form_2303)
        berms.supporting_documents.file_add_company_profile_of_parent_comp(data_obj.supporting_documents.company_profile_of_parent_comp)
        berms.supporting_documents.file_add_resume_of_principal_officers(data_obj.supporting_documents.resume_of_principal_officers)

    def test_create_new_berms_supporting_documents_5(self) -> None:

        berms.supporting_documents.file_add_sec_certificate(data_obj.supporting_documents.sec_certificate)
        berms.supporting_documents.click_btn_save_proceed()

    def test_create_new_berms_submit(self) -> None:

        berms.application_submission.click_btn_application_submit()
        berms.application_submission.click_btn_submission_proceed()
        berms.application_submission.verify_txt_application_number()
        berms.application_submission.file_save_application_number()
        berms.application_submission.click_btn_submission_proceed_confirm()

