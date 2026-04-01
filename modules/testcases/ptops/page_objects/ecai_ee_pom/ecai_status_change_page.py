from playwright.sync_api import Page, Locator, expect
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.custom_logger import log

class EcaiStatusChangePage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_fw = FrameWorkPWDriver(self.page)
        # for evaluation
        self.btn_evaluate_all_importable = page.locator("(//button[@id='btnApproveAll'])[1]")
        self.btn_proceed_evaluate_all_importable = page.locator("(//button[normalize-space()='Proceed'])[1]")
        self.btn_ok_evaluate_all_importable = page.locator("(//button[normalize-space()='OK'])[1]")

        self.btn_evaluate_application = page.locator("(//button[normalize-space()='Evaluate Application'])[1]")
        self.opt_status = page.locator("(//span[@id='select2-statusTypeId-container'])[1]")
        self.txt_remarks = page.locator("(//textarea[@id='remarksId'])[1]")
        self.btn_submit = page.locator("(//button[@id='btnScreenAppSubmit'])[1]")
        self.btn_confirm_proceed = page.locator("(//button[normalize-space()='Proceed'])[1]") # need 5-10 sec delay
        self.btn_ok = page.locator("(//button[normalize-space()='OK'])[1]")
        self.btn_close = page.locator("(//a[@class='btn btn-primary'])[1]")
        # self.lbl_application_number = page.locator("(//span[normalize-space()='AN-2519016ME'])[1]")

        self.btn_application_approval = page.locator("(//button[normalize-space()='Application Approval'])[1]")

    # To change the application number in flexible way
    def get_application_number_locator(self, application_number: str):
        return self.page.locator(f"//a[normalize-space()='{application_number}']")

    def select_application_number(self, application_number: str):
        # search then click
        log.info("Searching.....")
        log.info("Selecting the application from dashboard data table")
        self.page.locator("(//input[@aria-controls='dt_applications'])[1]").fill(application_number)
        locator = self.get_application_number_locator(application_number)
        locator.click()

    def change_status_to_evaluation(self):
        log.info("-----Evaluate the application-----")
        self.btn_evaluate_all_importable.click()
        self.btn_proceed_evaluate_all_importable.click()
        self.btn_ok_evaluate_all_importable.click()

        self.btn_evaluate_application.click()
        self.playwright_fw.dropdown_select_option(self.opt_status, "Evaluated")
        self.playwright_fw.text_fill(self.txt_remarks, "Remarks")
        self.btn_submit.click()
        self.btn_confirm_proceed.click()
        self.page.wait_for_timeout(5000)
        self.btn_ok.click()
        self.btn_close.click()

    def change_status_to_approval(self):
        log.info("-----Approval of the application-----")
        self.btn_application_approval.click()
        self.playwright_fw.dropdown_select_option(self.opt_status, "Approved")
        self.playwright_fw.text_fill(self.txt_remarks, "Remarks")
        self.btn_submit.click()
        self.btn_confirm_proceed.click()
        self.page.wait_for_timeout(5000)
        self.btn_ok.click()
        self.btn_close.click()
