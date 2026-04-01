from playwright.sync_api import Page
from modules.frame_work.utility.custom_logger import log

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_btn = page.get_by_role("button", name="Sign in")

        # logout
        self.users_logo = page.locator(".avatar-online").first
        self.btn_logout = page.get_by_text("Log Out", exact=True)
        # self.btn_logout = page.locator("//div[@class='layout-page']//li[7]//a[1]")

    def navigate(self, url: str):
        log.info(f"Navigating to: {url}")
        self.page.goto(url)

    def login(self, user, pwd):
        log.info(f"Logging in as user: {user}")
        # Wait for preloader to disappear before interacting
        self.page.wait_for_selector("#preloader", state="hidden", timeout=30000)
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()

    def logout(self):
        log.info("Logging out")
        # self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)
        self.users_logo.click()
        self.btn_logout.click()