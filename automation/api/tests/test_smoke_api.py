# sanity test: prove the setup works

import requests
from automation.config.settings import API_URL


def test_products_endpoint_is_reachable():
    response = requests.get(f"{API_URL}/products", timeout=10)
    assert response.status_code == 200
    assert "data" in response.json()