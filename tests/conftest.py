import pytest
import requests
from configuration import GOREST_USERS
from random import randrange


@pytest.fixture
def get_users():
    response = requests.get(GOREST_USERS)
    return response


@pytest.fixture
def get_conftest():
    return "tests conftest"


@pytest.fixture
def get_rnd_number():
    return randrange(1, 11)


def _calc(a, b):
    return a + b


@pytest.fixture
def calculate():
    print("\nBefore test")
    yield _calc
    print("\nCalculation is finished")
