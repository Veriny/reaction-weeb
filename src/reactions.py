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
    async def nou(self, ctx):
        embed = discord.Embed(colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_image(url="https://i.redd.it/bs73e7ibk1431.gif")
        await ctx.send(embed=embed)
    @commands.command()
    async def no(self, ctx):
        embed = discord.Embed(colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_image(url="https://cdn.discordapp.com/attachments/400909034766467072/577241058929410090/image0.jpg")
        await ctx.send(embed=embed)
    @commands.command()
    async def holdup(self, ctx):
        embed = discord.Embed(colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_image(url="https://i.redd.it/zjhaurjckcq21.png")
        await ctx.send(embed=embed)
        #https://cdn.discordapp.com/attachments/400909034766467072/568991691672125440/image0.jpg
    @commands.command()
    async def gun(self, ctx, member: discord.Member = None):
        string = ""
        if member is None:
            string = ""
        else:
            string = "<@!{}>'s post has been deemed cursed and unworthy".format(member.id)

        embed = discord.Embed(description = string, colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_image(url="https://cdn.discordapp.com/attachments/400909034766467072/568991691672125440/image0.jpg")
        await ctx.send(embed=embed)
    @commands.command()
    async def uwu(self, ctx, member: discord.Member = None):
        string = ""
        if member is None:
            embed = discord.Embed(description = "The furry <@!{}> has illegally uwu'd and will be euthanized immediately.".format(ctx.message.author.id),  colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
            embed.set_image(url="https://i.redd.it/erp4cf8kact21.png")
        else:
            embed = discord.Embed(description = "The furry <@!{}> has illegally uwu'd or owo'd and will be euthanized immediately.".format(member.id),  colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
            embed.set_image(url="https://i.redd.it/erp4cf8kact21.png")
        await ctx.send(embed=embed)
    @commands.command()
    async def silence(self, ctx, member: discord.Member = None):
        string = ""
        if member is None:
            embed = discord.Embed(description = "Tag a person to silence.",  colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        else:
            embed = discord.Embed(description = "<@!{}>, Ben Shapiro demands your silence.".format(member.id),  colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
            embed.set_image(url="https://i.redd.it/m7gl0a2ydkt21.gif")
        await ctx.send(embed=embed)
    @commands.command()
    async def invite(self, ctx):
        await ctx.send("https://discordapp.com/oauth2/authorize?client_id=558016541514399744&scope=bot&permissions=8")
    @commands.command()
    async def yareyaredaze(self, ctx):
        embed = discord.Embed(description="Oh? You're approaching me?",colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_image(url="https://i.redd.it/dq0db04gic431.gif")
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(reactions())
