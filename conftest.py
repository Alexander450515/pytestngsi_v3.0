import pytest

from api.client import RestfulBookerClient


@pytest.fixture(scope="session")
def client():
    client = RestfulBookerClient("http://172.26.66.23:1026")
    # client.authorize("admin", "password123")
    return client
