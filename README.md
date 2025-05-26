
# PhotoMusic Bot 🎵🤖

Telegram-бот, который создает музыкальные плейлисты на основе изображения.

## Возможности
- Принимает фотографию
- Определяет жанры с помощью YOLO
- Создает плейлист на Яндекс.Музыке

## Запуск

1. Установите зависимости:
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
```

2. Создайте `.env` файл:

```dotenv
TGTOKEN=...
YMTOKEN=...
MODEL_PATH=...
USERS_DB=...
TRACKS_DB=...
```

3. Запустите бота:

```bash
python bot.py
```

## Зависимости

* aiogram
* ultralytics (YOLO)
* aiosqlite
* python-dotenv
* yandex-music


