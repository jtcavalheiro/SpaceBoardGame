from PIL import Image, ImageDraw, ImageFont, ImageOps
import json


result = [
'Planet',
'Asteroid',
'Debris'
]

for i in range(3):
    for x in range(10):
        img = Image.new('RGB', (600, 800), color = 'gray')
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 28, encoding="unic")
        d.text((30, 30), result[i] , font=font, fill='black')
        img_with_border = ImageOps.expand(img,border=20,fill='black')
        card_name= 'explore_' + str(i+1) + str(x+1) + '.png'
        img_with_border.save(card_name)
