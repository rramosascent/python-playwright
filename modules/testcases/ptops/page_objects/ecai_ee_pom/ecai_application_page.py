from playwright.sync_api import Page, Locator
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.custom_logger import log
import os
import csv
import json

class EcaiApplicationPage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_fw = FrameWorkPWDriver(self.page)
        self._opt_application_type = page.locator("(//span[@id='select2-applicationType-container'])[1]")
        self._opt_zone_location = page.locator("(//span[@id='select2-zoneId-container'])[1]")
        self._opt_enterprise_type = page.locator("#select2-enterpriseTypeId-container")
        self.chbox_registered_activities = page.locator("(//td[@class='text-center dtr-control'])[1]")
        self.btn_add_ecai_item = page.locator("(//button[@class='btn btn-outline-primary-blue btn-primary addItemBtn'])[1]")
        self.btn_upload_items = page.locator("(//button[@class='btn btn-outline-primary-blue btn-primary uploadItemBtn'])[1]")
        self.upload_input_files = page.locator("(//input[@id='file'])[1]")
        self.btn_upload = page.locator("(//button[normalize-space()='Upload'])[1]")

        # Add Item Modal
        self.txt_item_code = page.locator("(//input[@id='itemCodeId'])[1]")
        self.txt_item_description = page.locator("(//textarea[@id='itemDescription'])[1]")
        self.opt_ahtn_code = page.locator("(//span[@id='select2-ahtnCodeId-container'])[1]")
        self.txt_search_box_ahtn_code = page.locator("(//input[@role='searchbox'])[1]")
        self.txt_loa_number = page.locator("(//input[@id='loaNumber'])[1]")
        self.dt_loa_validity_date = page.locator("(//input[@id='loaValidityDate'])[1]")
        self.txt_generic_category = page.locator("(//textarea[@id='itemsRequested'])[1]")
        self.opt_nature_of_import = page.locator("(//span[@id='select2-natureOfImportId-container'])[1]")
        self.btn_save_item = page.locator("(//button[@id='btnSubmit'])[1]")

        self.btn_submit_application = page.locator("(//button[@id='btnSubmitApplication'])[1]")
        self.btn_proceed = page.locator("(//button[normalize-space()='Proceed'])[1]")
        self.btn_proceed_to_payment = page.locator("(//button[normalize-space()='Proceed to Payment'])[1]")
        self.btn_proceed_confirmation_payment = page.locator("(//button[normalize-space()='Proceed'])[1]")
        self.btn_ok_successful = page.locator("button.swal2-confirm.btn.btn-primary:visible")

        self.lbl_id = page.locator("(//td)[2]")


    def fillup_ecai_application(
            self,
            application_type: str,
            zone_location: str,
            enterprise_type: str
    ):
        log.info("-----Filling up ECAI Application-----")
        log.info("Selecting Application Type")
        self.playwright_fw.dropdown_select_option(self._opt_application_type, application_type)
        log.info("Selecting Zone Location")
        self.playwright_fw.dropdown_select_option(self._opt_zone_location, zone_location)
        log.info("Selecting Enterprise Type")
        self.playwright_fw.dropdown_select_option(self._opt_enterprise_type, enterprise_type)
        log.info("Selecting and clicking Registered Activities")
        self.chbox_registered_activities.click()
        log.info("Clicking Add item button")

    def fillup_item(
            self,
            item_code: str,
            item_description: str,
            search_box_ahtn_code: str,
            loa_number: str,
            loa_validity_date: str,
            generic_category: str,
            opt_nature_of_import: str
    ):
        log.info("-----Filling up ECAI item-----")
        self.btn_add_ecai_item.click()
        log.info("Filling up Item Code")
        self.playwright_fw.text_fill(self.txt_item_code, item_code)
        log.info("Filling up Item Description")
        self.playwright_fw.text_fill(self.txt_item_description, item_description)
        log.info("Clicking AHTN Code")
        self.opt_ahtn_code.click()
        log.info("Search for AHTN Code")
        self.playwright_fw.text_fill(self.txt_search_box_ahtn_code, search_box_ahtn_code)
        self.page.wait_for_timeout(3000)
        log.info("Select and enter AHTN Code")
        self.page.keyboard.press("Enter")
        log.info("Filling up Loa number")
        self.playwright_fw.text_fill(self.txt_loa_number, loa_number)
        log.info("Filling up LOA Validity Date")
        self.playwright_fw.text_fill(self.dt_loa_validity_date, loa_validity_date)
        # self.dt_loa_validity_date.fill("2027-03-22")
        log.info("Filling up Generic Category")
        self.playwright_fw.text_fill(self.txt_generic_category, generic_category)
        log.info("Selecting Nature of Import")
        self.playwright_fw.dropdown_select_option(self.opt_nature_of_import, opt_nature_of_import)
        log.info("Clicking Save button")
        self.btn_save_item.click()

    # def fillup_ecai_application(self):
    #     log.info("-----Filling up ECAI Application-----")
    #     log.info("Selecting Application Type")
    #     self.playwright_fw.dropdown_select_option(self._opt_application_type, "SUPPLEMENTAL")
    #     log.info("Selecting Zone Location")
    #     self.playwright_fw.dropdown_select_option(self._opt_zone_location, "[MHCP] McKinley Hill Cyberpark")
    #     log.info("Selecting Enterprise Type")
    #     self.playwright_fw.dropdown_select_option(self._opt_enterprise_type, "Domestic Market")
    #     log.info("Selecting and clicking Registered Activities")
    #     self.chbox_registered_activities.click()
    #     log.info("Clicking Add item button")

    # def fillup_item(self):
    #     log.info("-----Filling up ECAI item-----")
    #     self.btn_add_ecai_item.click()
    #     log.info("Filling up Item Code")
    #     self.playwright_fw.text_fill(self.txt_item_code, "qc001")
    #     log.info("Filling up Item Description")
    #     self.playwright_fw.text_fill(self.txt_item_desciption, "description 001")
    #     log.info("Clicking AHTN Code")
    #     self.opt_ahtn_code.click()
    #     log.info("Search for AHTN Code")
    #     self.playwright_fw.text_fill(self.txt_search_box_ahtn_code, "123")
    #     self.page.wait_for_timeout(2000)
    #     log.info("Select and enter AHTN Code")
    #     self.page.keyboard.press("Enter")
    #     log.info("Filling up Loa number")
    #     self.playwright_fw.text_fill(self.txt_loa_number, "123456")
    #     log.info("Filling up LOA Validity Date")
    #     self.playwright_fw.text_fill(self.dt_loa_validity_date, "2027-03-22")
    #     # self.dt_loa_validity_date.fill("2027-03-22")
    #     log.info("Filling up Generic Category")
    #     self.playwright_fw.text_fill(self.txt_generic_category, "test 101")
    #     log.info("Selecting Nature of Import")
    #     self.playwright_fw.dropdown_select_option(self.opt_nature_of_import, "[ADH] Adhesive")
    #     log.info("Clicking Save button")
    #     self.btn_save_item.click()

    def proceed_to_payment(self):
        log.info("Clicking submit application button")
        self.page.wait_for_timeout(5000)
        self.btn_submit_application.click()
        log.info("Clicking proceed button")
        self.btn_proceed.click()
        log.info("Clicking proceed to payment button")
        self.btn_proceed_to_payment.click()
        log.info("Clicking proceed confirmation button")
        self.btn_proceed_confirmation_payment.click()
        # self.get_value_application_id()
        log.info("Clicking OK button")
        self.btn_ok_successful.click()

    def upload_multiple_items(self):
        log.info("Clicking Upload Items button")
        self.btn_upload_items.click()
        log.info("Uploading items...")
        self.playwright_fw.get_file_upload(self.upload_input_files, "modules/test_data/ECAI-Template-500-Items.xlsx")
        log.info("Clicking upload button")
        self.btn_upload.click()
        # self.wait_for_preloader()

    def get_value_application_id(self):
        self.page.wait_for_timeout(3000)
        label = self.lbl_id.inner_text()

        self.save_to_csv(label)
        # self.save_to_json(label)

