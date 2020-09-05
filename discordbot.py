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
    
@bot.event
async def on_message(message): #メッセージを受け取る関数なので必ず必要
    if message.content == "おはよう": #:を忘れずつけよう！Enterを押すと自動で4文字分あけて改行されるよ！
        await client.send_message(message.channel, "ねむい")

    if message.content == "占い":
#レスポンスされる運勢のリストを作成
        unsei = ["大吉", "中吉", "吉", "末吉", "小吉", "凶", "大凶"]
        choice = random.choice(unsei) #randomモジュール使用
        await message.send_message(message.channel, choice)
            
bot.run(token)
