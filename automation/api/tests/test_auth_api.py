import pytest
from automation.config.settings import USER_EMAIL, USER_PASSWORD


@pytest.mark.api
@pytest.mark.smoke
def test_login_with_valid_credentials_returns_token(api, test_user):
    response = api.login(test_user["email"], test_user["password"])
    assert response.status_code == 200
    body = response.json()
    assert "access_token" in body
    assert body["access_token"]


@pytest.mark.api
def test_login_with_wrong_password_is_rejected(api, fresh_user):
    response = api.login(fresh_user["email"], "definitely-wrong-123")
    assert response.status_code == 401
    assert "access_token" not in response.text


@pytest.mark.api
def test_login_with_unregistered_email_is_rejected(api):
    response = api.login("nobody.here@example.com", "whatever123")
    assert response.status_code == 401


@pytest.mark.api
def test_login_with_empty_body_is_client_error(api):
    response = api.post("/users/login", json={})
    assert 400 <= response.status_code < 500


@pytest.mark.api
def test_profile_requires_token(api):
    response = api.get("/users/me")
    assert response.status_code == 401


@pytest.mark.api
def test_profile_rejects_garbage_token(api):
    api.set_token("abc.def.ghi")
    response = api.get("/users/me")
    assert response.status_code == 401


@pytest.mark.api
@pytest.mark.smoke
def test_profile_with_valid_token_returns_user(auth_api, test_user):
    response = auth_api.get("/users/me")
    assert response.status_code == 200
    assert response.json()["email"] == test_user["email"]


@pytest.mark.api
def test_profile_never_exposes_password(auth_api):
    response = auth_api.get("/users/me")
    assert "password" not in response.json()