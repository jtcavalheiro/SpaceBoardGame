from PIL import Image, ImageDraw, ImageFont, ImageOps
import json, os


# Settings
files_folder = os.path.join(os.getcwd(), 'SpaceBoardGame\\files')
icons_folder = os.path.join(os.getcwd(), 'SpaceBoardGame\\files\\icons')
temp_folder = os.path.join(os.getcwd(), 'SpaceBoardGame\\files\\temp')
save_folder = os.path.join(os.getcwd(), 'SpaceBoardGame\\files\\cards')
  
f = open(os.path.join(files_folder,'planets.json'))
planets = json.load(f)

card_size = (630,880)
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
bg_img = Image.open(os.path.join(temp_folder, 'croped.png'))
body_box = (bord_size, bord_size, card_size[0] - bord_size, card_size[1] - bord_size)
bg_img = bg_img.resize(body_size)
new_card = Image.new('RGBA', body_size)
new_card.paste(bg_img, (0, 0))
new_card = ImageOps.expand(new_card, border=bord_size, fill='black')
savepath = os.path.join(temp_folder, 'base.png')
new_card.save(savepath)


# Create Cards
for i in planets['planets']:

    # Load Background
    base_img = Image.open(os.path.join(temp_folder, 'base.png'))
    new_card = Image.new('RGBA', (base_img.width, base_img.height))
    new_card.paste(base_img, (0, 0))

    # Load Ilustration
    img_path = os.path.join(os.getcwd(), 'SpaceBoardGame\\files\\temp\\planets', str(i['id']) + '.png')
    planet_image = Image.open(img_path)
    ratio = planet_image.size[0]/planet_image.size[1]
    newsize = (body_size[0], int(body_size[0]/ratio))
    planet_image = planet_image.resize(newsize)
    center_x = int(card_size[0]/2) - int(planet_image.size[0]/2)
    new_card.paste(planet_image, (center_x, ilustration_y), planet_image)


    # Manufacture
    man_pos = [(),(0,0),(0,0),(0,0)]

    # # all icons
    # count = 0
    # for ii in icons:
    #     icon = Image.open(ii)
    #     newsize = (70, 70)
    #     icon = icon.resize(newsize)
    #     dst_img.paste(icon, (60 + (count * icon.width) + (count * 40), 500), icon)
    #     count = count + 1

    # Planets Images

    # Population
    icon = Image.open(icons[0])
    newsize = (50, 50)
    icon = icon.resize(newsize)
    center_x = int(card_size[0]/2) - int(icon.size[0]/2)
    new_card.paste(icon, ( center_x, body_size[1] - 35), icon)

    draw = ImageDraw.Draw(new_card)

    # Industry
    ind_list = []
    for rec, value in i['resources'].items():
        for iii in range(int(value)):
            ind_list.append(rec)
    for ii in range(len(ind_list)):
        cur = ii + 1
        size_outer = 100
        x_pos = ((card_size[0]/(len(ind_list)+1)) * cur) - (size_outer / 2)
        y_pos = 500
        draw.ellipse((x_pos, y_pos, x_pos + size_outer, y_pos + size_outer), fill='black', outline=(0, 0, 0))
        size_inner = 85
        y_pos_inner = y_pos + (size_outer - size_inner)/2
        x_pos = ((card_size[0]/(len(ind_list)+1)) * cur) - (size_inner / 2)
        draw.ellipse((x_pos, y_pos_inner, x_pos + size_inner, y_pos_inner + size_inner), fill=res_color[ind_list[ii]], outline=(0, 0, 0))
        
    # System + Planet Name
    font = ImageFont.truetype("arial.ttf", 40)
    planet_name = i['system'] + ' - ' + i['planet']
    l, u, r, b = font.getbbox(planet_name)
    w = l + r
    h = u + b
    draw.text(((new_card.width-w)/2, 40), planet_name, font=font, fill='black')

    # Resources
    font = ImageFont.truetype("arial.ttf", 16)
    resources = ''
    count = 0
    for rec, value in i['resources'].items():
        l, u, r, b = font.getbbox(value)   
        w = l + r  
        w_pos = 95 + (count * 70) + (count * 40) - (w / 2)
        draw.text((w_pos, 470), value, font=font, fill='black')
        count = count + 1

    # Save card
    card_name= 'planet_' + str(i['id']) + '.png'
    new_card.save(os.path.join(save_folder, card_name))
    print (card_name)

