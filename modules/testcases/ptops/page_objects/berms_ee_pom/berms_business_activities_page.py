from playwright.sync_api import Page, Locator
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.custom_logger import log

class BermsBusinessActivitiesPage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_fw = FrameWorkPWDriver(self.page)
        self.opt_proposed_product_activity = page.locator("#select2-proposedBusinessActivity-container") # Updated from span to id
        self.txt_proposed_product_activity = page.locator("(//input[@id='proposedBusinessActivity'])[1]")
        self.txt_description = page.locator("#description")
        self.txt_uses_application = page.locator("#business_prod_service_application")
        self.upload_image_product = page.locator("#activity_product_img_documentsDropzone")
        self.btn_proceed = page.get_by_role("button", name="Proceed")

    # def fillup_berms_business_activities(self):
    #     log.info("-----Filling up Berms Business Product Activities-----")
    #     log.info("Selecting Proposed Product/Activity")
    #     self.playwright_fw.dropdown_select_option(self.opt_proposed_product_activity, "Proposed Product/Activity 001") # Proposed Product/Activity 001, CBGC
    #     log.info("Filling up Description")
    #     self.txt_description.fill("test 101")
    #     log.info("Filling up Uses/Application")
    #     self.txt_uses_application.fill("test 101")
    #     log.info("Uploading Image of the Product")
    #     self.playwright_fw.get_file_upload(self.upload_image_product, "modules/test_data/Testing_document.png")
    #     log.info("Clicking Proceed Button")
    #     self.btn_proceed.click()

    def fillup_berms_business_activities(
        self,
        proposed_product_activity: str,
        description: str,
        uses_application: str,
        upload_image_product: str
    ):
        log.info("-----Filling up Berms Business Product Activities-----")
        log.info("Selecting Proposed Product/Activity")
        # self.playwright_fw.text_fill(self.txt_proposed_product_activity, proposed_product_activity)
        self.playwright_fw.dropdown_select_option(self.opt_proposed_product_activity, proposed_product_activity) # Proposed Product/Activity 001, CBGC
        log.info("Filling up Description")
        self.txt_description.fill(description)
        log.info("Filling up Uses/Application")
        self.txt_uses_application.fill(uses_application)
        log.info("Uploading Image of the Product")
        # self.playwright_fw.get_file_upload(self.upload_image_product, upload_image_product)
        self.get_file_upload(self.upload_image_product, upload_image_product)
        log.info("Clicking Proceed Button")
        self.btn_proceed.click()

    def get_file_upload(self, locator: Locator, file_path: str):
        # Find the file input element within the dropzone container
        # Dropzone divs typically contain a hidden input[type=file]

        with self.page.expect_file_chooser() as fc_info:
            locator.click()
            file_chooser = fc_info.value
            file_chooser.set_files(file_path)
            self.page.wait_for_timeout(2000)