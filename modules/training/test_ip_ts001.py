import pytest, re
from modules.frame_work.utility.utility_package import UtilityPackage
from modules.testcases.ptops.api_import_permit import PtopsIpXml
@pytest.mark.usefixtures("setup")
class TestIPTestSuite0001:

    @pytest.fixture(scope="function", autouse=True)
    def before_each_after_each(self):
        print("before the test runs")
        # Go to the starting url before each test.
        global test_page_objects
        test_page_objects = PtopsIpXml(self.driver)
        global application_counter
        application_counter = UtilityPackage().padd_zeroes_2(1)
        yield
        print("after the test runs")
        # self.driver.wait_for_timeout(10000)
    def test_send_api_ip(self):
        test_page_objects.post_api_import_permit()
