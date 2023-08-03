import os
import time
from pathlib import Path  

path = Path("calculator") 


def pytest_sessionstart(session):
    os.chdir(f"{path}")
    os.system("wine webcalculator.exe start")
    time.sleep(2.5)

def pytest_sessionfinish(session, exitstatus):
    os.chdir(f"{path}")
    os.system("wine webcalculator.exe stop")
    time.sleep(2.5)
