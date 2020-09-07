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
        word_list = ["ん～……？　ねむい……","なに……？まだねてろよ……","うるせーな、起こすな！","https://cdn.discordapp.com/attachments/740524923847573555/751840011577458770/gr120.png","ぐぅ……あと1時間……"]
        await message.channel.send(random.choice(word_list))

    if "おやすみ" in message.content:
        word_list2 = ["なんだよ、はよねろ","あーはいはい。さっさとねろよ……","……僕はまだ寝ないけど？","はいはい、おやすみ……"]
        await message.channel.send(random.choice(word_list2))

    if "ななぎして" in message.content:
        word_list3 = ["ななぎして","な～ぎ……って僕はやんねーから……","最近、なぎさ太ったんじゃね？",":cat: :boom:"]
        await message.channel.send(random.choice(word_list3))
   
    if bot.user in message.mentions:
        reply = f'{message.author.mention} ……なんか用？　大した事やんねえからな。\n```[せつめいしょ]\nおはよう、おやすみ、ななぎして\nじゃんけん→Shinobuの返事→ぐー、ちょき、ぱー```'
        await message.channel.send(reply)


    if message.content == "じゃんけん":
        await message.channel.send("へーへー。最初はぐー、じゃんけん……")
        
        jkbot = random.choice(("ぐー", "ちょき", "ぱー"))
        draw = random.choice((":punch:\nあいこじゃん。つまんねーな",
                              ":punch:\nはいはい、引き分け",":punch:\nあいこ～。もう終わり？"))
        draw2 = random.choice((":v:\nあいこじゃん。つまんねーな",
                              ":v:\nはいはい、引き分け",":v:\nあいこ～。もう終わり？"))
        draw3 = random.choice((":hand_splayed:\nあいこじゃん。つまんねーな",
                              ":hand_splayed:\nはいはい、引き分け",":hand_splayed:\nあいこ～。もう終わり？"))
        wn = random.choice((":v:\nチッ、お前の勝ちだよ……",
                              ":v:\nくそ、負けた……次は勝つからな！",":v:\n負けた……はぁ？　ふざけんなよ……",":v:\n負けたし……お前……後出ししただろ！"))
        lst = random.choice((":v:\n僕の勝ち！お前弱いな～～！！！",
                              ":v:\n僕の勝ち～～～～！！！まあ、何度でも勝負してやるよ",":v:\nお前の負け。僕って強いだろ？",":v:\nお前の負け！　雑魚だな～！"))
        wn2 = random.choice((":hand_splayed:\nチッ、お前の勝ちだよ……",
                              ":hand_splayed:\nくそ、負けた……次は勝つからな！",":hand_splayed:\n負けた……はぁ？　ふざけんなよ……",":hand_splayed:\n負けたし……お前……後出ししただろ！"))
        lst2 = random.choice((":hand_splayed:\n僕の勝ち！お前弱いな～～！！！",
                              ":hand_splayed:\n僕の勝ち～～～～！！！まあ、何度でも勝負してやるよ","hand_splayed:\nお前の負け。僕って強いだろ？",":hand_splayed:\nお前の負け！　雑魚だな～！"))
        wn3 = random.choice((":punch:\nチッ、お前の勝ちだよ……",
                              ":punch:\nくそ、負けた……次は勝つからな！",":punch:\n負けた……はぁ？　ふざけんなよ……",":punch:\n負けたし……お前……後出ししただろ！"))
        lst3 = random.choice((":punch:\n僕の勝ち！お前弱いな～～！！！",
                              ":punch:\n僕の勝ち～～～～！！！まあ、何度でも勝負してやるよ",":punch:\nお前の負け。僕って強いだろ？",":punch:\nお前の負け！　雑魚だな～！"))
        

        def jankencheck(m):
            return (m.author == message.author) and (m.content in ['ぐー', 'ちょき', 'ぱー'])

        reply = await bot.wait_for("message", check=jankencheck)
        if reply.content == jkbot:
             if reply.content == "ぐー":
                if jkbot == "ちょき":
                    judge = wn
                else:
                    if jkbot == "ぱー":
                    judge = lst2
                    else:
                        if jkbot == "ぐー":
                        judge = draw
          
             elif reply.content == "ちょき":
                     if jkbot == "ちょき":
                        judge = draw2
                    else:
                        if jkbot == "ぱー":
                        judge = wn2
                        else:
                            if jkbot == "ぐー":
                            judge = lst2
                
             else:
                 if jkbot == "ちょき":
                    judge = wn3
                    else:
                        if jkbot == "ぱー":
                        judge = lst3
                        else:
                            if jkbot == "ぐー":
                            judge = draw3

        await message.channel.send(judge)
 
    
bot.run(token)
