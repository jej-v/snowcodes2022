import discord
import json
import config
import pprint
from discord.ext import commands
from discord.commands import Option
from urllib.request import urlopen, Request

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
        
        # Search the anime and get its id.
        search_url = f'https://api.myanimelist.net/v2/anime?q={title}'
        result = urlopen(Request(search_url, headers={'X-MAL-CLIENT-ID': config.mal_api_key}))
        
        anime_id = json.loads(result.read().decode('utf-8'))['data'][0]['node']['id']

        # Get anime details by id
        url = f'https://api.myanimelist.net/v2/anime/{anime_id}?fields=id,title,main_picture,alternative_titles,start_date,end_date,synopsis,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,related_anime,related_manga,recommendations,studios,statistics'
        
        r = urlopen(Request(url, headers={'X-MAL-CLIENT-ID': config.mal_api_key}))  
        anim = json.loads(r.read().decode('utf-8'))

        embed = discord.Embed(
            title = f"{anim['title']}",
            url = f"https://myanimelist.net/anime/{anime_id}",
            colour = discord.Colour.random()
        )

        embed.set_thumbnail(url=f"{anim['main_picture']['medium']}")

        syn = list(filter(None, anim['synopsis'].split('\n')))

        embed.add_field(name='Description', value=syn[0], inline=False)
        
        for i in range(1, len(syn)):
            embed.add_field(name='\u200b', value=syn[i], inline=False)

        if anim['media_type'] == 'tv':
            embed.add_field(name='Episodes', value=anim['num_episodes'], inline=True)
            embed.add_field(name='Duration', value=f"{anim['average_episode_duration']//60} min", inline=True)
            embed.add_field(name='Status', value=" ".join(anim['status'].split('_')).capitalize(), inline=True)
            embed.add_field(name='Broadcast', value=f"{anim['broadcast']['day_of_the_week'].capitalize()}, {anim['broadcast']['start_time']}", inline=True)
        
        elif anim['media_type'] == 'movie':
            embed.add_field(name='Duration', value=f"{anim['average_episode_duration']//60} min", inline=True)
            embed.add_field(name='Status', value=" ".join(anim['status'].split('_')).capitalize(), inline=True)   
        
        embed.add_field(name='Started Airing at:', value=anim['created_at'][:10], inline=True)
        embed.add_field(name='Finished Airing at:', value=anim['end_date'], inline=True)
       
        genres = []
        for i in range(0, len(anim['genres'])):
            genres.append(anim['genres'][i]['name'])

        embed.add_field(name='Genres', value=", ".join(genres), inline=False)

        await ctx.respond(embed=embed)

    # Catch Anime Error
    @anime.error
    async def anime_error(self,ctx,error):
        print(error)
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

        # Search the manga and get its id.
        search_url = f'https://api.myanimelist.net/v2/manga?q={title}'
        result = urlopen(Request(search_url, headers={'X-MAL-CLIENT-ID': config.mal_api_key}))
        
        manga_id = json.loads(result.read().decode('utf-8'))['data'][0]['node']['id']
            
        # Get manga details by id
        url = f'https://api.myanimelist.net/v2/manga/{manga_id}?fields=id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_volumes,num_chapters,pictures,background,related_anime,related_manga,recommendations'
        
        r = urlopen(Request(url, headers={'X-MAL-CLIENT-ID': config.mal_api_key}))  
        mang = json.loads(r.read().decode('utf-8'))


        embed = discord.Embed(
            title = f"{mang['title']}",
            url = f"https://myanimelist.net/manga/{manga_id}",
            colour = discord.Colour.random()
        )

        embed.set_thumbnail(url=f"{mang['main_picture']['medium']}")

        syn = list(filter(None, mang['synopsis'].split('\n')))
        embed.add_field(name='Description', value=syn[0], inline=False)
        
        for i in range(1, len(syn)):
            embed.add_field(name='\u200b', value=syn[i], inline=False)

        embed.add_field(name='Volumes', value=mang['num_volumes'], inline=True)
        embed.add_field(name='Chapters', value=mang['num_chapters'], inline=True)
        embed.add_field(name='Status', value=" ".join(mang['status'].split('_')).capitalize(), inline=True)  

        genres = []
        for i in range(0, len(mang['genres'])):
            genres.append(mang['genres'][i]['name'])

        embed.add_field(name='Genres', value=", ".join(genres), inline=False)

        await ctx.respond(embed=embed)

    # Catch Manga Error
    @manga.error
    async def manga_error(self,ctx,error):
        print(error)
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