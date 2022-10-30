from PIL import Image
import os


print (os.getcwd())
data_folder = os.path.join(os.getcwd(), 'Work\\TableTop\\files\\original_planets')
save_folder = os.path.join(os.getcwd(), 'Work\\TableTop\\files\\temp\\planets')

files = os.listdir(data_folder)

count = 1
for f in files:
    print (f)
    fpath = os.path.join(data_folder, f)
    img = Image.open(fpath)
    area = (460, 175, 2100, 1225)
    cropped_img = img.crop(area)
    
    fname = str(count) + '.png'
    spath = os.path.join(save_folder, fname)
    cropped_img.save(spath)
    count = count + 1

