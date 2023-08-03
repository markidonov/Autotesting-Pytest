import requests
from http import HTTPStatus

URL = 'http://127.0.0.1:8000/api'


def test_get_state():
    """Запуск приложения осуществляется с помощью команды
    start с указанием дополнительных аргументов host и port.
    """
    try:
        response = requests.get(f'{URL}/state')
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    assert response.json()['statusCode'] == 0, 'Ошибка кода статуса сервера'
    assert response.json()['state'] == "OК", 'Ошибка ответа о состоянии сервера'
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'


def test_options():
    """Проверка ответа сервера при запросе OPTIONS."""
    try:
        response = requests.options(f'{URL}/')
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'


def test_addition_post():
    """Проверка ответа сервера при POST-запросе 
    к эндпоинту /addition.
    """
    try:
        response = requests.post(f'{URL}/addition', json={"x":0, "y":0})
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    assert response.json()['statusCode'] == 0, 'Ошибка кода статуса сервера'
    assert response.json()['result'] == 0, 'Ошибка ответа о состоянии сервера'
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'


def test_multiplication_post():
    """Проверка ответа сервера при POST-запросе 
    к эндпоинту /multiplication.
    """
    try:
        response = requests.post(f'{URL}/multiplication', json={"x":0, "y":0})
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    assert response.json()['statusCode'] == 0, 'Ошибка кода статуса сервера'
    assert response.json()['result'] == 0, 'Ошибка ответа о состоянии сервера'
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'


def test_division_post():
    """Проверка ответа сервера при POST-запросе 
    к эндпоинту /division.
    """
    try:
        response = requests.post(f'{URL}/division', json={"x":10, "y":20})
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    assert response.json()['statusCode'] == 0, 'Ошибка кода статуса сервера'
    assert response.json()['result'] == 0, 'Ошибка ответа о состоянии сервера'
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'


def test_remainder_post():
    """Проверка ответа сервера при POST-запросе 
    к эндпоинту /remainder.
    """
    try:
        response = requests.post(f'{URL}/remainder', json={"x":10, "y":20})
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    assert response.json()['statusCode'] == 0, 'Ошибка кода статуса сервера'
    assert response.json()['result'] == 10, 'Ошибка ответа о состоянии сервера'
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'

