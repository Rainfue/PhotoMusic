# Импортирование библиотек
from datetime import date
import logging
import os

# Создание папки для логов, если ее нет
os.makedirs('logs', exist_ok=True)

# Создание объекта логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 1. Обработчик для записи в файл
file_handler = logging.FileHandler(f'logs/{date.today()}_logs')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

# 2. Обработчик для вывода в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))

# Добавляем обработчики к объекту логирования
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# # Тестовые логи
# logger.info('Это сообщение будет и в файле и в консоли')
# logger.debug('Это сообщение будет только в файле')