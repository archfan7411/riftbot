import os
import discord

# Get bot token

token = ""
with open("token.cfg") as t:
    token = t.read()

# Default prefix

prefix = "/"

# API functions

def register_command(command, function):
    commands[command] = function

def set_prefix(newPrefix):
    prefix = newPrefix

def command_exists(command):
    if command in commands:
        return true
    else:
        return false
    
async def send(channel, response):
    await channel.send(response)
    
# Initialized with no commands
    
commands = {}

# Default commands should be registered here.

async def cmd_help(message):
    response = "Available commands:"
    for command in commands:
        response += "\n" + prefix + command
    await send(message.channel, response)
register_command("help", cmd_help)
    
# End default command registration

# Load external commands

os.chdir('commands')
for filename in os.listdir():
    if filename != 'bot.py':
        with open(filename) as file:
            exec(file.read())

# Create bot client object

client = discord.Client()

# When message detected

@client.event
async def on_message(message):
    for command in commands:
        if message.content.startswith(prefix+command):
            await commands[command](message)

# When logged in

@client.event
async def on_ready():
    print("Logged in as\n" + client.user.name + "\n" + str(client.user.id) + "\n---")

# Log in

client.run(token)
