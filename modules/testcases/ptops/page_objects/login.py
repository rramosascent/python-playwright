from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.utility_package import UtilityPackage
from modules.testcases.ptops.data_objects.ptops_data_reference import DataReferenceCompilation


class LoginPage(FrameWorkPWDriver):
	def __init__(self, driver):
		self.driver = driver
		self.utility_f = UtilityPackage()
		self.data_reference = DataReferenceCompilation()
		self.url = ["open_url", "xxx"]
		self.user_name = ["get_by_role_name", "textbox_a", "Username", "xxx"]
		self.pass_word = ["get_by_role_name", "textbox_b", "Password", "xxx"]
		self.btn_sign_in = ["get_by_role_name", "button", "Sign in"]
		self.link_berms = ["expect_by_role_name", "link", " Applications & Accreditations"]

	def get_ptops_url(self, get_data):
		data_ref = self.data_reference.get_data_reference(get_data)
		self.open_url_ptops(data_ref)
	def open_url_ptops(self, get_data):
		data_processed = self.utility_f.add_data_in_array(self.url, get_data)
		self.fw_execute_test_suites(data_processed)

	def get_user_name(self, get_data):
		data_ref = self.data_reference.get_data_reference(get_data)
		self.input_user_name(data_ref["un"])
	def input_user_name(self, get_data):
		data_processed = self.utility_f.add_data_in_array(self.user_name, get_data)
		self.fw_execute_test_suites(data_processed)

	def get_pass_word(self, get_data):
		data_ref = self.data_reference.get_data_reference(get_data)
		self.input_pass_word(data_ref["pw"])

	def input_pass_word(self, get_data):
		data_processed = self.utility_f.add_data_in_array(self.pass_word, get_data)
		self.fw_execute_test_suites(data_processed)

	def proceed_ptops_login(self):
		self.fw_execute_test_suites(self.btn_sign_in)

	def verify_link_berms(self):
		self.fw_execute_test_suites(self.link_berms)