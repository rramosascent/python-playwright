class DataReferenceCompilation:

    def get_data_reference(self, get_data):
        data_set = {
            "url_x": "http://112.199.119.250:96/peza/login",
            "url": "http://192.168.20.25:82/peza/login",
            "url_1": "http://112.199.119.250:82/ECP/auth/login",
            "002": {"un": 'cgbc', "pw": 'Peza_123'},
            "001": {"un": 'amkortech', "pw": 'Password_123'},
            "examiner_1": {"un": 'balahibongpusa', "pw": 'Blitzkri3g!50088'}
        }
        return data_set[get_data]
