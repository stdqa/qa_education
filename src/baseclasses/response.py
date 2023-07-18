from src.enums.global_enums import GlobalErrorMessages


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get('data')
        self.response_status = response.status_code
        self.parsed_object = None

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                parsed_object = schema.parse_obj(item)
                self.parsed_object = parsed_object
        else:
            schema.model_validate(self.response_json)
        return self

    def assert_status_code(self, status_code):
        """
        Method for status code validation. It compares value from response
        object and compare it with received value from method params.

        """
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

    def get_parsed_object(self):
        return self.parsed_object

    def __str__(self):
        """
         Method for string displaying of class instance. In case when our
         validation will be failed, we will get full information about our
         object and comparation data, that will help us in fail investigation.

        """
        return f"\nStatus code: {self.response_status}\n" \
            f"Requested url: {self.response.url}\n" \
            f"Response body: {self.response_json}"
