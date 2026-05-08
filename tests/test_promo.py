def test_redeem_promo_success(client, auth_headers, active_promo):
    response = client.post(
        "/promo/redeem",
        json={"code": "PROMO10"},
        headers=auth_headers,
    )
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Promo code redeemed successfully"
    assert data["code"] == "PROMO10"
    assert data["credit_amount"] == 10
    assert data["new_balance"] == 10


def test_redeem_promo_not_found(client, auth_headers):
    response = client.post(
        "/promo/redeem",
        json={"code": "DOESNOTEXIST"},
        headers=auth_headers,
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Promo code not found"


def test_redeem_promo_twice_same_user(client, auth_headers, active_promo):
    first = client.post(
        "/promo/redeem",
        json={"code": "PROMO10"},
        headers=auth_headers,
    )
    assert first.status_code == 200

    second = client.post(
        "/promo/redeem",
        json={"code": "PROMO10"},
        headers=auth_headers,
    )
    assert second.status_code == 400
    assert second.json()["detail"] == "Promo code already redeemed by this user"