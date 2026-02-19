import pytest
import re
from playwright.sync_api import Playwright, sync_playwright, expect
from pathlib import Path
from modules.frame_work.utility.utility_package import UtilityPackage


class FrameWorkPWDriver:
    def __init__(self, driver):
        self.driver = driver
    def fw_execute_test_suites(self, data_list):
        match data_list[0]:
            case 'get_by_role_name':
                self.get_by_role_name(data_list)
            case 'get_by_location_con_text':
                self.get_by_location_con_text(data_list)
            case 'open_url':
                self.open_url(data_list)
            case 'get_by_location_fill_a':
                self.get_by_location_fill_a(data_list)
            case 'get_by_location_fill_b':
                self.get_by_location_fill_b(data_list)
            case 'get_by_location_option_select':
                self.get_by_location_option_select(data_list)
            case 'expect_by_role_name':
                self.expect_by_role_name(data_list)
            case 'get_by_location':
                self.get_by_location(data_list)
            case 'expect_locator_filter_has_txt':
                self.expect_locator_filter_has_txt(data_list)
            case 'get_by_role_combox_select':
                self.get_by_role_combox_select(data_list)
            case 'get_by_text_click':
                self.get_by_text_click(data_list)
            case 'get_by_text_set_files':
                self.get_by_text_set_files(data_list)
            case 'get_by_file_chooser':
                self.get_by_file_chooser(data_list)
            case 'get_by_title_click':
                self.get_by_title_click(data_list)
            case 'select_date_picker_v1':
                self.select_date_picker_v1(data_list)
            case _:
                pytest.fail('invalid function')
    def open_url(self, get_by_data):
        self.driver.goto(get_by_data[1])
    def get_by_location_con_text(self, get_by_data):
        expect(self.driver.locator(get_by_data[1])).to_contain_text(get_by_data[2])

    def get_by_location(self, get_by_data):
        match get_by_data[1]:
            case 'expect':
                expect(self.driver.locator(get_by_data[2])).to_be_visible(timeout=5000)
                self.driver.locator(get_by_data[2]).scroll_into_view_if_needed()
            case 'click':
                self.driver.locator(get_by_data[2]).click()
            case 'checkbox':
                self.driver.locator(get_by_data[2]).check()
            case 'fill':
                # expect(self.driver.locator(get_by_data[2])).to_be_visible(timeout=10000)
                # self.driver.locator(get_by_data[2]).count()
                self.driver.locator(get_by_data[2]).fill(get_by_data[3])
            case 'fill2':
                # expect(self.driver.locator(get_by_data[2])).to_be_visible(timeout=10000)
                self.driver.locator(get_by_data[2]).locator('.numInput cur-year').fill(get_by_data[3])
                # self.driver.locator(get_by_data[2]).fill(get_by_data[3])
            case 'set_input_fIles':
                self.driver.locator(get_by_data[2]).set_input_files(get_by_data[3])
            case 'filter_th_click':
                self.driver.locator(get_by_data[2]).filter(has_text=get_by_data[3]).nth(get_by_data[4]).click()
            case _:
                pytest.fail('invalid option')
    def expect_by_role_name(self, get_by_data):
        expect(self.driver.get_by_role(get_by_data[1], name=get_by_data[2])).to_be_visible(timeout=10000)
        self.driver.get_by_role(get_by_data[1], name=get_by_data[2]).scroll_into_view_if_needed()

    def expect_locator_filter_has_txt(self, get_by_data):
        expect(self.driver.locator(get_by_data[1]).filter(has_text=get_by_data[2]).first).to_be_visible(timeout=10000)

    def get_by_location_option_select(self, get_by_data):
        self.driver.locator(get_by_data[1]).select_option(get_by_data[2])
        # (get_by_data[2]))

    def get_by_role_combox_select(self,get_by_data):
        self.driver.wait_for_timeout(5000)
        combobox_text = self.driver.locator(get_by_data[1]).inner_text()
        if combobox_text == "":
            self.driver.get_by_role("combobox").filter(has_text=re.compile(r"^$")).locator("b").click()
        else:
            expect(self.driver.get_by_role("combobox", name=combobox_text)).to_be_visible(timeout=10000)
            self.driver.get_by_role("combobox", name=combobox_text).click()

        expect(self.driver.get_by_role("option", name=get_by_data[2])).to_be_visible(timeout=10000)
        self.driver.get_by_role("option", name=get_by_data[2]).click()

    def get_by_title_click(self, get_by_data):
        expect(self.driver.get_by_title(get_by_data[1])).to_be_visible(timeout=10000)
        self.driver.get_by_title(get_by_data[1]).click()

    def get_by_text_click(self, get_by_data):
        self.driver.get_by_text(get_by_data[1]).click()
    def get_by_text_set_files(self, get_by_data):
        self.drag_and_drop_file(get_by_data[1], get_by_data[2])
        # self.driver.get_by_text(get_by_data[1]).set_input_files(get_by_data[2])

    def get_by_file_chooser(self, get_by_data):
        # self.driver.file_chooser(get_by_data[1], get_by_data[2])

        with self.driver.expect_file_chooser() as fc_info:
            self.driver.get_by_text(get_by_data[1]).click()

        file_chooser = fc_info.value
        file_chooser.set_files(get_by_data[2])


    def get_by_location_fill_a(self, get_by_data):
        self.driver.locator(get_by_data[1]).click()
        self.driver.locator(get_by_data[1]).fill(get_by_data[2])
        self.driver.locator(get_by_data[1]).press("Tab")

    def get_by_location_fill_b(self, get_by_data):
        self.driver.locator(get_by_data[1]).fill(get_by_data[2])
        self.driver.locator(get_by_data[1]).press("Tab")

    def get_by_role_name(self, get_by_data):
        match get_by_data[1]:
            case 'checkbox':
                self.driver.get_by_role(get_by_data[1], name=get_by_data[2]).scroll_into_view_if_needed()
                expect(self.driver.get_by_role(get_by_data[1], name=get_by_data[2])).to_be_visible()
                self.driver.get_by_role(get_by_data[1], name=get_by_data[2]).check()
            case 'button':
                expect(self.driver.get_by_role(get_by_data[1], name=get_by_data[2])).to_be_visible(timeout=10000)
                self.driver.get_by_role(get_by_data[1], name=get_by_data[2]).scroll_into_view_if_needed()
                expect(self.driver.get_by_role(get_by_data[1], name=get_by_data[2])).to_be_in_viewport()
                self.driver.get_by_role(get_by_data[1], name=get_by_data[2]).click()
            case 'button_set_files':
                self.driver.get_by_role("button", name=get_by_data[2]).set_input_files(get_by_data[3])
            case 'link':
                expect(self.driver.get_by_role(get_by_data[1], name=get_by_data[2])).to_be_visible()
                self.driver.get_by_role(get_by_data[1], name=get_by_data[2]).click()
            case 'textbox_a':
                expect(self.driver.get_by_role("textbox", name=get_by_data[2])).to_be_visible()
                self.driver.get_by_role("textbox", name=get_by_data[2]).click()
                self.driver.get_by_role("textbox", name=get_by_data[2]).fill(get_by_data[3])
                self.driver.get_by_role("textbox", name=get_by_data[2]).press("Tab")
            case 'textbox_b':
                expect(self.driver.get_by_role("textbox", name=get_by_data[2])).to_be_visible()
                self.driver.get_by_role("textbox", name=get_by_data[2]).fill(get_by_data[3])
                self.driver.get_by_role("textbox", name=get_by_data[2]).press("Tab")
            case 'link':
                expect(self.driver.get_by_role(get_by_data[1], name=get_by_data[2])).to_be_visible()
            case 'row_item':
                expect(self.driver.get_by_role("row", name=get_by_data[2]).get_by_role("link")).to_be_visible()
                self.driver.get_by_role("row", name=get_by_data[2]).get_by_role("link").click()
            case 'row_dp':
                expect(self.driver.get_by_role("row", name=get_by_data[2]).get_by_placeholder(get_by_data[3])).to_be_visible()
                self.driver.get_by_role("row", name=get_by_data[2]).get_by_placeholder(get_by_data[3]).fill(get_by_data[4])
            case 'radio_b':
                expect(self.driver.get_by_role("radio", name=get_by_data[2])).to_be_visible()
                self.driver.get_by_role("radio", name=get_by_data[2]).click()
            case 'spinbutton':
                expect(self.driver.get_by_role("spinbutton", name=get_by_data[2])).to_be_visible()
                self.driver.get_by_role("spinbutton", name=get_by_data[2]).fill(get_by_data[3])
                self.driver.get_by_role("spinbutton", name=get_by_data[2]).press("Tab")
            case _:
                pytest.fail('invalid option')
    def select_date_picker_v1(self, get_by_data):
        div_class = "flatpickr-calendar animate flatpickr-monthSelect-theme-light open"
        open_date_picker_xpath = f"xpath=//div[contains(@class, \"{div_class}\")]"


        self.driver.locator(get_by_data[1]).click()
        get_by_data_date = UtilityPackage().date_picker_data_strptime(get_by_data[2])
        get_month_num = UtilityPackage().month_number_conversion_xxx(get_by_data_date[1])

        expect(self.driver.locator(open_date_picker_xpath).locator("//div[1]/div/div/div/input").filter(visible=True)).to_be_visible(timeout=10000)
        self.driver.locator(open_date_picker_xpath).locator("//div[1]/div/div/div/input").filter(visible=True).click()
        self.driver.locator(open_date_picker_xpath).locator("//div[1]/div/div/div/input").filter(visible=True).press_sequentially(get_by_data_date[0])
        self.driver.locator(open_date_picker_xpath).locator("//div[1]/div/div/div/input").filter(visible=True).press("Tab")

        # expect(self.driver.get_by_role("spinbutton", name="Year")).to_be_visible(timeout=10000)
        # self.driver.get_by_role("spinbutton", name="Year").click()
        # self.driver.get_by_role("spinbutton", name="Year").press_sequentially(get_by_data_date[0])
        # self.driver.get_by_role("spinbutton", name="Year").press("Tab")

        # expect(self.driver.get_by_label(get_by_data_date[3])).to_be_visible(timeout=10000)
        # self.driver.get_by_label(get_by_data_date[3]).click()

        expect(self.driver.locator(open_date_picker_xpath).locator("//div[2]/div/div/span").filter(has_text=get_month_num).filter(visible=True)).to_be_visible(timeout=10000)
        self.driver.locator(open_date_picker_xpath).locator("//div[2]/div/div/span").filter(has_text=get_month_num).filter(visible=True).click()

        # locator_partial_class = page.locator('xpath=//*[contains(@class, "my-class") and contains(text(), "Welcome")]')

    def drag_and_drop_file(self, selector: str, file_path: str):
        """
        Drag and drop a file onto an element

        Args:
            page: Playwright page object
            selector: CSS selector for the drop zone
            file_path: Path to the file to upload
        """
        file_name = Path(file_path).name

        self.driver.evaluate("""
        ([selector, fileName, filePath]) => {
            const dropZone = document.querySelector(selector);

            // You can customize this based on your needs
            const file = new File([''], fileName, {
                type: 'application/octet-stream'
            });

            const dataTransfer = new DataTransfer();
            dataTransfer.items.add(file);

            // Trigger drag events
            ['dragenter', 'dragover', 'drop'].forEach(eventName => {
                const event = new DragEvent(eventName, {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                dropZone.dispatchEvent(event);
            });
        }
        """, [selector, file_name, file_path])
