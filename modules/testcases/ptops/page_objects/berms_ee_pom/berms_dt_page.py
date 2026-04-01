from playwright.sync_api import Page, expect
from modules.frame_work.utility.custom_logger import log

class BermsDtPage:
    def __init__(self, page: Page):
        self.page = page
        self._btn_new_ecozone_enterprise = page.get_by_role("button", name="New Ecozone Enterprise")
        self.btn_register_an_ecozone = page.locator("(//button[@class='btn btn-outline-primary-blue add-new btn-primary mb-3 mb-md-0'])[1]")

    def click_new_ecozone_enterprise(self):
        log.info("Clicking New Ecozone Enterprise")
        expect(self._btn_new_ecozone_enterprise).to_be_visible(timeout=5000)
        self._btn_new_ecozone_enterprise.click()

    def click_register_an_ecozone(self):
        log.info("Clicking Register an Ecozone")
        expect(self.btn_register_an_ecozone).to_be_visible(timeout=5000)
        self.btn_register_an_ecozone.click()
        