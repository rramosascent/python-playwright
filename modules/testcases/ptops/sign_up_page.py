from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver


class SignUpPageClass(FrameWorkPWDriver):

    def __init__(self, driver):
        self.driver = driver

    def open_url_ptops(self, get_data):
        open_url_complete = ["open_url", "xxx"]
        print(open_url_complete)
        open_url_complete[1] = get_data
        print(open_url_complete)

        self.fw_execute_test_suites(open_url_complete)

    def landing_link_create_account(self):
        data_link = ["get_by_role_name", "link", "Create an account"]
        self.fw_execute_test_suites(data_link)
