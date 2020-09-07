import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
import traceback
import glob
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
        reply = f'{message.author.mention} ……なんか用？　大した事やんねえからな。\n```[せつめいしょ]\nおはよう、おやすみ、ななぎして\nネコチャンバトル→火風水の三種のねこを使って勝負。```'
        await message.channel.send(reply)
        

    if message.content == "ネコチャンバトル":
        await message.channel.send("へえ。僕にネコチャンバトルを挑むとは良い度胸だな！\n僕はもう召喚するねこを決めたぜ……お前は？")
        embed=discord.Embed(title="▼火のねこ", description="燃え盛る火のネコチャン。風に強く、水に弱い", color=0xff0000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/740524923847573555/752435155888636015/hinoneko.png")
        await message.channel.send(embed=embed)
        embed=discord.Embed(title="▼風のねこ", description="吹きすさぶ風のネコチャン。水に強く、火に弱い", color=0x00ff11)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/740524923847573555/752440859152351292/kazenoneko.png")
        await message.channel.send(embed=embed)       
        embed=discord.Embed(title="▼水のねこ", description="流るる水のネコチャン。火に強く、風に弱い", color=0x72a8ee)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/740524923847573555/752440865070383104/mizunoneko.png")
        await message.channel.send(embed=embed)        
        
        jkbot = random.choice(("火のねこ", "風のねこ", "水のねこ"))
        draw = random.choice((":hineko: あいこじゃん。つまんねーな",":hineko: あいこって一番つまんねーな、僕が勝つまでやるべきだろ。",
                              ":hineko: はいはい、引き分け",":hineko: あいこ～。もう終わり？"))
        draw2 = random.choice((":mizuneko: あいこじゃん。つまんねーな",":mizuneko: お前、やる気あんのか？",
                              ":mizuneko: はいはい、引き分け",":mizuneko: あいこ～。もう終わり？"))
        draw3 = random.choice((":mizuneko: あいこじゃん。つまんねーな",":mizuneko: は？これはもう一回だろ。",":mizuneko: もう僕の勝ちでいいんじゃね？",
                              ":mizuneko: はいはい、引き分け",":mizuneko: あいこ～。もう終わり？"))
        wn = random.choice((":mizuneko: は？　ふざけんなもう一回勝負しろ！",":mizuneko: お前、ずるしただろ！！！！",":mizuneko: チッ、お前の勝ちだよ……",
                              ":mizuneko: くそ、負けた……僕のねこが……次は勝つからな！",":mizuneko: 負けた……僕のねこが……はぁ？　ふざけんなよ……",":mizuneko: 負けたし……お前……イカサマしただろ！"))
        wn2 = random.choice((":mizuneko: チッ、お前の勝ちだよ……",
                              ":mizuneko: くそ、負けた……僕のねこが……次は勝つからな！",":mizuneko: 負けた……僕のねこが……はぁ？　ふざけんなよ……",":mizuneko: 負けたし……お前……イカサマしただろ！"))
        wn3 = random.choice((":hineko: 僕の火のねこが負けるわけないだろ。もう一回勝負しろ",":hineko: は？火のねこが負けるワケないだろ！これで殴れば人は死ぬ",":hineko: お前をなぐっていいか？",":hineko: チッ、お前の勝ちだよ……",
                              ":hineko: くそ、負けた……僕のねこが……次は勝つからな！",":hineko: 負けた……僕のねこが……はぁ？　ふざけんなよ……",":hineko: 負けたし……お前……イカサマしただろ！"))
        lst = random.choice((":mizuneko: 僕の勝ち！お前弱いな～～！！！",":mizuneko: うわ、僕って、強すぎ……？",":mizuneko: 僕の勝ちだ。いや、イカサマじゃねーから！",
                              ":mizuneko: 僕の勝ち～～～～！！！まあ、何度でも勝負してやるよ",":mizuneko: お前の負け。僕って強いだろ？",":mizuneko: お前の負け！　雑魚だな～！"))
        lst2 = random.choice((":mizuneko: 僕の勝ち！お前弱いな～～！！！",":mizuneko: ふん、僕が勝つってことは最初から決まってたんだよ！",":mizuneko: お前のねこはまだまだみたいだな！！！！！！僕の勝利！",
                              ":mizuneko: 僕の勝ち～～～～！！！まあ、何度でも勝負してやるよ",":mizuneko: お前の負け。僕って強いだろ？",":mizuneko: お前の負け！　雑魚だな～！"))
        lst3 = random.choice((":hineko: 僕の勝ち！お前弱いな～～！！！",":hineko: はいはい、僕の勝ち。罰ゲームに一発殴っていい？",":hineko: なんで負けたかって？考えなくてもわかるだろ？僕が強いからだよ！",
                              ":hineko: 僕の勝ち～～～～！！！まあ、何度でも勝負してやるよ",":hineko: お前の負け。僕って強いだろ？",":hineko: お前の負け！　雑魚だな～！"))
            

        def jankencheck(m):
            return (m.author == message.author) and (m.content in ['火のねこ', '風のねこ', '水のねこ'])

        reply = await bot.wait_for("message", check=jankencheck)
        if reply.content == "火のねこ":
            if jkbot == "風のねこ":
                judge = wn
            elif jkbot == "火のねこ":
                judge = draw
            else:
                judge = lst2

        elif reply.content == "風のねこ":
            if jkbot == "水のねこ":
                judge = wn2
            elif jkbot == "風のねこ":
                judge = draw2
            else:
                judge = lst3

        else:
            if jkbot == "火のねこ":
                judge = wn3
            elif jkbot == "水のねこ":
                 judge = draw3
            else:
                judge = lst
                
        await message.channel.send(judge)
 

bot.run(token)
