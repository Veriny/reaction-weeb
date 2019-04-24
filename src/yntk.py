import discord
from discord.ext import commands
import random
import json
from operator import itemgetter
UNITS_ACTIVE = 5
users_solving = []

class yntk(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def corroborate(self, ctx):
        await ctx.send("YNTKs are active.")

    @commands.command()
    async def yntk(self, ctx):
        if users_solving != []:
            await ctx.send("Someone is already solving a YNTK.")
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
        if (content == "1" or content == "2" or content == "3") and msg.author.id == ctx.message.author.id:
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
                await correct_answer(ctx, date1, date2 + 0.999999999999999999999, users)
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

    # @commands.command()
    # async def stats(self, ctx):
    #     with open('/home/ubuntu/reaction_weeb-II/res/users.json', 'r') as f:
    #         users = json.load(f)
    #     points = get_points(ctx, users)
    #     streak = get_streak(ctx, users)
    #     await ctx.send('RP: {} | streak: {}'.format(points, streak))
    @commands.command()
    async def despacito(self, ctx, member: discord.Member):
        with open('/home/ubuntu/reaction_weeb-II/res/users.json', 'r+') as f:
            users = json.load(f)

        if ctx.message.author.id == 383116010971987971:
            users[str(member.id)]['ranking_points'] = 0

        await ctx.send('Ranking points reset to 100')

        with open('/home/ubuntu/reaction_weeb-II/res/users.json', 'w') as f:
            json.dump(users, f)
            print("Did this too!")

    @commands.command()
    async def stats(self, ctx, member: discord.Member = None):
        with open('/home/ubuntu/reaction_weeb-II/res/users.json', 'r') as f:
            users = json.load(f)
        if member is None:
            #Things
            await process_info(ctx, users, ctx.message.author)
        else:
            #more things
            await process_info(ctx, users, member)
    @commands.command()
    async def ranking(self, ctx):
        with open('/home/ubuntu/reaction_weeb-II/res/users.json', 'r') as f:
            users = json.load(f)
        # sorted_dict = sorted(users.iteritems(), key=lambda (x, y): y['ranking_points'])
        # print(sorted_dict)
        string = ""
        for user in sorted(users, key=lambda x: users[x]['ranking_points'], reverse = True):
            print(user)
            string = string + "<@!{}> **RP {}, streak {}**\n".format(user, users[user]['ranking_points'], users[user]['streak'])
        embed = discord.Embed(description = string, colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_author(name="Top Historians")
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/529472867805691904.gif')
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(yntk(bot))

def check(m):
    return m.content in ['1', '2', '3']

def calc_points_earned(date1, date2):
    return round(1/(max(date1, date2)-min(date1, date2)) * 100, 3)

def calc_points_lost(date1, date2):
    return (max(date1, date2)-min(date1, date2))

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
    earned_points = calc_points_lost(date1, date2)
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

async def process_info(ctx, users, user):
    ranking_points = users[str(user.id)]['ranking_points']
    streak = users[str(user.id)]['streak']
    if ranking_points <= 300:
        embed = discord.Embed(description='**Historian title: Pupil**\n**Ranking points: {}**\n**Streak: {}**'.format(ranking_points, streak), colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url = 'https://royaleapi.com/static/img/arenas/arena13.png')
        embed.set_author(name="{}'s stats".format(user.name), icon_url="{}".format(user.avatar_url))
    elif 300 < ranking_points <= 600:
        embed = discord.Embed(description='**Historian title: Newbie**\n**Ranking points: {}**\n**Streak: {}**'.format(ranking_points, streak), colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url = 'https://royaleapi.com/static/img/arenas/arena14.png')
        embed.set_author(name="{}'s stats".format(user.name), icon_url="{}".format(user.avatar_url))
    elif 600 < ranking_points <= 900:
        embed = discord.Embed(description='**Historian title: Specialist**\n**Ranking points: {}**\n**Streak: {}**'.format(ranking_points, streak), colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url = 'https://royaleapi.com/static/img/arenas/arena15.png')
        embed.set_author(name="{}'s stats".format(user.name), icon_url="{}".format(user.avatar_url))
    elif 900 < ranking_points <= 1200:
        embed = discord.Embed(description='**Historian title: Expert**\n**Ranking points: {}**\n**Streak: {}**'.format(ranking_points, streak), colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url = 'https://royaleapi.com/static/img/arenas/arena16.png')
        embed.set_author(name="{}'s stats".format(user.name), icon_url="{}".format(user.avatar_url))
    elif 1200 < ranking_points <= 1500:
        embed = discord.Embed(description='**Historian title: Candidate Master**\n**Ranking points: {}**\n**Streak: {}**'.format(ranking_points, streak), colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url = 'https://royaleapi.com/static/img/arenas/arena17.png')
        embed.set_author(name="{}'s stats".format(user.name), icon_url="{}".format(user.avatar_url))
    elif 1500 < ranking_points <= 1800:
        embed = discord.Embed(description='**Historian title: Master**\n**Ranking points: {}**\n**Streak: {}**'.format(ranking_points, streak), colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url = 'https://royaleapi.com/static/img/arenas/arena18.png')
        embed.set_author(name="{}'s stats".format(user.name), icon_url="{}".format(user.avatar_url))
    elif 1800 < ranking_points <= 2100:
        embed = discord.Embed(description='**Historian title: Grandmaster**\n**Ranking points: {}**\n**Streak: {}**'.format(ranking_points, streak), colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url = 'https://royaleapi.com/static/img/arenas/arena19.png')
        embed.set_author(name="{}'s stats".format(user.name), icon_url="{}".format(user.avatar_url))
    elif 2100 < ranking_points <= 2400:
        embed = discord.Embed(description='**Historian title: International Grandmaster**\n**Ranking points: {}**\n**Streak: {}**'.format(ranking_points, streak), colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url = 'https://royaleapi.com/static/img/arenas/arena20.png')
        embed.set_author(name="{}'s stats".format(user.name), icon_url="{}".format(user.avatar_url))
    elif 2400 < ranking_points <= 2700:
        embed = discord.Embed(description='**Historian title: Legendary Grandmaster**\n**Ranking points: {}**\n**Streak: {}**'.format(ranking_points, streak), colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url = 'https://royaleapi.com/static/img/arenas/arena21.png')
        embed.set_author(name="{}'s stats".format(user.name), icon_url="{}".format(user.avatar_url))
    elif 2700 < ranking_points <= 3000:
        embed = discord.Embed(description='**Historian title: Legendary Grandmaster [Bronze I]**\n**Ranking points: {}**\n**Streak: {}**'.format(ranking_points, streak), colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url = 'https://royaleapi.com/static/img/badge/bronze-1/Cherry_Blossom_01.png')
        embed.set_author(name="{}'s stats".format(user.name), icon_url="{}".format(user.avatar_url))
        embed.set_footer(text = 'This person has reached Legendary Grandmaster.', icon_url='https://royaleapi.com/static/img/arenas/arena21.png')
    elif 3000 < ranking_points <= 3300:
        embed = discord.Embed(description='**Historian title: Legendary Grandmaster [Bronze II]**\n**Ranking points: {}**\n**Streak: {}**'.format(ranking_points, streak), colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url = 'https://royaleapi.com/static/img/badge/bronze-2/Cherry_Blossom_01.png')
        embed.set_author(name="{}'s stats".format(user.name), icon_url="{}".format(user.avatar_url))
        embed.set_footer(text = 'This person has reached Legendary Grandmaster.', icon_url='https://royaleapi.com/static/img/arenas/arena21.png')
    elif 3300 < ranking_points <= 3600:
        embed = discord.Embed(description='**Historian title: Legendary Grandmaster [Bronze III]**\n**Ranking points: {}**\n**Streak: {}**'.format(ranking_points, streak), colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url = 'https://royaleapi.com/static/img/badge/bronze-3/Cherry_Blossom_01.png')
        embed.set_author(name="{}'s stats".format(user.name), icon_url="{}".format(user.avatar_url))
        embed.set_footer(text = 'This person has reached Legendary Grandmaster.', icon_url='https://royaleapi.com/static/img/arenas/arena21.png')
    elif 3600 < ranking_points <= 3900:
        embed = discord.Embed(description='**Historian title: Legendary Grandmaster [Silver I]**\n**Ranking points: {}**\n**Streak: {}**'.format(ranking_points, streak), colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url = 'https://royaleapi.com/static/img/badge/silver-1/Cherry_Blossom_01.png')
        embed.set_author(name="{}'s stats".format(user.name), icon_url="{}".format(user.avatar_url))
        embed.set_footer(text = 'This person has reached Legendary Grandmaster.', icon_url='https://royaleapi.com/static/img/arenas/arena21.png')
    elif 3900 < ranking_points <= 4200:
        embed = discord.Embed(description='**Historian title: Legendary Grandmaster [Silver II]**\n**Ranking points: {}**\n**Streak: {}**'.format(ranking_points, streak), colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url = 'https://royaleapi.com/static/img/badge/silver-2/Cherry_Blossom_01.png')
        embed.set_author(name="{}'s stats".format(user.name), icon_url="{}".format(user.avatar_url))
        embed.set_footer(text = 'This person has reached Legendary Grandmaster.', icon_url='https://royaleapi.com/static/img/arenas/arena21.png')
    elif 4200 < ranking_points <= 4500:
        embed = discord.Embed(description='**Historian title: Legendary Grandmaster [Silver III]**\n**Ranking points: {}**\n**Streak: {}**'.format(ranking_points, streak), colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url = 'https://royaleapi.com/static/img/badge/silver-3/Cherry_Blossom_01.png')
        embed.set_author(name="{}'s stats".format(user.name), icon_url="{}".format(user.avatar_url))
        embed.set_footer(text = 'This person has reached Legendary Grandmaster.', icon_url='https://royaleapi.com/static/img/arenas/arena21.png')
    elif 4500 < ranking_points <= 4800:
        embed = discord.Embed(description='**Historian title: Legendary Grandmaster [Gold I]**\n**Ranking points: {}**\n**Streak: {}**'.format(ranking_points, streak), colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url = 'https://royaleapi.com/static/img/badge/gold-1/Cherry_Blossom_01.png')
        embed.set_author(name="{}'s stats".format(user.name), icon_url="{}".format(user.avatar_url))
        embed.set_footer(text = 'This person has reached Legendary Grandmaster.', icon_url='https://royaleapi.com/static/img/arenas/arena21.png')
    elif 4800 < ranking_points <= 5100:
        embed = discord.Embed(description='**Historian title: Legendary Grandmaster [Gold II]**\n**Ranking points: {}**\n**Streak: {}**'.format(ranking_points, streak), colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url = 'https://royaleapi.com/static/img/badge/gold-2/Cherry_Blossom_01.png')
        embed.set_author(name="{}'s stats".format(user.name), icon_url="{}".format(user.avatar_url))
        embed.set_footer(text = 'This person has reached Legendary Grandmaster.', icon_url='https://royaleapi.com/static/img/arenas/arena21.png')
    elif 5100 < ranking_points <= 5400:
        embed = discord.Embed(description='**Historian title: Legendary Grandmaster [Gold III]**\n**Ranking points: {}**\n**Streak: {}**'.format(ranking_points, streak), colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url = 'https://royaleapi.com/static/img/badge/gold-3/Cherry_Blossom_01.png')
        embed.set_author(name="{}'s stats".format(user.name), icon_url="{}".format(user.avatar_url))
        embed.set_footer(text = 'This person has reached Legendary Grandmaster.', icon_url='https://royaleapi.com/static/img/arenas/arena21.png')
    elif ranking_points > 5400:
        embed = discord.Embed(description='**Historian title: Legendary Grandmaster [Platinum]**\n**Ranking points: {}**\n**Streak: {}**'.format(ranking_points, streak), colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.set_thumbnail(url = 'https://royaleapi.com/static/img/badge/legendary/Cherry_Blossom_01.png')
        embed.set_author(name="{}'s stats".format(user.name), icon_url="{}".format(user.avatar_url))
        embed.set_footer(text = 'This person has reached Legendary Grandmaster and has reached the maximum rank.', icon_url='https://royaleapi.com/static/img/arenas/arena21.png')
    await ctx.send(embed = embed)
