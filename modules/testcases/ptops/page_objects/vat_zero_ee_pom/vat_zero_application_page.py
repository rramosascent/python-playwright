from openpyxl.worksheet import page
from playwright.sync_api import Page, Locator
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.custom_logger import log
import os
import csv
import json

class VatApplicationPage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_fw = FrameWorkPWDriver(self.page)
        self.opt_type_of_request = page.locator("(//span[@id='select2-requestTypeId-container'])[1]")
        self.opt_coverage_period = page.locator("(//select[@id='coveragePeriodId'])[1]")
        self.opt_responsible_officer = page.locator("(//span[@id='select2-responsibleOfficerId-container'])[1]")

        # Add Officer
        self.btn_new_officer = page.locator("(//span[@id='select2-responsibleOfficerId-container'])[1]")
        self.txt_name = page.locator("(//input[@id='name_officer'])[1]")
        self.txt_position = page.locator("(//input[@id='position_officer'])[1]")
        self.txt_contact_no = page.locator("(//input[@id='number_officer'])[1]")
        self.txt_email_address = page.locator("(//input[@id='email_address_officer'])[1]")
        self.txt_alternative_email_address = page.locator("(//input[@id='email_address_alternative_officer'])[1]")
        self.btn_add = page.locator("(//button[normalize-space()='Add'])[1]")
        self.btn_proceed_to_add_officer = page.locator("(//button[normalize-space()='Proceed'])[1]")
        self.btn_ok_add_officer = page.locator("(//button[normalize-space()='OK'])[1]")

        self.chkbox_add_registered_activities = page.locator("(//td[@class='text-center sorting_1'])[1]")
        self.txt_tin = page.locator("//tbody/tr[1]/td[5]/input[1]")

        self.upload_sales_summary = page.locator("//div[@class='supporting-doc-item item_cl_esd']//div[@class='col-md-4 col-xxl-4 py-3 ']")
        self.upload_notarized_undertaking = page.locator("//div[@class='supporting-doc-item item_nu_do']//div[contains(@class,'col-md-4 col-xxl-4 py-3')]")

        self.radio_btn = page.locator("(//input[@id='vatCheckbox'])[1]")

        self.btn_submit_application = page.locator("(//button[@id='btnSubmitApplication'])[1]")
        self.btn_proceed_to_submit = page.locator("(//button[normalize-space()='Proceed'])[1]")
        self.btn_ok_application = page.locator("(//button[normalize-space()='OK'])[1]")
        self.btn_close = page.locator("(//a[contains(text(),'Close')])[1]")
        self.lbl_vat_id_application = page.locator("//div[@id='confirmationQrCodeWrapper']//div//div[@class='text-center fw-semibold fs-3']")

    def fillup_vat_application(
            self,
            application_type: str,
            responsible_officer: str,
            tin: str,
            sales_summary: str,
            notarized_undertaking: str
    ):
        log.info("-----Filling up VAT ZERO RATING Application-----")
        self.page.wait_for_timeout(2000)
        self.opt_type_of_request.click()
        self.select_type_of_request(application_type)
        self.opt_coverage_period.click()
        self.playwright_fw.dropdown_select_option(self.opt_responsible_officer, responsible_officer)
        self.chkbox_add_registered_activities.click()
        # self.txt_tin.click()
        self.txt_tin.type(tin)
        self.get_file_upload(self.upload_sales_summary, sales_summary)
        self.get_file_upload(self.upload_notarized_undertaking, notarized_undertaking)
        self.radio_btn.click()
        self.btn_submit_application.click()
        self.btn_proceed_to_submit.click()
        self.btn_ok_application.click()
        self.get_value_application_id()
        self.btn_close.click()

    def select_type_of_request(self, type_of_request):
        if type_of_request == "NEW":
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")
        else:
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")

    def get_value_application_id(self):
        self.page.wait_for_timeout(3000)
        label = self.lbl_vat_id_application.inner_text()

        self.save_to_csv(label)

    @staticmethod
    def save_to_csv(vat_id_value, filename="vat_ee_id.csv"):
        # If file doesn't exist, write header first
        file_exists = os.path.exists(filename)

        with open(filename, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["vat_id_value"])  # header
            writer.writerow([vat_id_value])

    def get_file_upload(self, locator: Locator, file_path: str):
        # Find the file input element within the dropzone container
        # Dropzone divs typically contain a hidden input[type=file]

        with self.page.expect_file_chooser() as fc_info:
            locator.click()
            file_chooser = fc_info.value
            file_chooser.set_files(file_path)
            self.page.wait_for_timeout(2000)