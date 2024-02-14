# %%
# Importing the necessary modules
from keras.models import load_model
from keras.preprocessing import image                               
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import image_dataset_from_directory
import re
from yandex_music import Client
from random import randint

# %%
# Assigning classes
classes_names = ['alternative', 'classical', 'electronics', 'metal', 'pop', 'rap', 'rock']  

# %%
# Download model
model = load_model('D:\Project\Model\\album_image_model.h5')        
#
# %%
# Download image that you want to run
img_path = r'D:\Project\Dataset\val\rap\rap.10263.jpg'                              

img = image.load_img(img_path, target_size=(128, 128))
# Convert the image to an array
x = image.img_to_array(img)
# Changing the shape of the array into a flat vector
x = x.reshape(1, 128, 128, 3)
# Invert the image
x = 255 - x
# Normalize the image
x /= 255


# %%
# Use predict() metod to run your image
# through the model
prediction = model.predict(x)
# Get the max value of predict() metod
sorted_array = np.argsort(prediction[0], axis=0)
prediction1 = np.argmax(prediction) 
prediction2 = sorted_array[5]
prediction3 = sorted_array[4]

pred1_value = float((prediction[0])[prediction1])
pred2_value = float((prediction[0])[prediction2])
pred3_value = float((prediction[0])[prediction3])
# %%
# Show the image and a result using
# a matplotlib
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()
ax.imshow(img)
 
plt.show()
print(f'Genre: {classes_names[prediction1]}\n')
print(f'{classes_names[prediction1]}: {round(pred1_value*100, 1)} %')
print(f'{classes_names[prediction2]}: {round(pred2_value*100, 1)} %')
print(f'{classes_names[prediction3]}: {round(pred3_value*100, 1)} %')

# %%

def give_index(request, num):
    client = Client('y0_AgAAAABUzxkNAAG8XgAAAAD5FT2pAAANjfSxyG5KUJGWZL4YyRTcLHW4qQ').init()
    try:
        search = client.search(f'{request}',
                           nocorrect=False, 
                           page=randint(1, 99), 
                           type_ = 'album')
    except IndexError:
        search = client.search(f'{request}',
                           nocorrect=False, 
                           page=1, 
                           type_ = 'album')

    search_split = str(search).split('}, {')
    album_name_list = []

    for el in search_split:
        string = str(el)

        # Извлечение названия
        
        start_index = string.find("'genre': ") + len("'genre': ")
        end_index = string.find(",", start_index)
        
        start_index2 = string.find("'id': '") + len("'id': '")
        end_index2 = string.find(",", start_index2)
        name2 = string[start_index2:end_index2]
        album_name_list.append(name2)
        
    return (album_name_list[2:len(album_name_list)])[0:num]

# %%
print(f'List of max procent predict: {give_index(classes_names[prediction1], 5)}')
print(f'List of max procent predict: {give_index(classes_names[prediction2], 3)}')
print(f'List of max procent predict: {give_index(classes_names[prediction3], 2)}')

# %%

def give_track_id(id, num):
    
    token='y0_AgAAAABUzxkNAAG8XgAAAAD5FT2pAAANjfSxyG5KUJGWZL4YyRTcLHW4qQ'
    client=Client(token=token).init()
    album_info = ((str(client.albumsWithTracks(id)).split("[[{"))[1])

    pattern = r"'id': '\d+"
    # pattern2 = r"'\w: "
    id_tracks2 = re.findall(pattern, album_info)
    id_tracks3 = []
    for el in id_tracks2:
        result = re.findall(r'\d+', el)
        id_tracks3.append(result)
        id_tracks = []
        for x in id_tracks3:
            id_tracks.extend(x if isinstance(x, list) else [x])


    return id_tracks[0:num]

# %%

def create_playlsit(predict1, predict2, predict3):
    from datetime import date
    token='y0_AgAAAABUzxkNAAG8XgAAAAD5FT2pAAANjfSxyG5KUJGWZL4YyRTcLHW4qQ'
    client=Client(token=token).init()
    old=[]
    new=""
    for elem in Client.users_playlists_list(self=client):
        old.append(elem["kind"])
    Client.users_playlists_create(self=client,title=f"mostly {predict1} {date.today().strftime('%d/%m/%y')}")
    for elem in Client.users_playlists_list(self=client):
        if elem["kind"] not in old:
            new=elem["kind"]

    predict_list = [predict1, predict2, predict3]        

    j=0

    for i in range(len(predict_list)):
        match i:
            case 0:
                id_album_list = give_index(predict_list[i], 5)
            case 1:
                id_album_list = give_index(predict_list[i], 3)
            case 2:
                id_album_list = give_index(predict_list[i], 2)

        
        for el in id_album_list:
            album_id = el
            track_list = give_track_id(el, 3)
            for i in range(1,len(track_list)+1):    
                Client.users_playlists_insert_track(self=client,
                                                    kind=new,
                                                    album_id=f"{album_id}", 
                                                    revision=i+j,
                                                    track_id=f"{track_list[i-1]}")
            j+=len(track_list)
    
    return f"https://music.yandex.ru/users/mrrainfue/playlists/{new}"

# %%
#print(create_playlsit(classes_names[prediction1], classes_names[prediction2], classes_names[prediction3]))
print(create_playlsit(classes_names[prediction1],classes_names[prediction2],classes_names[prediction3]))

# %%
