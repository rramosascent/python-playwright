from playwright.sync_api import Page, Locator
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.custom_logger import log

class BermsInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_fw = FrameWorkPWDriver(self.page)
        self.txt_company_name = page.locator("#addtlInfocompany_companyName")
        self.opt_country = page.locator("#select2-addtlInfocompany_companyCountryId-container")
        self.txt_business_nature = page.locator("#businessNatureName")
        self.txt_business_profile = page.locator("#businessCompanyProfile")
        self.txt_landline = page.locator("#representative0TelephoneNumber")
        self.btn_proceed = page.get_by_role("button", name="Proceed")

    # def fillup_berms_information(self):
    #     log.info("-----Filling up Berms Company and Personal Information-----")
    #     log.info("Filling up Company Name")
    #     self.txt_company_name.fill("Ascent")
    #     log.info("Selecting Country")
    #     self.playwright_fw.dropdown_select_option(self.opt_country, "[PH] Philippines")
    #     log.info("Filling up Business Nature")
    #     self.txt_business_nature.fill("Testing 101")
    #     log.info("Filling up Business Profile")
    #     self.txt_business_profile.fill("Testing 101")
    #     log.info("Filling up Landline")
    #     self.txt_landline.fill("912312321")
    #     log.info("Clicking Proceed Button")
    #     self.btn_proceed.click()

    def fillup_berms_information(
        self,
        company_name: str,
        country: str,
        business_nature: str,
        business_profile: str,
        landline: str
    ):
        log.info("-----Filling up Berms Company and Personal Information-----")
        log.info("Filling up Company Name")
        self.txt_company_name.fill(company_name)
        log.info("Selecting Country")
        self.playwright_fw.dropdown_select_option(self.opt_country, country)
        log.info("Filling up Business Nature")
        self.txt_business_nature.fill(business_nature)
        log.info("Filling up Business Profile")
        self.txt_business_profile.fill(business_profile)
        log.info("Filling up Landline")
        self.txt_landline.fill(landline)
        log.info("Clicking Proceed Button")
        self.btn_proceed.click()