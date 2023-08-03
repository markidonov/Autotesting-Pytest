import requests
from http import HTTPStatus
import pytest


URL = 'http://127.0.0.1:17678/api'



def test_server_auto():
    """Если адрес хоста так же не указан будет
    использован адрес по умолчанию (127.0.0.1).
    """
    try:
        response = requests.get(f'{URL}/state')
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    assert response.json()['statusCode'] == 0, 'Ошибка кода статуса сервера'
    assert response.json()['state'] == "OК", 'Ошибка ответа о состоянии сервера'
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'
    

def test_addition_count(a, b):
    """Проверка правильности работы вычислительной логики 
    при обращении к эндпоинту /addition.
    """
    try:
        response = requests.post(f'{URL}/addition', json={"x":a, "y":b})
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    assert response.json()['statusCode'] == 0, 'Ошибка кода статуса сервера'
    assert response.json()['result'] == a+b, 'Ошибка ответа о состоянии сервера'
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'


def test_remainder_count( a, b):
    """Проверка правильности работы вычислительной логики 
    при обращении к эндпоинту /remainder.
    """
    try:
        response = requests.post(f'{URL}/remainder', json={"x":b, "y":a})
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    assert response.json()['statusCode'] == 0, 'Ошибка кода статуса сервера'
    assert response.json()['result'] == b%a, 'Ошибка ответа о состоянии сервера'
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'


def test_division_count( a, b):
    """Проверка правильности работы вычислительной логики 
    при обращении к эндпоинту /division.
    """
    try:
        response = requests.post(f'{URL}/division', json={"x":b, "y":a})
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    assert response.json()['statusCode'] == 0, 'Ошибка кода статуса сервера'
    assert response.json()['result'] == b//a, 'Ошибка ответа о состоянии сервера'
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'


def test_multiplication_count(a, b):
    """Проверка правильности работы вычислительной логики 
    при обращении к эндпоинту /multiplication.
    """
    try:
        response = requests.post(f'{URL}/multiplication', json={"x":a, "y":b})
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    assert response.json()['statusCode'] == 0, 'Ошибка кода статуса сервера'
    assert response.json()['result'] == a*b, 'Ошибка ответа о состоянии сервера'
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'

