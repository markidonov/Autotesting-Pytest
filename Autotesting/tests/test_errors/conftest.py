import os
import time
from pathlib import Path  
import requests
from http import HTTPStatus
from contextlib import redirect_stdout


path = Path("calculator") 
host= "127.0.0.2"
port = "17678"
URL = f"http://{host}:{port}/api"


def test_restart():
    """Команда restart осуществляет перезапуск приложения,
       После выполнения команды приложение продолжает работать
       на том же адресе и порту, что и до перезапуска.
    """
    os.system("wine webcalculator.exe restart")
    try:
        response = requests.get(f'{URL}/state')
    except Exception:
        raise
    assert response.json()['statusCode'] == 0, 'Ошибка кода статуса сервера'
    assert response.json()['state'] == "OК", 'Ошибка ответа о состоянии сервера'
    assert response.status_code == HTTPStatus.OK, 'Ошибка ответа от сервера'
    


def pytest_sessionstart(session):
    os.chdir(f"{path}")
    os.system(f"wine webcalculator.exe start {host}")
    time.sleep(2.5)
    with open('../logs/test_restart.txt', 'w') as f:
        with redirect_stdout(f):
            try:
                test_restart()
                print("Команда restart осуществила перезапуск приложения,\n"
                      "После выполнения команды приложение продолжает работать\n"
                      "на том же адресе и порту, что и до перезапуска.")
            except Exception as err:
                print(f"При проверке команды restart возникла"
                      f" ошибка:\n{err=}, \n{type(err)=}")
                os.system(f"wine webcalculator.exe stop")
                os.system(f"wine webcalculator.exe start {host}")


def pytest_sessionfinish(session, exitstatus):
    os.chdir(f"{path}")
    os.system("wine webcalculator.exe stop")
    time.sleep(2.5)
