import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")



@bot.command()
async def get_names(ctx):
  names = list()
  for user in ctx.guild.members:
    names.append(user.name)
    
  await ctx.channel.send('\n'.join(names))

bot.run("Nzg3Njc4NTk5NzY2ODY4MDMy.X9Yc3A.pqsReNPdyf8IV8QMjdNMDd7ff_0")