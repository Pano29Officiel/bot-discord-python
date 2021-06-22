import discord
from discord.ext import commands

from PIL import Image
from io import BytesIO

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="=", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready.")





@bot.command()
async def wanted(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    wanted = Image.open("wanted.png")

    asset = user.avatar_url_as(size = 128)

    data = BytesIO(await asset.read())

    pfp = Image.open(data)

    pfp = pfp.resize((177,177))

    wanted.paste(pfp, (50,50))

    wanted.save("profile.png")

    await ctx.send(file =  discord.File("profile.png"))







@bot.group(pass_context=True)
async def Help(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Invalid sub command passed...')

@Help.command(pass_context=True)
async def Ui(ctx):
    msg = 'Finally got success {0.author.mention}'.format(ctx.message)
    await ctx.send(msg)


@bot.command()
async def ping(ctx):
    embed = discord.Embed(title="** :ping_pong:  •  Pong !**", description=f"`{round(bot.latency * 1000)}ms`",
                          color=0x3bc200)
    await ctx.send(embed=embed)


bot.run(TOKEN)
