# Importing the necessary modules
from yandex_music import Client  

# Specify your YaMusic account token
client = Client('y0_AgAAAABUzxkNAAG8XgAAAAD5FT2pAAANjfSxyG5KUJGWZL4YyRTcLHW4qQ').init()
# Put genres that you need in genre_list
# using a str format
genre_list = []

# Function of the album covers downloading
def down_alb_cov(i, file):
    try:
        name = f'{album.genre}.{i}'
        client.albums(f'{i}')[0].downloadCover(f'D:/Project/new_datset/{file}/{name}.png', '200x200')
        print(f'album {i} installed')
    except AttributeError:
        print(f"no {i} id album")

# Use the 'for' cycle to check existing album id
# and find there a genre that you want
for i in range(3000000,10000000):
    album=client.albums_with_tracks(i)
    if album.genre in genre_list:
        down_alb_cov(i, f'{album.genre}')
    else:
        print(f'no {i} album id')
        
        
