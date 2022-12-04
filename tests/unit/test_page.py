import requests_mock

from soccer_sdk_utils.page import PageObject


class TestConstructor:
    def test_url(self):
        page = PageObject(url="https://www.google.com")
        assert page.url == "https://www.google.com"

    def test_url_none(self):
        page = PageObject()
        assert page.url is None

    def test_soup(self):
        page = PageObject()
        assert page.soup is None

    def test_response(self):
        page = PageObject()
        assert page.response is None

    def test_headers(self):
        page = PageObject()
        assert page.headers is None


def test_url_setter():
    page = PageObject()
    page.url = "https://www.google.com"
    assert page.url == "https://www.google.com"


def test_soup_setter():
    page = PageObject()
    page.soup = "soup"
    assert page.soup == "soup"


def test_response_setter():
    page = PageObject()
    page.response = "response"
    assert page.response == "response"


def test_headers_setter():
    page = PageObject()
    page.headers = "headers"
    assert page.headers == "headers"


def test_status_code():
    page = PageObject()
    assert page.status_code is None


def test_status_code_with_response():
    page = PageObject()

    with requests_mock.Mocker() as m:
        m.get("https://www.google.com", text="Hello World", status_code=999)
        page.load("https://www.google.com")

    assert page.status_code == 999


def test_load_with_headers():
    page = PageObject()

    with requests_mock.Mocker() as m:
        m.get("https://www.google.com", text="Hello World", status_code=200)
        page.headers = {"test": "test"}
        page.load("https://www.google.com")

    assert page.status_code == 200


def test_erase():
    page = PageObject()

    with requests_mock.Mocker() as m:
        m.get("https://www.google.com", text="Hello World", status_code=200)
        page.load("https://www.google.com")

    assert page.status_code == 200

    page.erase()

    assert page.status_code is None
    assert page.url is None
    assert page.soup is None
    assert page.response is None


def test_repr():
    page = PageObject(url="https://www.google.com")
    assert repr(page) == "<PageObject(url='https://www.google.com')>"
