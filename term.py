import os
import getpass
import subprocess
import socket


close = False
commandlist = ["whoami","help","exit","ls"]
username = getpass.getuser()
pcname = socket.gethostname()
if not os.name == "nt":
    print("请在Windows上启动!")
    close = True

while not close:
    pwd = os.getcwd()
    sysprompt = f"{username}@{pcname}:{pwd}$ "
    try:
        userprompt = input(sysprompt).strip().lower()
    except (KeyboardInterrupt, EOFError):
        print()
        break
    if not userprompt:
        continue
    if userprompt == "help":
        print(commandlist)
    elif userprompt == "exit":
        close = True
    elif userprompt == "whoami":
        print(f"{username}")
    elif userprompt == "ls":
        print(subprocess.getoutput("powershell -Command ls"))
    else:
        print (f"{userprompt}: command not found")
