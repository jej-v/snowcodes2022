import discord
import json
from discord.ext import commands
from discord.commands import Option

# List of commands here:
# /aboutme
# /info <member>
# /help

class About(commands.Cog, description="About commands."):
    
    def __init__(self, bot):
        self.bot = bot
        self.footer = "Developed by jej#6495 for Snowcodes 2022 ❄️"

    class scButton(discord.ui.View):
        def __init__(self, *, timeout=180):
            super().__init__(timeout=timeout)
    
    @commands.slash_command()
    async def aboutme(self, ctx):

        '''Me!'''
        bot = self.bot
        embed = discord.Embed(
            title = 'About Me',
            description = f"Greetings! I'm {bot.user.name}, nice to meet you!\n I'm a Xmas-themed bot for your server~\n\
                I provide a variaty of fun commands, from helping boredom to creating special themed profile pictures for you and your friends!\n\
                Hope you have fun with me! :blush: \n\n\
                May all the beauty be blessed. \n\
                \nProfile Picture Source:",
            color = discord.Colour.from_rgb(187, 37, 40)
        )
        
        embed.set_thumbnail(url=bot.user.avatar)
        embed.set_author(name=bot.user, icon_url=bot.user.avatar)

        embed.set_image(url='https://webstatic.hoyoverse.com/upload/uploadstatic/contentweb/20190909/2019090914221232481.jpg')
        embed.set_footer(text='Developed by jej#6495 for Snowcodes 2022 ❄️')

        buttons = self.scButton()
        buttons.add_item(discord.ui.Button(label="Source Code",style=discord.ButtonStyle.link,url="https://github.com/jej-v/snowcodes2022", emoji="<a:923308881550114897>"))
        buttons.add_item(discord.ui.Button(label="Snowcodes 2022",style=discord.ButtonStyle.link,url="https://www.snowcodes.org/", emoji="❄️"))
        
        await ctx.respond(embed=embed, view=buttons)
    
    # Info
    @commands.slash_command()
    async def info(
        self,
        ctx: discord.ApplicationContext,
        member: Option(discord.Member, "member", required=False)):
        
        """Shows member information"""

        if member is None:
            member = ctx.author

        embed = discord.Embed(
            title = str(member.name) + "#" + str(member.discriminator),
            colour = discord.Colour.random()
            )

        embed.set_footer(text='Developed by jej#6495 for Snowcodes 2022 ❄️')
        embed.set_thumbnail(url= str(member.display_avatar))

        embed.add_field(name="Nickname:", value=str(member.display_name) ,inline=False)
        joined = member.joined_at # Month-Date-Year  Hour:Minute AM/PM
        embed.add_field(name="Joined this server at:", value=joined.strftime("%b-%d-%y %I:%M %p [UTC]"), inline=False)
        created = member.created_at # Month-Date-Year  Hour:Minute AM/PM
        embed.add_field(name="Account created at:", value=created.strftime("%b-%d-%y %I:%M %p [UTC]"), inline=False)
        
        with open('db.json') as f:
            db = json.load(f)
        
        if member.bot is False:
            embed.add_field(name='Snowballs thrown:', value=db[str(member.id)]['sb_thrown'], inline=True)
            embed.add_field(name='Got thrown at:', value=db[str(member.id)]['sb_got_thrown'], inline=True)
        
        embed.add_field(name="Is a bot?", value=str(member.bot) ,inline=False)

        await ctx.respond(embed=embed)

    # Help Command
    @commands.slash_command()
    async def help(self,ctx):
        
        """Shows the command list."""
        
        embed = discord.Embed(
            title = 'Command list',
            colour = discord.Colour.from_rgb(187, 37, 40)
        )

        embed.set_thumbnail(url="https://img-os-static.hoyolab.com/communityWeb/upload/e1ebe40512b84cdf0387e6f6fd0ac118.gif")
        embed.set_author(name = self.bot.user, icon_url=self.bot.user.avatar)
        embed.set_footer(text=self.footer)

        embed.add_field(name="☃️ Xmas themed Commands", value='''
    `/countdown` - How many days left till Xmas?
    `/snowball` - Throw a snowball at someone.
    `/wishcard` - Create a card with your wishes in it.
    `/snowglobe` - Picture yourself in a Snowglobe!
    `/twelvedays` - The Twelve Computerized Days of Christmas.''', inline=False)

        embed.add_field(name="🗿 Standard Commands", value='''
    `/help` - This message.
    `/aboutme` - Information about me!
    `/info` - Shows member information.
    `/leaderboard` - Shows the leaderboard of the most snowballs thrown.''', inline=False)

        embed.add_field(name='🖼️ Image/Gif Commands', value='''
    `/deepfry` - Deepfries an image or a member.
    `/yatta` - Get Yatta'd by the great Herrscher of Sentience.
    `/yattagif` - Get Yatta'd live by the great Herrscher of Sentience.
    ''')
        embed.add_field(name="✨ Fun Commands", value='''
    `/cat` - cat.
    `/advice` - Have a random slip of advice~
    `/bored` - Bored? This may help~
    `/inspiro` - Best Inspirational Quotes ever. Source: ||trust me bro||
    `/anime` - Anime Search.
    `/manga` - Manga Search.
    `/magic8ball` - Ask the magic ball~
    `/choose` - Let the bot decide for you.''',inline=False)

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(About(bot))