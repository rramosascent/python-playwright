from playwright.sync_api import Page, Locator
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.custom_logger import log

class BermsStockholdersPage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_fw = FrameWorkPWDriver(self.page)
        # Add Stockholder
        self.btn_add_stockholder = page.locator("#btnAddStockholder:visible")
        self.opt_stockholder_salutation = page.locator("#select2-proposedStockholderSalutationId-container")
        self.txt_stockholder_first_name = page.locator("#proposedStockholderFirstName")
        self.txt_stockholder_last_name = page.locator("#proposedStockholderLastName")
        self.opt_stockholder_nationality = page.locator("#select2-proposedStockholderNationalityId-container")
        self.txt_stockholder_shares = page.locator("#proposedStockholderNumberOfShares")
        self.txt_stockholder_subscribe_amount = page.locator("#proposedStockholderSubscribeAmt")
        self.txt_stockholder_paidup_amount = page.locator("#proposedStockholderPaidupAmt")
        self.btn_add_stockholder_save = page.locator("(//button[@id='btnAddStockholder'])[2]")
        
        # Add Principal Officer
        self.btn_add_principal_officer = page.locator("div[id='dt_principalOfficers_wrapper'] div[class='dt-buttons btn-group flex-wrap']")
        self.opt_principal_officer_salutation = page.locator("#select2-officerSalutationId-container:visible")
        self.txt_principal_officer_first_name = page.locator("#officerFirstName")
        self.txt_principal_officer_last_name = page.locator("#officerLastName")
        self.opt_principal_officer_nationality = page.locator("#select2-officerNationalityId-container:visible")
        self.txt_principal_officer_position = page.locator("#officerPosition")
        self.btn_add_principal_officer_save = page.locator("#btnAddPrincipalOfficer")

        self.btn_proceed_stockholders_principal_officers = page.locator("div[id='stockholders-and-principles'] div[class='row mt-3'] div[class='col-12 d-flex justify-content-between align-items-center section-footer'] div button[type='button']")

    # def fillup_berms_stockholders(self):
    #     log.info("-----Filling up Berms List of Proposed Stockholders-----")
    #     log.info("Clicking Add Stockholder on the list")
    #     self.btn_add_stockholder.click()
    #     log.info("Selecting Salutation")
    #     self.playwright_fw.dropdown_select_option(self.opt_stockholder_salutation, "Mr.")
    #     log.info("Filling up First Name")
    #     self.playwright_fw.text_fill(self.txt_stockholder_first_name, "John")
    #     log.info("Filling up Last Name")
    #     self.playwright_fw.text_fill(self.txt_stockholder_last_name, "Doe")
    #     log.info("Selecting Nationality")
    #     self.playwright_fw.dropdown_select_option(self.opt_stockholder_nationality, "Filipino")
    #     log.info("Filling up No. of Shares")
    #     self.playwright_fw.text_fill(self.txt_stockholder_shares, "10")
    #     log.info("Filling up Amount Subscribe (PHP)")
    #     self.playwright_fw.text_fill(self.txt_stockholder_subscribe_amount, "10")
    #     log.info("Filling up Amount Paid-up (PHP)")
    #     self.playwright_fw.text_fill(self.txt_stockholder_paidup_amount, "10")
    #     log.info("Clicking Save and Add stockholder")
    #     self.btn_add_stockholder_save.click()

    #     log.info("-----Filling up Berms (Proposed) Principal Officers -----")
    #     log.info("Clicking Add principal officer on the list")
    #     self.btn_add_principal_officer.click()
    #     log.info("Selecting Salutation")
    #     self.playwright_fw.dropdown_select_option(self.opt_principal_officer_salutation, "Mr.")
    #     log.info("Filling up First Name")
    #     self.playwright_fw.text_fill(self.txt_principal_officer_first_name, "John")
    #     log.info("Filling up Last Name")
    #     self.playwright_fw.text_fill(self.txt_principal_officer_last_name, "Doe")
    #     log.info("Selecting Nationality")
    #     self.playwright_fw.dropdown_select_option(self.opt_principal_officer_nationality, "Filipino")
    #     log.info("Filling up Position")
    #     self.playwright_fw.text_fill(self.txt_principal_officer_position, "CEO")
    #     log.info("Clicking Save and Add principal officer")
    #     self.btn_add_principal_officer_save.click()

    #     log.info("Clicking Save and Proceed button")
    #     self.btn_proceed_stockholders_principal_officers.click()

    def fillup_berms_stockholders(
        self,
        stockholder_salutation: str,
        stockholder_first_name: str,
        stockholder_last_name: str,
        stockholder_nationality: str,
        stockholder_shares: str,
        stockholder_subscribe_amount: str,
        stockholder_paidup_amount: str,
        principal_officer_salutation: str,
        principal_officer_first_name: str,
        principal_officer_last_name: str,
        principal_officer_nationality: str,
        principal_officer_position: str
    ):
        log.info("-----Filling up Berms List of Proposed Stockholders-----")
        log.info("Clicking Add Stockholder on the list")
        self.btn_add_stockholder.click()
        log.info("Selecting Salutation")
        self.playwright_fw.dropdown_select_option(self.opt_stockholder_salutation, stockholder_salutation)
        log.info("Filling up First Name")
        self.playwright_fw.text_fill(self.txt_stockholder_first_name, stockholder_first_name)
        log.info("Filling up Last Name")
        self.playwright_fw.text_fill(self.txt_stockholder_last_name, stockholder_last_name)
        log.info("Selecting Nationality")
        self.playwright_fw.dropdown_select_option(self.opt_stockholder_nationality, stockholder_nationality)
        log.info("Filling up No. of Shares")
        self.playwright_fw.text_fill(self.txt_stockholder_shares, stockholder_shares)
        log.info("Filling up Amount Subscribe (PHP)")
        self.playwright_fw.text_fill(self.txt_stockholder_subscribe_amount, stockholder_subscribe_amount)
        log.info("Filling up Amount Paid-up (PHP)")
        self.playwright_fw.text_fill(self.txt_stockholder_paidup_amount, stockholder_paidup_amount)
        log.info("Clicking Save and Add stockholder")
        self.btn_add_stockholder_save.click()

        log.info("-----Filling up Berms (Proposed) Principal Officers -----")
        log.info("Clicking Add principal officer on the list")
        self.btn_add_principal_officer.click()
        log.info("Selecting Salutation")
        self.playwright_fw.dropdown_select_option(self.opt_principal_officer_salutation, principal_officer_salutation)
        log.info("Filling up First Name")
        self.playwright_fw.text_fill(self.txt_principal_officer_first_name, principal_officer_first_name)
        log.info("Filling up Last Name")
        self.playwright_fw.text_fill(self.txt_principal_officer_last_name, principal_officer_last_name)
        log.info("Selecting Nationality")
        self.playwright_fw.dropdown_select_option(self.opt_principal_officer_nationality, principal_officer_nationality)
        log.info("Filling up Position")
        self.playwright_fw.text_fill(self.txt_principal_officer_position, principal_officer_position)
        log.info("Clicking Save and Add principal officer")
        self.btn_add_principal_officer_save.click()

        log.info("Clicking Save and Proceed button")
        self.btn_proceed_stockholders_principal_officers.click()

    # def dropdown_select_option(self, locator: Locator, option: str):
    #     # expect(self.page.get_by_role("option", name=option)).to_be_visible()
    #     self.page.wait_for_timeout(2000)
    #     locator.click()
    #     self.page.get_by_role("option", name=option).click()