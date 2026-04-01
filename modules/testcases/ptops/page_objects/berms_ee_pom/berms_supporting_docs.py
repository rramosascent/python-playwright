from playwright.sync_api import Page, Locator, expect
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.custom_logger import log
import os
import csv
import pytest

class BermsSupportingDocsPage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_fw = FrameWorkPWDriver(self.page)
        self.upload_notarized_secretary_cert = page.locator("div[id='docType_sc_agraft'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_notarized_applicant_undertaking = page.locator("div[id='docType_und'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_by_laws = page.locator("div[id='docType_by_law'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_articles_of_incorporation = page.locator("div[id='docType_aoi'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_general_information_sheet = page.locator("div[id='docType_gis'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_20_year_projected_financial = page.locator("div[id='docType_pfs'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_bir_form_2303 = page.locator("div[id='docType_bir'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_company_profile = page.locator("div[id='docType_cppc'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_resume_of_biodata = page.locator("div[id='docType_rbpo'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_certificate_of_registration = page.locator("div[id='docType_crsec'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_site_development_plan = page.locator("div[id='docType_SDPVM'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_proof_of_land_ownership = page.locator("div[id='docType_plo'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_notarized_affidavit_option = page.locator("div[id='docType_nao'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_list_of_goods_handled = page.locator("div[id='docType_lgh'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_cert_from_national = page.locator("div[id='docType_CN'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_favorable_endorsement_from_doe = page.locator("div[id='docType_FEDOE'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_favorable_endorsement_from_water = page.locator("div[id='docType_FELWD'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_complete_operation_plan = page.locator("div[id='docType_COP'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_drawing_layout = page.locator("div[id='docType_SSA'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_cert_from_nwrb = page.locator("div[id='docType_nwrc'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_endorsement_from_dot = page.locator("div[id='docType_edt_dh'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_summary_of_sales = page.locator("div[id='supporting-documents'] div[id='docType_sum_exp'] div[class='py-3 supporting-docs-wrapper']")
        self.upload_copy_of_audited_accounting = page.locator("div[id='supporting-documents'] div[id='docType_afs'] div[class='py-3 supporting-docs-wrapper']")


        # self.upload_notarized_Certificate = page.locator("(//div[@class='dropzone-item'])[1]")
        # self.upload_notarize_undertaking = page.locator("(//div[@class='dropzone-item'])[2]")
        # self.upload_by_laws_purpose = page.locator("(//div[@class='dropzone-item'])[3]")
        # self.upload_articles_incorporation = page.locator("(//div[@class='dropzone-item'])[4]")
        # self.upload_general_info_sheet = page.locator("(//div[@class='dropzone-item'])[5]")
        # self.upload_project_financial = page.locator("(//div[@class='dropzone-item'])[6]") # upload excel file
        # self.upload_bir_2303 = page.locator("(//div[@class='dropzone-item'])[7]")
        # self.upload_company_profile = page.locator("(//div[@class='dropzone-item'])[8]")
        # self.upload_resume_principal_officers = page.locator("(//div[@class='dropzone-item'])[9]")
        # self.upload_cert_of_registration = page.locator("(//div[@class='dropzone-item'])[10]")
        # self.upload_site_dev_plan = page.locator("(//div[@class='dropzone-item'])[1]")
        # self.upload_notorized_affidavit_option = page.locator("(//div[@class='dropzone-item'])[2]")
        # self.upload_proof_of_land_ownership = page.locator("(//div[@class='dropzone-item'])[3]")
        # self.upload_notorized_secretary_cert = page.locator("(//div[@class='dropzone-item'])[4]")
        # self.upload_notorized_applicant_undertaking = page.locator("(//div[@class='dropzone-item'])[5]")

        self.btn_proceed_supporting_docs = page.locator("//div[@id='supporting-documents']//div[@class='row mt-3']//div[@class='col-12 d-flex justify-content-between align-items-center section-footer']//div//button[@type='button']")
        self.btn_submit_application = page.locator("#btnSubmitApplication:visible")
        self.btn_proceed_confirmation = page.locator("(//button[@class='swal2-confirm btn btn-primary btn-lg skip-submit-loading skip-text-change gap-2'])[1]")
        self.btn_ok_confirmation = page.locator("button.swal2-confirm.btn.btn-primary:visible")
        self.btn_save_as_draft = page.locator("#btnCompleteApproval")

        self.lbl_id = page.locator("div[id='swal2-html-container'] strong span")

        self.lnk_supporting_docs = page.locator("div[data-target='#supporting-documents'] button[type='button']")

    # def fillup_berms_supporting_docs(
    #     self,
    #     upload_notarized_certificate: str,
    #     upload_notarize_undertaking: str,
    #     upload_by_laws_purpose: str,
    #     upload_articles_incorporation: str,
    #     upload_general_info_sheet: str,
    #     upload_project_financial: str,
    #     upload_bir_2303: str,
    #     upload_company_profile: str,
    #     upload_resume_principal_officers: str,
    #     upload_cert_of_registration: str
    # ):
    #     log.info("-----Filling up Berms Supporting Documents-----")
    #     log.info("Uploading image of Notarized Secretary's Certificate & Anti-graft")
    #     self.get_file_upload(self.upload_notarized_Certificate, upload_notarized_certificate)
    #     log.info("Uploading image of Notarized Applicant's Undertaking")
    #     self.get_file_upload(self.upload_notarize_undertaking, upload_notarize_undertaking)
    #     log.info("Uploading of By-Laws indicating in its purpose the applicant’s export")
    #     self.get_file_upload(self.upload_by_laws_purpose, upload_by_laws_purpose)
    #     log.info("Uploading of Articles of Incorporation")
    #     self.get_file_upload(self.upload_articles_incorporation, upload_articles_incorporation)
    #     log.info("Uploading of General Information Sheet")
    #     self.get_file_upload(self.upload_general_info_sheet, upload_general_info_sheet)
    #     log.info("Uploading of 20-year Projected Financial Statement")
    #     self.get_file_upload(self.upload_project_financial, upload_project_financial)
    #     log.info("Uploading of BIR Form No. 2303")
    #     self.get_file_upload(self.upload_bir_2303, upload_bir_2303)
    #     log.info("Uploading of Company profile of parent company (as applicable)")
    #     self.get_file_upload(self.upload_company_profile, upload_company_profile)
    #     log.info("Uploading of Resume of Biodata of Principal Officers")
    #     self.get_file_upload(self.upload_resume_principal_officers, upload_resume_principal_officers)
    #     log.info("Uploading of Certificate of Registration from Securities and Exchange Commission")
    #     self.get_file_upload(self.upload_cert_of_registration, upload_cert_of_registration)
    #
    #     self.page.wait_for_timeout(2000)
    #
    #     log.info("Clicking Save and Proceed button")
    #     self.btn_proceed_supporting_docs.click()

    def application_confirmation(self):
        log.info("Clicking Submit button")
        self.page.locator("#btnSubmitApplication:visible").wait_for(state="visible")
        self.btn_submit_application.click()
        log.info("Clicking proceed button")
        self.btn_proceed_confirmation.click()
        # self.page.wait_for_timeout(5000) # waiting for the uplading documents
        # may behaviour na yung status journey is Application palang, hindi sya natutuloy sa generate payment
        # once yung application is hindi na click yung ok confirmation or nawalang ng net or nag auto close ang browser
        # self.page.wait_for_selector("(//div[@id='preloader'])[1]", state="hidden")
        # self.page.wait_for_selector("(//div[@id='preloaderStatusText'])[1]", state="hidden")
        self.get_value_application_id()
        log.info("Clicking OK button")
        self.wait_for_preloader()
        self.page.locator("(//div[@class='swal2-popup swal2-modal swal2-icon-success swal2-show'])[1]").wait_for(state="visible")
        # self.click_button(self.btn_ok_confirmation)
        self.btn_ok_confirmation.click()

    def save_as_draft(self):
        log.info("Clicking Save as draft button")
        self.btn_save_as_draft.click()

    def click_button(self, locator: Locator):
        self.page.get_by_role("button", name="OK").scroll_into_view_if_needed()
        expect(self.page.get_by_role("button", name="OK")).to_be_in_viewport()
        self.page.get_by_role("button", name="OK").click()
        # locator.scroll_into_view_if_needed()
        # expect(locator).to_be_in_viewport()
        # locator.click()

    def expect_locator(self):
        expect(self.page.locator("#swal2-html-container strong span")).to_be_visible(timeout=30000)

    def wait_for_preloader(self):
        try:
            self.page.wait_for_function(
            "document.querySelector('#preloader')?.getAttribute('aria-hidden') === 'true'",
            timeout=20000
        )
        except:
        # Fallback: wait until element is detached
            self.page.wait_for_selector("#preloader", state="detached", timeout=20000)


    def get_file_upload(self, locator: Locator, file_path: str):
        # Find the file input element within the dropzone container
        # Dropzone divs typically contain a hidden input[type=file]

        with self.page.expect_file_chooser() as fc_info:
            locator.click()
            file_chooser = fc_info.value
            file_chooser.set_files(file_path)
            self.page.wait_for_timeout(2000)

    def get_value_application_id(self):
        self.page.wait_for_timeout(3000)
        label = self.lbl_id.inner_text()
        self.save_to_csv(label)

    @staticmethod
    def save_to_csv(id_value, filename="berms_ee_id.csv"):
        # If file doesn't exist, write header first
        file_exists = os.path.exists(filename)

        with open(filename, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["id_value"])  # header
            writer.writerow([id_value])

    def berms_ee_transaction(self, transaction_type, type_ee):
        if transaction_type == "NEW ECOZONE ENTERPRISE":
            match type_ee:
                case 'Domestic Market':
                    self.domestic_upload_supporting_docs(
                        notarized_secretary_cert="modules/Testing_document.png",
                        notarized_applicant_undertaking="modules/Testing_document.png",
                        by_laws="modules/Testing_document.png",
                        articles_of_incorporation="modules/Testing_document.png",
                        general_information_sheet="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        company_profile="modules/Testing_document.png",
                        resume_of_biodata="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case 'Facilities':
                    self.facilities_upload_supporting_docs(
                        site_development_plan="modules/Testing_document.png",
                        notarized_affidavit_option="modules/Testing_document.png",
                        proof_of_land_ownership="modules/Testing_document.png",
                        notarized_secretary_cert="modules/Testing_document.png",
                        notarized_applicant_undertaking="modules/Testing_document.png",
                        by_laws="modules/Testing_document.png",
                        articles_of_incorporation="modules/Testing_document.png",
                        general_information_sheet="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        company_profile="modules/Testing_document.png",
                        resume_of_biodata="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case 'Logistics Service':
                    self.logistic_upload_supporting_docs(
                        notarized_affidavit_option="modules/Testing_document.png",
                        list_of_goods_handled="modules/Testing_document.png",
                        notarized_secretary_cert="modules/Testing_document.png",
                        notarized_applicant_undertaking="modules/Testing_document.png",
                        by_laws="modules/Testing_document.png",
                        articles_of_incorporation="modules/Testing_document.png",
                        general_information_sheet="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        company_profile="modules/Testing_document.png",
                        resume_of_biodata="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case 'Utilities':
                    self.utilities_upload_supporting_docs(
                        cert_from_national="modules/Testing_document.png",
                        favorable_endorsement_from_doe="modules/Testing_document.png",
                        favorable_endorsement_from_water="modules/Testing_document.png",
                        site_development_plan="modules/Testing_document.png",
                        complete_operation_plan="modules/Testing_document.png",
                        drawing_layout="modules/Testing_document.png",
                        notarized_affidavit_option="modules/Testing_document.png",
                        cert_from_nwrb="modules/Testing_document.png",
                        proof_of_land_ownership="modules/Testing_document.png",
                        notarized_secretary_cert="modules/Testing_document.png",
                        notarized_applicant_undertaking="modules/Testing_document.png",
                        by_laws="modules/Testing_document.png",
                        articles_of_incorporation="modules/Testing_document.png",
                        general_information_sheet="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        company_profile="modules/Testing_document.png",
                        resume_of_biodata="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case 'Export Enterprise':
                    self.export_upload_supporting_docs(
                        notarized_affidavit_option="modules/Testing_document.png",
                        notarized_secretary_cert="modules/Testing_document.png",
                        notarized_applicant_undertaking="modules/Testing_document.png",
                        by_laws="modules/Testing_document.png",
                        articles_of_incorporation="modules/Testing_document.png",
                        general_information_sheet="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        company_profile="modules/Testing_document.png",
                        resume_of_biodata="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case 'IT Enterprise':
                    self.it_upload_supporting_docs(
                        notarized_affidavit_option="modules/Testing_document.png",
                        notarized_secretary_cert="modules/Testing_document.png",
                        notarized_applicant_undertaking="modules/Testing_document.png",
                        by_laws="modules/Testing_document.png",
                        articles_of_incorporation="modules/Testing_document.png",
                        general_information_sheet="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        company_profile="modules/Testing_document.png",
                        resume_of_biodata="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case 'Tourism':
                    self.tourism_upload_supporting_docs(
                        notarized_affidavit_option="modules/Testing_document.png",
                        endorsement_from_dot="modules/Testing_document.png",
                        notarized_secretary_cert="modules/Testing_document.png",
                        notarized_applicant_undertaking="modules/Testing_document.png",
                        by_laws="modules/Testing_document.png",
                        articles_of_incorporation="modules/Testing_document.png",
                        general_information_sheet="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        company_profile="modules/Testing_document.png",
                        resume_of_biodata="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case _:
                    pytest.fail('invalid enterprise value')

        elif transaction_type == "NEW PROJECT OF AN EXISTING ENTERPRISE":
            match type_ee:
                case 'Domestic Market':
                    self.project_existing_domestic_upload_supporting_docs(
                        notarized_secretary_cert="modules/Testing_document.png",
                        summary_of_sales="modules/Testing_document.png",
                        copy_of_audited_accounting="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case 'Facilities':
                    self.project_existing_facilities_upload_supporting_docs(
                        site_development_plan="modules/Testing_document.png",
                        notarized_affidavit_option="modules/Testing_document.png",
                        proof_of_land_ownership="modules/Testing_document.png",
                        notarized_secretary_cert="modules/Testing_document.png",
                        summary_of_sales="modules/Testing_document.png",
                        copy_of_audited_accounting="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case 'Logistics Service':
                    self.project_existing_logistic_upload_supporting_docs(
                        notarized_affidavit_option="modules/Testing_document.png",
                        list_of_goods_handled="modules/Testing_document.png",
                        notarized_secretary_cert="modules/Testing_document.png",
                        summary_of_sales="modules/Testing_document.png",
                        copy_of_audited_accounting="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case 'Utilities':
                    self.project_existing_utilities_upload_supporting_docs(
                        cert_from_national="modules/Testing_document.png",
                        favorable_endorsement_from_doe="modules/Testing_document.png",
                        favorable_endorsement_from_water="modules/Testing_document.png",
                        site_development_plan="modules/Testing_document.png",
                        complete_operation_plan="modules/Testing_document.png",
                        drawing_layout="modules/Testing_document.png",
                        notarized_affidavit_option="modules/Testing_document.png",
                        list_of_goods_handled="modules/Testing_document.png",
                        proof_of_land_ownership="modules/Testing_document.png",
                        notarized_secretary_cert="modules/Testing_document.png",
                        summary_of_sales="modules/Testing_document.png",
                        copy_of_audited_accounting="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case 'Export Enterprise':
                    self.project_existing_export_upload_supporting_docs(
                        notarized_affidavit_option="modules/Testing_document.png",
                        notarized_secretary_cert="modules/Testing_document.png",
                        summary_of_sales="modules/Testing_document.png",
                        copy_of_audited_accounting="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case 'IT Enterprise':
                    self.project_existing_it_upload_supporting_docs(
                        notarized_affidavit_option="modules/Testing_document.png",
                        notarized_secretary_cert="modules/Testing_document.png",
                        summary_of_sales="modules/Testing_document.png",
                        copy_of_audited_accounting="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case 'Tourism':
                    self.project_existing_tourism_upload_supporting_docs(
                        notarized_affidavit_option="modules/Testing_document.png",
                        endorsement_from_dot="modules/Testing_document.png",
                        notarized_secretary_cert="modules/Testing_document.png",
                        summary_of_sales="modules/Testing_document.png",
                        copy_of_audited_accounting="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case _:
                    pytest.fail('invalid enterprise value')

        elif transaction_type == "EXPANSION PROJECT OF AN EXISTING ENTERPRISE":
            match type_ee:
                case 'Domestic Market':
                    self.expansion_domestic_upload_supporting_docs(
                        notarized_secretary_cert="modules/Testing_document.png",
                        summary_of_sales="modules/Testing_document.png",
                        copy_of_audited_accounting="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case 'Facilities':
                    self.expansion_existing_facilities_upload_supporting_docs(
                        site_development_plan="modules/Testing_document.png",
                        notarized_affidavit_option="modules/Testing_document.png",
                        proof_of_land_ownership="modules/Testing_document.png",
                        notarized_secretary_cert="modules/Testing_document.png",
                        summary_of_sales="modules/Testing_document.png",
                        copy_of_audited_accounting="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case 'Logistics Service':
                    self.expansion_existing_logistic_upload_supporting_docs(
                        notarized_affidavit_option="modules/Testing_document.png",
                        list_of_goods_handled="modules/Testing_document.png",
                        notarized_secretary_cert="modules/Testing_document.png",
                        summary_of_sales="modules/Testing_document.png",
                        copy_of_audited_accounting="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case 'Utilities':
                    self.expansion_existing_utilities_upload_supporting_docs(
                        cert_from_national="modules/Testing_document.png",
                        favorable_endorsement_from_doe="modules/Testing_document.png",
                        favorable_endorsement_from_water="modules/Testing_document.png",
                        site_development_plan="modules/Testing_document.png",
                        complete_operation_plan="modules/Testing_document.png",
                        drawing_layout="modules/Testing_document.png",
                        notarized_affidavit_option="modules/Testing_document.png",
                        list_of_goods_handled="modules/Testing_document.png",
                        proof_of_land_ownership="modules/Testing_document.png",
                        notarized_secretary_cert="modules/Testing_document.png",
                        summary_of_sales="modules/Testing_document.png",
                        copy_of_audited_accounting="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case 'Export Enterprise':
                    self.expansion_existing_export_upload_supporting_docs(
                        notarized_affidavit_option="modules/Testing_document.png",
                        notarized_secretary_cert="modules/Testing_document.png",
                        summary_of_sales="modules/Testing_document.png",
                        copy_of_audited_accounting="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case 'IT Enterprise':
                    self.expansion_existing_it_upload_supporting_docs(
                        notarized_affidavit_option="modules/Testing_document.png",
                        notarized_secretary_cert="modules/Testing_document.png",
                        summary_of_sales="modules/Testing_document.png",
                        copy_of_audited_accounting="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case 'Tourism':
                    self.expansion_existing_tourism_upload_supporting_docs(
                        notarized_affidavit_option="modules/Testing_document.png",
                        endorsement_from_dot="modules/Testing_document.png",
                        notarized_secretary_cert="modules/Testing_document.png",
                        summary_of_sales="modules/Testing_document.png",
                        copy_of_audited_accounting="modules/Testing_document.png",
                        year_projected_financial="modules/testexcel.xlsx",
                        bir_form_2303="modules/Testing_document.png",
                        certificate_of_registration="modules/Testing_document.png"
                    )
                case _:
                    pytest.fail('invalid enterprise value')

    def domestic_upload_supporting_docs(
            self,
            notarized_secretary_cert: str,
            notarized_applicant_undertaking: str,
            by_laws: str,
            articles_of_incorporation: str,
            general_information_sheet: str,
            year_projected_financial: str,
            bir_form_2303: str,
            company_profile: str,
            resume_of_biodata: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_notarized_applicant_undertaking, notarized_applicant_undertaking)
        self.get_file_upload(self.upload_by_laws, by_laws)
        self.get_file_upload(self.upload_articles_of_incorporation, articles_of_incorporation)
        self.get_file_upload(self.upload_general_information_sheet, general_information_sheet)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_company_profile, company_profile)
        self.get_file_upload(self.upload_resume_of_biodata, resume_of_biodata)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

    def facilities_upload_supporting_docs(
            self,
            site_development_plan: str,
            notarized_affidavit_option: str,
            proof_of_land_ownership: str,
            notarized_secretary_cert: str,
            notarized_applicant_undertaking: str,
            by_laws: str,
            articles_of_incorporation: str,
            general_information_sheet: str,
            year_projected_financial: str,
            bir_form_2303: str,
            company_profile: str,
            resume_of_biodata: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_site_development_plan, site_development_plan)
        self.get_file_upload(self.upload_notarized_affidavit_option, notarized_affidavit_option)
        self.get_file_upload(self.upload_proof_of_land_ownership, proof_of_land_ownership)
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_notarized_applicant_undertaking, notarized_applicant_undertaking)
        self.get_file_upload(self.upload_by_laws, by_laws)
        self.get_file_upload(self.upload_articles_of_incorporation, articles_of_incorporation)
        self.get_file_upload(self.upload_general_information_sheet, general_information_sheet)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_company_profile, company_profile)
        self.get_file_upload(self.upload_resume_of_biodata, resume_of_biodata)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

    def logistic_upload_supporting_docs(
            self,
            notarized_affidavit_option: str,
            list_of_goods_handled: str,
            notarized_secretary_cert: str,
            notarized_applicant_undertaking: str,
            by_laws: str,
            articles_of_incorporation: str,
            general_information_sheet: str,
            year_projected_financial: str,
            bir_form_2303: str,
            company_profile: str,
            resume_of_biodata: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_notarized_affidavit_option, notarized_affidavit_option)
        self.get_file_upload(self.upload_list_of_goods_handled, list_of_goods_handled)
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_notarized_applicant_undertaking, notarized_applicant_undertaking)
        self.get_file_upload(self.upload_by_laws, by_laws)
        self.get_file_upload(self.upload_articles_of_incorporation, articles_of_incorporation)
        self.get_file_upload(self.upload_general_information_sheet, general_information_sheet)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_company_profile, company_profile)
        self.get_file_upload(self.upload_resume_of_biodata, resume_of_biodata)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

    def utilities_upload_supporting_docs(
            self,
            cert_from_national: str,
            favorable_endorsement_from_doe: str,
            favorable_endorsement_from_water: str,
            site_development_plan: str,
            complete_operation_plan: str,
            drawing_layout: str,
            notarized_affidavit_option: str,
            cert_from_nwrb: str,
            proof_of_land_ownership: str,
            notarized_secretary_cert: str,
            notarized_applicant_undertaking: str,
            by_laws: str,
            articles_of_incorporation: str,
            general_information_sheet: str,
            year_projected_financial: str,
            bir_form_2303: str,
            company_profile: str,
            resume_of_biodata: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_cert_from_national, cert_from_national)
        self.get_file_upload(self.upload_favorable_endorsement_from_doe, favorable_endorsement_from_doe)
        self.get_file_upload(self.upload_favorable_endorsement_from_water, favorable_endorsement_from_water)
        self.get_file_upload(self.upload_site_development_plan, site_development_plan)
        self.get_file_upload(self.upload_complete_operation_plan, complete_operation_plan)
        self.get_file_upload(self.upload_drawing_layout, drawing_layout)
        self.get_file_upload(self.upload_notarized_affidavit_option, notarized_affidavit_option)
        self.get_file_upload(self.upload_cert_from_nwrb, cert_from_nwrb)
        self.get_file_upload(self.upload_proof_of_land_ownership, proof_of_land_ownership)
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_notarized_applicant_undertaking, notarized_applicant_undertaking)
        self.get_file_upload(self.upload_by_laws, by_laws)
        self.get_file_upload(self.upload_articles_of_incorporation, articles_of_incorporation)
        self.get_file_upload(self.upload_general_information_sheet, general_information_sheet)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_company_profile, company_profile)
        self.get_file_upload(self.upload_resume_of_biodata, resume_of_biodata)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

    def export_upload_supporting_docs(
            self,
            notarized_affidavit_option: str,
            notarized_secretary_cert: str,
            notarized_applicant_undertaking: str,
            by_laws: str,
            articles_of_incorporation: str,
            general_information_sheet: str,
            year_projected_financial: str,
            bir_form_2303: str,
            company_profile: str,
            resume_of_biodata: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_notarized_affidavit_option, notarized_affidavit_option)
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_notarized_applicant_undertaking, notarized_applicant_undertaking)
        self.get_file_upload(self.upload_by_laws, by_laws)
        self.get_file_upload(self.upload_articles_of_incorporation, articles_of_incorporation)
        self.get_file_upload(self.upload_general_information_sheet, general_information_sheet)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_company_profile, company_profile)
        self.get_file_upload(self.upload_resume_of_biodata, resume_of_biodata)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

    def it_upload_supporting_docs(
            self,
            notarized_affidavit_option: str,
            notarized_secretary_cert: str,
            notarized_applicant_undertaking: str,
            by_laws: str,
            articles_of_incorporation: str,
            general_information_sheet: str,
            year_projected_financial: str,
            bir_form_2303: str,
            company_profile: str,
            resume_of_biodata: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_notarized_affidavit_option, notarized_affidavit_option)
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_notarized_applicant_undertaking, notarized_applicant_undertaking)
        self.get_file_upload(self.upload_by_laws, by_laws)
        self.get_file_upload(self.upload_articles_of_incorporation, articles_of_incorporation)
        self.get_file_upload(self.upload_general_information_sheet, general_information_sheet)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_company_profile, company_profile)
        self.get_file_upload(self.upload_resume_of_biodata, resume_of_biodata)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

    def tourism_upload_supporting_docs(
            self,
            notarized_affidavit_option: str,
            endorsement_from_dot: str,
            notarized_secretary_cert: str,
            notarized_applicant_undertaking: str,
            by_laws: str,
            articles_of_incorporation: str,
            general_information_sheet: str,
            year_projected_financial: str,
            bir_form_2303: str,
            company_profile: str,
            resume_of_biodata: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_notarized_affidavit_option, notarized_affidavit_option)
        self.get_file_upload(self.upload_endorsement_from_dot, endorsement_from_dot)
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_notarized_applicant_undertaking, notarized_applicant_undertaking)
        self.get_file_upload(self.upload_by_laws, by_laws)
        self.get_file_upload(self.upload_articles_of_incorporation, articles_of_incorporation)
        self.get_file_upload(self.upload_general_information_sheet, general_information_sheet)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_company_profile, company_profile)
        self.get_file_upload(self.upload_resume_of_biodata, resume_of_biodata)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

# New Project of an Existing Enterprise
    def project_existing_domestic_upload_supporting_docs(
            self,
            notarized_secretary_cert: str,
            summary_of_sales: str,
            copy_of_audited_accounting: str,
            year_projected_financial: str,
            bir_form_2303: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_summary_of_sales, summary_of_sales)
        self.get_file_upload(self.upload_copy_of_audited_accounting, copy_of_audited_accounting)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

    def project_existing_facilities_upload_supporting_docs(
            self,
            site_development_plan: str,
            notarized_affidavit_option: str,
            proof_of_land_ownership: str,
            notarized_secretary_cert: str,
            summary_of_sales: str,
            copy_of_audited_accounting: str,
            year_projected_financial: str,
            bir_form_2303: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_site_development_plan, site_development_plan)
        self.get_file_upload(self.upload_notarized_affidavit_option, notarized_affidavit_option)
        self.get_file_upload(self.upload_proof_of_land_ownership, proof_of_land_ownership)
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_summary_of_sales, summary_of_sales)
        self.get_file_upload(self.upload_copy_of_audited_accounting, copy_of_audited_accounting)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

    def project_existing_logistic_upload_supporting_docs(
            self,
            notarized_affidavit_option: str,
            list_of_goods_handled: str,
            notarized_secretary_cert: str,
            summary_of_sales: str,
            copy_of_audited_accounting: str,
            year_projected_financial: str,
            bir_form_2303: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_notarized_affidavit_option, notarized_affidavit_option)
        self.get_file_upload(self.upload_list_of_goods_handled, list_of_goods_handled)
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_summary_of_sales, summary_of_sales)
        self.get_file_upload(self.upload_copy_of_audited_accounting, copy_of_audited_accounting)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

    def project_existing_utilities_upload_supporting_docs(
            self,
            cert_from_national: str,
            favorable_endorsement_from_doe: str,
            favorable_endorsement_from_water: str,
            site_development_plan: str,
            complete_operation_plan: str,
            drawing_layout: str,
            notarized_affidavit_option: str,
            list_of_goods_handled: str,
            proof_of_land_ownership: str,
            notarized_secretary_cert: str,
            summary_of_sales: str,
            copy_of_audited_accounting: str,
            year_projected_financial: str,
            bir_form_2303: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_cert_from_national, cert_from_national)
        self.get_file_upload(self.upload_favorable_endorsement_from_doe, favorable_endorsement_from_doe)
        self.get_file_upload(self.upload_favorable_endorsement_from_water, favorable_endorsement_from_water)
        self.get_file_upload(self.upload_site_development_plan, site_development_plan)
        self.get_file_upload(self.upload_complete_operation_plan, complete_operation_plan)
        self.get_file_upload(self.upload_drawing_layout, drawing_layout)
        self.get_file_upload(self.upload_notarized_affidavit_option, notarized_affidavit_option)
        self.get_file_upload(self.upload_cert_from_nwrb, list_of_goods_handled)
        self.get_file_upload(self.upload_proof_of_land_ownership, proof_of_land_ownership)
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_summary_of_sales, summary_of_sales)
        self.get_file_upload(self.upload_copy_of_audited_accounting, copy_of_audited_accounting)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

    def project_existing_export_upload_supporting_docs(
            self,
            notarized_affidavit_option: str,
            notarized_secretary_cert: str,
            summary_of_sales: str,
            copy_of_audited_accounting: str,
            year_projected_financial: str,
            bir_form_2303: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_notarized_affidavit_option, notarized_affidavit_option)
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_summary_of_sales, summary_of_sales)
        self.get_file_upload(self.upload_copy_of_audited_accounting, copy_of_audited_accounting)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

    def project_existing_it_upload_supporting_docs(
            self,
            notarized_affidavit_option: str,
            notarized_secretary_cert: str,
            summary_of_sales: str,
            copy_of_audited_accounting: str,
            year_projected_financial: str,
            bir_form_2303: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_notarized_affidavit_option, notarized_affidavit_option)
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_summary_of_sales, summary_of_sales)
        self.get_file_upload(self.upload_copy_of_audited_accounting, copy_of_audited_accounting)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

    def project_existing_tourism_upload_supporting_docs(
            self,
            notarized_affidavit_option: str,
            endorsement_from_dot: str,
            notarized_secretary_cert: str,
            summary_of_sales: str,
            copy_of_audited_accounting: str,
            year_projected_financial: str,
            bir_form_2303: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_notarized_affidavit_option, notarized_affidavit_option)
        self.get_file_upload(self.upload_endorsement_from_dot, endorsement_from_dot)
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_summary_of_sales, summary_of_sales)
        self.get_file_upload(self.upload_copy_of_audited_accounting, copy_of_audited_accounting)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

# Expansion Project of an Existing Enterprise
    def expansion_domestic_upload_supporting_docs(
            self,
            notarized_secretary_cert: str,
            summary_of_sales: str,
            copy_of_audited_accounting: str,
            year_projected_financial: str,
            bir_form_2303: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_summary_of_sales, summary_of_sales)
        self.get_file_upload(self.upload_copy_of_audited_accounting, copy_of_audited_accounting)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

    def expansion_existing_facilities_upload_supporting_docs(
            self,
            site_development_plan: str,
            notarized_affidavit_option: str,
            proof_of_land_ownership: str,
            notarized_secretary_cert: str,
            summary_of_sales: str,
            copy_of_audited_accounting: str,
            year_projected_financial: str,
            bir_form_2303: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_site_development_plan, site_development_plan)
        self.get_file_upload(self.upload_notarized_affidavit_option, notarized_affidavit_option)
        self.get_file_upload(self.upload_proof_of_land_ownership, proof_of_land_ownership)
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_summary_of_sales, summary_of_sales)
        self.get_file_upload(self.upload_copy_of_audited_accounting, copy_of_audited_accounting)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

    def expansion_existing_logistic_upload_supporting_docs(
            self,
            notarized_affidavit_option: str,
            list_of_goods_handled: str,
            notarized_secretary_cert: str,
            summary_of_sales: str,
            copy_of_audited_accounting: str,
            year_projected_financial: str,
            bir_form_2303: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_notarized_affidavit_option, notarized_affidavit_option)
        self.get_file_upload(self.upload_list_of_goods_handled, list_of_goods_handled)
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_summary_of_sales, summary_of_sales)
        self.get_file_upload(self.upload_copy_of_audited_accounting, copy_of_audited_accounting)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

    def expansion_existing_utilities_upload_supporting_docs(
            self,
            cert_from_national: str,
            favorable_endorsement_from_doe: str,
            favorable_endorsement_from_water: str,
            site_development_plan: str,
            complete_operation_plan: str,
            drawing_layout: str,
            notarized_affidavit_option: str,
            list_of_goods_handled: str,
            proof_of_land_ownership: str,
            notarized_secretary_cert: str,
            summary_of_sales: str,
            copy_of_audited_accounting: str,
            year_projected_financial: str,
            bir_form_2303: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_cert_from_national, cert_from_national)
        self.get_file_upload(self.upload_favorable_endorsement_from_doe, favorable_endorsement_from_doe)
        self.get_file_upload(self.upload_favorable_endorsement_from_water, favorable_endorsement_from_water)
        self.get_file_upload(self.upload_site_development_plan, site_development_plan)
        self.get_file_upload(self.upload_complete_operation_plan, complete_operation_plan)
        self.get_file_upload(self.upload_drawing_layout, drawing_layout)
        self.get_file_upload(self.upload_notarized_affidavit_option, notarized_affidavit_option)
        self.get_file_upload(self.upload_cert_from_nwrb, list_of_goods_handled)
        self.get_file_upload(self.upload_proof_of_land_ownership, proof_of_land_ownership)
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_summary_of_sales, summary_of_sales)
        self.get_file_upload(self.upload_copy_of_audited_accounting, copy_of_audited_accounting)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

    def expansion_existing_export_upload_supporting_docs(
            self,
            notarized_affidavit_option: str,
            notarized_secretary_cert: str,
            summary_of_sales: str,
            copy_of_audited_accounting: str,
            year_projected_financial: str,
            bir_form_2303: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_notarized_affidavit_option, notarized_affidavit_option)
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_summary_of_sales, summary_of_sales)
        self.get_file_upload(self.upload_copy_of_audited_accounting, copy_of_audited_accounting)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

    def expansion_existing_it_upload_supporting_docs(
            self,
            notarized_affidavit_option: str,
            notarized_secretary_cert: str,
            summary_of_sales: str,
            copy_of_audited_accounting: str,
            year_projected_financial: str,
            bir_form_2303: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_notarized_affidavit_option, notarized_affidavit_option)
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_summary_of_sales, summary_of_sales)
        self.get_file_upload(self.upload_copy_of_audited_accounting, copy_of_audited_accounting)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

    def expansion_existing_tourism_upload_supporting_docs(
            self,
            notarized_affidavit_option: str,
            endorsement_from_dot: str,
            notarized_secretary_cert: str,
            summary_of_sales: str,
            copy_of_audited_accounting: str,
            year_projected_financial: str,
            bir_form_2303: str,
            certificate_of_registration: str
    ):
        log.info("-----Filling up Berms Supporting Documents-----")
        self.lnk_supporting_docs.click()
        self.get_file_upload(self.upload_notarized_affidavit_option, notarized_affidavit_option)
        self.get_file_upload(self.upload_endorsement_from_dot, endorsement_from_dot)
        self.get_file_upload(self.upload_notarized_secretary_cert, notarized_secretary_cert)
        self.get_file_upload(self.upload_summary_of_sales, summary_of_sales)
        self.get_file_upload(self.upload_copy_of_audited_accounting, copy_of_audited_accounting)
        self.get_file_upload(self.upload_20_year_projected_financial, year_projected_financial)
        self.get_file_upload(self.upload_bir_form_2303, bir_form_2303)
        self.get_file_upload(self.upload_certificate_of_registration, certificate_of_registration)

    def click_proceed(self):
        self.page.wait_for_timeout(2000)

        log.info("Clicking Save and Proceed button")
        self.btn_proceed_supporting_docs.click()