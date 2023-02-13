import os
import gettext
import random
import discord
import interactions
from discord.ext import commands
# from discord_slash import SlashCommand
# from discord_slash.utils import manage_commands

from bot_config import BOT_NAME, BOT_ENV_TOKEN

bot = interactions.Client(token=BOT_ENV_TOKEN)

# Implementation

def pick_impl(ctx, count):
    if count < 1:
        # [LOC] Used with ;pick <n> when n < 1.
        return str('You must pick at least one member.')


    author = ctx.author
    if not (hasattr(author, 'voice') and author.voice and author.voice.channel):
        # [LOC] Used with ;pick when user not in voice channel.
        print(hasattr(author, 'voice'))
        return str(
            'You must be in a voice channel :loudspeaker: '
            'and {} must have access to this channel.'
        ).format(BOT_NAME)

    members = author.voice.channel.members
    if len(members) < 2:
        # [LOC] Used with ;pick when user is alone in voice channel.
        return str(
            'You are alone in this channel :thinking: Call some friends!\n'
            'Do you have friends, are you?'
        )

    if len(members) < count:
        # [LOC] Used with ;pick <n> when n greater than number of members in voice channel.
        return str('Too few members in this channel')

    sample = random.sample(members, count)
    return ', '.join([user.mention for user in sample])


@bot.command(
    name="pick_user",
    description="Mamaki oh nabo!",
    options=[
        interactions.Option(
            name="count",
            description="members count (1 by default)",
            type=interactions.OptionType.INTEGER,
            required=False,
        ),
    ],
)
async def pick_user(ctx: interactions.CommandContext, count: 1):
    # await ctx.send(f"You said '{text}' https://cdn.shopify.com/s/files/1/0345/9180/1483/files/ek-2-player-ek--optimized.png?v=1642104393!")
    await ctx.send(content=(pick_impl(ctx, count)))

# Run bot
bot.start()
