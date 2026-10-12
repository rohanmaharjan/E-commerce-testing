from automation.api.clients.api_client import ApiClient
from automation.utils.data_factory import new_user_payload


def create_user_via_api():
    payload = new_user_payload()
    response = ApiClient().post("/users/register", json=payload)
    assert response.status_code in (200, 201), (
        f"Register failed: {response.status_code} {response.text[:300]}"
    )
    return {"email": payload["email"], "password": payload["password"]}

def parse_price(text):
    """'$14.15' or '$ 1,014.15' -> 14.15"""
    cleaned = "".join(ch for ch in text if ch.isdigit() or ch == ".")
    return float(cleaned)

def get_invoices_via_api(email, password):
    api = ApiClient()
    response = api.login(email, password)
    assert response.status_code == 200, response.text
    api.set_token(response.json()["access_token"])
    result = api.get("/invoices")
    assert result.status_code == 200, result.text
    return result.json()["data"]