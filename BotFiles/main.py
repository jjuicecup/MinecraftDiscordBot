import os
import discord
from serverManager import ListenServerCommands
from dotenv import load_dotenv

TOKEN = '...'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    messageContent = message.content
    response = ListenServerCommands(messageContent)
    await message.channel.send(response)

client.run(TOKEN)