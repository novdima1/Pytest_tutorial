from src.baseclasses.response import Response
from src.pydantic_schemas.user import User


def test_getting_posts(get_users):
    Response(get_users).assert_status_code(200).validate(User) # POST_SCHEMA


def test_get_response_json(get_users):
    response = Response(get_users)
    response.print_response_json()


def test_get_conf(get_conftest, get_rnd_number, calculate):
    print(get_conftest)
    print(get_rnd_number)
    print(calculate(2, 3))
