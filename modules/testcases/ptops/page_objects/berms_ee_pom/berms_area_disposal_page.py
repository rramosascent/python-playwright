from playwright.sync_api import Page, Locator
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.custom_logger import log

class BermsAreaDisposalPage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_fw = FrameWorkPWDriver(self.page)
        self.txt_area_sqm = page.locator("(//input[@id='total_area_sqm'])[1]")
        self.opt_location_zone = page.locator("(//span[@id='select2-zoneId-container'])[1]")

        # Zone Address
        self.opt_zone_region = page.locator("(//span[@id='select2-zone_addressRegionId-container'])[1]")
        self.opt_zone_province = page.locator("(//span[@id='select2-zone_addressProvinceId-container'])[1]")
        self.opt_zone_city_municipality = page.locator("(//span[@id='select2-zone_addressCityId-container'])[1]")
        self.opt_zone_barangay = page.locator("(//span[@id='select2-zone_addressBarangayId-container'])[1]")
        self.txt_zone_street_name = page.locator("(//input[@name='activity.street_name'])[1]")

        # Owner of the building
        self.txt_building_owner_first_name = page.locator("(//input[@id='unitOwnerFirstname'])[1]")
        self.txt_building_owner_middle_name = page.locator("(//input[@id='unitOwnerMiddlename'])[1]")
        self.txt_building_owner_last_name = page.locator("(//input[@id='unitOwnerLastname'])[1]")

        # Owner of the lot
        self.txt_lot_owner_first_name = page.locator("(//input[@id='lotOwnerFirstname'])[1]")
        self.txt_lot_owner_middle_name = page.locator("(//input[@id='lotOwnerMiddlename'])[1]")
        self.txt_lot_owner_last_name = page.locator("(//input[@id='lotOwnerLastname'])[1]")

        # Lessor of the bldg/area
        self.txt_lessor_first_name = page.locator("(//input[@id='lessorFirstname'])[1]")
        self.txt_lessor_middle_name = page.locator("(//input[@id='lessorMiddlename'])[1]")
        self.txt_lessor_last_name = page.locator("(//input[@id='lessorLastname'])[1]")

        # Utilities Requirement
        self.txt_water = page.locator("(//input[@id='water_yr_req'])[1]")
        self.txt_electricity = page.locator("(//input[@id='electric_yr_req'])[1]")

        # Waste and System Disposal
        self.txt_waste_products_description = page.locator("(//textarea[@id='waste_disposal_desc'])[1]")
        self.txt_waste_discussion_disposal = page.locator("(//textarea[@id='waste_disposal_method_desc'])[1]")
        self.upload_waste_description_docs = page.locator("(//div[@id='activity_wasteproducts_supporting_documentsDropzone'])[1]")
        self.upload_waste_disposal_docs = page.locator("(//div[@id='activity_generatedwaste_supporting_documentsDropzone'])[1]")

        self.btn_proceed_area_utilities_waste_disposal = page.locator("//div[@id='area-disposable-waste-disposal']//div[@class='row mt-3']//div[@class='col-12 d-flex justify-content-between align-items-center section-footer']//div//button[@type='button']")


    def fillup_berms_area_disposal(
        self,
        area_sqm: str,
        location_zone: str,
        zone_region: str,
        zone_province: str,
        zone_city_municipality: str,
        zone_barangay: str,
        zone_street_name: str,
        building_owner_first_name: str,
        building_owner_middle_name: str,
        building_owner_last_name: str,
        lot_owner_first_name: str,
        lot_owner_middle_name: str,
        lot_owner_last_name: str,
        lessor_first_name: str,
        lessor_middle_name: str,
        lessor_last_name: str,
        water: str,
        electricity: str,
        waste_products_description: str,
        waste_discussion_disposal: str,
        upload_waste_description_docs: str,
        upload_waste_disposal_docs: str
    ):
        log.info("-----Filling up Berms Area, Utilities and Waste Disposal-----")
        log.info("Filling up Area (sq.m.)")
        self.playwright_fw.text_fill(self.txt_area_sqm, area_sqm)
        log.info("Selecting Location/Zone/IT Building/IT Center")
        self.playwright_fw.dropdown_select_option(self.opt_location_zone, location_zone)

        log.info("Selecting REGION")
        self.playwright_fw.dropdown_select_option(self.opt_zone_region, zone_region)
        log.info("Selecting PROVINCE")
        self.playwright_fw.dropdown_select_option(self.opt_zone_province, zone_province)
        log.info("Selecting CITY/MUNICIPALITY")
        self.playwright_fw.dropdown_select_option(self.opt_zone_city_municipality, zone_city_municipality)
        log.info("Selecting BARANGAY")
        self.playwright_fw.dropdown_select_option(self.opt_zone_barangay, zone_barangay)
        log.info("Filling up STREET NAME")
        self.playwright_fw.text_fill(self.txt_zone_street_name, zone_street_name)

        log.info("Filling up Owner of the Building")
        self.playwright_fw.text_fill(self.txt_building_owner_first_name, building_owner_first_name)
        self.playwright_fw.text_fill(self.txt_building_owner_middle_name, building_owner_middle_name)
        self.playwright_fw.text_fill(self.txt_building_owner_last_name, building_owner_last_name)
        log.info("Filling up Owner of the Lot")
        self.playwright_fw.text_fill(self.txt_lot_owner_first_name, lot_owner_first_name)
        self.playwright_fw.text_fill(self.txt_lot_owner_middle_name, lot_owner_middle_name)
        self.playwright_fw.text_fill(self.txt_lot_owner_last_name, lot_owner_last_name)
        log.info("Filling up Lessor of the Bldg/Area")
        self.playwright_fw.text_fill(self.txt_lessor_first_name, lessor_first_name)
        self.playwright_fw.text_fill(self.txt_lessor_middle_name, lessor_middle_name)
        self.playwright_fw.text_fill(self.txt_lessor_last_name, lessor_last_name)
        log.info("Filling up Water (cu.m/yr)")
        self.playwright_fw.text_fill(self.txt_water, water)
        log.info("Filling up Electricity (kwhr/yr)")
        self.playwright_fw.text_fill(self.txt_electricity, electricity)
        log.info("Filling up Description and quantity of waste products")
        self.playwright_fw.text_fill(self.txt_waste_products_description, waste_products_description)
        log.info("Filling up Discussion on the methods of treatment and disposal of generated wastes")
        self.playwright_fw.text_fill(self.txt_waste_discussion_disposal, waste_discussion_disposal)
        log.info("Uploading of image of Description and quantity of waste products")
        self.get_file_upload(self.upload_waste_description_docs, upload_waste_description_docs)
        log.info("Uploading of image of Discussion on the methods of treatment and disposal of generated wastes")
        self.get_file_upload(self.upload_waste_disposal_docs, upload_waste_disposal_docs)
        
        log.info("Clicking Save and Proceed button")
        self.btn_proceed_area_utilities_waste_disposal.click()

#     def dropdown_select_option(self, locator: Locator, option: str):
#         # expect(self.page.get_by_role("option", name=option)).to_be_visible()
#         self.page.wait_for_timeout(2000)
#         locator.click()
#         self.page.get_by_role("option", name=option).click()

    def get_file_upload(self, locator: Locator, file_path: str):
        # Find the file input element within the dropzone container
        # Dropzone divs typically contain a hidden input[type=file]

        with self.page.expect_file_chooser() as fc_info:
            locator.click()
            file_chooser = fc_info.value
            file_chooser.set_files(file_path)
            self.page.wait_for_timeout(2000)