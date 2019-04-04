import os
import discord

# Get bot token

token = ""
with open("token.cfg") as t:
    token = t.read()

# Create bot client

client = discord.Client()

# IDs of bot admins

admins = []

# User attributes

attr = {}

# Default prefix

prefix = "r."

# Default color, to be used for embeds.

color = discord.Colour.blue()

# API functions

def register_command(command, function):

    commands[command] = function

def register_admin_command(command, function):

    admin_commands[command] = function

def get_commands():
    return commands

def get_admin_commands():
    return admin_commands

def get_bot_prefix():
    return prefix

def get_embed_color():
    return color

def set_user_attr(user, attribute, value):
    name = str(user.id)
    attr[name][attribute] = value
    
def get_user_attr(user, attribute):
    name = str(user.id)
    if name in attr.keys():
        if attribute in attr[name].keys():
            return attr[name][attribute]
    return None

def command_exists(command):

    if command in commands:
        return True

    if command in admin_commands:
        return True

    return False

def is_admin(id):

    return id in admins

async def restart():
    os.system('./restart.sh')
    # Exit cleanly
    exit()
    
# Initializing the command dictionaries

# Commands anyone can use!   
commands = {}

# Commands only accessible to admins
admin_commands = {}

# Load commands

os.chdir('commands')

for filename in os.listdir():

    # Make sure it isn't this source file. Needs to be abstracted in the future.
    if filename != 'bot.py':

        # Open the file.
        with open(filename) as file:

            # Run the file in the current scope.
            exec(file.read())

# When message detected

@client.event
async def on_message(message):
    
    # If it looks like a command...
    if message.content.startswith(prefix):

        for command in commands:

            if message.content.startswith(prefix+command):

                try:
                    args = message.content[len(message.content.split()[0])+1:]
                    await commands[command](message, args)

                except Exception as e:
                    msg = "**Exception in command `" + command + "`:**\n" + str(e)
                    await message.channel.send(msg)

        # Checking for admin commands as well! But only if the author is an admin.        
        if is_admin(str(message.author.id)):

            for command in admin_commands:

                if message.content.startswith(prefix+command):

                    try:
                        args = message.content[len(message.content.split()[0])+1:]
                        await commands[command](message, args)

                    except Exception as e:
                        msg = "**Exception in command `" + command + "`:**\n" + str(e)
                        await message.channel.send(msg)


# When logged in

@client.event
async def on_ready():
    print("Logged in as\n" + client.user.name + "\n" + str(client.user.id) + "\n---")

# Log in

client.run(token)
