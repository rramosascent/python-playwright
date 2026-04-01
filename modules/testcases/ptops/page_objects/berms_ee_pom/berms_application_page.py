from playwright.sync_api import Page
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.custom_logger import log

class BermsApplicationPage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_fw = FrameWorkPWDriver(self.page)
        self._opt_type_of_application = page.locator("#select2-applicationTypeId-container")
        self._opt_section_code = page.locator("#select2-sectionCodeId-container")
        self._opt_division_code = page.locator("#select2-divisionCodeId-container")
        self._opt_groups_code = page.locator("#select2-groupCodeId-container")
        self._opt_classes_code = page.locator("#select2-classesCodeId-container")
        self._opt_sub_classes_code = page.locator("#select2-subClassesCodeId-container")
        self._btn_proceed = page.get_by_role("button", name="Proceed")

    # def fillup_berms_application(self):
    #     log.info("-----Filling up Berms Application-----")
    #     log.info("Selecting Type of Application")
    #     self.playwright_fw.dropdown_select_option(self._opt_type_of_application, "NEW ECOZONE ENTERPRISE")
    #     log.info("Selecting Type of Ecozone Enterprise")
    #     self.playwright_fw.rdbox_select_option("Domestic Market")
    #     log.info("Selecting Section Code")
    #     self.playwright_fw.dropdown_select_option(self._opt_section_code, "Accommodation and Food Service Activities")
    #     log.info("Selecting Division Code")
    #     self.playwright_fw.dropdown_select_option(self._opt_division_code, "[55] ACCOMMODATION")
    #     log.info("Selecting Groups Code")
    #     self.playwright_fw.dropdown_select_option(self._opt_groups_code, "[559] Other accommodation")
    #     log.info("Selecting Classes Code")
    #     self.playwright_fw.dropdown_select_option(self._opt_classes_code, "[5590] Other accommodation")
    #     log.info("Selecting Sub Classes Code")
    #     self.playwright_fw.dropdown_select_option(self._opt_sub_classes_code, "[55901] Dormitories/boarding houses")
    #     log.info("Clicking Proceed Button")
    #     self._btn_proceed.click()

    def fillup_berms_application(
        self,
        type_of_application: str,
        market: str,
        section_code: str,
        division_code: str,
        groups_code: str,
        classes_code: str,
        sub_classes_code: str
    ):
        log.info("-----Filling up Berms Application-----")
        self.playwright_fw.dropdown_select_option(self._opt_type_of_application, type_of_application)
        self.playwright_fw.rdbox_select_option(market)
        self.playwright_fw.dropdown_select_option(self._opt_section_code, section_code)
        self.playwright_fw.dropdown_select_option(self._opt_division_code, division_code)
        self.playwright_fw.dropdown_select_option(self._opt_groups_code, groups_code)
        self.playwright_fw.dropdown_select_option(self._opt_classes_code, classes_code)
        self.playwright_fw.dropdown_select_option(self._opt_sub_classes_code, sub_classes_code)
        self._btn_proceed.click()