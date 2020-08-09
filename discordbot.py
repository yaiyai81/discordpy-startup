from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='')
token = ""

@bot.event
async def on_message(message):
    print("")
    await bot.process_commands(message)

@bot.command()
async def おはよう(ctx):
    await ctx.send('ねむいな')
  
@bot.command()
async def ななぎして(ctx):
    await ctx.send('な～ぎ')

 
    
bot.run(token)

