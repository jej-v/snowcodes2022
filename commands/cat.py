import discord
import json
from urllib.request import urlopen, Request
from discord.ext import commands
from discord.commands import Option

class Cat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Cat Button
    class catButton(discord.ui.View):
        @discord.ui.button(emoji='🐱', style=discord.ButtonStyle.primary)
        async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed (
                title = 'cat',
                colour = discord.Colour.random()
            )
        
            url = 'https://api.thecatapi.com/v1/images/search'
            r = urlopen(url)

            img = json.loads(r.read().decode('utf-8'))[0]['url']

            embed.set_image(url=img)
            embed.set_footer(text='cat')

            await interaction.response.send_message(embed=embed, view=Cat.catButton())

    # Cat
    @commands.slash_command()
    async def cat(self, ctx):
        
        '''cat'''
        
        embed = discord.Embed (
            title = 'cat',
            colour = discord.Colour.random()
        )
        
        url = 'https://api.thecatapi.com/v1/images/search'
        r = urlopen(url)

        img = json.loads(r.read().decode('utf-8'))[0]['url']

        embed.set_image(url=img)
        embed.set_footer(text='cat')

        await ctx.respond(embed=embed, view=self.catButton())

    # Catch cat error
    @cat.error
    async def cat_error(self,ctx,error):
        if isinstance(error, discord.errors.ApplicationCommandInvokeError):

            embed = discord.Embed (
                title = '429',
                colour = discord.Colour.from_rgb(248, 178, 41)
            )

            embed.set_image(url="https://http.cat/429")
            embed.set_footer(text='many purrequests!')

            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Cat(bot))