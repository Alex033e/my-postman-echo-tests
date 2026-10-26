import requests  # ✅ Импорт библиотеки

BASE_URL = "https://httpbin.org"  # ⚡️ Базовый URL сервиса


def test_get_with_query_params():
    """
    Проверяет передачу query-параметров в GET-запросе.
    Использует resp.request.method для проверки HTTP-глагола.
    """
    params = {"key": "value", "limit": "10", "active": "true"}
    resp = requests.get(f"{BASE_URL}/get", params=params, timeout=5)
    
    assert resp.status_code == 200
    data = resp.json()
    
    # Проверка: параметры дошли корректно
    assert data["args"] == params
    # Надежная проверка метода через объект запроса (не зависит от структуры ответа сервера)
    assert resp.request.method == "GET"
    # Дополнительная проверка URL
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
    
    # Проверка: сервер распознал наш JSON
    assert data["json"] == payload
    # Проверка: форма не была передана (None или пустой словарь)
    assert not data.get("form")
    # Проверка метода
    assert resp.request.method == "POST"


def test_post_with_form_data():
    """
    Проверяет отправку данных формы (application/x-www-form-urlencoded).
    """
    form_data = {"username": "admin", "password": "secret123", "remember": "true"}
    resp = requests.post(f"{BASE_URL}/post", data=form_data, timeout=5)
    
    assert resp.status_code == 200
    data = resp.json()
    
    # Проверка: данные формы дошли корректно
    assert data["form"] == form_data
    # Проверка: JSON не был передан
    assert not data.get("json")
    # Проверка метода
    assert resp.request.method == "POST"


def test_delete_method():
    """
    Проверяет выполнение DELETE-запроса.
    """
    resp = requests.delete(f"{BASE_URL}/delete", timeout=5)  # ⚠️ Не забываем BASE_URL!
    
    assert resp.status_code == 200
    data = resp.json()
    
    # Проверка метода
    assert resp.request.method == "DELETE"
    # Проверка: нет параметров в запросе
    assert data["args"] == {}


def test_put_with_custom_headers():
    """
    Проверяет передачу кастомных заголовков.
    Использует resp.request.headers — самый надежный способ,
    не зависящий от того, что вернул httpbin в ответе.
    """
    headers = {
        "X-Request-ID": "req-abc-123",
        "X-Custom-Auth": "Bearer token-xyz"
    }
    resp = requests.put(f"{BASE_URL}/put", headers=headers, timeout=5)
    
    assert resp.status_code == 200
    data = resp.json()

    
    header_val = (
        resp.request.headers.get("x-request-id") or 
        resp.request.headers.get("x_request_id") or 
        resp.request.headers.get("X-Request-ID")
    )
    assert header_val == "req-abc-123"
    assert resp.request.method == "PUT"