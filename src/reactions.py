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
    @commands.command()
    async def wtf(self, ctx):
        embed = discord.Embed(colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_image(url="https://i.redd.it/tgxodpn7qeh21.jpg")
        await ctx.send(embed=embed)
    @commands.command()
    async def nut(self, ctx):
        embed = discord.Embed(colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_image(url="https://i.redd.it/d343a7ahicq21.png")
        await ctx.send(embed=embed)
    @commands.command()
    async def fear(self, ctx):
        embed = discord.Embed(colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_image(url="https://i.redd.it/wc3wz623icq21.png")
        await ctx.send(embed=embed)
    @commands.command()
    async def bad(self, ctx):
        embed = discord.Embed(colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_image(url="https://i.redd.it/78ugmt18kcq21.png")
        await ctx.send(embed=embed)
    @commands.command()
    async def holdup(self, ctx):
        embed = discord.Embed(colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_image(url="https://i.redd.it/zjhaurjckcq21.png")
        await ctx.send(embed=embed)
    @commands.command()
    async def invite(self, ctx):
        await ctx.send("https://discordapp.com/oauth2/authorize?client_id=558016541514399744&scope=bot&permissions=8")
def setup(bot):
    bot.add_cog(reactions())
