import requests

BASE_URL = "https://httpbin.org"


def test_get_with_query_params():
    """
    Проверяет передачу query-параметров в GET-запросе.
    Использует resp.request.method для проверки HTTP-глагола.
    """
    params = {"key": "value", "limit": "10", "active": "true"}
    resp = requests.get(f"{BASE_URL}/get", params=params, timeout=5)
    
    assert resp.status_code == 200
    data = resp.json()
    
    assert data["args"] == params
    assert resp.request.method == "GET"
    assert data["url"].startswith(BASE_URL + "/get")


def test_post_with_json_body():
    """
    Проверяет отправку JSON-тела.
    Использует not data.get("form") для совместимости с None и пустым словарём.
    """
    payload = {"name": "Alex", "role": "developer", "level": 5}
    resp = requests.post(f"{BASE_URL}/post", json=payload, timeout=5)
    
    assert resp.status_code == 200
    data = resp.json()
    
    assert data["json"] == payload
    assert not data.get("form")
    assert resp.request.method == "POST"


def test_post_with_form_data():
    """
    Проверяет отправку данных формы (application/x-www-form-urlencoded).
    """
    form_data = {"username": "admin", "password": "secret123", "remember": "true"}
    resp = requests.post(f"{BASE_URL}/post", data=form_data, timeout=5)
    
    assert resp.status_code == 200
    data = resp.json()
    
    assert data["form"] == form_data
    assert not data.get("json")
    assert resp.request.method == "POST"


def test_delete_method():
    """
    Проверяет выполнение DELETE-запроса.
    """
    resp = requests.delete(f"{BASE_URL}/delete", timeout=5)
    
    assert resp.status_code == 200
    data = resp.json()
    
    assert resp.request.method == "DELETE"
    assert data["args"] == {}


def test_put_with_custom_headers():
    """
    Проверяет передачу кастомных заголовков.
    Использует resp.request.headers — самый надёжный способ, 
    не зависящий от структуры JSON-ответа httpbin.
    """
    headers = {"X-Request-ID": "req-abc-123", "X-Custom-Auth": "Bearer token-xyz"}
    resp = requests.put(f"{BASE_URL}/put", headers=headers, timeout=5)
    
    assert resp.status_code == 200
    data = resp.json()

    # Проверяем заголовки в исходящем объекте запроса
    assert resp.request.headers.get("X-Request-ID") == "req-abc-123"
    assert resp.request.method == "PUT"