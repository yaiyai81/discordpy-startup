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
        word_list = ["ん～……？　ねむい……","なに……？まだねてろよ……","うるせーな、起こすな！","https://cdn.discordapp.com/attachments/740524923847573555/751840011577458770/gr120.png","ぐぅ……あと1時間……","なんだよ、朝から暇人だな。"]
        await message.channel.send(random.choice(word_list))

    if "おやすみ" in message.content:
        word_list2 = ["なんだよ、はよねろ","あーはいはい。さっさとねろよ……","……僕はまだ寝ないけど？","はいはい、おやすみ……","寝るのはやくね？　まあ、いいけど……","寝るまえに勝負しろよ！ネコチャンバトルをよ～"]
        await message.channel.send(random.choice(word_list2))

    if "ななぎして" in message.content:
        word_list3 = ["ななぎして","な～ぎ……って僕はやんねーから……","最近、なぎさ太ったんじゃね？",":cat: :boom:","おいなぎ！お手！","それって一生そろわないんじゃね？","なななな～ぎな"]
        await message.channel.send(random.choice(word_list3))
   
    if bot.user in message.mentions:
        reply = f'{message.author.mention} ……なんか用？　大した事やんねえからな。\n```[Hello Sinobu bot!]\n挨拶：おはよう、おやすみ\n会話：ななぎして、今日更新日、しのなぎ幸せになれると思う？\nゲーム：ネコチャンバトル→火風水の三種のねこを使って勝負。じゃんけん形式。```'
        await message.channel.send(reply)
        
    if "今日更新日" in message.content:
        word_list4 = ["https://cdn.discordapp.com/attachments/740524923847573555/752579834013548610/EYbNJduXsAE88WC.png"]
        await message.channel.send(random.choice(word_list4))

    if "しのなぎ幸せになれると思う？" in message.content:
        word_list5 = ["https://cdn.discordapp.com/attachments/724950481662902352/749945323769823302/EgfLwdUU0AA8-dK.png",
                      "https://cdn.discordapp.com/attachments/740524923847573555/752581562788216902/9f08c7fa1fedbf6ba0fa43968f71103c_600.png",
                      "https://cdn.discordapp.com/attachments/740524923847573555/752583065532104714/20180307170541.png"]
        await message.channel.send(random.choice(word_list5))


    if message.content == "ネコチャンバトル":
        await message.channel.send("へえ。僕にバトルを挑むとは良い度胸だな！\n僕はもう召喚するねこを決めてる……いくぜ、ドローだ！\n```！ドローするねこを以下の3種から選択```")
        embed=discord.Embed(title=":fire:火のねこ", description="燃え盛る火のネコチャン。風に強く、水に弱い\n:fire::fire::fire::cat::fire::fire::fire:", color=0xff0000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/740524923847573555/752435155888636015/hinoneko.png")
        await message.channel.send(embed=embed)
        embed=discord.Embed(title=":cloud_tornado:風のねこ", description="吹きすさぶ風のネコチャン。水に強く、火に弱い\n:cloud_tornado::cloud_tornado::cloud_tornado::cat::cloud_tornado::cloud_tornado::cloud_tornado:", color=0x00ff11)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/740524923847573555/752440859152351292/kazenoneko.png")
        await message.channel.send(embed=embed)       
        embed=discord.Embed(title=":droplet:水のねこ", description="流るる水のネコチャン。火に強く、風に弱い\n:droplet::droplet::droplet::cat::droplet::droplet::droplet:", color=0x72a8ee)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/740524923847573555/752440865070383104/mizunoneko.png")
        await message.channel.send(embed=embed)        
        
        jkbot = random.choice(("火のねこ", "風のねこ", "水のねこ"))
        draw = random.choice((":fire::fire::fire::cat::fire::fire::fire:\n引き分けか。つまんねーな……",":fire::fire::fire::cat::fire::fire::fire:\n引き分け？　なかなかやるじゃん。でも僕が勝つまでやるべきだろ。",":fire::fire::fire::cat::fire::fire::fire:\nはいはい、引き分け",":fire::fire::fire::cat::fire::fire::fire:\nあいこ～。もう終わり？もうひと勝負くらいできるだろ？"))
        draw2 = random.choice((":cloud_tornado::cloud_tornado::cloud_tornado::cat::cloud_tornado::cloud_tornado::cloud_tornado:\nあいこじゃん。つまんねーな！もう一回やろうぜ",":cloud_tornado::cloud_tornado::cloud_tornado::cat::cloud_tornado::cloud_tornado::cloud_tornado:\nお前、やる気あんのか？",":cloud_tornado::cloud_tornado::cloud_tornado::cat::cloud_tornado::cloud_tornado::cloud_tornado:\nはいはい、引き分け",":cloud_tornado::cloud_tornado::cloud_tornado::cat::cloud_tornado::cloud_tornado::cloud_tornado:\nあいこ～。もう終わり？"))
        draw3 = random.choice((":droplet::droplet::droplet::cat::droplet::droplet::droplet:\n引き分けじゃん。つまんねーな",":droplet::droplet::droplet::cat::droplet::droplet::droplet:\nは？これはもう一回だろ。",":droplet::droplet::droplet::cat::droplet::droplet::droplet:\nもう僕の勝ちでいいんじゃね？",":droplet::droplet::droplet::cat::droplet::droplet::droplet:\nはいはい、引き分け",":droplet::droplet::droplet::cat::droplet::droplet::droplet:\nあいこ～。もう終わり？"))
        wn = random.choice((":cloud_tornado::cloud_tornado::cloud_tornado::cat::cloud_tornado::cloud_tornado::cloud_tornado\nは？　ふざけんなもう一回勝負しろ！",":cloud_tornado::cloud_tornado::cloud_tornado::cat::cloud_tornado::cloud_tornado::cloud_tornado:\nお前、ずるしただろ！！！！",":cloud_tornado::cloud_tornado::cloud_tornado::cat::cloud_tornado::cloud_tornado::cloud_tornado:\nチッ、お前の勝ちだよ……僕のねこが負けるなんてな",":cloud_tornado::cloud_tornado::cloud_tornado::cat::cloud_tornado::cloud_tornado::cloud_tornado:\nくそ、負けた……僕のねこが……次は勝つからな！",":cloud_tornado::cloud_tornado::cloud_tornado::cat::cloud_tornado::cloud_tornado::cloud_tornado:\n負けた……僕のねこが……はぁ？　ふざけんなよ……",":cloud_tornado::cloud_tornado::cloud_tornado::cat::cloud_tornado::cloud_tornado::cloud_tornado:\n負けたし……お前……イカサマしただろ！"))
        wn2 = random.choice((":droplet::droplet::droplet::cat::droplet::droplet::droplet:\nチッ、お前の勝ちだよ……",":droplet::droplet::droplet::cat::droplet::droplet::droplet:\nくそ、負けた……僕のねこが……次は勝つからな！",":droplet::droplet::droplet::cat::droplet::droplet::droplet:\n負けた……僕のねこが……はぁ？　ふざけんなよ……",":droplet::droplet::droplet::cat::droplet::droplet::droplet:\n負けたし……お前……イカサマしただろ！"))
        wn3 = random.choice((":fire::fire::fire::cat::fire::fire::fire:\n僕の火のねこが負けるわけないだろ。もう一回勝負しろ",":fire::fire::fire::cat::fire::fire::fire:\nは？僕の火のねこが負けるワケないだろ！これのカドで殴れば人は死ぬ",":fire::fire::fire::cat::fire::fire::fire:\nお前をなぐっていいか？",":fire::fire::fire::cat::fire::fire::fire:\nチッ、お前の勝ちだよ……",":fire::fire::fire::cat::fire::fire::fire:\nくそ、負けた……僕のねこが……次は勝つからな！",":fire::fire::fire::cat::fire::fire::fire:\n負けた……僕のねこが……はぁ？　ふざけんなよ……",":fire::fire::fire::cat::fire::fire::fire:\n負けたし……お前……イカサマしただろ！"))
        lst = random.choice((":cloud_tornado::cloud_tornado::cloud_tornado::cat::cloud_tornado::cloud_tornado::cloud_tornado:\n僕の勝ち！お前弱いな～～！！！",":cloud_tornado::cloud_tornado::cloud_tornado::cat::cloud_tornado::cloud_tornado::cloud_tornado:\nうわ、僕って、強すぎ……？",":cloud_tornado::cloud_tornado::cloud_tornado::cat::cloud_tornado::cloud_tornado::cloud_tornado:\n僕の勝ちだ。いや、イカサマじゃねーから！",":cloud_tornado::cloud_tornado::cloud_tornado::cat::cloud_tornado::cloud_tornado::cloud_tornado:\n僕の勝ち～～～～！！！まあ、何度でも勝負してやるよ",":cloud_tornado::cloud_tornado::cloud_tornado::cat::cloud_tornado::cloud_tornado::cloud_tornado:\nお前の負け。僕って強いだろ？",":cloud_tornado::cloud_tornado::cloud_tornado::cat :cloud_tornado::cloud_tornado::cloud_tornado:\nお前の負け！　雑魚だな～！"))
        lst2 = random.choice((":droplet::droplet::droplet::cat::droplet::droplet::droplet:\n僕の勝ち！お前弱いな～～！！！",":droplet::droplet::droplet::cat::droplet::droplet::droplet:\nふん、僕が勝つってことは最初から決まってたんだよ！",":droplet::droplet::droplet::cat::droplet::droplet::droplet:\nお前のねこはまだまだみたいだな！！！！！！僕の勝利！",":droplet::droplet::droplet::cat::droplet::droplet::droplet:\n僕の勝ち～～～～！！！まあ、何度でも勝負してやるよ",":droplet::droplet::droplet::cat::droplet::droplet::droplet:\nお前の負け。僕って強いだろ？",":droplet::droplet::droplet::cat::droplet::droplet::droplet:\nお前の負け！　雑魚だな～！"))
        lst3 = random.choice((":fire::fire::fire::cat::fire::fire::fire:\n僕の勝ち！お前弱いな～～！！！",":fire::fire::fire::cat::fire::fire::fire:\nはいはい、僕の勝ち。罰ゲームに一発殴っていい？",":fire::fire::fire::cat::fire::fire::fire:\nなんで負けたかって？考えなくてもわかるだろ？僕が強いからだよ！",":fire::fire::fire::cat::fire::fire::fire:\n僕のねこの勝ち～～～～！！！まあ、何度でも勝負してやるよ",":fire::fire::fire::cat::fire::fire::fire:\nお前の負け。僕のねこが最強ってことだな！",":fire::fire::fire::cat::fire::fire::fire:\nお前の負け！　雑魚だな～！"))
   

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
