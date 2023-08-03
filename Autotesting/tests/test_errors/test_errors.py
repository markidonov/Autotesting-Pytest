import requests
from http import HTTPStatus
import pytest


URL = "http://127.0.0.2:17678/api"


def test_port_auto():
    """В случае если указан только адрес хоста,
       будет использован порт по умолчанию (17678).
    """
    try:
        response = requests.get(f'{URL}/state')
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    assert response.json()['statusCode'] == 0, 'Ошибка кода статуса сервера'
    assert response.json()['state'] == "OК", 'Ошибка ответа о состоянии сервера'
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'
    

def test_remainder_zero(code_one, a, d):
    """Ошибка данных. Получение остатка при делении на ноль."""
    try:
        response = requests.post(f'{URL}/remainder', json={"x":a, "y":d})
    except ZeroDivisionError as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise 
    assert response.json()['statusCode'] == 1, 'Ошибка кода статуса сервера'
    assert response.json()['statusMessage'] == code_one, 'Ошибка ответа о состоянии сервера'
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'


def test_division_zero(code_one, a, d):
    """Ошибка данных. Деление на ноль."""
    with pytest.raises(ZeroDivisionError) as err:
        response = requests.post(f'{URL}/division', json={"x":a, "y":d})
        print(f"Unexpected {err=}, {type(err)=}")
        raise ZeroDivisionError
    assert response.json()['statusCode'] == 1, 'Ошибка кода статуса сервера'
    assert response.json()['statusMessage'] == code_one, 'Ошибка ответа о состоянии сервера'
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'


def test_data_half(c,d, code_two):
    """Ошибка данных. Не хватает ключей в теле запроса."""
    try:
        response = requests.post(f'{URL}/addition', json={"x":c})
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    assert response.json()['statusCode'] == 2, 'Ошибка кода статуса сервера'
    assert response.json()['statusMessage'] == code_two, 'Ошибка ответа о состоянии сервера'
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'


def test_int_wrong(c,d, code_three):
    """Ошибка данных. Введено не целое число."""
    try:
        response = requests.post(f'{URL}/addition', json={"x":c, "y":d})
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    assert response.json()['statusCode'] == 3, 'Ошибка кода статуса сервера'
    assert response.json()['statusMessage'] == code_three, 'Ошибка ответа о состоянии сервера'
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'


def test_str_wrong(a, code_three):
    """Ошибка данных. Введено строковое значение вместо числа."""
    try:
        response = requests.post(f'{URL}/addition', json={"x":a, "y":"d"})
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    assert response.json()['statusCode'] == 3, 'Ошибка кода статуса сервера'
    assert response.json()['statusMessage'] == code_three, 'Ошибка ответа о состоянии сервера'
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'


def test_big_number(e,d, code_four):
    """Ошибка данных. Введено слишком большое число."""
    try:
        response = requests.post(f'{URL}/multiplication', json={"x":e, "y":d})
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    assert response.json()['statusCode'] == 4, 'Ошибка кода статуса сервера'
    assert response.json()['statusMessage'] == code_four, 'Ошибка ответа о состоянии сервера'
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'


def test_get_wrong(code_five):
    """Неправильный формат тела запроса."""
    try:
        response = requests.get(f'{URL}/anywrong')
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    assert response.json()['statusCode'] == 5, 'Ошибка кода статуса сервера'
    assert response.json()['statusMessage'] == f': anywrong - {code_five}', 'Ошибка ответа о состоянии сервера'
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'
