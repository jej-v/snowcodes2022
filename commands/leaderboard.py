import discord
from discord.ext import commands
from commands.funcs.leaderboard_img import final

class Leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.footer = "Developed by jej#6495 for Snowcodes 2022 ❄️"
    
    # Snowball Leaderboard
    @commands.slash_command()
    async def leaderboard(self, ctx):
        
        '''Shows the /snowball leaderboard.'''

        final()

        await ctx.respond("Loading....")
        
        embed = discord.Embed(
            colour = discord.Colour.random()
        )

        file = discord.File('assets/images/leaderboard/leaderboard_result.png', filename='leaderboard_result.png')

        embed.set_image(url='attachment://leaderboard_result.png')
        embed.set_footer(text=self.footer)

        await ctx.edit(content=None, file=file, embed=embed)

def setup(bot):
    bot.add_cog(Leaderboard(bot))