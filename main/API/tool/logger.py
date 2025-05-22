# Импортирование библиотек
from datetime import date
import logging
from logging.handlers import RotatingFileHandler
import os


# Функция для инициализации объекта логирования
def setup_logger(name: str) -> logging.Logger:
    '''Настройка объекта логирования'''

    # Создание папки для логов, если ее нет
    os.makedirs('logs', exist_ok=True)

    # Создание объекта логирования
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # 1. Обработчик для записи в файл
    file_handler = RotatingFileHandler(
        f'logs/{date.today()}.log',
        maxBytes=5*1024*1024,           # 5 MB
        backupCount=3,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    )

    # 2. Обработчик для вывода в консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(
        logging.Formatter('%(levelname)s - %(message)s')
    )
    
    # Очистка старых обработчиков
    logger.handlers.clear()

    # Добавляем обработчики к объекту логирования
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger