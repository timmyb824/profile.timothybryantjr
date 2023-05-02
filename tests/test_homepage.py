import pytest
from src.main import app, parse_config

def test_parse_config():
    name, location, linkedin, github, resume, blog = parse_config()
    assert name == "Timothy Bryant Jr."
    assert location == "Boston, MA"
    assert linkedin == "https://www.linkedin.com/in/timothy-bryant-7aa00026/"
    assert github == "https://www.github.com/timmyb824"
    assert resume == "https://drive.google.com/file/d/12mSxN5dPsnuiLGuJuL8ztozBjFkoLnDt/view?usp=sharing"
    assert blog == "https://blog.timothybryantjr.com"

@pytest.fixture
def client():
    # create a test client
    test_client = app.test_client()
    # use the app context
    with app.app_context():
        yield test_client

def test_homepage(client):
    # make a GET request to the root URL
    response = client.get('/')
    # assert that the response status code is 200
    assert response.status_code == 200
    assert b'Timothy Bryant Jr.' in response.data







