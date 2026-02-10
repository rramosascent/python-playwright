my_dict = {
    "gen": {"fname": "Alice", "lname": "Grace","mname": "Castro"},
    "age": 30,
    "city": "New York"
}
# print(my_dict)
# print(my_dict.keys())
# print(my_dict["gen"]["fname"])

# from testcases.ecp.data import DictionaryData

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
# with open(r"C:\Users\ASCENT\Documents\GitHub\python-playwright\pythonProject\testcases\ecp\file_uploads\ecp_test_data.json",'r', encoding="utf-8") as file:
#     data_for_test = file.read()
#
# # print(json.dumps(data_for_test, indent=4))
#
# d = ast.literal_eval(data_for_test)

# print(d["test_data_01"]["login"]["link_login"])
# print(type(d),d)


#
# path = r'C:\Users\ASCENT\Documents\GitHub\python-playwright\pythonProject\testcases\ecp\file_uploads'
# file = 'ecp_test_data'
# extension = 'txt'
# itenation = int(time.time())
#
# orig_file = f"{path}\{file}.{extension}"
# new_file = f"{path}\{file}_{itenation}.{extension}"

# with open(orig_file, 'r', encoding="utf-8") as file:save
#     dictionary_extraction = file.read()
# data_for_test = ast.literal_eval(dictionary_extraction)


# with open(r"C:\Users\ASCENT\Documents\GitHub\python-playwright\pythonProject\testcases\ecp\file_uploads\ecp_test_data_1760349178.txt", 'r', encoding="utf-8") as file:
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


# path = r'C:\Users\ASCENT\Documents\GitHub\python-playwright\pythonProject\testcases\ecp\file_uploads'
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

ecp_action_map = {
    "login": {
        "link_login": ["open_url", "XXXXXX"],
        "privacy_policy": ["get_by_role_name", "checkbox", "I agree"],
        "privacy_pbutton": ["get_by_role_name", "button", "Proceed"],
        "user_name": ["get_by_role_name", "textbox_a", "Enter your email or username", "XXXXXX"],
        "password": ["get_by_role_name", "textbox_b", "Password", "XXXXXX"],
        "btn_sign_in": ["get_by_role_name", "button", "SIGN IN"]
    }
}

ecp_action_data = {
        "login": {
            "link_login": [
                1,
                "url"
            ],
            "user_name": [
                3,
                "001"
            ],
            "password": [
                3,
                "001"
            ]
        }
}

for key, value in ecp_action_data["login"].items():
    ecp_action_map["login"][key][value[0]] = value[1]

print(ecp_action_map)


#
# open_excel_path_location = r"C:\Users\ASCENT\Documents\GitHub\python-playwright\pythonProject\testcases\ecp\file_uploads\CBU_ - Test ECP_x.xlsx"
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
