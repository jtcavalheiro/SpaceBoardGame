from PIL import Image, ImageDraw, ImageFont, ImageOps
import json, os


icons_folder = os.path.join(os.getcwd(), 'Work\\TableTop\\files\\icons')
temp_folder = os.path.join(os.getcwd(), 'Work\\TableTop\\files\\temp')
save_folder = os.path.join(os.getcwd(), 'Work\\TableTop\\files\\cards')

card_size = (630,880)
bord_size = 25
body_size = (card_size[0] - bord_size*2, card_size[1] - bord_size*2)



bg_img = Image.open(os.path.join(temp_folder, 'bg.jpg'))
body_box = (bord_size, bord_size, card_size[0] - bord_size, card_size[1] - bord_size)
bg_img = bg_img.crop(body_box)
new_card = Image.new('RGBA', body_size)
new_card.paste(bg_img, (0, 0))
new_card = ImageOps.expand(new_card, border=bord_size, fill='black')
savepath = os.path.join(temp_folder, 'base.png')
new_card.save(savepath)