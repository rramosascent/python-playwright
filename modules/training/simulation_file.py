# my_dict = {
#     "gen": {"fname": "Alice", "lname": "Grace","mname": "Castro"},
#     "age": 30,
#     "city": "New York"
# }
# print(my_dict)
# print(my_dict.keys())
# print(my_dict["gen"]["fname"])
# print(my_dict["age"])

# my_dict = {"brand": "Ford", "model": "Mustang"}
# ecp_data = DictionaryData()
#
# for key, value in my_dict.items():
#     print(f"{key}: {value}")

# for key in my_dict.keys():
#     print(f"{key}")

# for key in ecp_data.get_data_for_test("test_data_01").keys():
#     print(f"{key}")

# for key in ecp_data.get_data_for_test_all().keys():
#     print(f"{key}")

# import ast
#
# data_for_test = {}
#
# with open(r"C:\Users\ASCENT\Documents\GitHub\file_uploads\ecp_test_data.json",'r', encoding="utf-8") as file:
#     data_for_test = file.read()
#
# # print(json.dumps(data_for_test, indent=4))
#
# d = ast.literal_eval(data_for_test)

# print(d["test_data_01"]["login"]["link_login"])
# print(type(d),d)


#
# path = r'C:\Users\ASCENT\Documents\GitHub\file_uploads'
# file = 'ecp_test_data'
# extension = 'txt'
# itenation = int(time.time())
#
# orig_file = f"{path}\{file}.{extension}"
# new_file = f"{path}\{file}_{itenation}.{extension}"

# with open(orig_file, 'r', encoding="utf-8") as file:save
#     dictionary_extraction = file.read()
# data_for_test = ast.literal_eval(dictionary_extraction)


# with open(r"C:\Users\ASCENT\Documents\GitHub\file_uploads\ecp_test_data_1760349178.txt", 'r', encoding="utf-8") as file:
#     dictionary_extraction = file.read()
# data_for_test = ast.literal_eval(dictionary_extraction)

# print(data_for_test)
# for data_key, data_value in data_for_test.items():
#     # print(data_for_test[data_key]["gen"]["fname"])
#     # data_for_test[data_key]["gen"]["fname"] = 'Alice'
#     print(data_key)

# with open(new_file, 'w', encoding="utf-8") as file:
#     # file.write(str(my_dict))
#     json.dump(data_for_test, file, indent=4)

# os.rename(orig_file,new_file)
#
# data_for_test = ast.literal_eval(dictionary_extraction)

# print(f"{path}\{file}_{itenation}.{extension}")


# path = r'C:\Users\ASCENT\Documents\GitHub\file_uploads'
# file = 'entry_numbers'
# extension = 'txt'
# iteration = int(time.time())
#
# orig_file = f"{path}\{file}.{extension}"
# new_file = f"{path}\{file}_{iteration}.{extension}"
#
# with open(orig_file, 'r', encoding="utf-8") as file:
#     dictionary_extraction = file.read()
# data_for_test = ast.literal_eval(dictionary_extraction)
#
# for data_key, data_value in data_for_test.items():
#     o_entry_no = data_for_test[data_key]["counter"]
#     u_entry_no = str(int(o_entry_no.lstrip('0')) + 1).zfill(6)
#     data_for_test[data_key]["counter"] = u_entry_no
#
# with open(new_file, 'w', encoding="utf-8") as file:
#     json.dump(data_for_test, file, indent=4)

# padding and filling
# o_entry_no = '000100'
# u_entry_no = int(o_entry_no.lstrip('0'))+1
#
# print(str(u_entry_no).zfill(6))


# def open_test_case_excel_file(self, open_excel_path_location):

# ecp_action_map = {
#     "login": {
#         "link_login": ["open_url", "XXXXXX"],
#         "privacy_policy": ["get_by_role_name", "checkbox", "I agree"],
#         "privacy_pbutton": ["get_by_role_name", "button", "Proceed"],
#         "user_name": ["get_by_role_name", "textbox_a", "Enter your email or username", "XXXXXX"],
#         "password": ["get_by_role_name", "textbox_b", "Password", "XXXXXX"],
#         "btn_sign_in": ["get_by_role_name", "button", "SIGN IN"]
#     }
# }
#
# ecp_action_data = {
#         "login": {
#             "link_login": [
#                 1,
#                 "url"
#             ],
#             "user_name": [
#                 3,
#                 "001"
#             ],
#             "password": [
#                 3,
#                 "001"
#             ]
#         }
# }
#
# for key, value in ecp_action_data["login"].items():
#     ecp_action_map["login"][key][value[0]] = value[1]
#
# print(ecp_action_map)


#
# open_excel_path_location = r"C:\Users\ASCENT\Documents\GitHub\file_uploads\CBU_ - Test ECP_x.xlsx"
# get_work_book = load_workbook(open_excel_path_location)
# get_active_sheet = get_work_book.active
# get_total_rows = get_active_sheet.max_row
#     # return get_work_book, get_active_sheet, get_total_rows
#
# # print(get_active_sheet, get_total_rows)
#
# for x in range(get_total_rows):
#     if x > 0:
#         CellRow = x + 1
#         extension_num = str(x).zfill(4)
#
#         engine_data = f'{data_entry_num["cbu_engine"]}{data_ecp_information[3]}{extension_num}'
#         chassis_data = f'{data_entry_num["cbu_chassis"]}{data_ecp_information[3]}{extension_num}'
#         vin_data = f'{data_entry_num["cbu_vin"]}{data_ecp_information[3]}{extension_num}'
#         get_active_sheet.cell(row=CellRow, column=9, value=engine_data)
#         get_active_sheet.cell(row=CellRow, column=10, value=chassis_data)
#         get_active_sheet.cell(row=CellRow, column=11, value=vin_data)
#
# get_work_book.save(open_excel_path_location)

import requests
from requests.auth import HTTPBasicAuth

url = 'http://192.168.20.25:82/peza/api/v1/auth'
username = 'cdec@dmin_J5!X3kL'
password = 'Password_123'

data = ""

headers = {
    "Authorization": "Basic Y2RlY0BkbWluX0o1IVgza0w6UGFzc3dvcmRfMTIz",
    "Content-Lenght":"0",
    "User-Agent": "PostmanRuntime/7.51.1",
    # "Content-Type": "application/json",
    "Accept": "*.*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Cache-Control": "no-cache"
}

# response = requests.post(url,json=data,headers=headers, auth=HTTPBasicAuth(username, password))
response = requests.post(url, auth=HTTPBasicAuth(username, password))

bearer_token = response.json().get("response")["auth-token"]
print(bearer_token)


url_ip = 'http://192.168.20.25:82/peza/api/v1/importPermits'



headers_ip = {
    "Authorization": f"Bearer {bearer_token}",
    "Accept": "application/json"  # Optional: specify expected response format
}

json_payload = {
    "Vasp_code": "VS3PZ9QY",
    "Date_applied": "2026-03-08 14:23:40",
    "Date_created": "2026-03-08 13:39:47",
    "Application_number": "IP-TII10775-IT001",
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

response_ip = requests.post(url_ip, headers=headers_ip, json=json_payload)

print(response_ip.json())