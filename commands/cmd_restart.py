async def cmd_restart(message, args):
    await message.channel.send("Restarting!")
    restart()
register_admin_command("restart", cmd_restart)
