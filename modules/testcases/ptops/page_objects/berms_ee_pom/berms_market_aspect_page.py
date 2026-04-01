from playwright.sync_api import Page, Locator, expect
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.custom_logger import log

class BermsMarketAspectPage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_fw = FrameWorkPWDriver(self.page)
        self.opt_percent_export = page.locator("(//span[@id='select2-exportPercent-container'])[1]")
        self.opt_country_of_export_market = page.locator("(//ul[@class='select2-selection__rendered'])[1]")
        self.txt_domestic_client = page.locator("(//span[@class='tagify__input'])[1]")
        self.txt_export_selling_price = page.locator("(//input[@id='export_selling_price'])[1]")
        self.txt_export_domestic_price = page.locator("[name='projectMarketAspectAppsBean.domestic_selling_price']")
        self.opt_unit_of_measure = page.locator("(//span[@id='select2-projected_volume_sales_id-container'])[1]")

        self.txt_export_volume_1 = page.locator("#export_marketAspectVolumeValue0")
        self.txt_export_volume_2 = page.locator("#export_marketAspectVolumeValue1")
        self.txt_export_volume_3 = page.locator("#export_marketAspectVolumeValue2")

        self.txt_local_market_volume_1 = page.locator("#import_marketAspectVolumeValue0")
        self.txt_local_market_volume_2 = page.locator("#import_marketAspectVolumeValue1")
        self.txt_local_market_volume_3 = page.locator("#import_marketAspectVolumeValue2")

        self.btn_proceed_market_aspect = page.locator("//div[@id='market-aspect']//div[@class='row mt-3']//div[@class='col-12 d-flex justify-content-between align-items-center section-footer']//div//button[@type='button']")

    def fillup_berms_market_aspect(
        self,
        percent_export: str,
        country_of_export_market: str,
        domestic_client: str,
        export_selling_price: str,
        export_domestic_price: str,
        unit_of_measure: str,
        export_volume_1: str,
        export_volume_2: str,
        export_volume_3: str,
        local_market_volume_1: str,
        local_market_volume_2: str,
        local_market_volume_3: str
    ):
        log.info("-----Filling up Berms Market Aspect-----")
        log.info("Selecting Percentage Export")
        self.select_percentage(self.opt_percent_export, percent_export)
        log.info("Selecting Country of Export Market")
        self.playwright_fw.dropdown_select_option(self.opt_country_of_export_market, country_of_export_market)
        log.info("Filling up Domestic Clients")
        self.playwright_fw.text_fill(self.txt_domestic_client, domestic_client)
        log.info("Filling up Export Selling Price per unit US$")
        self.playwright_fw.text_fill(self.txt_export_selling_price, export_selling_price)
        log.info("Filling up Domestic Selling Price Per Unit PHP")
        self.playwright_fw.text_fill(self.txt_export_domestic_price, export_domestic_price)
        log.info("Selecting Unit of Measure")
        self.playwright_fw.dropdown_select_option(self.opt_unit_of_measure, unit_of_measure)

        log.info("Filling Export Projected Volume and Sales Value")
        self.playwright_fw.text_fill(self.txt_export_volume_1, export_volume_1)
        self.playwright_fw.text_fill(self.txt_export_volume_2, export_volume_2)
        self.playwright_fw.text_fill(self.txt_export_volume_3, export_volume_3)

        log.info("Filling Local Projected Volume and Sales Value")
        self.playwright_fw.text_fill(self.txt_local_market_volume_1, local_market_volume_1)
        self.playwright_fw.text_fill(self.txt_local_market_volume_2, local_market_volume_2)
        self.playwright_fw.text_fill(self.txt_local_market_volume_3, local_market_volume_3)

        log.info("Clicking Save and Proceed button")
        self.btn_proceed_market_aspect.click()

# Select Percentage
    def select_percentage(self, locator: Locator, optionValue: str):
        # Click first then
        locator.wait_for(state="visible")
        # expect(locator).to_be_visible()
        locator.click()

        # select percentage
        self.page.get_by_role('option', name=optionValue).click()

    # def dropdown_select_option(self, locator: Locator, option: str):
    #     # expect(self.page.get_by_role("option", name=option)).to_be_visible()
    #     self.page.wait_for_timeout(2000)
    #     locator.click()
    #     self.page.get_by_role("option", name=option).click()

    def fill_export_local(self, locator: Locator, inputValue):
        locator.click()
        locator.fill(inputValue)
        locator.press("Tab")
