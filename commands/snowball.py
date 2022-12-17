import discord
import json
import random
import config
from urllib.request import urlopen, Request
from discord.ext import commands
from discord.commands import Option

class Snowball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.footer = "Developed by jej#6495 for Snowcodes 2022 ❄️"

    # Snowball fight
    @commands.slash_command()
    async def snowball(
        self,
        ctx: discord.ApplicationContext,
        member: Option(discord.Member, "Member", required=False)):
        
        '''Throw a snowball!'''
        
        if member is None:
            member = ctx.user

        url = f"https://api.giphy.com/v1/gifs/search?api_key={config.giphy_api_key}&q=snowball+fight&limit=25&offset=0&rating=g&lang=en"
    
        r = urlopen(url)

        gif = json.loads(r.read().decode('utf-8'))

        if member is ctx.user:
            title = f"**{ctx.user.name}** has thrown a snowball at themselves!"
        else:
            title = f"**{ctx.user.name}** has thrown a snowball at **{member.name}**!"

        embed = discord.Embed(
            title = title,
            #description = gif['data'][random.randint(0,24)]['url'],
            colour = discord.Colour.random()
        )

        ran_gif = random.randint(0,24)

        embed.set_image(url=gif['data'][ran_gif]['images']['original']['url'])
        
        # Open it
        with open('db.json') as f:
            db = json.load(f)

        if str(member.id) not in db and member.bot is False:
            # Start keeping track of member's snowball throws
            db[member.id] = {"name": member.name, "sb_thrown": 0, "sb_got_thrown": 0}

            # Save it
            with open('db.json', 'w') as out:
                json.dump(db, out, indent=4)
       
        # Reload
        with open('db.json') as f:
            db = json.load(f)

        db[str(ctx.user.id)]["sb_thrown"] += 1
        db[str(member.id)]["sb_got_thrown"] += 1
        
        # Save it
        with open('db.json', 'w') as out:
            json.dump(db, out, indent=4)   
        
        embed.set_thumbnail(url="https://img-os-static.hoyolab.com/communityWeb/upload/aaf3c9a359e7c974f83363164d17b751.gif")
        embed.set_footer(icon_url=ctx.user.avatar, text=f"{ctx.user} has thrown a total of {db[str(ctx.user.id)]['sb_thrown']} snowballs!")

        await ctx.respond(f"{member.mention}", embed=embed)

def setup(bot):
    bot.add_cog(Snowball(bot))