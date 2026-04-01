from playwright.sync_api import Page, Locator, expect
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.custom_logger import log

class BermsManpowerTimetablePage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_fw = FrameWorkPWDriver(self.page)
        # self.dtp_building_construction_from = page.locator("");
        # self.dtp_building_construction_select_from = page.locator("");
        # self.dtp_building_construction_to = page.locator("");
        # self.dtp_building_construction_select_to = page.locator("");

        self.txt_service_personnel_1 = page.locator("#servicePersonnelCount0")
        self.txt_service_personnel_2 = page.locator("#servicePersonnelCount1")
        self.txt_service_personnel_3 = page.locator("#servicePersonnelCount2")

        self.txt_indirect_personnel_1 = page.locator("#indirectPersonnelCount0")
        self.txt_indirect_personnel_2 = page.locator("#indirectPersonnelCount1")
        self.txt_indirect_personnel_3 = page.locator("#indirectPersonnelCount2")

        self.txt_admin_personnel_1 = page.locator("#adminPersonnelCount0")
        self.txt_admin_personnel_2 = page.locator("#adminPersonnelCount1")
        self.txt_admin_personnel_3 = page.locator("#adminPersonnelCount2")

        self.btn_proceed_manpower_timetable = page.locator("div[id='manpower-and-timetable'] div[class='row mt-3'] div[class='col-12 d-flex justify-content-between align-items-center section-footer'] div button[type='button']")

    def fillup_berms_manpower_timetable(
        self,
        service_personnel_1: str,
        service_personnel_2: str,
        service_personnel_3: str,
        indirect_personnel_1: str,
        indirect_personnel_2: str,
        indirect_personnel_3: str,
        admin_personnel_1: str,
        admin_personnel_2: str,
        admin_personnel_3: str
    ):
        log.info("-----Filling up Berms Manpower & Timetable-----")
        log.info("Selecting Building construction/renovation date FROM")
        # Building construction/renovation
        self.get_by_timetable_picker(1)
        self.get_by_month_picker()

        log.info("Selecting Building construction/renovation date TO")
        self.get_and_click_month_picker(4)
        self.get_by_month_picker()

        # Importation/Procurement of Machinery and Equipment
        log.info("Selecting Importation/Procurement of Machinery and Equipment date FROM")
        self.get_and_click_month_picker(6)
        self.get_by_month_picker()

        log.info("Selecting Importation/Procurement of Machinery and Equipment date TO")
        self.get_and_click_month_picker(8)
        self.get_by_month_picker()

        # Installation of machinery/equipment
        log.info("Selecting Installation of machinery/equipment date FROM")
        self.get_and_click_month_picker(10)
        self.get_by_month_picker()

        log.info("Selecting Installation of machinery/equipment date TO")
        self.get_and_click_month_picker(12)
        self.get_by_month_picker()

        # Hiring/Training of Personnel
        log.info("Selecting Hiring/Training of Personnel date FROM")
        self.get_and_click_month_picker(14)
        self.get_by_month_picker()

        log.info("Selecting Hiring/Training of Personnel date TO")
        self.get_and_click_month_picker(16)
        self.get_by_month_picker()

        # Start of Commercial Operations
        log.info("Selecting Start of Commercial Operations date FROM")
        self.get_and_click_month_picker(18)
        self.get_by_month_picker()

        log.info("-----Filling up Berms Manpower Requirement-----")
        log.info("-----Filling up Service Personnel-----")
        self.fill_manpower_requirements(self.txt_service_personnel_1, service_personnel_1)
        self.fill_manpower_requirements(self.txt_service_personnel_2, service_personnel_2)
        self.fill_manpower_requirements(self.txt_service_personnel_3, service_personnel_3)

        log.info("-----Filling up Indirect Service Personnel-----")
        self.fill_manpower_requirements(self.txt_indirect_personnel_1, indirect_personnel_1)
        self.fill_manpower_requirements(self.txt_indirect_personnel_2, indirect_personnel_2)
        self.fill_manpower_requirements(self.txt_indirect_personnel_3, indirect_personnel_3)

        log.info("-----Filling up Admin Personnel-----")
        self.fill_manpower_requirements(self.txt_admin_personnel_1, admin_personnel_1)
        self.fill_manpower_requirements(self.txt_admin_personnel_2, admin_personnel_2)
        self.fill_manpower_requirements(self.txt_admin_personnel_3, admin_personnel_3)

        log.info("Clicking Save and Proceed Button")
        self.btn_proceed_manpower_timetable.click()

    def fill_manpower_requirements(self, locator: Locator, inputValue):
        locator.click()
        locator.fill(inputValue)
        locator.press("Tab")

# Timetable Picker
    def get_by_timetable_picker(self, get_by_data: int):
        # self.page.wait_for_timeout(2000)
        self.page.locator("div.col-sm-6.text-center").nth(get_by_data).wait_for(state="visible")
        # expect(self.page.locator("div.col-sm-6.text-center").locator("input").nth(get_by_data)).to_be_visible()
        self.page.locator("div.col-sm-6.text-center").locator("input").nth(get_by_data).click()

# Month Picker  
    def get_by_month_picker(self):
        # self.page.wait_for_timeout(2000)
        self.page.locator("span.flatpickr-monthSelect-month.today:visible").wait_for(state="visible")
        # expect(self.page.locator("span.flatpickr-monthSelect-month.today:visible")).to_be_visible()
        self.page.locator("span.flatpickr-monthSelect-month.today:visible").click()

# February 1, 2026
    def get_and_click_month_picker(self, get_by_data: int):
        # self.page.wait_for_timeout(1000)
        # self.page.locator(f"(//input[@placeholder='MMM-YYYY'])[{get_by_data}]").nth(get_by_data).wait_for(state="visible")
        expect(self.page.locator(f"(//input[@placeholder='MMM-YYYY'])[{get_by_data}]")).to_be_visible()
        self.page.locator(f"(//input[@placeholder='MMM-YYYY'])[{get_by_data}]").click()

