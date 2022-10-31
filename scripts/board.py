from PIL import Image, ImageDraw, ImageFont, ImageOps
import json, os


# Settings
files_folder = os.path.join(os.getcwd(), 'SpaceBoardGame\\files')
icons_folder = os.path.join(os.getcwd(), 'SpaceBoardGame\\files\\icons')
temp_folder = os.path.join(os.getcwd(), 'SpaceBoardGame\\files\\temp')
save_folder = os.path.join(os.getcwd(), 'SpaceBoardGame\\files\\player_mat')

n_size = (630, 880)
card_size = (n_size[0]*6,n_size[1]*2)
board_size = (2000, 2000)
bord_size = 50
body_size = (board_size[0] - bord_size*2, board_size[1] - bord_size*2)


bg_img = Image.open(os.path.join(temp_folder, 'board_bg.jpg'))
cropped_img = bg_img.resize(board_size)
body_box = (bord_size, bord_size, body_size[0] - bord_size, body_size[1] - bord_size)

body_box = (bord_size, bord_size, card_size[0] - bord_size, card_size[1] - bord_size)
bg_img = cropped_img.resize(body_size)
new_card = Image.new('RGBA', body_size)
new_card.paste(bg_img, (0, 0))
new_card = ImageOps.expand(new_card, border=bord_size, fill='black')


draw = ImageDraw.Draw(new_card)

system_size = 200


# Starter System
x_pos = (board_size[0] / 2) - (system_size /2)
xx_pos = x_pos + system_size
y_pos = (board_size[1] / 4) - (system_size /2)
yy_pos = y_pos + system_size
draw.ellipse((x_pos, y_pos , xx_pos , yy_pos), fill='black', outline=(0, 0, 0))


# System 1

x_pos = (board_size[0] / 3) - (system_size /2)
xx_pos = x_pos + system_size
y_pos = (board_size[1] / 6) - (system_size /2)
yy_pos = y_pos + system_size
draw.ellipse((x_pos, y_pos , xx_pos , yy_pos), fill='black', outline=(0, 0, 0))

# System 2

x_pos = 2*(board_size[0] / 3) - (system_size /2)
xx_pos = x_pos + system_size
y_pos = (board_size[1] / 6) - (system_size /2)
yy_pos = y_pos + system_size
draw.ellipse((x_pos, y_pos , xx_pos , yy_pos), fill='black', outline=(0, 0, 0))

# System 3

x_pos = (board_size[0] / 3) - (system_size /2)
xx_pos = x_pos + system_size
y_pos = (board_size[1] / 3) - (system_size /2)
yy_pos = y_pos + system_size
draw.ellipse((x_pos, y_pos , xx_pos , yy_pos), fill='black', outline=(0, 0, 0))

# System 4

x_pos = 2*(board_size[0] / 3) - (system_size /2)
xx_pos = x_pos + system_size
y_pos = (board_size[1] / 3) - (system_size /2)
yy_pos = y_pos + system_size
draw.ellipse((x_pos, y_pos , xx_pos , yy_pos), fill='black', outline=(0, 0, 0))

# System 5
x_pos = (board_size[0] / 6) - (system_size /2)
xx_pos = x_pos + system_size
y_pos = (board_size[1] / 4) - (system_size /2)
yy_pos = y_pos + system_size
draw.ellipse((x_pos, y_pos , xx_pos , yy_pos), fill='black', outline=(0, 0, 0))

# System 6
x_pos = (5*(board_size[0] / 6)) - (system_size /2)
xx_pos = x_pos + system_size
y_pos = (board_size[1] / 4) - (system_size /2)
yy_pos = y_pos + system_size
draw.ellipse((x_pos, y_pos , xx_pos , yy_pos), fill='black', outline=(0, 0, 0))



savepath = os.path.join(temp_folder, 'board_ready.png')
new_card.save(savepath)








ilustration_y = 100

icons = ['credits.png', 'food.png', 'water.png', 'fuel.png', 'ore.png']
resources = ['credits', 'food', 'water', 'fuel', 'ore']
res_color = {'credits': '#E7B936', 'food': '#C3FF8D', 'water': '#96EDFF', 'fuel':'black', 'ore':'gray'}