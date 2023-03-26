import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random

load_dotenv('bot_config.env')  # Load environment variables from .env file
token = os.getenv("DISCORD_TOKEN")
bot_name = os.getenv("BOT_NAME")

intents = discord.Intents.default()
intents.members = True  # You need to enable the Members Intent to get information about members in voice channels.

bot = commands.Bot(command_prefix="-", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name="pick",
             description="Pick a random user from a voice channel")
async def pick_random_user(ctx):
  # Get the voice channel that the command user is currently in
  voice_state = ctx.author.voice
  if not voice_state:
    await ctx.send(
      f"Tens que estar num canal de voz :loudspeaker: e o {bot_name} tem que ter acesso a este canal"
    )
    return
  channel = voice_state.channel

  # Get a list of users currently in the voice channel
  members = channel.members

  # Pick a random user from the list of members
  random_member = random.choice(members)

  # Send a message with the name of the picked user
  await ctx.send(
    f"O colaborador do canal {channel.name} que será sacrificado é o {random_member.mention}! Parabéns! :skull:"
  )


bot.run(token)
