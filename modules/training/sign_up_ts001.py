import pytest, re
from modules.testcases.ecp.data_processing import DataProcessingClass
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.testcases.ptops.sign_up_page import SignUpPageClass
@pytest.mark.usefixtures("setup")
class TestSignUpTestSuite0001:
    @pytest.fixture(scope="function", autouse=True)
    def before_each_after_each(self):
        print("before the test runs")
        # Go to the starting url before each test.
        global test_page_objects
        test_page_objects = SignUpPageClass(self.driver)
        yield
        print("after the test runs")
        self.driver.wait_for_timeout(10000)
    def test_open_ptops_url_link_create_account(self):
        test_page_objects.open_url_ptops("http://112.199.119.250:96/peza/login")
        test_page_objects.landing_link_create_account()
