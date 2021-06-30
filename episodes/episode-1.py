import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="=", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready.")

@bot.command()
async def hello(ctx):
    await(f"hello {ctx.author.name}")
@bot.command()
async def ping(ctx):
    embed = discord.Embed(title="** :ping_pong:  •  Pong !**", description=f"`{round(bot.latency * 1000)}ms`",
                          color=0x3bc200)
    await ctx.send(embed=embed)

bot.run(TOKEN) #ATTENTION remplacer "TOKEN" par le token de votre bot, disponible sur le portail discord develloper
