import discord
import json
import random
from urllib.request import urlopen
from discord.ext import commands
from discord.commands import Option
from datetime import date

# List of commands here:
# /advice
# /bored
# /choose
# /countdown
# /magic8ball

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.footer = "Developed by jej#6495 for Snowcodes 2022 ❄️"

    # Advice
    @commands.slash_command()
    async def advice(self, ctx):

        '''Have a random slip of advice~'''
        
        url = "https://api.adviceslip.com/advice"

        r = urlopen(url)
        adv = json.loads(r.read().decode('utf-8'))

        embed = discord.Embed(
            title = f"Have a random slip of advice~",
            description = f"{adv['slip']['advice']}",
            colour = discord.Colour.random()
        )

        embed.set_thumbnail(url="https://upload-os-bbs.hoyolab.com/upload/2022/08/24/fbfc78ea104a8a3294edbb04352138fb_2018653294500640692.png")
        
        await ctx.respond(embed=embed)

    # Bored
    @commands.slash_command()
    async def bored(
        self,
        ctx: discord.ApplicationContext,
        type: Option(str, "type", required=False, choices=["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])):
        
        '''Bored?'''
        
        if type is None:
            url = 'https://www.boredapi.com/api/activity'
        else:
            url = f'http://www.boredapi.com/api/activity?type={type}'
        
        r = urlopen(url)

        act = json.loads(r.read().decode('utf-8'))

        embed = discord.Embed(
            title = f":boar: {act['activity']}",
            description = f"type: {act['type']}",
            colour = discord.Colour.random()
        )

        embed.set_thumbnail(url="https://img-os-static.hoyolab.com/communityWeb/upload/2ce4180d7704430894392038528941f2.gif")

        await ctx.respond(embed=embed)
    
    # Choose
    @commands.slash_command()
    async def choose(
        self,
        ctx: discord.ApplicationContext,
        text: Option(str, "Enter your text")):
        
        """Let me decide for you~"""

        author_name = ctx.author.name
        
        # split the text
        if ' or ' in text:
            options = text.split(' or ')
            decision = random.randint(0,len(options)-1)
            embed = discord.Embed(
                title = ":candle: It's been decided, " + author_name,
                description = f"I choose... **{options[decision]}**.",
                colour = discord.Colour.random()
            )
            
            await ctx.respond(embed=embed)

        else:
            await ctx.respond(f'I don\'t understand, {author_name}. Usage: `/choose <option1> or <option2>`')

    # XMAS Countdown
    @commands.slash_command()
    async def countdown(self, ctx):

        '''How many days till Xmas?'''
        
        today = date.today()
        xmas_day = date(today.year, 12, 25)

        if xmas_day < today:
            xmas_day = xmas_day.replace(year=today.year + 1)
        
        time_to_xmas = abs(xmas_day - today)

        if time_to_xmas.days == 0: # Xmas Day
            embed = discord.Embed(
                title = ":christmas_tree: Merry Christmas!",
                description= f"{time_to_xmas.days} days left for Xmas!",
                colour = discord.Colour.from_rgb(20, 107, 58)
                )

            file = discord.File('assets/images/wishcard/example.png', filename='example.png')

            embed.set_image(url='attachment://example.png')
            embed.set_footer(text=self.footer)

            await ctx.respond(embed=embed, file=file)
        
        else:
            embed = discord.Embed(
                title = ":christmas_tree: Countdown",
                description= f"{time_to_xmas.days} days left for Xmas!",
                colour = discord.Colour.from_rgb(20, 107, 58)
                )

            await ctx.respond(embed=embed)

    # Magic 8 Ball
    @commands.slash_command()
    async def magic8ball(
        self,
        ctx: discord.ApplicationContext,
        text: Option(str, "Enter your text", required=True)):
        
        '''Ask the magic 8 ball~'''

        num = random.randint(0, 9)
        await ctx.respond("Thinking......")
        
        embed = discord.Embed(
            title = f"The Magic 8 Ball has decided...",
            colour = discord.Colour.random()
        )

        embed.add_field(name='Question', value=text)
        embed.set_footer(text=self.footer)

        with open('assets/8ball.json') as f:
            ans = json.load(f)
        
        if num >= 6 and num<= 9:
            x = random.randint(0,len(ans[0]['positive']) - 1)
            embed.set_thumbnail(url="https://img-os-static.hoyolab.com/communityWeb/upload/acec2e33575c74105a65081ad0db4e53.png")
            embed.add_field(name='Answer', value=f":8ball: {ans[0]['positive'][x]}", inline=False)
            await ctx.edit(content=None, embed=embed)
        
        elif num >= 3 and num < 6:
            y = random.randint(0,len(ans[1]['neutral']) - 1)
            embed.set_thumbnail(url="https://img-os-static.hoyolab.com/communityWeb/upload/6a96e093f345b0fcf6ebab17627000d7.png")
            embed.add_field(name='Answer', value=f":8ball: {ans[1]['neutral'][y]}", inline=False)
            await ctx.edit(content=None, embed=embed)
        
        elif num >= 0 and num < 3:
            z = random.randint(0,len(ans[2]['negative']) - 1)
            embed.set_thumbnail(url="https://img-os-static.hoyolab.com/communityWeb/upload/7011c2aaabfb825d48e80d1a57897217.png")
            embed.add_field(name='Answer', value=f":8ball: {ans[2]['negative'][z]}", inline=False)
            await ctx.edit(content=None, embed=embed)

def setup(bot):
    bot.add_cog(Misc(bot))