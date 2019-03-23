# The Help command *only* displays commands available to normal users.
# It is assumed that admins already know the admin commands :)
# (though an admin help command is easily done!)

# Registering the command function.
# With latest RiftBot, the new command argument, 'args', is here.
# It contains the message text *after* the command.
async def cmd_help(message, args):

    help_msg = "Available commands:"

    # Iterating through available commands.
    for command in get_commands():

        help_msg += "\n" + get_bot_prefix() + command

    help_embed = discord.Embed(
        title = "**Help**",
        description = help_msg,
        colour = get_embed_color()
    )

    # Send the help embed.
    await message.channel.send(embed = help_embed)

register_command("help", cmd_help)
