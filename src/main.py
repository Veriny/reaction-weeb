import discord
from discord.ext import commands
direct = "/home/ubuntu/rxn-weeb-res/"
file = open(direct + "token2.txt", 'r')
BOT_TOKEN = file.readline()
file.close()

Bot = commands.Bot(command_prefix = "!")

extensions = ['reactions', 'yntk']

@Bot.event
async def on_ready():
    print('Reaction-Weeb II is online')

@Bot.command()
async def load(ctx, cogname):
    try:
        Bot.load_extension(cogname)
        await ctx.send("Loaded {}".format(cogname))

    except Exception as e:
        await ctx.send("Unable to load that cog. '{}'".format(str(e)))

@Bot.command()
async def reload(ctx, cogname):
    try:
        Bot.reload_extension(cogname)
        await ctx.send("Reloaded {}".format(cogname))
    except Exception as e:
        await ctx.send("Unable to reload that cog. '{}'".format(str(e)))

for ext in extensions:
    Bot.load_extension(ext)

Bot.run(BOT_TOKEN)
