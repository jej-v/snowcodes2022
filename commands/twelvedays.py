import discord
import json
from discord.ext import commands, pages

# List of commands here:
# /twelvedays

class TwDays(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pages = [0,0,0,0,0,0,0,0,0,0,0,0]

        with open('assets/12dayscompdays.json') as f:
            twdays = json.load(f)
            
        for i in range(0, len(twdays)):

            self.pages[i] = discord.Embed (
                    title = 'The Twelve Computerized Days of Christmas',
                    colour = discord.Colour.random())

            self.pages[i].set_footer(text='from xmas_twe.lve on textfiles.com')
            self.pages[i].set_thumbnail(url="https://img-os-static.hoyolab.com/communityWeb/upload/9eb3b2dea8b25eea2e5dd0bd3a433389.gif")
            self.pages[i].add_field(name=f'Day {i+1}', value='\n'.join(twdays[i][str(i+1)]), inline=False)

    def get_pages(self):
        return self.pages
    
    @commands.slash_command()
    async def twelvedays(self, ctx: discord.ApplicationContext):

        """The Twelve Computerized Days of Christmas."""
        
        page_buttons = [
            pages.PaginatorButton("prev", emoji="⬅", style=discord.ButtonStyle.green),
            pages.PaginatorButton(
                "page_indicator", style=discord.ButtonStyle.gray, disabled=True
            ),
            pages.PaginatorButton("next", emoji="➡", style=discord.ButtonStyle.green)
        ]
        paginator = pages.Paginator(
            pages=self.get_pages(),
            show_disabled=True,
            show_indicator=True,
            use_default_buttons=False,
            custom_buttons=page_buttons,
            loop_pages=True,
        )
        await paginator.respond(ctx.interaction, ephemeral=False)  

def setup(bot):
    bot.add_cog(TwDays(bot))