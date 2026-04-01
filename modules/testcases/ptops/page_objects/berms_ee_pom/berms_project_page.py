from playwright.sync_api import Page, Locator
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.custom_logger import log

class BermsProjectPage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_fw = FrameWorkPWDriver(self.page)
        self.txt_building_construction_amount = page.locator("(//input[@name='projectCost[building_construction_renovation]'])[1]")
        self.txt_factory_tools_amount = page.locator("(//input[@name='projectCost[factory_tools]'])[1]")
        self.txt_transportation_amount = page.locator("(//input[@name='projectCost[transporation]'])[1]")
        self.txt_office_equipment_amount = page.locator("(//input[@name='projectCost[office_equipment]'])[1]")
        self.txt_other_assets_amount = page.locator("(//input[@id='otherTotal'])[1]")
        self.action_keys = page.locator("(//input[@id='otherTotal'])[1]")
        self.txt_assets_remarks = page.locator("(//input[@id='specific'])[1]")
        self.txt_pre_operating_expenses_amount = page.locator("(//input[@name='projectCost[operating_expenses]'])[1]")
        self.txt_working_capital_amount = page.locator("(//input[@name='projectCost[working_capital]'])[1]")
        self.lbl_value_of_initial_total_project_cost = page.locator("#initialTotalProjectCost:visible")
        self.txt_equity_amount = page.locator("(//input[@name='fund_source[0][amount]'])[1]")
        self.txt_additional_equity_amount = page.locator("(//input[@name='fund_source[1][amount]'])[1]")
        self.opt_advances_type_of_loan = page.locator("(//select[@id='fundSource2'])[1]")
        self.opt_loans_type_of_loan = page.locator("(//select[@id='fundSource3'])[1]")
        self.txt_advances_amount = page.locator("(//input[@name='fund_source[2][amount]'])[1]")
        self.txt_loans_amount = page.locator("(//input[@name='fund_source[3][amount]'])[1]")

        self.btn_proceed_project = page.locator("//div[@id='project-cost-and-source-of-financing']//div[@class='row mt-3']//div[@class='col-12 d-flex justify-content-between align-items-center section-footer']//div//button[@type='button']")

    def fillup_berms_project(
        self,
        building_construction_amount: str,
        factory_tools_amount: str,
        transportation_amount: str,
        office_equipment_amount: str,
        other_assets_amount: str,
        assets_remarks: str,
        pre_operating_expenses_amount: str,
        working_capital_amount: str,
        equity_amount: str,
        advances_amount: str,
        loans_amount: str
    ):
        log.info("-----Filling up Berms Project Cost & Source of Financing-----")
        log.info("Filling up Building Construction/Renovation")
        self.playwright_fw.text_fill(self.txt_building_construction_amount, building_construction_amount)
        log.info("Filling up Factory Tools")
        self.playwright_fw.text_fill(self.txt_factory_tools_amount, factory_tools_amount)
        log.info("Filling up Transportation")
        self.playwright_fw.text_fill(self.txt_transportation_amount, transportation_amount)
        log.info("Filling up Office Furniture, Fixtures and Equipment")
        self.playwright_fw.text_fill(self.txt_office_equipment_amount, office_equipment_amount)
        log.info("Filling up Other Assets")
        self.playwright_fw.text_fill(self.txt_other_assets_amount, other_assets_amount)
        log.info("Filling remarks")
        self.do_actions_keys(self.action_keys)
        self.playwright_fw.text_fill(self.txt_assets_remarks, assets_remarks)
        log.info("Filling up Pre-operating Expenses")
        self.playwright_fw.text_fill(self.txt_pre_operating_expenses_amount, pre_operating_expenses_amount)
        log.info("Filling up  Working Capital (one quarter only)")
        self.playwright_fw.text_fill(self.txt_working_capital_amount, working_capital_amount)

        # get the total value of project cost
        label = self.get_initial_total_project_cost(self.lbl_value_of_initial_total_project_cost)
        # self.lbl_value_of_initial_total_project_cost.fill(label)
        log.info("Filling up Equity amount")
        self.playwright_fw.text_fill(self.txt_equity_amount, equity_amount)
        log.info("Filling up Additional Equity amount")
        self.playwright_fw.text_fill(self.txt_additional_equity_amount, label)
        log.info("Selecting Advances investment determination")
        self.opt_advances_type_of_loan.select_option("FOREIGN_LOAN")
        log.info("Selecting Loans investment determination")
        self.opt_loans_type_of_loan.select_option("LOCAL_LOAN")
        log.info("Filling up Advances amount")
        self.fillup_action_keys(self.txt_advances_amount, advances_amount)
        log.info("Filling up Loans amount")
        self.fillup_action_keys(self.txt_loans_amount, loans_amount)
        log.info("Clicking Save and Proceed button")
        self.btn_proceed_project.click()

# Do action keys to enable the specify assets
    def do_actions_keys(self, locator: Locator):
        locator.press("Enter")


# Select the type of loan
    # def select_by_option(self, locator: Locator, optionValue):
    #     self.page.select_option(locator)
    #     self.page.select_option(optionValue)

    def get_initial_total_project_cost(self, locator: Locator):
        value_label = locator.text_content()
        self.page.wait_for_timeout(2000)
        return value_label

    def fillup_action_keys(self, locator: Locator, textValue: str):
        locator.click()
        locator.fill(textValue)
        locator.press("Tab")