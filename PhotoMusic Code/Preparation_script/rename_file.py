# %%
# Importing the necessary modules
import os

# %%
# Specify the path to your folder
folder_path = "D:\\Project\\data_aug\\val\\rap\\"  

file_list = os.listdir(folder_path)
# %%
# We go through each file
for index, file_name in enumerate(file_list):
        prefix = 'rap'
        extension = '.jpg'
        # Creating a new file name with an index
        new_file_name = f"{prefix}.{index+10236}{extension}"
        # The full path to the old file
        old_file_path = os.path.join(folder_path, file_name)
        # The full path to the new file
        new_file_path = os.path.join(folder_path, new_file_name)
        # Rename file
        os.rename(old_file_path, new_file_path)
# %%
