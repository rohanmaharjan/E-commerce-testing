from automation.api.clients.api_client import ApiClient
from automation.utils.data_factory import new_user_payload


def create_user_via_api():
    payload = new_user_payload()
    response = ApiClient().post("/users/register", json=payload)
    assert response.status_code in (200, 201), (
        f"Register failed: {response.status_code} {response.text[:300]}"
    )
    return {"email": payload["email"], "password": payload["password"]}