# https://my-json-server.typicode.com/typicode/demo/posts
import requests
from configuration import GOREST_USERS
from src.schemas.post import POST_SCHEMA
from src.baseclasses.response import Response
from src.pydantic_schemas.user import User


def test_getting_posts():
    r = requests.get(GOREST_USERS)
    response = Response(r)
    response.assert_status_code(200).validate(User) # POST_SCHEMA

def test_get_responce_json():
    r = requests.get(GOREST_USERS)
    response = Response(r)
    response.print_response_json()
