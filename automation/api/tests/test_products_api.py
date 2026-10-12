import pytest


@pytest.mark.api
@pytest.mark.smoke
def test_list_products_returns_paginated_data(api):
    response = api.get("/products")
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0


@pytest.mark.api
def test_every_product_has_required_fields(api):
    products = api.get("/products").json()["data"]
    for product in products:
        assert product["id"]
        assert product["name"]
        assert float(product["price"]) > 0


@pytest.mark.api
def test_get_single_product_matches_list(api, first_product):
    response = api.get(f"/products/{first_product['id']}")
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == first_product["id"]
    assert body["name"] == first_product["name"]


@pytest.mark.api
def test_unknown_product_returns_404(api):
    response = api.get("/products/00000000000000000000000000")
    assert response.status_code == 404


@pytest.mark.api
def test_search_finds_matching_products(api):
    response = api.get("/products/search", params={"q": "hammer"})
    assert response.status_code == 200
    names = [p["name"].lower() for p in response.json()["data"]]
    assert names, "expected at least one result for 'hammer'"
    assert all("hammer" in n for n in names)


@pytest.mark.api
def test_search_with_no_match_returns_empty_list(api):
    response = api.get("/products/search", params={"q": "xyzabc123nomatch"})
    assert response.status_code == 200
    assert response.json()["data"] == []


@pytest.mark.api
@pytest.mark.parametrize("term", ["HAMMER", "Hammer", "hammer"])
def test_search_is_case_insensitive(api, term):
    response = api.get("/products/search", params={"q": term})
    assert response.status_code == 200, f"q={term}: {response.status_code} {response.text[:200]}"

    baseline = api.get("/products/search", params={"q": "hammer"})
    assert baseline.status_code == 200, f"baseline: {baseline.status_code} {baseline.text[:200]}"

    assert len(response.json()["data"]) == len(baseline.json()["data"])


@pytest.mark.api
@pytest.mark.parametrize("bad_page", ["abc", "-1", "0", "99999999"])
def test_bad_page_value_never_causes_server_error(api, bad_page):
    response = api.get("/products", params={"page": bad_page})
    assert response.status_code < 500


@pytest.mark.api
def test_products_response_time_is_reasonable(api):
    response = api.get("/products")
    assert response.elapsed.total_seconds() < 3