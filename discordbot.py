from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.command()
async def おはよう(ctx):
    await ctx.send('ねむいな')
  
@bot.command()
async def ななぎして(ctx):
    await ctx.send('な～ぎ')
    
@client.event
async def on_ready(): # botが起動したときに動作する処理
    print('ログインしました')
    await client.change_presence(activity=discord.Game(name="with discord.py", type=1))

bot.run(token)

