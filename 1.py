import subprocess

bat_file = r'C:\1.bat'

command = f'runas /user:Administrator "{bat_file}"'

subprocess.run(command, shell=True)
