"""
##########################################
Based on Code Written By: tschuy 

Repo Link: https://github.com/tschuy/minecraft-server-control/blob/master/minecraft.py

GitHub Link: https://github.com/tschuy
########################################## 
"""

import threading
import shutil
from os.path import join
import os
import time
import sys
import datetime
minecraft_dir = "C:\\Users\\nickg\\Desktop\\Mc Servers\\1.16"


def server_command(cmd):
    os.system('screen -S minecraft -X stuff "{}\015"'.format(cmd))

def start():
    if not status():
        os.chdir(minecraft_dir)
        os.system('"C:\\Program Files\\Java\\jre1.8.0_251\\bin\\java.exe" -Xms4G -Xmx4G -jar server.jar nogui java')
        print("Server started.")
    else:
        print("Server already started.")

def stop():
    if status():
        server_command('stop')
        print("Server stopped.")
    else:
        print("Server not running.")

def status():
    output = os.popen('screen -ls').read()
    if '.minecraft'  in output:
        print("Server is running.")
        return True
    else:
        print("Server is not running.")
        return False

def main(input_):
    if input_ == 'start':
        th = threading.Thread(target=start())
        th.start()
        return f'Starting server... Server Status: {status()}'
    elif input_ == 'stop':
        stop()
        return f"Stopping server... Server Status: {status()}"
    else:
        return 'Unknown command.'

def ListenServerCommands(input):
    
    response = main(input)
    return response

        