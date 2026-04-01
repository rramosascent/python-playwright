from playwright.sync_api import Page, expect
from modules.frame_work.utility.custom_logger import log

class BermsUndertakingPage:
    def __init__(self, page: Page):
        self.page = page
        self._modal_container = page.locator("#undertakingsModal")
        self._window_applicant_undertaking = page.locator("#oath-scroller")
        self._chkbox_i_agree = page.locator("#undertakingsModal input[type='checkbox']")
        self._btn_undertaking_proceed = page.locator("#undertakingsModal button:has-text('Proceed')")

    def agree_applicants_undertaking(self):
        log.info("Agreeing to Applicants Undertaking")
        self._window_applicant_undertaking.hover()
        self.page.mouse.wheel(0, 1000)
        self._chkbox_i_agree.click()
        self._btn_undertaking_proceed.click()
        # # Wait for the modal to be visible first
        # expect(self._modal_container).to_be_visible(timeout=10000)
        
        # # Scroll the undertaking text to the bottom
        # # Some applications require scrolling to the end before enabling the checkbox
        # log.info("Scrolling undertaking to the bottom")
        # self._window_applicant_undertaking.scroll_into_view_if_needed()
        # self._window_applicant_undertaking.evaluate("e => e.scrollTop = e.scrollHeight")
        
        # # Give a small buffer for any JS state updates
        # self.page.wait_for_timeout(1000)
        
        # log.info("Checking 'I Agree' checkbox")
        # self._chkbox_i_agree.check(force=True)
        
        # log.info("Clicking Proceed Button in Undertaking Modal")
        # self._btn_undertaking_proceed.click()
        