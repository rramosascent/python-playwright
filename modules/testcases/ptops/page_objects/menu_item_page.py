from playwright.sync_api import Page
from modules.frame_work.utility.custom_logger import log

class MenuItemsPage:
    def __init__(self, page: Page):
        self.page = page
        self.berms_application_accreditations = page.locator("//div[normalize-space()='Applications & Accreditations']")
        self.ecai_application_certificates = page.locator("(//div[contains(text(),'Applications & Certificates')])[1]")
        self.vat_zero_rating = page.locator("(//a[@href='/peza/vat/applications-certificates'])[1]")

    def navigate_to_berms_application(self):
        log.info("Navigating to Berms Applications & Accreditations")
        self.berms_application_accreditations.click()

    def navigate_to_ecai_application(self):
        log.info("Navigating to ECAI Applications & Certificates")
        self.ecai_application_certificates.click()

    def navigate_to_vat_zero_application(self):
        log.info("Navigating to Vat Zero Rating Application")
        self.vat_zero_rating.click()
