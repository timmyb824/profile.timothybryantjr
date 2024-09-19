import pytest
from src.main import app


@pytest.fixture
def client():
    # create a test client
    test_client = app.test_client()
    # use the app context
    with app.app_context():
        yield test_client


def test_homepage(client):
    # make a GET request to the root URL
    response = client.get("/")
    # assert that the response status code is 200
    assert response.status_code == 200
    assert b"Timothy Bryant Jr." in response.data
