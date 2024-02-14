import os


for filename in os.listdir('D:\\Project\\data_aug\\test\\rap\\'):
    if not filename.endswith('.jpg'):
        os.remove(f'D:\\Project\\data_aug\\test\\rap\\{filename}')
        
        

