import os
# Импортирование библиотек
import sqlite3

from config import USERS_DB, TRACKS_DATA

print(os.listdir('API/database/users_data.db'))


# Класс для работы с базами данных
class UserDB():
    # Конструктор класса
    def __init__(self):
        self.path = 'API/database/users_data.db'

    def add_info(self, info):
        '''Ф-я для добавления юзера в базу данных'''
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO users (first_name, 
                                            last_name,
                                            user_id,
                                            is_premium,
                                            username,
                                            is_bot)
                            VALUES (?, ?, ?, ?, ?, ?)

                    ''', (info))
        
        cursor.execute('''DELETE FROM users WHERE rowid NOT IN 
                        (SELECT MIN(rowid) FROM users GROUP BY user_id)''')
        
        conn.commit()
        conn.close()

    def fetch_random_track(self, genre: str, count: int):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute('''SELECT album_id, track_id FROM tracks WHERE genre = ? ORDER BY RANDOM() LIMIT ?''', (genre, count))
        songs = cursor.fetchmany(count)
        conn.close()
        return songs
    
if __name__ == '__main__':
    usersDb = UserDB()
    usersDb.fetch_random_track('rap', 12)
