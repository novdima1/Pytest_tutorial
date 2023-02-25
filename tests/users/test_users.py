import pytest

from src.baseclasses.response import Response
from src.pydantic_schemas.user import User


def test_getting_posts(get_users):
    Response(get_users).assert_status_code(200).validate(User) # POST_SCHEMA


def test_get_response_json(get_users):
    response = Response(get_users)
    response.print_response_json()


@pytest.mark.skip("failed Test")
def test_skipped(calculate):
    assert 1 == 1, "Assertion failed"
    print(calculate(3, 4))


data = [
    (1, 2, 3),
    (1, 3, 4),
    (1, 3, 4)
]


@pytest.mark.dev
@pytest.mark.parametrize("n1, n2, res", data)
def test_calculation(n1, n2, res, calculate):
    assert calculate(n1, n2) == res, "Wrong calculation"
