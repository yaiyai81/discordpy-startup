from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    activity = discord.Game(name="Netflix", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")
    
@bot.command()
async def おはよう(ctx):
    await ctx.send('ねむいな')
  
@bot.command()
async def ななぎして(ctx):
    await ctx.send('な～ぎ')

 
    
bot.run(token)

