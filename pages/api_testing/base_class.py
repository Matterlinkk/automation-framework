class BaseClass:
    response = None
    response_json = None

    def is_status_code_200(self):
        return self.response.status_code == 200
