# Импортирование библиотек
import asyncio
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

from tool.model import ClassificationModel
from tool.config import TGTOKEN, MODEL_PATH
from tool.ymusic import YMusic
from tool.database import UserDB

# Класс для телеграмм бота
class TGBot():
    # Конструктор класса
    def __init__(self, model_path: str = MODEL_PATH):
        self.bot = Bot(token=TGTOKEN)
        self.dp = Dispatcher()
        self.model = ClassificationModel(model_path)
        self.ymusic = YMusic()
        self._register_handlers()
        self.db = UserDB()
        self.user_id = None

    def _register_handlers(self):
        '''Регистрация обработчиков сообщений'''
        self.dp.message(Command('start'))(self._start_handler)
        self.dp.message(F.photo)(self._photo_handler)

    async def _start_handler(self, message: types.Message):
        '''Обработчик команды /start'''
        info = (message.from_user.first_name, 
          message.from_user.last_name,
          message.from_user.id, 
          message.from_user.is_premium,
          message.from_user.username,
          message.from_user.is_bot,
          )
        
        self.user_id = message.from_user.id
        print(f'user ID: {self.user_id}')
        self.db.add_info(info)

        await message.answer('''Привет! Этот бот умеет создавать плейлисты с музыкой на основе присланной фотографии.
                             \nПо всем вопросом можно обратиться анонимно здесь 👉https://t.me/HlebAnonBot
                             \nИли написать лично сюда 👉https://t.me/marrainfue
                             ''')

    async def _photo_handler(self, message: types.Message):
        '''Обработчик фотографий'''
        # Получаем ID пользователя и сохраняем
        self.user_id = message.from_user.id
        # Обновляем кол-во фотографий от пользователя в базе данных
        self.db.update_img_count(self.user_id)
        try:
            # Скачиваем фото 
            photo = message.photo[-1]   # Берем самое высокое качество
            file_id = photo.file_id
            file = await self.bot.get_file(file_id)

            # Сохраняем на сервер
            os.makedirs('downloads', exist_ok=True)
            download_path = f'downloads/{message.from_user.username}_{self.db.get_img_count(self.user_id)}.jpg'

            await self.bot.download_file(file.file_path, download_path)

            # Классификация изображения 
            top3, top3conf = self.model.classificate(download_path)
            # Считаем треки
            tracks_count = self.ymusic.tracks_counter(top3conf)

            tracklist = []
            for i in range(3):
                tracklist = tracklist + self.db.fetch_random_track(top3[i], tracks_count[i])
            playlist_link = self.ymusic.create_playlist(
                top3[0],
                tracklist=tracklist 
            )

            # Отправляем результат пользователю
            await message.reply(
                f'Ваш плейлист готов! \n{playlist_link}'
            )

            # Логирование
            print('-'*30)
            print(f'Пользователь: {message.from_user.first_name} | {self.db.get_img_count(self.user_id)} ф-й')
            print(f'Путь к фотографии: {download_path}')
            print(f'Основной жанр: {top3[0]} | {top3conf[0]:.2f}')
            print(f'Доп. жанры: {top3[1]}, {top3[2]} | {top3conf[1]:.2f}, {top3conf[2]:.2f}')
            print(f'Путь к альбому: {playlist_link}')
            print('-'*30, '\n')

        except Exception as e:
            await message.reply(f'Произошла ошибка -- {e}')

    async def run(self):
        '''Запуск бота'''
        await self.dp.start_polling(self.bot)


# Запуск бота
if __name__ == '__main__':
    print(f'Директория основного файла: {os.getcwd()}')
    model_path = os.path.join(os.getcwd(), MODEL_PATH)
    print(f'Путь к модели(осн): {model_path}')
    print(os.path.exists(model_path))
    bot = TGBot()
    asyncio.run(bot.run())