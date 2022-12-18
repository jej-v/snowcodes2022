import discord
from discord.ext import commands
from discord.commands import Option
from commands.funcs.yatta_gif import yatta_gif

# List of commands here:
# /yattagif

class Gif(commands.Cog, description='Gif maker'):
    def __init__(self, bot):
        self.bot = bot
        self.footer = "Developed by jej#6495 for Snowcodes 2022 ❄️"

    @commands.slash_command()
    async def yattagif(
        self,
        ctx: discord.ApplicationContext,
        member: Option(discord.Member, "member", required=False)):
    
        """Get Yatta'd"""

        if member is None:
            member = ctx.author

        url = str(member.display_avatar)
        yatta_gif(url)
        await ctx.respond("Loading....")
        embed = discord.Embed (
            title = 'I will reverse all creations!',
            description = "",
            colour = discord.Colour.from_rgb(247, 168, 178)
        )

        file = discord.File("assets/images/yatta/result.gif", filename="result.gif")

        embed.set_image(url="attachment://result.gif")
        embed.set_thumbnail(url="https://img-os-static.hoyolab.com/communityWeb/upload/558a79d377063b7e0aec34cc65b9df87.png")
        embed.set_footer(text=self.footer)
        
        await ctx.edit(content=None, file=file, embed=embed)

def setup(bot):
    bot.add_cog(Gif(bot))
