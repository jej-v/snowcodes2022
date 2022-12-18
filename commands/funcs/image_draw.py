import io
import textwrap
from PIL import Image, ImageDraw, ImageFont
from urllib.request import urlopen, Request

"""
    All of the functions below work in the same way.

    Function adds the Discord User's profile picture onto
    the picture that was set as a background.

    Arguments:
        url: the url leading directly to the user's profile picture
        username: str, user's discord name
        text: for the wishcard command, types the user's input
    
    Returns:
        Sends and saves the image created, can be overwritten locally if
        it's run more than one times.
"""

def snowglobe_img(url, username):

    im1 = Image.open('assets/images/snowglobe/snow_globe.png')
    im2 = Image.open(urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))).resize(im1.size)

    mask = Image.open('assets/images/snowglobe/snow_globe_mask.png').resize(im1.size).convert('1')

    final = Image.composite(im1, im2, mask)
    
    # FONT
    font = ImageFont.truetype("assets/fonts/NotoSansCJKtc-Medium.ttf", 30)
    draw = ImageDraw.Draw(final)
    draw.text((395,730),username,(0,0,0),anchor="ma",font=font)

    final.save("assets/images/snowglobe/snow_globe_result.png")

def senti(url):

    bg = Image.open('assets/images/yatta/senti.png')
    img = Image.open(urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))).resize((170,170))

    img1 = Image.new("RGB", bg.size, (255, 255, 255))

    img1.paste(img, (230,90))
    mask_im = Image.open('assets/images/yatta/mask.png').resize(bg.size).convert('1')

    final = Image.composite(bg, img1, mask_im)
    final.save("assets/images/yatta/senti_result.png")

def xmas_card(url, username, text):
    
    bg = Image.open('assets/images/wishcard/bg.png')
    im1 = Image.open(urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))).resize((200,205))

    im2 = Image.new("RGB", bg.size, (255, 255, 255))
    im2.paste(im1, (712,92))
    mask_im = Image.open('assets/images/wishcard/mask.png').resize(bg.size).convert('1')

    final = Image.composite(bg, im2, mask_im)
    font = ImageFont.truetype("assets/fonts/VCR_OSD_MONO_1.001.ttf", 48)
    draw = ImageDraw.Draw(final)
    draw.text((70,225),f"{username}:~>\n{textwrap.fill(text, 20)}",(0,255,30),font=font)

    final.save("assets/images/wishcard/wishcard_result.png")