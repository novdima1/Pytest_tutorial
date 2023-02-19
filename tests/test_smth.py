# https://my-json-server.typicode.com/typicode/demo/posts
import requests
from configuration import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages

def test_python_site():
    r = requests.get('https://www.python.org')
    assert r.status_code == 200
    assert b'Python is a programming language' in r.content

def test_getting_post():
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    received_posts = response.json()
    assert len(received_posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT
