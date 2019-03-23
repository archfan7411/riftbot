import random

async def cmd_8ball(message, args):

    responses = ["Yep!", "Of course.", "Absolutely!", "Eh, ask again.", "Unsure", "What? No!", "I don't think so.", "Probably a bad idea."]

    response = random.choice(responses)

    random_embed = discord.Embed(
        title = "**8ball**",
        description = response,
        colour = get_embed_color()
    )

    await message.channel.send(embed = random_embed)

register_command("8ball", cmd_8ball)
