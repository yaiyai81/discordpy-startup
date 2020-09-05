from discord.ext import commands
import os
import traceback
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import logging
logging.basicConfig(level=logging.ERROR)

bot = commands.Bot(command_prefix='')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    activity = discord.Game(name="アンジニティ", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")

@bot.event
async def on_message(message):

    global result, judge
    if message.author.bot: 
        return

    if message.content == "じゃんけん":
        await message.channel.send("はいはい。最初はぐー、じゃんけん")

        jkbot = random.choice(("ぐー", "ちょき", "ぱー"))
        draw = "引き分け。実質僕の勝ちだな"
        wn = "は？　お前後出ししただろ"
        lst = random.choice(("僕の勝ち！弱ｗｗｗｗｗｗｗｗｗｗｗｗやめたら？じゃんけん",
                              "僕の勝ちだな。ざ～こ"))

        def jankencheck(m):
            return (m.author == message.author) and (m.content in ['ぐー', 'ちょき', 'ぱー'])

        reply = await client.wait_for("message", check=jankencheck)
        if reply.content == jkbot:
            judge = draw
        else:
            if reply.content == "ぐー":
                if jkbot == "ちょき":
                    judge = wn
                else:
                    judge = lst

            elif reply.content == "ちょき":
                if jkbot == "ぱー":
                    judge = wn
                else:
                    judge = lst

            else:
                if jkbot == "ぐー":
                    judge = wn
                else:
                    judge = lst

        await message.channel.send(judge)
        
@bot.event
async def on_message(message):
        if "おはよう" in message.content:
        word_list = ["ねむい","なに？　寝てろよ","zzz..."]
        await message.channel.send(random.choice(word_list))
    
bot.run(token)
