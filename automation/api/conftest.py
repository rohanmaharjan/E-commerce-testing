import pytest
from automation.api.clients.api_client import ApiClient
from automation.utils.data_factory import new_user_payload


def _register_user():
    payload = new_user_payload()
    response = ApiClient().post("/users/register", json=payload)
    assert response.status_code in (200, 201), (
        f"Register failed: {response.status_code} {response.text[:300]}"
    )
    return {"email": payload["email"], "password": payload["password"]}


@pytest.fixture
def api():
    """A fresh, unauthenticated client for each test."""
    return ApiClient()


@pytest.fixture(scope="session")
def test_user():
    """One registered user for the whole run. Use only for tests that log in successfully."""
    return _register_user()


@pytest.fixture
def fresh_user():
    """A brand-new user per test. Use for tests that make failed logins."""
    return _register_user()


@pytest.fixture(scope="session")
def token(test_user):
    client = ApiClient()
    response = client.login(test_user["email"], test_user["password"])
    assert response.status_code == 200, f"Login failed: {response.status_code} {response.text[:300]}"
    return response.json()["access_token"]


@pytest.fixture
def auth_api(token):
    client = ApiClient()
    client.set_token(token)
    return client


@pytest.fixture(scope="session")
def first_product():
    response = ApiClient().get("/products")
    assert response.status_code == 200
    return response.json()["data"][0]