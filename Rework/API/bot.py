# Импортирование библиотек
import asyncio
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import FSInputFile

from tool.model import ClassificationModel
from tool.config import TGTOKEN, MODEL_PATH
from tool.ymusic import YMusic

# Класс для телеграмм бота
class TGBot():
    # Конструктор класса
    def __init__(self, model_path: str = MODEL_PATH):
        self.bot = Bot(token=TGTOKEN)
        self.dp = Dispatcher()
        self.model = ClassificationModel(model_path)
        self.ymusic = YMusic()
        self._register_handlers()

    def _register_handlers(self):
        '''Регистрация обработчиков сообщений'''
        self.dp.message(Command('start'))(self._start_handler)
        self.dp.message(F.photo)(self._photo_handler)

    async def _start_handler(self, message: types.Message):
        '''Обработчик команды /start'''
        await message.answer('Привет! Отправь мне фото')

    async def _photo_handler(self, message: types.Message):
        '''Обработчик фотографий'''
        try:
            # Скачиваем фото 
            photo = message.photo[-1]   # Берем самое высокое качество
            file_id = photo.file_id
            file = await self.bot.get_file(file_id)

            # Сохраняем на сервер
            os.makedirs('downloads', exist_ok=True)
            download_path = f'downloads/{file_id}.jpg'
            await self.bot.download_file(file.file_path, download_path)

            # Классификация изображения 
            top3, top3conf = self.model.classificate(download_path)

            # Отправляем результат пользователю
            await message.reply(
                f'Топ 3 класса: {top3}\n'
                f'Уверенность: {top3conf}\n'
                f'Кол-во треков: {self.ymusic.tracks_counter(top3conf)}'
                f'Плейлист: {self.ymusic.create_playlist(top3[0], tracklist=None)}'
            )

        except Exception as e:
            await message.reply(f'Произошла ошибка -- {e}')

    async def run(self):
        '''Запуск бота'''
        await self.dp.start_polling(self.bot)


# Запуск бота
if __name__ == '__main__':
    bot = TGBot()
    asyncio.run(bot.run())