import discord
from discord.ext import commands
import random

class reactions(commands.Cog):
    # def __init__(self, client):
    #     self.client = client
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")
    @commands.command()
    async def goodbye(self, ctx):
        embed = discord.Embed(colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_image(url="https://cdn.discordapp.com/attachments/400909034766467072/552637318167527424/image0.png")
        await ctx.send(embed=embed)
    @commands.command()
    async def joke(self, ctx):
        embed = discord.Embed(colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_image(url="https://cdn.discordapp.com/attachments/400909034766467072/563090807478026250/joke.jpg")
        await ctx.send(embed=embed)
    @commands.command()
    async def colglaziernut(self, ctx):
        embed = discord.Embed(description="When you hit that \n corroboration just right", colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_image(url="https://cdn.discordapp.com/attachments/400909034766467072/555403190292578305/unknown.png")
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(reactions())
