from playwright.sync_api import Page, Locator, sync_playwright
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.custom_logger import log
import pytest
import psycopg2
import time

def get_otp_from_db():
    global conn
    log.info("--- Attempting to connect to PostgreSQL ---")
    try:
        conn = psycopg2.connect(
            dbname="peza_db_test",
            user="postgres",
            password="postgres",
            host="192.168.20.26",
            port="5432",
            connect_timeout=5  # Stops it from hanging forever if the IP is wrong
        )
        # Use a DictCursor if you want to access by column name: result['otp_number']
        cursor = conn.cursor()

        # Simplified query: Directly target the table with the schema prefix
        query = """
            SELECT otp
            FROM cprs.company_registration_otp
            ORDER BY created_at DESC
            LIMIT 1
        """
        # SELECT otp_number FROM provider_otp WHERE accreditation_app_id = '3269' ORDER BY created_at DESC LIMIT 1;

        for i in range(5):
            log.info(f"Polling DB for OTP (Attempt {i + 1})...")
            cursor.execute(query)
            result = cursor.fetchone()

            if result and result[0]:
                otp = str(result[0])
                cursor.close()
                conn.close()
                return otp

            time.sleep(2)
            # Important: commit or rollback to ensure you aren't seeing cached data
            conn.rollback()

    except Exception as e:
        log.error(f"Database error: {e}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()
    return None

class PtopsRegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_fw = FrameWorkPWDriver(self.page)
        self.link_create_account = page.locator("(//span[normalize-space()='Create an account'])[1]")
        self.btn_ee_type_registration = page.locator("//div[@class='col regTypeEcozoneEnt btnStatus']//label[@class='btnRegType text-center btn-registration-type']")
        self.btn_ed_type_registration = page.locator("//div[@class='col regTypeEcozoneDev btnStatus']//label[@class='btnRegType text-center btn-registration-type']")
        self.btn_se_type_registration = page.locator("//div[@class='col regTypeServices btnStatus']//label[@class='btnRegType text-center btn-registration-type']")
        self.btn_proceed_to_registration = page.locator("(//button[normalize-space()='Proceed to Registration Form'])[1]")
        self.chkbox_read_agree = page.locator("(//input[@id='dpCheckbox'])[1]")
        self.btn_submit = page.locator("(//button[@id='dpSubmit'])[1]")
        self.txt_company_name = page.locator("(//input[@id='companyName'])[1]")
        self.txt_tin = page.locator("(//input[@id='companyTinNumber'])[1]")
        self.opt_region = page.locator("(//span[@id='select2-companyRegionId-container'])[1]")
        self.opt_province = page.locator("(//span[@id='select2-companyProvinceId-container'])[1]")
        self.opt_city = page.locator("(//span[@id='select2-companyCityId-container'])[1]")
        self.opt_barangay = page.locator("(//span[@id='select2-companyBarangayId-container'])[1]")
        self.txt_street_name = page.locator("(//input[@id='companyAddressLine1'])[1]")
        self.txt_company_mobile_number = page.locator("(//input[@id='companyMobileNumber'])[1]")
        self.txt_company_landline = page.locator("(//input[@id='companyTelephoneNumber'])[1]")
        self.txt_company_email = page.locator("(//input[@id='companyEmailAddress'])[1]")
        self.upload_first_file = page.locator("(//input[@id='supportingDocumentFilename'])[1]")
        self.upload_second_file = page.locator("(//input[@id='supportingDocumentFilename2'])[1]")
        self.btn_upload_first_file = page.locator("(//button[@id='btnAddSupportingDocument'])[1]")
        self.btn_upload_second_file = page.locator("(//button[@id='btnAddSupportingDocument2'])[1]")
        self.txt_account_last_name = page.locator("(//input[@id='lastname'])[1]")
        self.txt_account_first_name = page.locator("(//input[@id='firstname'])[1]")
        self.txt_account_middle_name = page.locator("(//input[@id='middlename'])[1]")
        self.txt_position = page.locator("(//input[@id='companyPosition'])[1]")
        self.txt_account_mobile_number = page.locator("(//input[@id='mobileNumber'])[1]")
        self.txt_account_email = page.locator("(//input[@id='email'])[1]")
        self.txt_account_username = page.locator("(//input[@id='username'])[1]")
        self.txt_account_password = page.locator("(//input[@id='password'])[1]")
        self.txt_confirm_password = page.locator("(//input[@id='confirmPassword'])[1]")
        self.btn_confirm_details = page.locator("(//button[normalize-space()='Details Confirmed'])[1]")

        self.btn_submit_registration = page.locator("(//button[@id='btnSubmitRegistration'])[1]")
        self.btn_registration_proceed = page.locator("(//button[normalize-space()='Proceed'])[1]")
        self.txt_input_otp = page.locator("#otp1")
        self.btn_submit_otp = page.locator("(//button[@id='btnSubmit'])[2]")

        self.btn_okay_pending = page.locator("(//button[normalize-space()='Okay'])[1]")

    def goto_registration_form(self, type_of_registration):
        self.link_create_account.click()

        match type_of_registration:
            case 'ed':
                self.btn_ed_type_registration.click()
            case 'ee':
                self.btn_ee_type_registration.click()
            case 'se':
                self.btn_se_type_registration.click()
            case _:
                pytest.fail('invalid registration type')

        self.btn_proceed_to_registration.click()
        self.chkbox_read_agree.click()
        self.btn_submit.click()

    def fillup_company_registration(
        self,
        company_type,
        company_name,
        tin,
        region,
        province,
        city,
        barangay,
        street_name,
        company_mobile_number,
        company_landline,
        company_email
    ):
        log.info("-----Filling up Company Details-----")
        self.playwright_fw.rdbox_select_option(company_type)
        self.playwright_fw.text_fill(self.txt_company_name, company_name)
        self.playwright_fw.text_fill(self.txt_tin, tin)
        self.playwright_fw.dropdown_select_option(self.opt_region, region)
        self.playwright_fw.dropdown_select_option(self.opt_province, province)
        self.playwright_fw.dropdown_select_option(self.opt_city, city)
        self.playwright_fw.dropdown_select_option(self.opt_barangay, barangay)
        self.playwright_fw.text_fill(self.txt_street_name, street_name)
        self.playwright_fw.text_fill(self.txt_company_mobile_number, company_mobile_number)
        self.playwright_fw.text_fill(self.txt_company_landline, company_landline)
        self.playwright_fw.text_fill(self.txt_company_email, company_email)

        if company_type == 'Sole Proprietorship':
            self.get_file_upload(self.upload_first_file, "modules/Testing_document.png")
            self.page.wait_for_timeout(2000)
            self.btn_upload_first_file.click()
        else:
            self.get_file_upload(self.upload_first_file, "modules/Testing_document.png")
            self.page.wait_for_timeout(2000)
            self.btn_upload_first_file.click()
            self.get_file_upload(self.btn_upload_second_file, "modules/Testing_document.png")
            self.btn_upload_second_file.click()

    def fillup_account_information(
        self,
        last_name,
        first_name,
        middle_name,
        position,
        contact_mobile_number,
        contact_email,
        contact_username,
        contact_password,
        confirm_password
    ):
        log.info("-----Filling up Account Information-----")
        self.playwright_fw.text_fill(self.txt_account_last_name, last_name)
        self.playwright_fw.text_fill(self.txt_account_first_name, first_name)
        self.playwright_fw.text_fill(self.txt_account_middle_name, middle_name)
        self.playwright_fw.text_fill(self.txt_position, position)
        self.playwright_fw.text_fill(self.txt_account_mobile_number, contact_mobile_number)
        self.playwright_fw.text_fill(self.txt_account_email, contact_email)
        self.playwright_fw.text_fill(self.txt_account_username, contact_username)
        self.playwright_fw.text_fill(self.txt_account_password, contact_password)
        self.playwright_fw.text_fill(self.txt_confirm_password, confirm_password)
        self.btn_confirm_details.click()

    def fillup_otp_registration(self):
        log.info("-----Filling up OTP Number-----")
        self.btn_submit_registration.click()
        self.btn_registration_proceed.click()
        self.page.wait_for_timeout(10000)
        otp = get_otp_from_db()
        self.txt_input_otp.type(f"{otp}")
        self.btn_submit_otp.click()
        self.btn_okay_pending.click()

    # @staticmethod
    # def test_connection():
    #     otp = get_otp_from_db()
    #     log.info(f"DATA: {otp}")

    def get_file_upload(self, locator: Locator, file_path: str):
        # Find the file input element within the dropzone container
        # Dropzone divs typically contain a hidden input[type=file]

        with self.page.expect_file_chooser() as fc_info:
            locator.click()
            file_chooser = fc_info.value
            file_chooser.set_files(file_path)
            self.page.wait_for_timeout(2000)