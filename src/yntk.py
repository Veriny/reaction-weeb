import discord
from discord.ext import commands
import random
import json
UNITS_ACTIVE = 2


class yntk(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def corroborate(self, ctx):
        await ctx.send("YNTKs are active.")

    @commands.command()
    async def yntk(self, ctx):
        unit = random.randint(1, UNITS_ACTIVE)
        with open('/home/ubuntu/reaction_weeb-II/res/unit{}.json'.format(unit), 'r') as f:
            YNTKpool = json.load(f)
        cout = 0
        cout = len(YNTKpool)
        firstYNTK = random.randint(1, cout)
        secondYNTK = random.randint(1, cout)
        while firstYNTK == secondYNTK:
            secondYNTK = random.randint(1, cout)
        content1 = YNTKpool['{}'.format(firstYNTK)]['content']
        content2 = YNTKpool['{}'.format(secondYNTK)]['content']
        date1 = YNTKpool['{}'.format(firstYNTK)]['date']
        date2 = YNTKpool['{}'.format(secondYNTK)]['date']
        await ctx.send("""Which came first?
        1: {}
                                        **OR**
        2: {}?
**__Respond with a number, 1 or 2. Respond with 3 if they happened at the same time.__**""".
                       format(content1,
                              content2))
        msg = await self.bot.wait_for('message', check=check, timeout=60.0)
        content = msg.content
        if content == "1" or content == "2":
            if content == "1" and date1 < date2:
                # The user got the question right.
                embed = discord.Embed(description="Wow, you got it right. Yay.", colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
                embed.set_image(url="https://i.redd.it/9zfn7innslq21.png")
                await ctx.send(embed=embed)
                return True
            elif content == "2" and date2 < date1:
                # User got it right
                embed = discord.Embed(description="Wow, you got it right. Yay.", colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
                embed.set_image(url="https://i.redd.it/9zfn7innslq21.png")
                await ctx.send(embed=embed)
                return True
            elif content == "3" and date2 == date1:
                # User got it right
                embed = discord.Embed(description="Wow, you got it right. Yay.",colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
                embed.set_image(url="https://i.redd.it/9zfn7innslq21.png")
                await ctx.send(embed=embed)
                return True
            else:
                # User got it wrong
                embed = discord.Embed(description="Someone needs to try harder. How are you so bad at this?",colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
                embed.set_image(url="https://i.redd.it/4ajfe9xdjaf11.gif")
                await ctx.send(embed=embed)
                return True


def setup(bot: commands.Bot):
    bot.add_cog(yntk(bot))
def check(m):
    return m.content in ['1', '2', '3']
