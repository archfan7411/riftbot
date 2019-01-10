async def cmd_debug(message):
    channel = message.channel
    content = message.content
    await send(channel, ("You said " + content))
register_command("debug", cmd_debug)
