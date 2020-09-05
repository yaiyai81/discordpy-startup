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
async def on_message(message):
    if "おはよう" in message.content:
        word_list = ["ねむい","なに？まだねてろよ","うるせー起こすな！","https://dl.dropboxusercontent.com/s/3qux2f89rgq1d22/gr120.png"]
        await message.channel.send(random.choice(word_list))

    if "おやすみ" in message.content:
        word_list = ["はよねな","さっさとねろ","ねみ…"]
        await message.channel.send(random.choice(word_list))

    if "ななぎして" in message.content:
        word_list = ["ななぎして","な～ぎ","なぎさ太った？",":cat: :boom:"]
        await message.channel.send(random.choice(word_list))
        
@bot.event
if message.author == client.user:
        return
    if message.content.startswith('@Shinobu'):
        await message.channel.send((embed))
        embed=embedobj
        embed = discord.Embed(title="ぼっとヘルプ一覧", colour=discord.Colour(0x112f43), url="https://discordapp.com", description="```Prefix:$```", timestamp=datetime.datetime.utcfromtimestamp(1551172370))
        embed.set_image()
        embed.set_thumbnail(url="http://3.bp.blogspot.com/-k74QBLjNuyg/TtiCcfDf2pI/AAAAAAAAAGw/coMwMiItguo/s1600/Mameshiba-Edamame-Wallpaper.jpg")
        embed.set_author(name="eDaMAme#1597", url="https://discordapp.com", icon_url="https://bit.ly/2SsIBiC")
        embed.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
        embed.add_field(name="$hello", value="挨拶をします")
        embed.add_field(name="$weather", value="お天気情報")
        embed.add_field(name="$zisin", value="地震情報")
        embed.add_field(name="$happy,$sad,$angry", value="絵文字表示", inline=True)
        embed.add_field(name="そのほかいろいろ", value="追加予定", inline=True)
        await bot.say(embed=embed)
        
bot.run(token)
