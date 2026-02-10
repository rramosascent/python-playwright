from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver


class TestExecutionClass(FrameWorkPWDriver):
    def __init__(self, driver):
        self.driver = driver
    def page_login_a_user(self, get_data):
        link_creds = {
            "url": "http://112.199.119.250:96/peza-ed/login",
            "url_1": "http://112.199.119.250:82/ECP/auth/login",
            "001": {"un": 'cgbc', "pw": 'Peza_123'},
            "examiner_1": {"un": 'balahibongpusa', "pw": 'Blitzkri3g!50088'},
        }
        return link_creds[get_data]

    def login_to_ptops(self, get_data) -> None:
        print(self.page_login_a_user(get_data))
        open_url = ["open_url", self.page_login_a_user(get_data)]
        login_creds = self.page_login_a_user(get_data[1])

        self.fw_execute_test_suites(open_url)
