import requests
import pytest

BASE_URL = "https://postman-echo.com"

def test_get_with_query_params():
    """Проверяем, что GET-запрос корректно отражает квери-параметры в ответе."""
    params = {"search": "pytest", "page": "1"}
    response = requests.get(f"{BASE_URL}/get", params=params)
    
    assert response.status_code == 200
    # Postman Echo возвращает параметры в поле 'args'
    assert response.json()["args"] == params

def test_post_json_body():
    """Проверяем, что POST с JSON-телом возвращает его в поле 'data'."""
    payload = {"username": "alex_isaev", "active": True}
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/post", json=payload, headers=headers)
    
    assert response.status_code == 200
    # Для JSON Postman Echo возвращает тело как строку в поле 'data'
    assert response.json()["data"] == '{"username": "alex_isaev", "active": true}'
    # Проверяем, что сервер увидел наш заголовок Content-Type
    assert response.json()["headers"]["Content-Type"] == "application/json"

def test_post_form_data():
    """Проверяем отправку формы и её отражение в поле 'form'."""
    payload = {"email": "test@example.com", "role": "admin"}
    response = requests.post(f"{BASE_URL}/post", data=payload)
    
    assert response.status_code == 200
    # Для form-data сервер использует поле 'form'
    assert response.json()["form"] == payload

def test_delete_method_reflection():
    """Проверяем, что сервер корректно отражает нестандартный для /post метод DELETE."""
    response = requests.delete(f"{BASE_URL}/post")
    
    assert response.status_code == 200
    # Метод передается внутри объекта args
    assert response.json()["args"]["method"] == "DELETE"

def test_put_with_headers():
    """Проверяем отражение метода PUT и кастомных заголовков."""
    custom_headers = {"X-Custom-Token": "secret-123"}
    response = requests.put(f"{BASE_URL}/put", headers=custom_headers)
    
    assert response.status_code == 200
    assert response.json()["args"]["method"] == "PUT"
    # Заголовки Echo-сервер возвращает с префиксом HTTP_ и в верхнем регистре
    assert response.json()["headers"]["X-Custom-Token"] == "secret-123"