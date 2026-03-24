import requests
import json
import ast
from requests.auth import HTTPBasicAuth
from modules.frame_work.framework_package.playwright_fw import FrameWorkPWDriver
from modules.frame_work.utility.utility_package import UtilityPackage
class PtopsIpXml(FrameWorkPWDriver):
    def __init__(self, driver):
        self.driver = driver
        self.utility_f = UtilityPackage()

    def get_data_file(self):
        with open(r"data_file.txt", 'r', encoding="utf-8") as file:
            dictionary_extraction = file.read()
        data_for_test = ast.literal_eval(dictionary_extraction)

        return data_for_test

    def save_data_file(self, updated_data):
        with open(r"data_file.txt", 'w', encoding="utf-8") as file:
            json.dump(updated_data, file, indent=4)

    def get_counter_reference(self):

        data_file_extract = self.get_data_file()

        for data_key_1, data_value_1 in data_file_extract.items():

            if data_key_1 == "counter":
                updated_counter = data_file_extract["counter"] + 1
                padded_entry_num = self.utility_f.padd_zeroes_2(updated_counter)
                data_file_extract["counter"] = updated_counter

            self.save_data_file(data_file_extract)

        return padded_entry_num
    def get_vasp_api_key(self):

        url = 'http://192.168.20.26:82/peza/api/v1/auth'
        username = 'cdec@dmin_J5!X3kL'
        password = 'Password_123'

        response = requests.post(url, auth=HTTPBasicAuth(username, password))

        # print(response.json().get("response")["auth-token"])
        return response.json().get("response")["auth-token"]

    def post_api_import_permit(self):

        counter_num = self.get_counter_reference()

        url = 'http://192.168.20.25:82/peza/api/v1/importPermits'

        bearer_token = self.get_vasp_api_key()

        headers = {
            "Authorization": f"Bearer {bearer_token}",
            "Accept": "application/json"  # Optional: specify expected response format
        }

        json_payload = {
            "Vasp_code": "VS3PZ9QY",
            "Date_applied": "2026-03-08 14:23:40",
            "Date_created": "2026-03-08 13:39:47",
            "Application_number": f"IP-TII10775-IT{counter_num}",
            "Locator": {
                "Locator_tin": "005-865-295-000",
                "Locator_zone": "CLTI",
                "Enterprise_type": "EE"
            },
            "Broker": {
                "Broker_tin": "738-464-204-000"
            },
            "Shipper": {
                "Shipper_name": "TEXAS INS PHILS, INC.",
                "Shipper_address": "GENERAL JUAN DELA CRUZ STREET, SGT. MARLBORO DRIVE, PHILIP MORRIS, LUCKY CITY"
            },
            "Purpose": "FOR PRODUCTION USE",
            "Delivery_address": "SM ICITY 3 - SMI3",
            "Remarks": "STANDARD DELIVERY",
            "Way_bill_number": "BL-ALO28392-IT001",
            "Payment_method": 1,
            "Origin": "CN",
            "Port": "P02A",
            "Departure_date": "2026-03-01",
            "Arrival_date": "2026-03-08",
            "Registry_no": "AAA0001-26",
            "Invoices_nos": "INV-TII10775-IT001",
            "Status": "PAID",
            "Receipt_number": "RNO-TII10775-IT001",
            "Receipt_date": "2026-03-13 13:39:47",
            "Payment_ref_no": "TII10775-IT001",
            "Processing_fee": 2000,
            "Exchange_Rate": 58.62,
            "Currency": "USD",
            "Items": [
                {
                    "Id": [
                        "TII10775-13850-1584203"
                    ],
                    "Description": "PC 8608.0020.000 I-0004",
                    "Uom": "OT",
                    "Item_use": "FOR PRODUCTION USE",
                    "Purchase_order_number": "",
                    "Quantity": 987,
                    "Invoice_value": 654,
                    "Gross_weight": 321,
                    "Other_uom": "PLT"
                },
                {
                    "Id": [
                        "TII10775-13850-1584204"
                    ],
                    "Description": "PC 8608.0020.000 I-0004",
                    "Uom": "OT",
                    "Item_use": "FOR PRODUCTION USE",
                    "Purchase_order_number": "",
                    "Quantity": 987,
                    "Invoice_value": 654,
                    "Gross_weight": 321,
                    "Other_uom": "PLT"
                }
            ]
        }

        response = requests.post(url, headers=headers, json=json_payload)

        assert response.status_code == 200