import discord
import json
from discord.ext import commands

i = 1
class TwDays(commands.Cog):
    # Buttons for twelvedays command
    class twButtons(discord.ui.View):
        @discord.ui.button(emoji='➡️', style=discord.ButtonStyle.secondary)
        async def right_botton(self, button: discord.ui.Button, interaction: discord.Interaction):
            global i
            i = i + 1
                
            if i == 13:
                button.disabled = True
                await interaction.response.edit_message(view=self)
                
            else:
                embed = discord.Embed (
                    title = 'The Twelve Computerized Days of Christmas',
                    colour = discord.Colour.random()
                )

                with open('assets/12dayscompdays.json') as f:
                    twdays = json.load(f)
                    
                embed.set_footer(text='from xmas_twe.lve on textfiles.com')
                embed.set_thumbnail(url="https://img-os-static.hoyolab.com/communityWeb/upload/9eb3b2dea8b25eea2e5dd0bd3a433389.gif")
                embed.add_field(name=f'Day {i}', value='\n'.join(twdays[i-1][str(i)]), inline=False)

                await interaction.response.edit_message(embed=embed)


    # THE TWELVE COMPUTERIZED DAYS OF CHRISTMAS from xmas_twe.lve on textfiles.com
    @commands.slash_command()
    async def twelvedays(self, ctx):

        '''The twelve computerized days of Christmas'''

        embed = discord.Embed (
            title = 'The Twelve Computerized Days of Christmas',
            colour = discord.Colour.random()
        )

        embed.set_thumbnail(url="https://img-os-static.hoyolab.com/communityWeb/upload/9eb3b2dea8b25eea2e5dd0bd3a433389.gif")
        with open('assets/12dayscompdays.json') as f:
            twdays = json.load(f)

        embed.set_footer(text='📄 from xmas_twe.lve on textfiles.com')
        embed.add_field(name=f'Day 1', value='\n'.join(twdays[0][str(1)]), inline=False)
        await ctx.respond(embed=embed, view=self.twButtons())

def setup(bot):
    bot.add_cog(TwDays(bot))