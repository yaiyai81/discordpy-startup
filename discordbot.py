import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import commands
import os
import traceback
import random

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
        word_list = ["ねむい","なに？　寝てろよ","zzz…"]
        await message.channel.send(random.choice(word_list))

@bot.event
async def on_message(message):
    if "じゃんけん" in message.content:
        word_list = ["グー","チョキ","パー"]
        await message.channel.send(random.choice(word_list))

    
bot.run(token)
