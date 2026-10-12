import pytest


@pytest.mark.api
def test_new_cart_can_be_created(auth_api):
    response = auth_api.post("/carts")
    assert response.status_code in (200, 201)
    assert response.json()["id"]


@pytest.mark.api
def test_added_item_appears_in_cart(auth_api, first_product):
    cart_id = auth_api.post("/carts").json()["id"]

    add = auth_api.post(
        f"/carts/{cart_id}",
        json={"product_id": first_product["id"], "quantity": 2},
    )
    assert add.status_code in (200, 201)

    cart = auth_api.get(f"/carts/{cart_id}").json()
    items = cart["cart_items"]
    assert len(items) == 1
    assert items[0]["quantity"] == 2