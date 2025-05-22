# Импортирование библиотек
import os
import sqlite3

from tool.config import USERS_DB, TRACKS_DB
from tool.logger import setup_logger
logger = setup_logger(__name__)

# Логирование
logger.debug('Модуль для баз данных импортирован!')


# Класс для работы с базами данных
class UserDB():
    # Конструктор класса
    def __init__(self):
        # Создаем папку для баз данных, если ее нет
        os.makedirs('API/database', exist_ok=True)
        # Получаем пути к БД
        self.user_path = USERS_DB
        self.track_path = TRACKS_DB

        # Если БД для пользователей отсутствует, создаю пустую
        self._init_user_db()

    # Функция для инициализации пустой базы данных пользователей
    def _init_user_db(self):
        '''Создает базу данных пользователей с нужной структурой'''
        with sqlite3.connect(self.user_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                           first_name TEXT,
                           last_name TEXT,
                           user_id INTEGER PRIMARY KEY,
                           is_premium INTEGER,
                           username TEXT,
                           is_bot INTEGER,
                           img_count INTEGER DEFAULT 0
                           )
                        ''')
            conn.commit()

    # Функция для добавления юзера в базу данных
    def add_info(self, info):
        '''
        Ф-я для добавления юзера в базу данных
        '''
        conn = sqlite3.connect(self.user_path)
        cursor = conn.cursor()
        cursor.execute('''INSERT OR IGNORE INTO users (first_name, 
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

    # Функция для получения списка случайных треков из жанра
    def fetch_random_track(self, genre: str, count: int):
        '''
        Ф-я для получения случайных треков из жанра
        '''
        conn = sqlite3.connect(self.track_path)
        cursor = conn.cursor()
        cursor.execute('''SELECT album_id, track_id FROM albums WHERE genre = ? ORDER BY RANDOM() LIMIT ?''', (genre, count))
        songs = cursor.fetchmany(count)
        conn.close()
        return songs
    
    def get_img_count(self, user_id):
        conn = sqlite3.connect(self.user_path)
        cursor = conn.cursor()

        cursor.execute('''SELECT img_count FROM users WHERE user_id = ?''', (user_id,))
        result = cursor.fetchone()

        conn.close()

        if result is None:
            return None

        return result[0]


    def update_img_count(self, user_id):
        current_count = self.get_img_count(user_id)

        if current_count is not None:
            new_count = current_count + 1

            conn = sqlite3.connect(self.user_path)
            cursor = conn.cursor()

            cursor.execute('''UPDATE users SET img_count = ? WHERE user_id = ?''', (new_count, user_id))

            conn.commit()
            conn.close()

            return new_count
        else:
            return None    
    
if __name__ == '__main__':
    usersDb = UserDB()
    print(usersDb.fetch_random_track('rap', 12))
