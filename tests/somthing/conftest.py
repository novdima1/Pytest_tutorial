import pytest
import requests
from configuration import GOREST_USERS


@pytest.fixture
def get_users():
    response = requests.get(GOREST_USERS)
    return response