# Date picker
    def get_by_date_picker(self, locatorName, placeholder, date):
        self.page.get_by_role("row", name=locatorName).get_by_placeholder(placeholder).fill(date)

    # def wait_for_preloader(self):
    #     try:
    #         self.page.wait_for_function(
    #         "document.querySelector('#preloader')?.getAttribute('aria-hidden') === 'true'",
    #         timeout=20000
    #     )
    #     except:
    #     # Fallback: wait until element is detached
    #         self.page.wait_for_selector("#preloader", state="detached", timeout=20000)
    
    @staticmethod
    def save_to_csv(ecai_id_value, filename="ecai_ee_id.csv"):
        # If file doesn't exist, write header first
        file_exists = os.path.exists(filename)

        with open(filename, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["ecai_id_value"])  # header
            writer.writerow([ecai_id_value])

    # def save_to_csv(ecai_id_value, ecai_ee_type_value, filename="ecai_ee_id.csv"):
    #     # If file doesn't exist, write header first
    #     file_exists = os.path.exists(filename)
    #
    #     with open(filename, "a", newline="") as f:
    #         writer = csv.writer(f)
    #         if not file_exists:
    #             writer.writerow(["ecai_id_value", "ecai_ee_type_value"])  # header
    #         writer.writerow([ecai_id_value, ecai_ee_type_value])

    # def save_to_json(label_value, filename="applicationId.json"):
    #     # Load existing file if it exists
    #     if os.path.exists(filename):
    #         with open(filename, "r") as f:
    #             data = json.load(f)
    #     else:
    #         data = {"labels": []}

    #     # Append new value
    #     data["labels"].append(label_value)

    #     # Save back
    #     with open(filename, "w") as f:
    #         json.dump(data, f, indent=4)

