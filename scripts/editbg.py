from PIL import Image
import os


print (os.getcwd())
temp_folder = os.path.join(os.getcwd(), 'Work\\TableTop\\files\\temp')
save_folder = os.path.join(os.getcwd(), 'Work\\TableTop\\files\\temp\\planets')

bg_img = Image.open(os.path.join(temp_folder, 'bg2.jpg'))
size = bg_img.size
reduce_y = int(bg_img.size[0]* 0.15)
reduce_x = int(bg_img.size[1]* 0.05)
area = (reduce_y, reduce_x ,bg_img.size[0] - reduce_y, bg_img.size[1]- reduce_x)
cropped_img = bg_img.crop(area)
savepath = os.path.join(temp_folder, 'croped.png')
cropped_img.save(savepath)

