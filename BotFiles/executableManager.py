import subprocess
import os
import sys
from dotenv import load_dotenv

executable = '"C:\\Program Files\\Java\\jre1.8.0_251\\bin\\java.exe" -Xms4G -Xmx4G -jar server.jar nogui java'
minecraft_dir = "C:\\Users\\nickg\\Desktop\\Mc Servers\\1.16"

def server_command(cmd, process_):
    process_.stdin.write(cmd+"\n") #just write the command to the input stream

def startServer(process_):
    command=input()
    command=command.lower()

    if process_ is None:
        if command==("start"):
            print("Correct Command")
            os.chdir(minecraft_dir)
            process_ = subprocess.Popen(executable, stdin=subprocess.PIPE)
            print(process_)
            print("Server started.")
            
    elif process_ is not None:
        if command==("stop"):
            process_.kill()