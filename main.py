import discord
import config
import asyncio
import os
from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), activity=discord.Activity(name='Moon Halo 🌑', type=discord.ActivityType.listening), intents=discord.Intents.all())

# Bot ON
@bot.event
async def on_ready():
    print(f'{bot.user.name}, ready to go!')

def load():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            try:
                bot.load_extension(f"commands.{filename[:-3]}")
            except Exception as e:
                print(e)


load()
bot.run(config.token)