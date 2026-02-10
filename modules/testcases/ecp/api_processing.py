import requests
from modules.testcases.ecp.data import DictionaryData
# from frame_work.framework_package.playwright_fw import FrameWorkPWDriver

class EcoConsumptionApi():

    def processing_consumption_api(self, test_case_data):
        # url = 'http://112.199.119.250:82/ECP/api/save-payment'
        url = 'http://192.168.10.62:82/ECP/api/save-payment'
        username = 'amwaiocIp=aEqb9SQdM2n!exuQnQmj'
        password = 'Blitzkri3g!5OO88'
        test_data = DictionaryData()
        test_data_tsuites = test_data.get_data_for_test_a(test_case_data)
        year = test_data_tsuites["create_ecp_consumption"]["ecp_year"][1]
        port = test_data_tsuites["create_ecp_consumption"]["ecp_port_code"][1]
        entry_no = test_data_tsuites["create_ecp_consumption"]["ecp_e_number"][1]
        declaration_no = test_data_tsuites["create_ecp_consumption"]["declaration"][1]
        receipt_no = test_data_tsuites["create_ecp_consumption"]["ecp_e_number"][2]
        consignee_tin = test_data_tsuites["create_ecp_consumption"]["consignee_rep_tin"][1]
        consignee_name = test_data_tsuites["create_ecp_consumption"]["consignee_rep_tin"][2]
        registry_no = test_data_tsuites["create_ecp_consumption"]["registry_num"][1]
        bl_number = test_data_tsuites["create_ecp_consumption"]["bl_number"][1]

        data = [
            {
                "registrationYear": year,
                "port": port,
                "registrationSerial": "C",
                "registrationNumber": entry_no,
                "declarantReferenceNumber": declaration_no,
                "receiptSerial": "R",
                "receiptNumber": receipt_no,
                "receiptDate": "2025-10-07T09:55:59",
                "registrationDate": "2025-10-07T09:35:59",
                "totalDutiesAndTaxes": 2834291.57,
                "consigneeCode": consignee_tin,
                "consigneeName": consignee_name,
                "sadStatus": "Paid",
                "registryNumber": registry_no,
                "bolReferenceNumber": bl_number,
                "sadItems": [
                    {
                        "itemNumber": 3,
                        "itemTaxAmount": 1405.00,
                        "supplementaryUnitsNumber": "3",
                        "itemHsCode": "87042273",
                        "supplementaryUnitsType": "UNIT",
                        "itemGoodsDescription": "TOYOTA VIOS",
                        "type": "CBU"
                    }
                ]
            }
        ]

        headers = {
            "Content-Type": "application/json",
            "Accept": "*.*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Cache-Control": "no-cache"
        }

        # json_data = json.dumps(data, indent=4)
        # print(json_data)

        # Send the POST request with Basic Authentication

        response = requests.post(url, json=data, headers=headers, auth=(username, password))

        # Check the response

        # if response.status_code == 200:
        #     print("Success!")
        #     print(response.json())
        # else:
        #     print(f"Error: {response.status_code}")
        #     print(response.text)

        return response.status_code