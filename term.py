"""
This project create by Waveder.




"""
import os
import getpass
import subprocess
import socket
import art


close = False
commandlist = ["whoami","help","exit","ls","cd","art"]
username = getpass.getuser()
pcname = socket.gethostname()
cdtip = "path: "
filenotfoundmsg = "File Not Found"
arttexttip = "text: "
if not os.name == "nt":
    print("Only support Windows")
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
        try:
            files = os.listdir(pwd)
            for file in files:
                print(file)
        except (OSError,EOFError,KeyboardInterrupt):
            print()
    elif userprompt == "cd":
        try:
           cddir = input(cdtip)
           os.chdir(cddir)
        except (OSError,EOFError,KeyboardInterrupt):
           print(filenotfoundmsg)
    elif userprompt == "art":
        arttext = input(arttexttip)
        print(art.text2art(arttext))
    elif userprompt == "crash":
        raise Exception("Crash command executed")
    else:
        print(f"{userprompt}: command not found")