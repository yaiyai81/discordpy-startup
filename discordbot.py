import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
import traceback
import random
import logging
import asyncio

bot = commands.Bot(command_prefix='')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    activity = discord.Game(name="アンジニティ", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")
    
@bot.event
async def on_message(message):
    if client.user != message.author:
        if message.content.startswith("おはよう"):
            m = "おはようございます" + message.author.name + "さん！"
            await client.send_message(message.channel, m)
        if message.content.startswith("こんにちは"):
            m = "こんにちは" + message.author.name + "さん！"
            await client.send_message(message.channel, m)
            
bot.run(token)
