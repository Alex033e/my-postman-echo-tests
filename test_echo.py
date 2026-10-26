import requests

BASE_URL = "https://httpbin.org"


def test_get_with_query_params():
<<<<<<< HEAD
    """
    Проверяет передачу query-параметров в GET-запросе.
    Использует resp.request.method для проверки HTTP-глагола.
    """
=======
>>>>>>> efdba26ff5173a77dd8934b9b6163ec9142c6279
    params = {"key": "value", "limit": "10", "active": "true"}
    resp = requests.get(f"{BASE_URL}/get", params=params, timeout=5)
    
    assert resp.status_code == 200
    data = resp.json()
    
    assert data["args"] == params
<<<<<<< HEAD
    assert resp.request.method == "GET"
=======
    assert data["method"] == "GET"
>>>>>>> efdba26ff5173a77dd8934b9b6163ec9142c6279
    assert data["url"].startswith(BASE_URL + "/get")


def test_post_with_json_body():
<<<<<<< HEAD
    """
    Проверяет отправку JSON-тела.
    Использует not data.get("form") для совместимости с None и пустым словарём.
    """
=======
>>>>>>> efdba26ff5173a77dd8934b9b6163ec9142c6279
    payload = {"name": "Alex", "role": "developer", "level": 5}
    resp = requests.post(f"{BASE_URL}/post", json=payload, timeout=5)
    
    assert resp.status_code == 200
    data = resp.json()
    
    assert data["json"] == payload
<<<<<<< HEAD
    assert not data.get("form")
    assert resp.request.method == "POST"


def test_post_with_form_data():
    """
    Проверяет отправку данных формы (application/x-www-form-urlencoded).
    """
=======
    assert data["form"] is None
    assert data["method"] == "POST"
    assert data["headers"]["Content-Type"] == "application/json"


def test_post_with_form_data():
>>>>>>> efdba26ff5173a77dd8934b9b6163ec9142c6279
    form_data = {"username": "admin", "password": "secret123", "remember": "true"}
    resp = requests.post(f"{BASE_URL}/post", data=form_data, timeout=5)
    
    assert resp.status_code == 200
    data = resp.json()
    
    assert data["form"] == form_data
<<<<<<< HEAD
    assert not data.get("json")
    assert resp.request.method == "POST"


def test_delete_method():
    """
    Проверяет выполнение DELETE-запроса.
    """
=======
    assert data["json"] is None
    assert data["method"] == "POST"


def test_delete_method():
>>>>>>> efdba26ff5173a77dd8934b9b6163ec9142c6279
    resp = requests.delete(f"{BASE_URL}/delete", timeout=5)
    
    assert resp.status_code == 200
    data = resp.json()
    
<<<<<<< HEAD
    assert resp.request.method == "DELETE"
=======
    assert data["method"] == "DELETE"
>>>>>>> efdba26ff5173a77dd8934b9b6163ec9142c6279
    assert data["args"] == {}


def test_put_with_custom_headers():
<<<<<<< HEAD
    """
    Проверяет передачу кастомных заголовков.
    Использует resp.request.headers — самый надёжный способ, 
    не зависящий от структуры JSON-ответа httpbin.
    """
=======
>>>>>>> efdba26ff5173a77dd8934b9b6163ec9142c6279
    headers = {"X-Request-ID": "req-abc-123", "X-Custom-Auth": "Bearer token-xyz"}
    resp = requests.put(f"{BASE_URL}/put", headers=headers, timeout=5)
    
    assert resp.status_code == 200
    data = resp.json()
<<<<<<< HEAD

    # Проверяем заголовки в исходящем объекте запроса
    assert resp.request.headers.get("X-Request-ID") == "req-abc-123"
    assert resp.request.method == "PUT"
=======
    
    header_val = data["headers"].get("X-Request-ID") or data["headers"].get("x-request-id")
    assert header_val == "req-abc-123"
    assert data["method"] == "PUT"
>>>>>>> efdba26ff5173a77dd8934b9b6163ec9142c6279
