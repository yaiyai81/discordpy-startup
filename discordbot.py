import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
import traceback
import random
import logging
import asyncio
import re

client = discord.Client()
bot = commands.Bot(command_prefix='')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    activity = discord.Game(name="アンジニティ", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")
    
    # コンソールにBOTとしてログインした名前とUSER-IDを出力
    print('Logged in as')
    print('BOT-NAME :', client.user.name)
    print('BOT-ID   :', client.user.id)
    print('------')  

@bot.event
async def on_message(message):
    global result, judge
    if message.author.bot:
        return
    
    if "おはよう" in message.content:
        word_list = ["ねむい","なに？まだねてろよ","うるせー起こすな！","https://cdn.discordapp.com/attachments/740524923847573555/751840011577458770/gr120.png"]
        await message.channel.send(random.choice(word_list))

    if "おやすみ" in message.content:
        word_list = ["はよねな","さっさとねろ","ねみ…"]
        await message.channel.send(random.choice(word_list))

    if "ななぎして" in message.content:
        word_list = ["ななぎして","な～ぎ","なぎさ太った？",":cat: :boom:"]
        await message.channel.send(random.choice(word_list))
   
    if bot.user in message.mentions:
        reply = f'{message.author.mention} ……なんか用？　大した事やんねえからな。\n```[とりあつかいせつめいしょ]\nおはよう、おやすみ、ななぎして```'
        await message.channel.send(reply)



bot.run(token)
