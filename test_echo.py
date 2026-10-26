import requests

BASE_URL = "https://httpbin.org"


def test_get_with_query_params():
    params = {"key": "value", "limit": "10", "active": "true"}
    resp = requests.get(f"{BASE_URL}/get", params=params, timeout=5)
    
    assert resp.status_code == 200
    data = resp.json()
    
    assert data["args"] == params
    assert data["method"] == "GET"
    assert data["url"].startswith(BASE_URL + "/get")


def test_post_with_json_body():
    payload = {"name": "Alex", "role": "developer", "level": 5}
    resp = requests.post(f"{BASE_URL}/post", json=payload, timeout=5)
    
    assert resp.status_code == 200
    data = resp.json()
    
    assert data["json"] == payload
    assert data["form"] is None
    assert data["method"] == "POST"
    assert data["headers"]["Content-Type"] == "application/json"


def test_post_with_form_data():
    form_data = {"username": "admin", "password": "secret123", "remember": "true"}
    resp = requests.post(f"{BASE_URL}/post", data=form_data, timeout=5)
    
    assert resp.status_code == 200
    data = resp.json()
    
    assert data["form"] == form_data
    assert data["json"] is None
    assert data["method"] == "POST"


def test_delete_method():
    resp = requests.delete(f"{BASE_URL}/delete", timeout=5)
    
    assert resp.status_code == 200
    data = resp.json()
    
    assert data["method"] == "DELETE"
    assert data["args"] == {}


def test_put_with_custom_headers():
    headers = {"X-Request-ID": "req-abc-123", "X-Custom-Auth": "Bearer token-xyz"}
    resp = requests.put(f"{BASE_URL}/put", headers=headers, timeout=5)
    
    assert resp.status_code == 200
    data = resp.json()
    
    header_val = data["headers"].get("X-Request-ID") or data["headers"].get("x-request-id")
    assert header_val == "req-abc-123"
    assert data["method"] == "PUT"
