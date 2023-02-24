# https://my-json-server.typicode.com/typicode/demo/posts
import requests
from configuration import TYPICODE_URL
from src.schemas.post import POST_SCHEMA
from src.baseclasses.response import Response
from src.pydantic_schemas.post import Post


def test_getting_posts():
    r = requests.get(TYPICODE_URL)
    response = Response(r)
    response.assert_status_code(200).validate(Post) # POST_SCHEMA

def test_get_responce_json():
    r = requests.get(TYPICODE_URL)
    response = Response(r)
    response.print_response_json()



