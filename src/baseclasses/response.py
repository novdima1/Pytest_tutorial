from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item) #validate(item, schema)
        else:
            schema.parse_obj(self.response_json) #validate(self.response_json, schema)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    def print_response_json(self):
        for post in self.response_json:
            print("\n", post)
        assert self.response_json[1] == {'id': 2, 'title': 'Post 2'}
        # for k in self.response_json[1]:
        print(self.response_json[1].values())
        assert "Post 2" in self.response_json[0].values(), f"\nExpected: Post 2, \nActual " \
                                                           f"{self.response_json[0].values()}," \
                                                           f" \n{GlobalErrorMessages.WRONG_POST_TITLE.value}"

