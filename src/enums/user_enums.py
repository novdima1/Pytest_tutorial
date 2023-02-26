from enum import Enum


class Genders(Enum):
    male = "male"
    female = "female"


class Statuses(Enum):
    active = "Active"
    inactive = "Inactive"


class UserErrors(Enum):
    WRONG_EMAIL = "Incorrect e-mail"
