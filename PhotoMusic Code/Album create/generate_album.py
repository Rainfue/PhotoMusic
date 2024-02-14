# %%
from yandex_music import Client

# %%
client = Client('y0_AgAAAABUzxkNAAG8XgAAAAD5FT2pAAANjfSxyG5KUJGWZL4YyRTcLHW4qQ').init()
# %%
# def send_search_request_and_print_result(query):
#     tracks=client.search(query).tracks["results"]
#     for elem in tracks:
#         print(elem,"\n"*2)
        
# %%
# input_query = input('Введите поисковой запрос: ')
# send_search_request_and_print_result(input_query)

# %%
# playlist = client.users_playlists_create('Title')
# client.users_playlists_insert_track(playlist.kind, track_id, album_id)

# %%
from yandex_music import Client
search = client.search('classical', nocorrect=False, type_ = 'album')
print(search)

# %%
search_split = str(search).split("}, {")
album_name_list = []
for el in search_split:
    string = str(el)

# Извлечение названия
    start_index = string.find("'id': '") + len("'id': '")
    end_index = string.find(",", start_index)
    name = string[start_index:end_index]
    album_name_list.append(name)
# album_name_list = set(album_name_list)
album_name_list.remove(album_name_list[0])
print(album_name_list[0:5])
# %%
