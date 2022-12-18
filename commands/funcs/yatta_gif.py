from PIL import Image, ImageSequence
from urllib.request import urlopen, Request

# A gif maker that takes the user's discord profile picture and 
# and makes the Herrscher of Sentience's ultimate come into action.

def yatta_gif(url):
    frames = []

    im1 = Image.open('assets/images/yatta/yatta.gif')
    im2 = Image.open(urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))).resize((200,200))
    
    img = Image.new("RGB", im1.size, (255, 255, 255))
    img.paste(im2, (210,60))

    for frame in ImageSequence.Iterator(im1):
        if len(frames) < 35:
            mask_im = Image.open(f'assets/images/yatta/fmask/senti{len(frames)}.png').resize(im1.size).convert('1')
            frame = Image.composite(im1, img, mask_im)
            frame = frame.copy()
            frames.append(frame)
        else:
            frame = frame.copy()
            frames.append(frame)
    
    print(len(frames))
    frames[0].save('assets/images/yatta/result.gif', save_all=True, append_images=frames[1:], duration=30, loop=0)