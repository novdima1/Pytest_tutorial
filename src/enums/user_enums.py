from enum import Enum


class Genders(Enum):
    male = "male"
    female = "female"


class Statuses(Enum):
    active = "active"
    inactive = "inactive"


class UserErrors(Enum):
    WRONG_EMAIL = "Incorrect e-mail"
