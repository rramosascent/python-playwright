from playwright.sync_api import Page, Locator
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.custom_logger import log


class BermsExistingBusinessPage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_fw = FrameWorkPWDriver(self.page)

        self.txt_registration_number = page.locator("input[name='businessRegInfoAppsBean[0].reg_no']")
        self.txt_sec_primary_purpose = page.locator("#secPrimaryPurpose")
        self.txt_authorized_amount = page.locator("#authorizedAmount")
        self.txt_subscribed_amount = page.locator("#subscribeAmount")
        self.txt_paid_up_amount = page.locator("#paidUpAmount")
        self.btn_proceed = page.locator("div[id='existing-business-registration'] div[class='row mt-3'] div[class='col-12 d-flex justify-content-between align-items-center section-footer'] div button[type='button']")
        self.txt_date = page.locator("//input[@name='businessRegInfoAppsBean[0].date_registered']")

    # def fillup_berms_existing_business(self):
    #     log.info("-----Filling up Berms Existing Business Registration-----")
    #     log.info("Filling up Date of business registration")
    #     self.get_by_date_picker("Securities & Exchange", "DD-MMM-YYYY", "2026-02-22")
    #     log.info("Filling up Date of registration number")
    #     self.playwright_fw.text_fill(self.txt_registration_number, "13254")
    #     log.info("Filling up Sec Primary Purpose")
    #     self.playwright_fw.text_fill(self.txt_sec_primary_purpose, "test 101")
    #     log.info("Filling up Authorized Amount (PHP)")
    #     self.playwright_fw.text_fill(self.txt_authorized_amount, "1")
    #     log.info("Filling up Subscribe Amount (PHP)")
    #     self.playwright_fw.text_fill(self.txt_subscribed_amount, "1")
    #     log.info("Paid-up Amount (PHP):")
    #     self.playwright_fw.text_fill(self.txt_paid_up_amount, "1")
    #     log.info("Clicking Save and Proceed Button")
    #     self.btn_proceed.click()

    def fillup_berms_existing_business(
        self,
        date: str,
        registration_number: str,
        sec_primary_purpose: str,
        authorized_amount: str,
        subscribed_amount: str,
        paid_up_amount: str
    ):
        log.info("-----Filling up Berms Existing Business Registration-----")
        log.info("Filling up Date of business registration")
        self.txt_date.click()
        self.txt_date.type(date)
        # self.get_by_date_picker("Securities & Exchange", "DD-MMM-YYYY", date)
        log.info("Filling up Date of registration number")
        self.playwright_fw.text_fill(self.txt_registration_number, registration_number)
        log.info("Filling up Sec Primary Purpose")
        self.playwright_fw.text_fill(self.txt_sec_primary_purpose, sec_primary_purpose)
        log.info("Filling up Authorized Amount (PHP)")
        self.playwright_fw.text_fill(self.txt_authorized_amount, authorized_amount)
        log.info("Filling up Subscribe Amount (PHP)")
        self.playwright_fw.text_fill(self.txt_subscribed_amount, subscribed_amount)
        log.info("Paid-up Amount (PHP):")
        self.playwright_fw.text_fill(self.txt_paid_up_amount, paid_up_amount)
        log.info("Clicking Save and Proceed Button")
        self.btn_proceed.click()

# Date picker
    def get_by_date_picker(self, locatorName, placeholder, date):
        self.page.get_by_role("row", name=locatorName).get_by_placeholder(placeholder).fill(date)

# # Registration Number
#     def fillup_registration_number(self, locator: Locator, regNo ):
#         locator.click()
#         locator.fill(regNo)
#         locator.press("Tab")

