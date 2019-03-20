import discord
from discord.ext import commands

TOKEN = 'NTU4MDE2NTQxNTE0Mzk5NzQ0.D3QtFA.ayPf8axbjvkpFPh2U-mFk0dQvRg'
client = commands.Bot(command_prefix = "!")

extensions = ['DJ', 'Ratto', 'YNTK', 'Reactions', 'Canvas']

@client.event
async def on_ready():
    print('Reaction-Weeb II is online')

if __name__ = = '__main__':
    client.run(TOKEN)
