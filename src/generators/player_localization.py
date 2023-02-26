from faker import Faker


class PlayerLocalization:

    def __init__(self, lang):
        self.fake = Faker(lang)
        self.result = {
            "nickname": self.fake.first_name()
        }

    def set_number(self, number=11):
        self.result["Number"] = number
        return self

    def build(self):
        return self.result
