# Импортирование библиотек
from dotenv import load_dotenv
import os

load_dotenv()

# Токены к API
TGTOKEN = os.getenv('TGTOKEN')
YMTOKEN = os.getenv('YMTOKEN')

# Пути к модели и базам даных
MODEL_PATH = os.getenv('MODEL_PATH')
USERS_DB = os.getenv('USERS_DB')
TRACKS_DB = os.getenv('TRACKS_DB')

# Логирование
for path in [MODEL_PATH, USERS_DB, TRACKS_DB]:

    print(f'Доступность: {os.path.exists(path)}')
    print(f'Путь: {path}')
    print('-'*30)