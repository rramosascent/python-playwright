from openpyxl import load_workbook

class UtilityPackage():
    def padd_zeroes(self, data):
        return str(data).zfill(6)

    def cbu_excel(self, data_path, data_entry_num, data_ecp_information):

        open_excel_path_location = data_path
        get_work_book = load_workbook(open_excel_path_location)
        get_active_sheet = get_work_book.active
        get_total_rows = get_active_sheet.max_row

        for x in range(get_total_rows):
            if x > 0:
                CellRow = x + 1
                extension_num = str(x).zfill(4)

                engine_data = f'{data_entry_num["cbu_engine"]}{data_ecp_information}{extension_num}'
                chassis_data = f'{data_entry_num["cbu_chassis"]}{data_ecp_information}{extension_num}'
                vin_data = f'{data_entry_num["cbu_vin"]}{data_ecp_information}{extension_num}'

                if get_active_sheet.cell(row=CellRow, column=9).value != "":
                    get_active_sheet.cell(row=CellRow, column=9, value=engine_data)
                if get_active_sheet.cell(row=CellRow, column=10).value != "":
                    get_active_sheet.cell(row=CellRow, column=10, value=chassis_data)
                if get_active_sheet.cell(row=CellRow, column=11).value != "":
                    get_active_sheet.cell(row=CellRow, column=11, value=vin_data)

        get_work_book.save(open_excel_path_location)

