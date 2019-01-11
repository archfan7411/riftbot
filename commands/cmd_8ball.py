import random
async def cmd_8ball(message):
    channel = message.channel
    responses = ["Yep!", "Of course.", "Absolutely!", "Eh, ask again.", "Unsure", "What? No!", "I don't think so.", "Probably a bad idea."]
    response = random.choice(responses)
    await send(channel, response)
register_command("8ball", cmd_8ball)
