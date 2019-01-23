import os
import discord

# Get bot token

token = ""
with open("token.cfg") as t:
    token = t.read()

# Default prefixes

prefix = "/"
lib_prefix = "lib_"
preload_prefix = "preload_"

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
    if filename.startswith(preload_prefix):
        with open(filename) as file:
            exec(file.read())
            
for filename in os.listdir():
    if filename != 'bot.py' and filename.startswith(lib_prefix) == False and filename.startswith(preload_prefix) == False:
        with open(filename) as file:
            exec(file.read())

# Create bot client object

client = discord.Client()

# When message detected

@client.event
async def on_message(message):
    for command in commands:
        if message.content.startswith(prefix+command):
            try:
                await commands[command](message)
            except Exception as e:
                msg = "**Exception in command `"+command+"`:**\n"+e
                message.channel.send(msg)

# When logged in

@client.event
async def on_ready():
    print("Logged in as\n" + client.user.name + "\n" + str(client.user.id) + "\n---")

# Log in

client.run(token)
