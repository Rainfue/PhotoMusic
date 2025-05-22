# Импортирование библиотек
from dotenv import load_dotenv
import os

from tool.logger import setup_logger
logger = setup_logger(__name__)

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
    logger.debug(f'Путь: {path}')
    logger.debug(f'Доступность: {os.path.exists(path)}')
    logger.debug('-'*30)