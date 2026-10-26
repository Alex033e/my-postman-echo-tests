import requests
import pytest

BASE_URL = "https://postman-echo.com"

def test_get_with_query_params():
    """Проверяем, что GET-запрос корректно отражает квери-параметры в ответе."""
    params = {"search": "pytest", "page": "1"}
    response = requests.get(f"{BASE_URL}/get", params=params)
    
    assert response.status_code == 200
    assert response.json()["args"] == params

def test_post_json_body():
    """Проверяем, что POST с JSON-телом возвращает его в поле 'json'."""
    payload = {"username": "alex_isaev", "active": True}
    response = requests.post(f"{BASE_URL}/post", json=payload)
    
    assert response.status_code == 200
    assert response.json()["json"] == payload

def test_post_form_data():
    """Проверяем отправку формы и её отражение в поле 'form'."""
    payload = {"email": "test@example.com", "role": "admin"}
    response = requests.post(f"{BASE_URL}/post", data=payload)
    
    assert response.status_code == 200
    assert response.json()["form"] == payload

def test_delete_method_reflection():
    """Проверяем отражение метода DELETE через универсальный эндпоинт /anything."""
    response = requests.delete(f"{BASE_URL}/anything")
    
    assert response.status_code == 200
    # В ответе /anything информация о методе всегда находится на верхнем уровне
    assert response.json()["method"] == "DELETE"

def test_put_with_headers():
    """Проверяем отражение метода PUT и кастомных заголовков через /anything."""
    custom_headers = {"X-Custom-Token": "secret-123"}
    response = requests.put(f"{BASE_URL}/anything", headers=custom_headers)
    
    assert response.status_code == 200
    # Проверяем, что сервер правильно определил метод
    assert response.json()["method"] == "PUT"
    # Проверяем, что сервер вернул наш кастомный заголовок в ответе
    assert response.json()["headers"]["X-Custom-Token"] == "secret-123"