import discord
from discord.ext import commands
from urllib.request import urlopen, Request

class Inspiro(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Inspiro Button
    class inpsButton(discord.ui.View):
        @discord.ui.button(emoji='🤖', style=discord.ButtonStyle.primary)

        async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(
                colour = discord.Colour.from_rgb(114, 166, 137)
            )

            url = 'https://inspirobot.me/api?generate=true&season=xmas'
            r = urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))
            img = r.read().decode('utf-8')

            embed.set_image(url = img)
            embed.set_footer(text='🤖 from inspirobot.me')

            await interaction.response.send_message(embed=embed, view=Inspiro.inpsButton())

    # Inspirational Quotes
    @commands.slash_command()
    async def inspiro(self, ctx):

        '''AI Generated Inspirational Quotes.'''
        
        embed = discord.Embed(
            colour = discord.Colour.random()
        )

        url = 'https://inspirobot.me/api?generate=true&season=xmas'
        r = urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))
        img = r.read().decode('utf-8')

        embed.set_image(url = img)
        embed.set_footer(text='🤖 from inspirobot.me')

        await ctx.respond(embed=embed, view=self.inpsButton())
    
    # Catch inspiro error
    @inspiro.error
    async def cat_error(self,ctx,error):
        if isinstance(error, discord.errors.ApplicationCommandInvokeError):

            embed = discord.Embed (
                title = '404 - Quote Not Found',
                colour = discord.Colour.from_rgb(248, 178, 41)
            )

            embed.set_image(url="https://http.cat/404")
            embed.set_footer(text='Site may be down.')

            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Inspiro(bot))