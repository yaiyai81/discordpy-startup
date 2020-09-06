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
    
@bot.event
async def on_message(message):
    global result, judge
    if message.author.bot:
        return
    
    if "おはよう" in message.content:
        word_list = ["ねむい","なに？まだねてろよ","うるせー起こすな！","https://cdn.discordapp.com/attachments/740524923847573555/751840011577458770/gr120.png"]
        await message.channel.send(random.choice(word_list))

    if "おやすみ" in message.content:
        word_list2 = ["はよねな","さっさとねろ","ねみ…"]
        await message.channel.send(random.choice(word_list2))

    if "ななぎして" in message.content:
        word_list3 = ["ななぎして","な～ぎ","なぎさ太った？",":cat: :boom:"]
        await message.channel.send(random.choice(word_list3))
   
    if bot.user in message.mentions:
        reply = f'{message.author.mention} ……なんか用？　大した事やんねえからな。\n```[せつめいしょ]\nおはよう、おやすみ、ななぎして\nじゃんけん→Shinobuの返事→ぐー、ちょき、ぱー```'
        await message.channel.send(reply)


    if message.content == "じゃんけん":
        await message.channel.send("お前、暇人だな。\nじゃあ、最初はぐー、じゃんけん……")
        
        jkbot = random.choice(("ぐー", "ちょき", "ぱー"))
        draw = random.choice(("あいこじゃん。つまんねーな",
                              "はいはい、引き分け","あいこ～。もう終わり？"))
        wn = random.choice(("チッ、お前の勝ちだよ……",
                              "くそ、負けた……次は勝つからな！","負けた……はぁ？　ふざけんなよ……","負けたし……お前……後出ししただろ！"))
        lst = random.choice(("僕の勝ち！お前弱いな～～！！！",
                              "僕の勝ち～～～～！！！まあ、何度でも勝負してやるよ","お前の負け。僕って強いだろ？","お前の負け！　雑魚だな～！"))

        def jankencheck(m):
            return (m.author == message.author) and (m.content in ['ぐー', 'ちょき', 'ぱー'])

        reply = await bot.wait_for("message", check=jankencheck)
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
 
    
bot.run(token)
