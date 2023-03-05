from src.enums.user_enums import Statuses
from src.generators.player_localization import PlayerLocalization
from src.baseclasses.builder import BuilderBaseClass


class Player(BuilderBaseClass):

    def __init__(self):
        super().__init__()
        self.reset()

    def set_status(self, status=Statuses.active.value):
        self.result["account_status"] = status
        return self

    def set_balance(self, balance=0):
        self.result["balance"] = balance
        return self

    def set_avatar(self, avatar="https://google.com/"):
        self.result["avatar"] = avatar
        return self

    def reset(self):
        self.set_status()
        self.set_avatar()
        self.set_balance()
        # self.result["localize"] = {
        #         "en": PlayerLocalization("en_US").build(),
        #         "ru": PlayerLocalization("pl_PL").build()
        #     }
        return self

    def update_inner_generator(self, key, generator):
        self.result[key] = {"fr": generator.build()}
        return self

    def build(self):
        return self.result