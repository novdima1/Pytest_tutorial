# https://my-json-server.typicode.com/typicode/demo/posts
import requests
from configuration import TYPICODE_URL
from src.schemas.post import POST_SCHEMA
from src.baseclasses.response import Response


def test_getting_posts():
    r = requests.get(TYPICODE_URL)
    response = Response(r)
    response.assert_status_code(200).validate(POST_SCHEMA)


