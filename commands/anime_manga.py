import discord
import json
from discord.ext import commands
from discord.commands import Option
from urllib.request import urlopen

class AnimeManga(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Anime
    @commands.slash_command()
    async def anime(
        self,
        ctx: discord.ApplicationContext,
        title: Option(str, "anime", required=True)):
        
        '''Anime Search'''

        title = '-'.join(title.split(' '))
        
        url = f'https://api.jikan.moe/v4/anime?q={title}'

        r = urlopen(url)

        anim = json.loads(r.read().decode('utf-8'))['data'][0]

        embed = discord.Embed(
            title = f"{anim['titles'][0]['title']}",
            url = f"{anim['url']}",
            colour = discord.Colour.random()
        )

        embed.set_thumbnail(url=f"{anim['images']['jpg']['image_url']}")

        if len(anim['synopsis']) > 1024:
            embed.add_field(name='Description', value=f"{anim['synopsis'][:1020]}...", inline=False)
        else:
            embed.add_field(name='Description', value=anim['synopsis'], inline=False)

        embed.add_field(name='Episodes', value=anim['episodes'], inline=True)
        embed.add_field(name='Duration', value=anim['duration'], inline=True)
        embed.add_field(name='Status', value=anim['status'], inline=True)

        genres = []
        for i in range(0, len(anim['genres'])):
            genres.append(anim['genres'][i]['name'])

        embed.add_field(name='Genres', value=", ".join(genres), inline=False)

        await ctx.respond(embed=embed)

    # Catch Anime Error
    @anime.error
    async def anime_error(self,ctx,error):
        if isinstance(error, discord.errors.ApplicationCommandInvokeError):
            embed = discord.Embed (
                title = '404 - Anime Not Found',
                colour = discord.Colour.from_rgb(248, 178, 41)
            )

            embed.set_image(url="https://http.cat/404")
            embed.set_footer(text='Try searching again!')

            await ctx.send(embed=embed)


    # Manga
    @commands.slash_command()
    async def manga(
        self,
        ctx: discord.ApplicationContext,
        title: Option(str, "manga", required=True)):
        
        '''Manga Search'''

        title = '-'.join(title.split(' '))
        
        url = f'https://api.jikan.moe/v4/manga?q={title}'

        r = urlopen(url)

        mang = json.loads(r.read().decode('utf-8'))['data'][0]

        embed = discord.Embed(
            title = f"{mang['titles'][0]['title']}",
            url = f"{mang['url']}",
            colour = discord.Colour.random()
        )

        embed.set_thumbnail(url=f"{mang['images']['jpg']['image_url']}")

        embed.add_field(name='Type', value=mang['type'], inline=True)

        if len(mang['synopsis']) > 1024:
            embed.add_field(name='Description', value=f"{mang['synopsis'][:1020]}...", inline=False)
        else:
            embed.add_field(name='Description', value=mang['synopsis'], inline=False)

        embed.add_field(name='Volumes', value=mang['volumes'], inline=True)
        embed.add_field(name='Chapters', value=mang['chapters'], inline=True)
        embed.add_field(name='Status', value=mang['status'], inline=True)

        genres = []
        for i in range(0, len(mang['genres'])):
            genres.append(mang['genres'][i]['name'])

        embed.add_field(name='Genres', value=", ".join(genres), inline=False)

        await ctx.respond(embed=embed)

    # Catch Manga Error
    @manga.error
    async def manga_error(self,ctx,error):
        if isinstance(error, discord.errors.ApplicationCommandInvokeError):
            embed = discord.Embed (
                title = '404 - Manga Not Found',
                colour = discord.Colour.from_rgb(248, 178, 41)
            )

            embed.set_image(url="https://http.cat/404")
            embed.set_footer(text='Try searching again!')

            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(AnimeManga(bot))