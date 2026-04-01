from playwright.sync_api import Page, Locator
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.custom_logger import log

class BermsManufacturingFlowPage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_fw = FrameWorkPWDriver(self.page)
        self.txt_manufacturing_process_service_flow = page.locator("#manufacturing_process_service_flow_id")
        self.upload_product_image = page.locator("#addtlInfo_supporting_documentsDropzone")
        self.btn_proceed_manufacturing_process_service_flow = page.locator("div[id='manufacturing-process-and-service-flow'] div[class='row mt-3'] div[class='col-12 d-flex justify-content-between align-items-center section-footer'] div button[type='button']")

    def fillup_berms_manufacturing_flow(
        self,
        manufacturing_process_service_flow: str,
        upload_product_image: str
    ):
        log.info("-----Filling up Berms Manufacturing Process and Service Flow-----")
        log.info("Filling up MANUFACTURING PROCESS/SERVICE FLOW")
        self.playwright_fw.text_fill(self.txt_manufacturing_process_service_flow, manufacturing_process_service_flow)
        log.info("Uploading Image FOR DIAGRAM/PROCESS/FLOW")
        self.get_file_upload(self.upload_product_image, upload_product_image)
        log.info("Clicking Save and Proceed button")
        self.btn_proceed_manufacturing_process_service_flow.click()


    def get_file_upload(self, locator: Locator, file_path: str):
        # Find the file input element within the dropzone container
        # Dropzone divs typically contain a hidden input[type=file]

        with self.page.expect_file_chooser() as fc_info:
            locator.click()
            file_chooser = fc_info.value
            file_chooser.set_files(file_path)
            self.page.wait_for_timeout(2000)