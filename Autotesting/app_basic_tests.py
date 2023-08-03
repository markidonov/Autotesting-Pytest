import os
import subprocess
from pathlib import Path 
from contextlib import redirect_stdout


path = Path("calculator") 
os.chdir(f"{path}")
print( os.getcwd())
URL = "http://127.0.0.2:17678/api"


app_commands =[
    "wine webcalculator.exe start",
    "wine webcalculator.exe restart",
    "wine webcalculator.exe show_log",
    "wine webcalculator.exe --help",
    "wine webcalculator.exe stop"
]


with open('../logs/test_app_commands.txt', 'w') as f:
    with redirect_stdout(f):
        for command in app_commands:
            try:
                command_res = subprocess.run(command, capture_output = False,
                    text = True, shell=True,)
                if command_res.returncode == 0:
                    print(f'Команда - {command.split()[-1]} успешно отработала')
                else:
                    print(f'Внимание! С командой - {command.split()[-1]} - возникли проблемы')    
                print(command_res)
                if command_res.stderr != None:
                    print(command_res.stderr)
                print('------------------------------------------------------')
            except Exception as err:    
                print(f"Unexpected {err=}, {type(err)=}")
            
        os.system("wine webcalculator.exe stop")
