import allure
import requests

BASE_URL = "https://httpbin.org"


@allure.feature("HTTP-методы httpbin")
@allure.title("GET-запрос с query-параметрами")
@allure.description("Проверяет передачу query-параметров в GET-запросе и корректность HTTP-метода через resp.request.method.")
def test_get_with_query_params():
    params = {"key": "value", "limit": "10", "active": "true"}

    with allure.step(f"Отправка GET-запроса на {BASE_URL}/get с параметрами {params}"):
        resp = requests.get(f"{BASE_URL}/get", params=params, timeout=5)

    with allure.step("Проверка статус-кода и переданных параметров"):
        assert resp.status_code == 200
        data = resp.json()
        assert data["args"] == params
        assert resp.request.method == "GET"
        assert data["url"].startswith(BASE_URL + "/get")


@allure.feature("HTTP-методы httpbin")
@allure.title("POST-запрос с JSON-телом")
@allure.description("Проверяет отправку JSON-тела в POST-запросе и отсутствие данных формы в ответе.")
def test_post_with_json_body():
    payload = {"name": "Alex", "role": "developer", "level": 5}

    with allure.step(f"Отправка POST-запроса с JSON: {payload}"):
        resp = requests.post(f"{BASE_URL}/post", json=payload, timeout=5)

    with allure.step("Проверка распознавания JSON сервером"):
        assert resp.status_code == 200
        data = resp.json()
        assert data["json"] == payload
        assert not data.get("form")
        assert resp.request.method == "POST"


@allure.feature("HTTP-методы httpbin")
@allure.title("POST-запрос с данными формы (form-data)")
@allure.description("Проверяет отправку данных формы в формате application/x-www-form-urlencoded.")
def test_post_with_form_data():
    form_data = {"username": "admin", "password": "secret123", "remember": "true"}

    with allure.step("Отправка POST-запроса с form-data"):
        resp = requests.post(f"{BASE_URL}/post", data=form_data, timeout=5)

    with allure.step("Проверка получения данных формы сервером"):
        assert resp.status_code == 200
        data = resp.json()
        assert data["form"] == form_data
        assert not data.get("json")
        assert resp.request.method == "POST"


@allure.feature("HTTP-методы httpbin")
@allure.title("Выполнение DELETE-запроса")
@allure.description("Проверяет корректную обработку DELETE-запроса и отсутствие query-параметров.")
def test_delete_method():
    with allure.step(f"Отправка DELETE-запроса на {BASE_URL}/delete"):
        resp = requests.delete(f"{BASE_URL}/delete", timeout=5)

    with allure.step("Проверка статус-кода и метода запроса"):
        assert resp.status_code == 200
        data = resp.json()
        assert resp.request.method == "DELETE"
        assert data["args"] == {}


@allure.feature("HTTP-методы httpbin")
@allure.title("PUT-запрос с кастомными заголовками")
@allure.description("Проверяет передачу пользовательских HTTP-заголовков X-Request-ID и X-Custom-Auth в PUT-запросе.")
def test_put_with_custom_headers():
    headers = {
        "X-Request-ID": "req-abc-123",
        "X-Custom-Auth": "Bearer token-xyz"
    }

    with allure.step("Отправка PUT-запроса с кастомными заголовками"):
        resp = requests.put(f"{BASE_URL}/put", headers=headers, timeout=5)

    with allure.step("Проверка статус-кода и наличия заголовка X-Request-ID"):
        assert resp.status_code == 200
        header_val = (
            resp.request.headers.get("x-request-id") or
            resp.request.headers.get("x_request_id") or
            resp.request.headers.get("X-Request-ID")
        )
        assert header_val == "req-abc-123"
        assert resp.request.method == "PUT"
