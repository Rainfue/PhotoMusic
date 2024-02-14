from PIL import Image
import os

path_test = "D:\\Project\\data_aug\\test\\rap\\"
dirs = os.listdir(path_test)

for item in dirs:
    if os.path.isfile(path_test+item):
            im = Image.open(path_test+item)
            f, e = os.path.splitext(path_test+item)
            imResize = im.resize((128,128), Image.LANCZOS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)
            
path_train = "D:\\Project\\data_aug\\train\\rap\\"
dirs = os.listdir(path_train)




