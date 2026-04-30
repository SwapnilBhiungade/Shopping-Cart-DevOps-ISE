import sqlite3

from main import DATABASE_PATH


def product_count():
    with sqlite3.connect(DATABASE_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT count(productId) FROM products")
        return cur.fetchone()[0]


def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200


def test_login_form(client):
    response = client.get("/loginForm")
    assert response.status_code == 200


def test_login_page(client):
    response = client.get("/login")
    assert response.status_code == 200


def test_register_page(client):
    response = client.get("/register")
    assert response.status_code == 200


def test_registration_form(client):
    response = client.get("/registerationForm")
    assert response.status_code == 200


def test_display_category(client):
    response = client.get("/displayCategory?categoryId=1")
    assert response.status_code in (200, 302, 404)


def test_add_page(client):
    response = client.get("/add")
    assert response.status_code == 200


def test_remove_page(client):
    response = client.get("/remove")
    assert response.status_code == 200


def test_remove_item(client):
    response = client.get("/removeItem")
    assert response.status_code in (200, 302, 404)


def test_remove_item_rejects_sql_injection_payload(client):
    before_count = product_count()
    response = client.get("/removeItem?productId=1 OR 1=1")
    after_count = product_count()

    assert response.status_code == 302
    assert after_count == before_count


def test_display_category_rejects_sql_injection_payload(client):
    response = client.get("/displayCategory?categoryId=1 OR 1=1")
    assert response.status_code == 302


def test_profile_redirect(client):
    response = client.get("/account/profile")
    assert response.status_code == 302


def test_edit_profile_redirect(client):
    response = client.get("/account/profile/edit")
    assert response.status_code == 302


def test_change_password_redirect(client):
    response = client.get("/account/profile/changePassword")
    assert response.status_code == 302


def test_update_profile_redirect(client):
    response = client.get("/updateProfile")
    assert response.status_code == 302


def test_add_to_cart_redirect(client):
    response = client.get("/addToCart")
    assert response.status_code == 302


def test_cart_redirect(client):
    response = client.get("/cart")
    assert response.status_code == 302


def test_remove_from_cart_redirect(client):
    response = client.get("/removeFromCart")
    assert response.status_code == 302


def test_logout_redirect(client):
    response = client.get("/logout")
    assert response.status_code == 302


def test_invalid_route(client):
    response = client.get("/invalid")
    assert response.status_code == 404
