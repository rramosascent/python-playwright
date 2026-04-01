from playwright.sync_api import Page, Locator, expect
from pathlib import Path
import os
import pytest
import csv
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.custom_logger import log

class BermsStatusChangePage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_fw = FrameWorkPWDriver(self.page)
        # for screening
        self.btn_proceed_to_screen_application = page.locator("(//button[@type='button'])[17]")
        self.opt_status = page.locator("//span[@id='select2-applicationStatus-container']")
        self.txt_remarks = page.locator("//textarea[@id='applicationRemarks']")
        self.btn_submit = page.locator("(//button[@id='btnSubmitApplication'])[2]")
        self.btn_confirm_proceed = page.locator("(//button[normalize-space()='Yes, proceed!'])[1]")
        self.btn_ok = page.locator("(//button[normalize-space()='OK'])[1]")
        self.lbl_application_number = page.locator("(//span[normalize-space()='AN-2519016ME'])[1]")

        # for af payment
        self.btn_proceed_to_af_payment = page.locator("(//button[@class='btn btn-outline-primary btn-next-parent me-1'])[1]")
        self.rd_btn_otc_payment = page.locator("(//div[@class='form-check'])[10]")
        self.btn_testing_payment = page.locator("(//button[contains(text(),'Click this button to create a payment for testing ')])[1]")
        self.btn_ok_success_test_payment = page.locator("(//button[normalize-space()='OK'])[1]")
        self.btn_proceed_to_payment = page.locator("(//button[@id='btnConfirmPayment'])[1]")
        self.btn_confirm_proceed_payment = page.locator("(//button[@class='swal2-confirm btn btn-primary btn-lg skip-submit-loading skip-text-change gap-2'])[1]")
        self.btn_ok_success_payment = page.locator("(//button[normalize-space()='OK'])[1]")

        # for eso assignment
        self.btn_proceed_to_eso_assignment = page.locator("(//button[@type='button'])[17]")
        self.opt_eso_assign_to = page.locator("(//span[@id='select2-esoId-container'])[1]")
        self.txt_eso_remarks = page.locator("(//textarea[@id='assignationRemarks'])[1]")
        self.btn_eso_submit = page.locator("(//button[@id='btnSubmitApplication'])[1]")
        self.btn_eso_confirm_proceed = page.locator("(//button[@class='swal2-confirm btn btn-primary btn-lg skip-submit-loading skip-text-change gap-2'])[1]")
        self.btn_eso_ok = page.locator("(//button[normalize-space()='OK'])[1]")

        # for evaluation report approval
        self.btn_proceed_to_evaluation_status = page.locator("(//button[@type='button'])[17]")
        self.opt_evaluation_approval_status = page.locator("(//select[@id='applicationStatus'])[1]")
        self.txt_evaluation_approval_remarks = page.locator("(//textarea[@id='applicationRemarks'])[1]")
        self.btn_evaluation_approval_submit = page.locator("(//button[normalize-space()='Submit'])[1]")
        self.btn_evaluation_approval_confirm_proceed = page.locator("(//button[@class='swal2-confirm btn btn-primary btn-lg skip-submit-loading skip-text-change gap-2'])[1]")
        self.btn_evaluation_approval_ok = page.locator("(//button[normalize-space()='OK'])[1]")

        # for evaluation report
        self.btn_proceed_to_evaluation_report = page.locator("(//button[@type='button'])[18]")
        self.txt_p_project_activity_listed_SIPP = page.locator("//div[@class='col-8']//div[@class='note-editing-area']//p")
        self.txt_p_recommended_basis = page.locator("(//div[@role='textbox'])[2]")
        self.opt_tier_classification = page.locator("(//span[@id='select2-tier-container'])[1]")
        self.txt_p_tier_classification = page.locator("(//div[@role='textbox'])[3]")
        self.txt_p_product_description = page.locator("(//div[@role='textbox'])[4]")
        self.opt_volume_export = page.locator("(//span[@id='select2-export_volume_symbol-container'])[1]")
        self.opt_value_export = page.locator("(//span[@id='select2-export_value_symbol-container'])[1]")
        self.opt_volume_import = page.locator("(//span[@id='select2-import_volume_symbol-container'])[1]")
        self.opt_value_import = page.locator("(//span[@id='select2-import_value_symbol-container'])[1]")
        self.opt_direct_personnel_years = page.locator("(//span[@id='select2-direct_symbol-container'])[1]")
        self.opt_indirect_personnel_years = page.locator("(//span[@id='select2-indirect_symbol-container'])[1]")
        self.opt_admin_personnel_years = page.locator("(//span[@id='select2-admin_symbol-container'])[1]")
        self.opt_fourthplus_total_years = page.locator("(//span[@id='select2-fourthplus_total_symbol-container'])[1]")
        self.opt_direct_personnel_average = page.locator("(//span[@id='select2-avg_direct_symbol-container'])[1]")
        self.opt_indirect_personnel_average = page.locator("(//span[@id='select2-avg_indirect_symbol-container'])[1]")
        self.opt_admin_personnel_average = page.locator("(//span[@id='select2-avg_admin_symbol-container'])[1]")
        self.opt_fourthplus_total_average = page.locator("(//span[@id='select2-avg_total_symbol-container'])[1]")
        self.btn_select_tier = page.locator("(//td[@class='ncr tier1'])[1]")
        self.txt_p_additional_information = page.locator("(//div[@role='textbox'])[5]")
        self.txt_p_company_profile = page.locator("(//div[@role='textbox'])[8]")
        self.txt_p_for_board_consideration = page.locator("(//div[@role='textbox'])[9]")
        self.btn_submit_evaluation_report = page.locator("(//button[normalize-space()='Submit'])[1]")
        self.btn_confirm_proceed_evaluation_report = page.locator("(//button[normalize-space()='Yes, proceed!'])[1]")
        self.btn_evaluation_report_ok = page.locator("(//button[normalize-space()='OK'])[1]")

        # endorsement of DC
        self.btn_proceed_to_endorsement_dc_status = page.locator("(//button[@type='button'])[19]")
        self.opt_endorsement_dc_status = page.locator("(//select[@id='applicationStatus'])[1]")
        self.txt_endorsement_dc_remarks = page.locator("(//textarea[@id='applicationRemarks'])[1]")
        self.btn_endorsement_dc_submit = page.locator("(//button[normalize-space()='Submit'])[1]")
        self.btn_endorsement_dc_confirm_proceed = page.locator("(//button[@class='swal2-confirm btn btn-primary btn-lg skip-submit-loading skip-text-change gap-2'])[1]")
        self.btn_endorsement_dc_ok = page.locator("(//button[normalize-space()='OK'])[1]")

        # endorsement of DM
        self.btn_proceed_to_endorsement_dm_status = page.locator("(//button[@type='button'])[19]")
        self.opt_endorsement_dm_status = page.locator("(//span[@id='select2-applicationStatus-container'])[1]")
        self.txt_endorsement_dm_remarks = page.locator("(//textarea[@id='applicationRemarks'])[1]")
        self.btn_endorsement_dm_submit = page.locator("(//button[@id='btnSubmitApplication'])[2]")
        self.btn_endorsement_dm_confirm_proceed = page.locator("(//button[normalize-space()='Yes, proceed!'])[1]")
        self.btn_endorsement_dm_ok = page.locator("(//button[normalize-space()='OK'])[1]")

        # endorsement of GM
        self.btn_proceed_to_endorsement_gm_status = page.locator("(//button[@type='button'])[19]")
        self.opt_endorsement_gm_status = page.locator("(//span[@id='select2-applicationStatus-container'])[1]")
        self.txt_endorsement_gm_remarks = page.locator("(//textarea[@id='applicationRemarks'])[1]")
        self.upload_gm_signature_document = page.locator("(//div[@id='eval-eSignatureDropzone'])[1]")
        self.btn_endorsement_gm_submit = page.locator("(//button[@id='btnSubmitApplication'])[2]")
        self.btn_endorsement_gm_confirm_proceed = page.locator("(//button[normalize-space()='Yes, proceed!'])[1]")
        self.btn_endorsement_gm_ok = page.locator("(//button[normalize-space()='OK'])[1]")

        # endorsement of DDG
        self.btn_proceed_to_endorsement_ddg_status = page.locator("(//button[@type='button'])[19]")
        self.opt_endorsement_ddg_status = page.locator("(//span[@id='select2-applicationStatus-container'])[1]")
        self.txt_endorsement_ddg_remarks = page.locator("(//textarea[@id='applicationRemarks'])[1]")
        self.upload_ddg_signature_document = page.locator("(//div[@id='eval-eSignatureDropzone'])[1]")
        self.btn_endorsement_ddg_submit = page.locator("(//button[@id='btnSubmitApplication'])[2]")
        self.btn_endorsement_ddg_confirm_proceed = page.locator("(//button[normalize-space()='Yes, proceed!'])[1]")
        self.btn_endorsement_ddg_ok = page.locator("(//button[normalize-space()='OK'])[1]")

        # board consideration
        self.btn_proceed_to_board_consideration = page.locator("(//button[@type='button'])[19]")
        self.opt_board_consideration_status = page.locator("(//span[@id='select2-applicationStatus-container'])[1]")
        self.txt_board_consideration_remarks = page.locator("(//textarea[@id='applicationRemarks'])[1]")
        self.upload_board_consideration_document = page.locator("(//div[@id='eval-eSignatureDropzone'])[1]")
        self.btn_board_consideration_submit = page.locator("(//button[@id='btnSubmitApplication'])[2]")
        self.btn_board_consideration_confirm_proceed = page.locator("(//button[normalize-space()='Yes, proceed!'])[1]")
        self.btn_board_consideration_ok = page.locator("(//button[normalize-space()='OK'])[1]")

        # pb approval
        self.btn_proceed_to_pb_approval = page.locator("(//button[@type='button'])[19]")
        self.opt_pb_approval_status = page.locator("(//span[@id='select2-applicationStatus-container'])[1]")
        self.txt_pb_approval_remarks = page.locator("(//textarea[@id='applicationRemarks'])[1]")
        self.upload_pb_approval_signature_document = page.locator("(//div[@id='eval-eSignatureDropzone'])[1]")
        self.btn_pb_approval_submit = page.locator("(//button[@id='btnSubmitApplication'])[2]")
        self.btn_pb_approval_confirm_proceed = page.locator("(//button[normalize-space()='Yes, proceed!'])[1]")
        self.btn_pb_approval_ok = page.locator("(//button[normalize-space()='OK'])[1]")

        # issuance of board consideration
        self.btn_proceed_to_issuance_of_board_consideration = page.locator("(//button[@type='button'])[19]")
        self.dt_picker_board_meeting = page.locator("(//input[@id='brMeetingDate'])[1]")
        self.dt_picker_date = page.locator("(//span[@aria-label='March 19, 2026'][normalize-space()='19'])[1]")
        self.txt_resolution_number = page.locator("(//input[@id='brResolutionNumber'])[1]")
        self.txt_initials = page.locator("(//span[@id='brAddtnlFour'])[2]")
        self.btn_issuance_of_board_consideration_submit = page.locator("(//button[normalize-space()='Submit'])[1]")
        self.btn_issuance_of_board_consideration_confirm_proceed = page.locator("(//button[@class='swal2-confirm btn btn-primary btn-lg skip-submit-loading skip-text-change gap-2'])[1]")
        self.btn_issuance_of_board_consideration_ok = page.locator("(//button[normalize-space()='OK'])[1]")

        # registration payment
        self.btn_proceed_to_rf_payment = page.locator("(//button[@class='btn btn-outline-primary btn-next-parent me-1'])[1]")
        self.chkbox_otc__rf_payment = page.locator("(//input[@id='paymentOption3'])[1]")
        self.btn_testing_rf_payment = page.locator("(//button[contains(text(),'Click this button to create a payment for testing ')])[1]")
        self.btn_ok_success_test_rf_payment = page.locator("(//button[normalize-space()='OK'])[1]")
        self.btn_proceed_to_rf_payment_submit = page.locator("(//button[@id='btnConfirmPayment'])[1]")
        self.btn_confirm_proceed_rf_payment = page.locator("(//button[@class='swal2-confirm btn btn-primary btn-lg skip-submit-loading skip-text-change gap-2'])[1]")
        self.btn_ok_success_rf_payment = page.locator("(//button[normalize-space()='OK'])[1]")

        # ra uploading
        self.btn_proceed_to_ra_uploading = page.locator("(//button[@type='button'])[20]")
        self.upload_ra_document = page.locator("(//div[@class='dropzone dz-clickable uploadSignedDZ'])[1]")
        self.btn_ra_uploading_submit = page.locator("(//button[normalize-space()='Submit'])[1]")
        self.btn_ok_success_ra_uploading = page.locator("(//button[normalize-space()='OK'])[1]")

        # preparation of cor
        self.btn_proceed_to_preparation_cor = page.locator("(//button[@type='button'])[21]")
        self.btn_cor_submit = page.locator("(//button[normalize-space()='Submit'])[1]")
        self.btn_ok_success_preparation = page.locator("(//button[normalize-space()='OK'])[1]")

    # To change the application number in flexible way
    def get_application_number_locator(self, application_number: str):
        return self.page.locator(f"//a[normalize-space()='{application_number}']")

    def select_application_number(self, application_number: str):
        # search then click
        log.info("Searching.....")
        log.info("Selecting the application from dashboard data table")
        self.page.locator("(//input[@aria-controls='dt_stakeholders'])[1]").fill(application_number)
        self.page.wait_for_timeout(2000)
        # locator = self.get_application_number_locator(application_number)
        # locator.click()

    def change_status_to_prescreened(self):
        log.info("-----Screening the application-----")
        log.info("Clicking Proceed to Screen Application")
        self.btn_proceed_to_screen_application.click()
        log.info("Selecting Status of the application")
        self.playwright_fw.dropdown_select_option(self.opt_status, "Pre-Screened")
        log.info("Filling up Remarks")
        self.playwright_fw.text_fill(self.txt_remarks, "test 101")
        log.info("Clicking Submit button")
        self.btn_submit.click()
        log.info("Clicking Yes, proceed! button")
        self.btn_confirm_proceed.click()
        self.page.wait_for_load_state("networkidle")
        log.info("Clicking OK button")
        self.btn_ok.click()

    def do_af_payment(self):
        log.info("-----AF Payment for the application-----")
        log.info("Clicking Proceed to Payment Application")
        self.btn_proceed_to_af_payment.click()
        self.page.wait_for_load_state("networkidle")
        log.info("Selecting test otc payment")
        self.rd_btn_otc_payment.click()
        self.page.wait_for_load_state("networkidle")
        log.info("Clicking test paymet button")
        self.btn_testing_payment.click()
        log.info("Clicking ok button")
        self.btn_ok_success_test_payment.click()
        log.info("Clicking proceed to payment button")
        self.btn_proceed_to_payment.click()
        log.info("Clicking confirm payment button")
        self.btn_confirm_proceed_payment.click()
        log.info("Clicking OK button")
        self.btn_ok_success_payment.click()

    def do_eso_assignment(self):
        log.info("-----ESO Assigning application-----")
        log.info("Clicking Proceed to ESO Assignment Application")
        self.btn_proceed_to_eso_assignment.click()
        log.info("Selecting assign to")
        self.playwright_fw.dropdown_select_option(self.opt_eso_assign_to, "ERD_EVALUATOR, ERD_EVALUATOR ERD_EVALUATOR")
        log.info("Filling up remarks")
        self.playwright_fw.text_fill(self.txt_eso_remarks,"test 101")
        log.info("Clicking Submit button")
        self.btn_eso_submit.click()
        log.info("Clicking Proceed button")
        self.btn_eso_confirm_proceed.click()
        self.page.wait_for_load_state("networkidle")
        log.info("Clicking OK button")
        self.btn_eso_ok.click()

    def do_evaluation_report_approval(self):
        log.info("-----Evaluation tagging application-----")
        log.info("Clicking Proceed to Evaluation Status Application")
        self.btn_proceed_to_evaluation_status.click()
        self.page.wait_for_timeout(3000)
        # page.wait_for_load_state("networkidle")
        log.info("Selecting Status")
        self.combo_box_select_option(self.opt_evaluation_approval_status, "approved")
        log.info("Filling up remarks")
        self.playwright_fw.text_fill(self.txt_evaluation_approval_remarks, "test 101")
        self.txt_evaluation_approval_remarks.fill("test 101")
        log.info("Clicking Submit button")
        self.btn_evaluation_approval_submit.click()
        log.info("Clicking Proceed button")
        self.btn_evaluation_approval_confirm_proceed.click()
        self.page.wait_for_load_state("networkidle")
        log.info("Clicking OK button")
        self.btn_evaluation_approval_ok.click()

    def do_evaluation_report(self):
        log.info("-----Evaluation Report application-----")
        log.info("Clicking Proceed to Evaluation Report Application")
        self.btn_proceed_to_evaluation_report.click()
        log.info("Zooming out the application")
        self.page.evaluate("document.body.style.zoom = '0.75'")
        self.page.mouse.wheel(0, 200)
        log.info("Filling up Project Activity listed in the SIPP")
        self.playwright_fw.text_fill(self.txt_p_project_activity_listed_SIPP, "test 101")
        log.info("Filling up Recommended Incentives and Basis")
        self.playwright_fw.text_fill(self.txt_p_recommended_basis, "test 101")
        # self.zoom_in_out() # 75% zoom
        log.info("Selecting Tier Classification Under the CREATE Act")
        self.page.get_by_role("textbox", name="Select Tier").click()
        self.page.get_by_role("option", name="TIER I", exact=True).click()
        log.info("Filling up Tier Classification Under the CREATE Act")
        self.playwright_fw.text_fill(self.txt_p_tier_classification, "test 101")
        log.info("Filling up Product Description")
        self.playwright_fw.text_fill(self.txt_p_product_description, "test 101")
        self.page.wait_for_load_state("networkidle")
        log.info("Selecting Projected Volume (Export)")
        self.playwright_fw.dropdown_select_option(self.opt_volume_export, ">")
        log.info("Selecting Projected Value of Sales Revenue (Export)")
        self.dropdown_select_option(self.opt_value_export, ">")
        log.info("Selecting Projected Volume (Local)")
        self.playwright_fw.dropdown_select_option(self.opt_volume_import, ">")
        log.info("Selecting Projected Value of Sales Revenue (Local)")
        self.playwright_fw.dropdown_select_option(self.opt_value_import, ">")
        log.info("Selecting Direct Personnel (years)")
        self.playwright_fw.dropdown_select_option(self.opt_direct_personnel_years, ">")
        log.info("Selecting Indirect Personnel (years)")
        self.playwright_fw.dropdown_select_option(self.opt_indirect_personnel_years, ">")
        log.info("Selecting Admin Personnel (years)")
        self.playwright_fw.dropdown_select_option(self.opt_admin_personnel_years, ">")
        log.info("Selecting Total (years)")
        self.playwright_fw.dropdown_select_option(self.opt_fourthplus_total_years, ">")
        log.info("Selecting Direct Personnel (average)")
        self.playwright_fw.dropdown_select_option(self.opt_direct_personnel_average, ">")
        log.info("Selecting Direct Personnel (average)")
        self.playwright_fw.dropdown_select_option(self.opt_indirect_personnel_average, ">")
        log.info("Selecting Direct Personnel (average)")
        self.playwright_fw.dropdown_select_option(self.opt_admin_personnel_average, ">")
        log.info("Selecting Total (average)")
        self.playwright_fw.dropdown_select_option(self.opt_fourthplus_total_average, ">")
        log.info("Selecting tier Incentives")
        self.btn_select_tier.click()
        log.info("Filling up additional information")
        self.playwright_fw.text_fill(self.txt_p_additional_information, "test 101")
        log.info("Filling up Company Profile of Parent Company")
        self.playwright_fw.text_fill(self.txt_p_company_profile, "test 101")
        log.info("Filling up For the Board's Consideration")
        self.playwright_fw.text_fill(self.txt_p_for_board_consideration, "test 101")
        log.info("Clicking Submit button")
        self.btn_submit_evaluation_report.click()
        log.info("Clicking Proceed button")
        self.btn_confirm_proceed_evaluation_report.click()
        self.page.wait_for_load_state("networkidle")
        log.info("Clicking OK button")
        self.btn_evaluation_report_ok.click()

    def do_endorsement_of_dc(self):
        log.info("-----Evaluation Report application-----")
        log.info("Clicking Proceed to Evaluation Report Application")
        self.btn_proceed_to_endorsement_dc_status.click()
        self.page.wait_for_load_state("networkidle")
        self.combo_box_select_option(self.opt_endorsement_dc_status, "approved")
        self.txt_endorsement_dc_remarks.fill("test 101")
        self.btn_endorsement_dc_submit.click()
        self.btn_endorsement_dc_confirm_proceed.click()
        self.page.wait_for_load_state("networkidle")
        self.btn_endorsement_dc_ok.click()

    def do_endorsement_of_dm(self):
        self.btn_proceed_to_endorsement_dm_status.click()
        self.page.wait_for_load_state("networkidle")
        self.dropdown_select_option(self.opt_endorsement_dm_status, "Endorsed to GM")
        self.txt_endorsement_dm_remarks.fill("test 101")
        self.btn_endorsement_dm_submit.click()
        self.btn_endorsement_dm_confirm_proceed.click()
        self.page.wait_for_load_state("networkidle")
        self.btn_endorsement_dm_ok.click()

    def do_endorsement_of_gm(self):
        self.btn_proceed_to_endorsement_gm_status.click()
        self.page.wait_for_load_state("networkidle")
        self.dropdown_select_option(self.opt_endorsement_gm_status, "Endorsed to DDG OPS")
        self.txt_endorsement_gm_remarks.fill("test 101")
        self.get_file_upload(self.upload_gm_signature_document, "modules/signature.jpg")
        self.btn_endorsement_gm_submit.click()
        self.btn_endorsement_gm_confirm_proceed.click()
        self.page.wait_for_load_state("networkidle")
        self.btn_endorsement_gm_ok.click()

    def do_endorsement_of_ddg(self):
        self.btn_proceed_to_endorsement_ddg_status.click()
        self.page.wait_for_load_state("networkidle")
        self.opt_endorsement_ddg_status.click()
        self.page.locator("(//input[@role='searchbox'])[2]").fill("Recommend to PEZA DG")
        self.page.keyboard.press("Enter")
        # self.dropdown_select_option(self.opt_endorsement_ddg_status, "Recommend to PEZA DG")
        self.txt_endorsement_ddg_remarks.fill("test 101")
        self.get_file_upload(self.upload_ddg_signature_document, "modules/signature.jpg")
        self.btn_endorsement_ddg_submit.click()
        self.btn_endorsement_ddg_confirm_proceed.click()
        self.page.wait_for_load_state("networkidle")
        self.btn_endorsement_ddg_ok.click()

    def do_board_consideration(self):
        self.btn_proceed_to_board_consideration.click()
        self.page.wait_for_load_state("networkidle")
        self.dropdown_select_option(self.opt_board_consideration_status, "For Board Consideration")
        self.txt_board_consideration_remarks.fill("test 101")
        self.get_file_upload(self.upload_board_consideration_document, "modules/signature.jpg")
        self.btn_board_consideration_submit.click()
        self.btn_board_consideration_confirm_proceed.click()
        self.page.wait_for_load_state("networkidle")
        self.btn_board_consideration_ok.click()

    def do_pb_approval(self):
        self.btn_proceed_to_pb_approval.click()
        self.page.wait_for_load_state("networkidle")
        self.dropdown_select_option(self.opt_pb_approval_status, "Approved")
        self.txt_pb_approval_remarks.fill("test 101")
        self.get_file_upload(self.upload_pb_approval_signature_document, "modules/signature.jpg")
        self.btn_pb_approval_submit.click()
        self.btn_pb_approval_confirm_proceed.click()
        self.page.wait_for_load_state("networkidle")
        self.btn_pb_approval_ok.click()

    def do_issuance_of_board_consideration(self):
        self.btn_proceed_to_issuance_of_board_consideration.click()
        self.page.wait_for_load_state("networkidle")
        self.dt_picker_board_meeting.click()
        self.dt_picker_date.click() # UPDATE TO THE LATEST DATE
        self.txt_resolution_number.fill("23232")
        self.txt_initials.fill("test 101")
        self.btn_issuance_of_board_consideration_submit.click()
        self.btn_issuance_of_board_consideration_confirm_proceed.click()
        self.page.wait_for_load_state("networkidle")
        self.btn_issuance_of_board_consideration_ok.click()

    def do_registration_payment(self):
        self.btn_proceed_to_rf_payment.click()
        self.page.wait_for_load_state("networkidle")
        self.chkbox_otc__rf_payment.click()
        self.page.wait_for_load_state("networkidle")
        self.btn_testing_rf_payment.click()
        self.btn_ok_success_test_rf_payment.click()
        self.btn_proceed_to_rf_payment_submit.click()
        self.btn_confirm_proceed_rf_payment.click()
        self.btn_ok_success_rf_payment.click()

    def do_ra_uploading(self):
        self.btn_proceed_to_ra_uploading.click()
        self.get_file_upload(self.upload_ra_document, "modules/sec-cert.pdf")
        self.btn_ra_uploading_submit.click()
        self.page.wait_for_load_state("networkidle")
        self.btn_ok_success_ra_uploading.click()

    def do_preparation_of_cor(self):
        self.btn_proceed_to_preparation_cor.click()
        self.btn_cor_submit.click()
        self.page.wait_for_load_state("networkidle")
        self.btn_ok_success_preparation.click() # check for OTP scenarios


    def dropdown_select_option(self, locator: Locator, option: str):
        # expect(self.page.get_by_role("option", name=option)).to_be_visible()
        self.page.wait_for_timeout(2000)
        locator.click()
        self.page.get_by_role("option", name=option).click()


    def combo_box_select_option(self, locator: Locator, option: str):
        # expect(self.page.get_by_role("option", name=option)).to_be_visible()
        self.page.wait_for_timeout(2000)
        locator.click()
        self.page.locator("#applicationStatus").select_option(option)

    def tier_select_option(self, locator: Locator, option: str):
        # expect(self.page.get_by_role("option", name=option)).to_be_visible()
        self.page.wait_for_timeout(2000)
        locator.click()
        expect(self.page.get_by_role("option", name=option)).to_be_visible()
        self.page.get_by_role("option", name=option).click()
        # self.page.locator("(//li[@id='select2-tier-result-cmqa-1'])[1]").click()
        # self.page.locator(locator).select_option(option)

    # def endorsed_to_dm_select_option(self, locator: Locator, option: str):
    #     # expect(self.page.get_by_role("option", name=option)).to_be_visible()
    #     self.page.wait_for_timeout(2000)
    #     locator.click()
    #     self.page.locator("#applicationStatus").select_option(option)

# upload images (self.driver = page)
    def get_file_upload(self, locator: Locator, file_path: str):
        # Find the file input element within the dropzone container
        # Dropzone divs typically contain a hidden input[type=file]

        with self.page.expect_file_chooser() as fc_info:
            locator.click()
            file_chooser = fc_info.value
            file_chooser.set_files(file_path)
            self.page.wait_for_timeout(2000)

    def zoom_in_out(self):
        self.page.evaluate("document.body.style.zoom = '0.8'")


    @staticmethod
    def save_to_csv(status, filename="berms_ee_id.csv"):
        # If file doesn't exist, write header first
        file_exists = os.path.exists(filename)

        with open(filename, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["status"])  # header
            writer.writerow([status])

    # USE THIS FOR SAVE ANOTHER CSV FILES
    @staticmethod
    def save_row(current_status, current_id, filename="berms_ee_status.csv"):
        file_exists = os.path.exists(filename)
        with open(filename, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["id_value", "status"])
            writer.writerow([current_id, current_status])
        # Clear them for the next row
        current_id = None
        current_status = None
