from PIL import Image, ImageDraw, ImageFont, ImageOps
import json, os


# Settings
files_folder = os.path.join(os.getcwd(), 'SpaceBoardGame\\files')
icons_folder = os.path.join(os.getcwd(), 'SpaceBoardGame\\files\\icons')
temp_folder = os.path.join(os.getcwd(), 'SpaceBoardGame\\files\\temp')
save_folder = os.path.join(os.getcwd(), 'SpaceBoardGame\\files\\player_mat')

f = open(os.path.join(files_folder,'factions.json'))  
factions = json.load(f)

n_size = (630, 880)
card_size = (n_size[0]*6,n_size[1]*2)

bord_size = 20
body_size = (card_size[0] - bord_size*2, card_size[1] - bord_size*2)

ilustration_y = 100

icons = ['credits.png', 'food.png', 'water.png', 'fuel.png', 'ore.png']
resources = ['credits', 'food', 'water', 'fuel', 'ore']
res_color = {'credits': '#E7B936', 'food': '#C3FF8D', 'water': '#96EDFF', 'fuel':'black', 'ore':'gray'}


# Load icons
icons = ['pop.png', 'credits.png', 'food.png', 'water.png', 'fuel.png', 'ore.png']
for i in range(len(icons)):
    icons[i] = os.path.join(icons_folder, icons[i])

# Create Base
bg_img = Image.open(os.path.join(temp_folder, 'bg.jpg'))
body_box = (bord_size, bord_size, card_size[0] - bord_size, card_size[1] - bord_size)
bg_img = bg_img.resize(body_size)
new_card = Image.new('RGBA', body_size)
new_card.paste(bg_img, (0, 0))
new_card = ImageOps.expand(new_card, border=bord_size, fill='black')
savepath = os.path.join(temp_folder, 'base_player.png')
new_card.save(savepath)


for i in factions['factions']:

    base_img = Image.open(os.path.join(temp_folder, 'base_player.png'))
    new_card = Image.new('RGBA', (base_img.width, base_img.height))
    new_card.paste(base_img, (0, 0))
    draw = ImageDraw.Draw(new_card)

    # Faction Name
    font = ImageFont.truetype("arial.ttf", 70)
    faction_name = i['faction']
    l, u, r, b = font.getbbox(faction_name)
    w = l + r
    h = u + b
    draw.text(((new_card.width-w)/2, 40), faction_name, font=font, fill='black')

# Tech Cards
    n_ship = 3
    n_civ = 2
    n_cards = n_ship + n_civ
    spacing = 75

    # Ship outer
    x_pos = bord_size
    xx_pos =(card_size[0]/2) - (((n_cards * n_size[0] ) + ((n_cards - 1)*spacing))/2) + ((n_ship * n_size[0] ) + (2 * spacing)) + 30
    y_pos = (card_size[1] / 2.2 ) - 70
    yy_pos = y_pos + n_size[1]  + 100
    draw.rectangle((x_pos, y_pos , xx_pos, yy_pos), fill='#71A9A4', outline=(0, 0, 0))

    # Ship text
    font = ImageFont.truetype("arial.ttf", 50)
    x_pos = bord_size + 10
    y_pos = (card_size[1] / 2.2 ) - 60
    draw.text((x_pos, y_pos), 'Ship Tech', font=font, fill='black')

    # Civ outer
    x_pos = (card_size[0]/2) - (((n_cards * n_size[0] ) + ((n_cards - 1) * spacing))/2) + ((n_ship * n_size[0] ) + (2*spacing)) + 45
    xx_pos =card_size[0] - bord_size
    y_pos = (card_size[1] / 2.2 ) - 70
    yy_pos = y_pos + n_size[1]  + 100
    draw.rectangle((x_pos, y_pos , xx_pos, yy_pos), fill='#71A979', outline=(0, 0, 0))    

    # Civ text
    font = ImageFont.truetype("arial.ttf", 50)
    x_pos = (card_size[0]/2) - (((n_cards * n_size[0] ) + ((n_cards - 1) * spacing))/2) + ((n_ship * n_size[0] ) + (2*spacing)) + 55
    y_pos = (card_size[1] / 2.2 ) - 60
    draw.text((x_pos, y_pos), 'Civ Tech', font=font, fill='black')

    # Cards Slots
    n_cards = 5
    x_pos = (card_size[0]/2) - (((n_cards * n_size[0] ) + ((n_cards - 1) * spacing))/2)
    for ii in range(n_cards):
        cur = ii + 1
        xx_pos = x_pos + n_size[0]
        y_pos = (card_size[1] / 2.2 )
        yy_pos = y_pos + n_size[1]
        draw.rectangle((x_pos, y_pos , xx_pos, yy_pos), fill='gray', outline=(0, 0, 0))
        x_pos = xx_pos + spacing


    # Fuel Slots
    fuel_size = 100
    fuel_slots = 10
    spacing = 10
    x_pos = (card_size[0]/2) - (((fuel_slots * fuel_size ) + ((fuel_slots - 1) * spacing))/2)
    for ii in range(fuel_slots):
        cur = ii + 1
        xx_pos = x_pos + fuel_size
        y_pos = (card_size[1] / 5)
        yy_pos = y_pos + fuel_size
        draw.rectangle((x_pos, y_pos , xx_pos, yy_pos), fill='black', outline=(0, 0, 0))
        x_pos = xx_pos + spacing   

    card_name= 'player_' + str(i['id']) + '.png'
    new_card.save(os.path.join(save_folder, card_name))
    print (card_name)
