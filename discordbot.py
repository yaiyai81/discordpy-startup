import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
import traceback
import random
import logging
import asyncio

client = discord.Client()
bot = commands.Bot(command_prefix='')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    activity = discord.Game(name="アンジニティ", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")
       
async def on_message(message):
    if "おはよう" in message.content:
        word_list = ["ねむい","なに？まだねてろよ","うるせー起こすな！","https://dl.dropboxusercontent.com/s/3qux2f89rgq1d22/gr120.png"]
        await message.channel.send(random.choice(word_list))

@bot.event
async def on_message(message):
    if "おやすみ" in message.content:
        word_list = ["はよねな","さっさとねろ","ねみ…"]
        await message.channel.send(random.choice(word_list))

@bot.event
async def on_message(message):
    if "ななぎして" in message.content:
        word_list = ["ななぎして","な～ぎ","なぎさ太った？"]
        await message.channel.send(random.choice(word_list))

        
bot.run(token)
