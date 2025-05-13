# Импортирование библиотек 
from datetime import date

from yandex_music import Client

from tool.config import YMTOKEN

# Класс для обращения к API Яндекс.Музыки
class YMusic():
    # Конструктор класса
    def __init__(self):
        self.client = Client(token=YMTOKEN).init()

    # Функция для создания плейлиста
    def create_playlist(self, title, tracklist):
        # Создание нового плейлиста
        playlist = self.client.users_playlists_create(title=f"PhotoMusic {title} {date.today().strftime('%d/%m/%y')}")
        # Получение ID плейлиста
        playlist_id = playlist["kind"]

        # Вставляю треки в плейлист
        for i in range(len(tracklist)):   
            album_id = tracklist[i].split()[0]
            track_id = tracklist[i].split()[1]

            # time.sleep(0.1)  # Эмулируем задержку выполнения
            Client.users_playlists_insert_track(self=self.clientclient,
                                                kind=playlist_id,
                                                album_id=f"{album_id}", 
                                                revision=i+1,
                                                track_id=f"{track_id}") 
        
        return f"https://music.yandex.ru/users/mrrainfue/playlists/{playlist_id}"    
    
    # Функция для расчета кол-ва треков по жанру
    @staticmethod
    def tracks_counter(preds: list):
        # Список для кол-ва на каждый жанр
        tracks = []
        for pred in preds:
            tracks.append(round(30*pred/sum(preds)))
        return tracks