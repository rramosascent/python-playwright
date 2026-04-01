from playwright.sync_api import Page, expect
from modules.frame_work.utility.custom_logger import log

class EcaiDtPage:
    def __init__(self, page: Page):
        self.page = page
        self._btn_new_application = page.locator("(//a[normalize-space()='New Application'])[1]")

    def click_new_application(self):
        log.info("Clicking New ECAI Application")
        expect(self._btn_new_application).to_be_visible(timeout=5000)
        self._btn_new_application.click()
        