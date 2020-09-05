from discord.ext import commands
import os
import traceback
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    activity = discord.Game(name="アンジニティ", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")
      global result, judge
    if message.author.bot:  # ボットからのメッセージを回避します
        return

    if message.content == "！じゃんけん":
        await message.channel.send("最初はぐー、じゃんけん")

        jkbot = random.choice(("ぐー", "ちょき", "ぱー"))
        draw = "チッ、引き分けかよ"
        wn = "は？　ふざけんなよ……僕が負けるわけない"
        lst = random.choice(("弱ｗｗｗｗｗｗｗｗｗｗｗｗやめたら？じゃんけん",
                              "僕の勝ち～～～～～！！！！ざこめ！"))

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
    
@bot.command()
async def おはよう(ctx):
    await ctx.send('ねむいな')
  
@bot.command()
async def ななぎして(ctx):
    await ctx.send('な～ぎ')

 
    
bot.run(token)

