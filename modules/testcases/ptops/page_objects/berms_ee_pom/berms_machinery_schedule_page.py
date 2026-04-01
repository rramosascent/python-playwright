from playwright.sync_api import Page, Locator
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.custom_logger import log

class BermsMachinerySchedulePage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_fw = FrameWorkPWDriver(self.page)
        # Machinery/Equipment List 
        self.btn_add_machinery = page.locator("#btnAddMachineryEquipment:visible")
        self.txt_machinery_description = page.locator("#itemDescription")
        self.txt_machinery_quantity = page.locator("#itemQty")
        self.txt_machinery_unit_price = page.locator("#itemUnitCost")
        self.opt_machinery_source = page.locator("#select2-itemSource-container")
        self.btn_add_machinery_save = page.locator("(//button[@id='btnAddMachineryEquipment'])[2]")

         # Raw Material/Semi Finished Product
        self.btn_add_raw_material = page.locator("#btnAddRawMaterial:visible")
        self.txt_raw_material_description = page.locator("#productDescription")
        self.opt_raw_material_source = page.locator("#select2-productSource-container")
        self.btn_add_raw_material_save = page.locator("(//button[@id='btnAddRawMaterial'])[2]")

         # Production Schedule 
        self.txt_no_of_shifts = page.locator("(//input[@id='prodSchedShifts0'])[1]")
        self.txt_no_of_hours = page.locator("(//input[@id='prodSchedHourShifts0'])[1]")
        self.txt_no_of_operating_days = page.locator("(//input[@id='prodSchedDaysMonth0'])[1]")

        self.btn_proceed_machinery_schedule = page.locator("//div[@id='machinery-and-production-schedule']//div[@class='row mt-3']//div[@class='col-12 d-flex justify-content-between align-items-center section-footer']//div//button[@type='button']")


    def fillup_berms_machinery_schedule(
        self,
        machinery_description: str,
        machinery_quantity: str,
        machinery_unit_price: str,
        machinery_source: str,
        raw_material_description: str,
        raw_material_source: str,
        no_of_shifts: str,
        no_of_hours: str,
        no_of_operating_days: str
    ):
        log.info("-----Filling up Berms Machinery, Raw Material Production Schedule-----")
        log.info("Clicking Add Machinery/Equipment in the list")
        self.btn_add_machinery.click()
        log.info("Filling up Item Description")
        self.playwright_fw.text_fill(self.txt_machinery_description, machinery_description)
        log.info("Filling up Quantity")
        self.playwright_fw.text_fill(self.txt_machinery_quantity, machinery_quantity)
        log.info("Filling up Unit Cost (PHP)")
        self.playwright_fw.text_fill(self.txt_machinery_unit_price, machinery_unit_price)
        log.info("Selecting Source")
        self.playwright_fw.dropdown_select_option(self.opt_machinery_source, machinery_source)
        log.info("Clicking Add and Save Machinery/Equipment")
        self.btn_add_machinery_save.click()

        log.info("Clicking Add Raw Material in the list")
        self.btn_add_raw_material.click()
        log.info("Filling up Item Description")
        self.playwright_fw.text_fill(self.txt_raw_material_description, raw_material_description)
        log.info("Selecting Source")
        self.playwright_fw.dropdown_select_option(self.opt_raw_material_source, raw_material_source)
        log.info("Clicking Add and Save Raw Material")
        self.btn_add_raw_material_save.click()

        log.info("Filling up Production Schedule")
        self.playwright_fw.text_fill(self.txt_no_of_shifts, no_of_shifts)
        self.playwright_fw.text_fill(self.txt_no_of_hours, no_of_hours)
        self.playwright_fw.text_fill(self.txt_no_of_operating_days, no_of_operating_days)
        
        log.info("Clicking Save and Proceed button")
        self.btn_proceed_machinery_schedule.click()

    # def dropdown_select_option(self, locator: Locator, option: str):
    #     # expect(self.page.get_by_role("option", name=option)).to_be_visible()
    #     self.page.wait_for_timeout(2000)
    #     locator.click()
    #     self.page.get_by_role("option", name=option).click()