import discord
from discord.ext import commands
from discord.commands import Option
from commands.funcs.image_draw import snowglobe_img, senti, xmas_card
from commands.funcs.deepfry import final

# List of commands here:
# /wishcard <text>
# /snowglobe <member>
# /yatta <member>
# /deepfry <member> <attachment>

class Image(commands.Cog, description="Image Commands"):
    def __init__(self, bot):
        self.bot = bot
        self.footer = "Developed by jej#6495 for Snowcodes 2022 ❄️"
    
    # Wish Card
    @commands.slash_command()
    async def wishcard(
        self,
        ctx: discord.ApplicationContext,
        text: Option(str, 'text', required=True, max_length=80)):

        '''Create a card with your wishes in it!'''
        
        member = ctx.author
        url = member.avatar

        xmas_card(url, member, text)

        await ctx.respond("Loading....")
        
        embed = discord.Embed(
            title = 'Wishcard',
            colour = discord.Colour.from_rgb(0,255,30)
        )

        file = discord.File('assets/images/wishcard/wishcard_result.png', filename='wishcard_result.png')

        embed.set_image(url='attachment://wishcard_result.png')
        embed.set_footer(text=self.footer)

        await ctx.edit(content=None, file=file, embed=embed)

    # Snow Globe
    @commands.slash_command()
    async def snowglobe(
        self,
        ctx: discord.ApplicationContext,
        member: Option(discord.Member, "member", required=False)):
        
        '''Picture yourself inside a snowglobe!'''

        if member is None:
            member = ctx.author

        if member.avatar is not None:
            url = member.avatar
            snowglobe_img(url, member.name)
            
            await ctx.respond("Loading....")
            embed = discord.Embed (
                title = f'Look, it\'s {member.name}!',
                description = "",
                colour = discord.Colour.from_rgb(234, 70, 48)
            )
            
            file = discord.File("assets/images/snowglobe/snow_globe_result.png", filename="snow_globe_result.png")

            embed.set_image(url="attachment://snow_globe_result.png")
            embed.set_footer(text=self.footer)
            
            await ctx.edit(content=None, file=file, embed=embed)

        else:
            embed = discord.Embed (
                title = ':x: Please provide a user with an uploaded avatar!',
                colour = discord.Colour.from_rgb(255, 0, 0)
            )        
            await ctx.respond(embed=embed)

    # Yatta
    @commands.slash_command()
    async def yatta(
        self,
        ctx: discord.ApplicationContext,
        member: Option(discord.Member, "member", required=False)):
        
        """Get Yatta'd"""

        if member is None:
            member = ctx.author

        url = str(member.display_avatar)
        senti(url)
        await ctx.respond("Loading....")
        embed = discord.Embed (
            title = 'I will reverse all creations!',
            description = "",
            colour = discord.Colour.from_rgb(247, 168, 178)
        )

        file = discord.File("assets/images/yatta/senti_result.png", filename="senti_result.png")

        embed.set_image(url="attachment://senti_result.png")
        embed.set_thumbnail(url="https://img-os-static.hoyolab.com/communityWeb/upload/558a79d377063b7e0aec34cc65b9df87.png")
        embed.set_footer(text=self.footer)
        
        await ctx.edit(content=None, file=file, embed=embed)
        
    # Deefry
    @commands.slash_command()
    async def deepfry(
        self,
        ctx: discord.ApplicationContext,
        attachment: Option(discord.Attachment, 'Deepfry an Image', required=False),
        member: Option(discord.Member, "Deepfry a member", required=False)):

        """Deepfries your image or a member."""

        if attachment != None or member != None:
            
            # Image preceeds the member
            if attachment is not None:
                await attachment.save('assets/images/deepfry/avatar.png')
                final('assets/images/deepfry/avatar.png')
                
                embed = discord.Embed(
                title="Lookin' Crispy!",
                colour = discord.Colour.from_rgb(234, 70, 48)
            )
            
            else:
                await member.avatar.save('assets/images/deepfry/avatar.png')
                final('assets/images/deepfry/avatar.png')            
                
                embed = discord.Embed(
                title=f"{member.name} lookin' crispy!",
                description=f"got deepfried by {ctx.author.name}",
                colour = discord.Colour.from_rgb(234, 70, 48)
            )        
            
            file = discord.File('assets/images/deepfry/deepfried.png', filename='deepfried.png')
            
            await ctx.respond("Loading....")

            embed.set_thumbnail(url="https://img-os-static.hoyolab.com/communityWeb/upload/159da7599d435a24ee228116adf80434.gif")
            embed.set_image(url="attachment://deepfried.png")
            embed.set_footer(text= self.footer)

            await ctx.edit(content=None, file=file, embed=embed)    

        # Both are none
        else:
            member = ctx.author
            
            await member.avatar.save('assets/images/deepfry/avatar.png')
            final('assets/images/deepfry/avatar.png')            
            
            embed = discord.Embed(
            title=f"{member.name} lookin' crispy!",
            description=f"{ctx.author.name} has deepfried themselves!",
            colour = discord.Colour.from_rgb(234, 70, 48)
        )        
        
            file = discord.File('assets/images/deepfry/deepfried.png', filename='deepfried.png')
            
            await ctx.respond("Loading....")

            embed.set_thumbnail(url="https://img-os-static.hoyolab.com/communityWeb/upload/159da7599d435a24ee228116adf80434.gif")
            embed.set_image(url="attachment://deepfried.png")
            embed.set_footer(text= self.footer)

            await ctx.edit(content=None, file=file, embed=embed) 

def setup(bot):
    bot.add_cog(Image(bot))