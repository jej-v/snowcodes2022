import json
from PIL import Image, ImageDraw, ImageFont


def leaderboard_sort():
    with open('db.json') as f:
        db = json.load(f)

    top_10 = sorted(db.items(), key=lambda x:x[1]['sb_thrown'], reverse=True)[0:10]
    return top_10

def final():

    bg = Image.open('assets/images/leaderboard/bg_1.png')

    font = ImageFont.truetype("assets/fonts/NotoSansCJKtc-Medium.ttf", 28)
    draw = ImageDraw.Draw(bg)
    
    top_10 = leaderboard_sort()
    places = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eigth', 'ninth', 'tenth']
    
    y = 45
    for i in range(0, len(top_10)):
        y += 67
        draw.text((53,y),f"{places[i]}@{top_10[i][1]['name']}:~> launched {top_10[i][1]['sb_thrown']} Snowballs",(255,255,255), stroke_width=1, stroke_fill=(0, 0, 0),font=font)

    bg.save("assets/images/leaderboard/leaderboard_result.png")
