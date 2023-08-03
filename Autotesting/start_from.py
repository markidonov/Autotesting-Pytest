# Стартовый файл для запуска тестов
import os
from pathlib import Path 
import shutil, glob

path = Path("calculator") 
path_logs = Path('logs')



pytest_commands =[
    "pytest tests/test_api -v -rA | tee logs/test_api.txt",
    "pytest tests/test_functions -v -rA | tee logs/test_functions.txt",
    "pytest tests/test_errors -v -rA | tee logs/test_errors.txt"
]


if __name__ == "__main__":
    
    # Проверка базовых команд приложения
    os.system("python app_basic_tests.py")
    
    #Тестирование работы приложения
    for command in pytest_commands:
        try:
            os.system(command)
        except Exception as err:    
            os.system("wine webcalculator.exe stop")
            print(f"Unexpected {err=}, {type(err)=}")

    # Собрать результаты в файле 'results.txt'
    os.chdir(f"{path_logs}")
    with open('../webcalculator/webcalculator.log', 'wb') as outfile:
        x=0
        for filename in glob.glob('*.txt'):
            if x>0:
                outfile.write(b'\n\n\n\n\n')
            outfile.write(filename.encode('ascii'))
            outfile.write(b'\n\n')
            x+=1
            with open(filename, 'rb') as readfile:
                shutil.copyfileobj(readfile, outfile)
                