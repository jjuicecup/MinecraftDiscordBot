import os
import discord
from dotenv import load_dotenv
from executableManager import startServer

process = None
while True:
    startServer(process)