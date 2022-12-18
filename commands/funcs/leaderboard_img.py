import json
from PIL import Image, ImageDraw, ImageFont


def leaderboard_sort():
    """
    Sorts by the amount of snowballs thrown according to db.json,
    Returns the first 10 results, as top10.
    """
    with open('db.json') as f:
        db = json.load(f)

    top_10 = sorted(db.items(), key=lambda x:x[1]['sb_thrown'], reverse=True)[0:10]
    return top_10

def final():
    """
    From leaderboard_sort(), we get a list of users to loop through and
    pass it onto ImageDraw, to draw text onto the bg_1.png, a leaderboard template.
    """

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
