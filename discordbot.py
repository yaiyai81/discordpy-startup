from discord.ext import commands
import os
import traceback
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random

client = discord.Client()
bot = commands.Bot(command_prefix='')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message):
    if "!じゃんけん" in message.content:
        word_list = ["グー","チョキ","パー"]
        await message.channel.send(random.choice(word_list))
    
client.run(token)
