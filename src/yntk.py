import discord
from discord.ext import commands
import random
import json
UNITS_ACTIVE = 4
users_solving = []

class yntk(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def corroborate(self, ctx):
        await ctx.send("YNTKs are active.")

    @commands.command()
    async def yntk(self, ctx):
        if ctx.message.author.id in users_solving:
            await ctx.send("You are already solving a YNTK.")
            return None
        users_solving.append(ctx.message.author.id)
        #JSON
        with open('/home/ubuntu/reaction_weeb-II/res/users.json') as f:
            users = json.load(f)
        #END OF JSON
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
        if (content == "1" or content == "2") and msg.author.id == ctx.message.author.id:
            if content == "1" and date1 < date2:
                # The user got the question right.
                users_solving.remove(ctx.message.author.id)
                await correct_answer(ctx, date1, date2, users)
                with open('/home/ubuntu/reaction_weeb-II/res/users.json', 'w') as f:
                    json.dump(users, f)
                    print("Did this too!")
                return True
            elif content == "2" and date2 < date1:
                # User got it right
                users_solving.remove(ctx.message.author.id)
                await correct_answer(ctx, date1, date2, users)
                with open('/home/ubuntu/reaction_weeb-II/res/users.json', 'w') as f:
                    json.dump(users, f)
                    print("Did this too!")
                return True
            elif content == "3" and date2 == date1:
                # User got it right
                users_solving.remove(ctx.message.author.id)
                await correct_answer(ctx, date1, date2, users)
                with open('/home/ubuntu/reaction_weeb-II/res/users.json', 'w') as f:
                    json.dump(users, f)
                    print("Did this too!")
                return True
            else:
                # User got it wrong
                users_solving.remove(ctx.message.author.id)
                await wrong_answer(ctx, date1, date2, users)
                with open('/home/ubuntu/reaction_weeb-II/res/users.json', 'w') as f:
                    json.dump(users, f)
                    print("Did this too!")
                return True

    @commands.command()
    async def stats(self, ctx):
        with open('/home/ubuntu/reaction_weeb-II/res/users.json', 'r') as f:
            users = json.load(f)
        points = get_points(ctx, users)
        streak = get_streak(ctx, users)
        await ctx.send('RP: {} | streak: {}'.format(points, streak))


def setup(bot: commands.Bot):
    bot.add_cog(yntk(bot))

def check(m):
    return m.content in ['1', '2', '3']

def calc_points_earned(date1, date2):
    return round(1/(max(date1, date2)-min(date1, date2)) * 100, 3)

async def correct_answer(ctx, date1, date2, users):
    update_data(ctx, users)
    earned_points = calc_points_earned(date1, date2)
    add_points(ctx, earned_points, True, users)
    total_points = get_points(ctx, users)
    streak = get_streak(ctx, users)
    embed = discord.Embed(description="Wow, you got it right. Yay.",colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
    embed.set_image(url="https://i.redd.it/9zfn7innslq21.png")
    embed.set_footer(text='RP +{} => total: {} | streak: {}'.format(earned_points, total_points, streak))
    await ctx.send(embed=embed)
    with open('/home/ubuntu/reaction_weeb-II/res/users.json', 'r+') as f:
        json.dump(users, f)

async def wrong_answer(ctx, date1, date2, users):
    update_data(ctx, users)
    earned_points = calc_points_earned(date1, date2)
    add_points(ctx, earned_points, False, users)
    total_points = get_points(ctx, users)
    streak = get_streak(ctx, users)
    embed = discord.Embed(description="Someone needs to try harder. How are you so bad at this?",colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
    embed.set_image(url="https://i.redd.it/4ajfe9xdjaf11.gif")
    embed.set_footer(text='RP -{} => total: {} | streak: {}'.format(earned_points, total_points, streak))
    await ctx.send(embed=embed)

def update_data(ctx, users):
    print(str(ctx.message.author.id) in users)
    if not (str(ctx.message.author.id) in users):
        print("I got here!")
        users[str(ctx.message.author.id)] = {}
        users[str(ctx.message.author.id)]['ranking_points'] = 0
        users[str(ctx.message.author.id)]['streak'] = 0
        users[str(ctx.message.author.id)]['multiplier'] = 0
        print("I got here as well!")
        print(users[str(ctx.message.author.id)]['ranking_points'])
        with open('/home/ubuntu/reaction_weeb-II/res/users.json', 'r+') as f:
            json.dump(users, f)

def add_points(ctx, points, correct, users):
    if correct:
        users[str(ctx.message.author.id)]['ranking_points'] += points
        users[str(ctx.message.author.id)]['streak'] += 1
    if not correct:
        users[str(ctx.message.author.id)]['ranking_points'] -= points
        users[str(ctx.message.author.id)]['streak'] = 0


def get_points(ctx, users):
    pog = users[str(ctx.message.author.id)]['ranking_points']
    return pog

def get_streak(ctx, users):
    pog = users[str(ctx.message.author.id)]['streak']
    return pog
