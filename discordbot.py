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
        reply = f'{message.author.mention} ……なんか用？　大した事やんねえからな。\n```[せつめいしょ]\nおはよう、おやすみ、ななぎして\nネコチャンバトル→火風水の三種のねこを使って勝負。```'
        await message.channel.send(reply)
        
    if message.content == "ネコチャンバトル":
        await message.channel.send("へえ。僕に勝負を挑むとは良い度胸だな……お前はどのねこにする？\n```[ネコチャンバトルのルール]\n炎のねこ→風のねこに強く、水のねこに弱い\n風のねこ→水のねこに弱く、火のねこに強い\n水のねこ→火の猫に強く、のねこに弱い```")
        
        jkbot = random.choice(("火のねこ", "風のねこ", "水のねこ"))
        draw = random.choice(("https://cdn.discordapp.com/attachments/740524923847573555/752435155888636015/hinoneko.png\nあいこじゃん。つまんねーな","https://cdn.discordapp.com/attachments/740524923847573555/752435155888636015/hinoneko.png\nあいこって一番つまんねーな、僕が勝つまでやるべきだろ。",
                              "https://cdn.discordapp.com/attachments/740524923847573555/752435155888636015/hinoneko.png\nはいはい、引き分け","https://cdn.discordapp.com/attachments/740524923847573555/752435155888636015/hinoneko.png\nあいこ～。もう終わり？"))
        draw2 = random.choice(("https://cdn.discordapp.com/attachments/740524923847573555/752440859152351292/kazenoneko.png\nあいこじゃん。つまんねーな","https://cdn.discordapp.com/attachments/740524923847573555/752440859152351292/kazenoneko.png\nお前、やる気あんのか？",
                              "https://cdn.discordapp.com/attachments/740524923847573555/752440859152351292/kazenoneko.png\nはいはい、引き分け","https://cdn.discordapp.com/attachments/740524923847573555/752440859152351292/kazenoneko.png\nあいこ～。もう終わり？"))
        draw3 = random.choice(("https://cdn.discordapp.com/attachments/740524923847573555/752440865070383104/mizunoneko.png\nあいこじゃん。つまんねーな","https://cdn.discordapp.com/attachments/740524923847573555/752440865070383104/mizunoneko.png\nは？これはもう一回だろ。","https://cdn.discordapp.com/attachments/740524923847573555/752440865070383104/mizunoneko.png\nもう僕の勝ちでいいんじゃね？",
                              "https://cdn.discordapp.com/attachments/740524923847573555/752440865070383104/mizunoneko.png\nはいはい、引き分け","https://cdn.discordapp.com/attachments/740524923847573555/752440865070383104/mizunoneko.png\nあいこ～。もう終わり？"))
        wn = random.choice(("https://cdn.discordapp.com/attachments/740524923847573555/752440859152351292/kazenoneko.png\nは？　ふざけんなもう一回勝負しろ！","https://cdn.discordapp.com/attachments/740524923847573555/752440859152351292/kazenoneko.png\nお前、ずるしただろ！！！！","https://cdn.discordapp.com/attachments/740524923847573555/752440859152351292/kazenoneko.png\nチッ、お前の勝ちだよ……",
                              "https://cdn.discordapp.com/attachments/740524923847573555/752440859152351292/kazenoneko.png\nくそ、負けた……僕のねこが……次は勝つからな！","https://cdn.discordapp.com/attachments/740524923847573555/752440859152351292/kazenoneko.png\n負けた……僕のねこが……はぁ？　ふざけんなよ……","https://cdn.discordapp.com/attachments/740524923847573555/752440859152351292/kazenoneko.png\n負けたし……お前……イカサマしただろ！"))
        wn2 = random.choice(("https://cdn.discordapp.com/attachments/740524923847573555/752440865070383104/mizunoneko.png\nチッ、お前の勝ちだよ……",
                              "https://cdn.discordapp.com/attachments/740524923847573555/752440865070383104/mizunoneko.png\nくそ、負けた……僕のねこが……次は勝つからな！","https://cdn.discordapp.com/attachments/740524923847573555/752440865070383104/mizunoneko.png\n負けた……僕のねこが……はぁ？　ふざけんなよ……","https://cdn.discordapp.com/attachments/740524923847573555/752440865070383104/mizunoneko.png\n負けたし……お前……イカサマしただろ！"))
        wn3 = random.choice(("https://cdn.discordapp.com/attachments/740524923847573555/752435155888636015/hinoneko.png\n僕の火のねこが負けるわけないだろ。もう一回勝負しろ","https://cdn.discordapp.com/attachments/740524923847573555/752435155888636015/hinoneko.png\nは？火のねこが負けるワケないだろ！これで殴れば人は死ぬ","https://cdn.discordapp.com/attachments/740524923847573555/752435155888636015/hinoneko.png\nお前をなぐっていいか？","https://cdn.discordapp.com/attachments/740524923847573555/752435155888636015/hinoneko.png\nチッ、お前の勝ちだよ……",
                              "https://cdn.discordapp.com/attachments/740524923847573555/752435155888636015/hinoneko.png\nくそ、負けた……僕のねこが……次は勝つからな！","https://cdn.discordapp.com/attachments/740524923847573555/752435155888636015/hinoneko.png\n負けた……僕のねこが……はぁ？　ふざけんなよ……","https://cdn.discordapp.com/attachments/740524923847573555/752435155888636015/hinoneko.png\n負けたし……お前……イカサマしただろ！"))
        lst = random.choice(("https://cdn.discordapp.com/attachments/740524923847573555/752440859152351292/kazenoneko.png\n僕の勝ち！お前弱いな～～！！！","https://cdn.discordapp.com/attachments/740524923847573555/752440859152351292/kazenoneko.png\nうわ、僕って、強すぎ……？","https://cdn.discordapp.com/attachments/740524923847573555/752440859152351292/kazenoneko.png\n僕の勝ちだ。いや、イカサマじゃねーから！",
                              "https://cdn.discordapp.com/attachments/740524923847573555/752440859152351292/kazenoneko.png\n僕の勝ち～～～～！！！まあ、何度でも勝負してやるよ","https://cdn.discordapp.com/attachments/740524923847573555/752440859152351292/kazenoneko.png\nお前の負け。僕って強いだろ？","https://cdn.discordapp.com/attachments/740524923847573555/752440859152351292/kazenoneko.png\nお前の負け！　雑魚だな～！"))
        lst2 = random.choice(("https://cdn.discordapp.com/attachments/740524923847573555/752440865070383104/mizunoneko.png\n僕の勝ち！お前弱いな～～！！！","https://cdn.discordapp.com/attachments/740524923847573555/752440865070383104/mizunoneko.png\nふん、僕が勝つってことは最初から決まってたんだよ！","https://cdn.discordapp.com/attachments/740524923847573555/752440865070383104/mizunoneko.png\nお前のねこはまだまだみたいだな！！！！！！僕の勝利！",
                              "https://cdn.discordapp.com/attachments/740524923847573555/752440865070383104/mizunoneko.png\n僕の勝ち～～～～！！！まあ、何度でも勝負してやるよ","https://cdn.discordapp.com/attachments/740524923847573555/752440865070383104/mizunoneko.png\nお前の負け。僕って強いだろ？","https://cdn.discordapp.com/attachments/740524923847573555/752440865070383104/mizunoneko.png\nお前の負け！　雑魚だな～！"))
        lst3 = random.choice(("https://cdn.discordapp.com/attachments/740524923847573555/752435155888636015/hinoneko.png\n僕の勝ち！お前弱いな～～！！！","https://cdn.discordapp.com/attachments/740524923847573555/752435155888636015/hinoneko.png\nはいはい、僕の勝ち。罰ゲームに一発殴っていい？","https://cdn.discordapp.com/attachments/740524923847573555/752435155888636015/hinoneko.png\nなんで負けたかって？考えなくてもわかるだろ？僕が強いからだよ！",
                              "https://cdn.discordapp.com/attachments/740524923847573555/752435155888636015/hinoneko.png\n僕の勝ち～～～～！！！まあ、何度でも勝負してやるよ","https://cdn.discordapp.com/attachments/740524923847573555/752435155888636015/hinoneko.png\nお前の負け。僕って強いだろ？","https://cdn.discordapp.com/attachments/740524923847573555/752435155888636015/hinoneko.png\nお前の負け！　雑魚だな～！"))
        

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
