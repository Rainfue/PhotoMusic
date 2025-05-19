# Импортирование библиотек
import os

import streamlit as st

from tool.model import ClassificationModel
from tool.config import MODEL_PATH

# Класс для GUI
class GUI():
    # Конструктор класса
    def __init__(self, model: ClassificationModel):
        self.model = model
        print(model)
        self.title = st.title('PhotoMusic')
        # Для загрузки изображения
        self.img_uploader = None
        # Кнопка для предсказания жанра
        self.predict_button = None

        # 

        

    # Функция для запуска приложения
    def run(self):
        '''Основной метод для запуска приложения'''
        self.img_uploader = st.file_uploader(
            label='Выберите изображение', 
            type=['png', 'jpg', 'jpeg']
            )
        # Создаю кнопку
        self.predict_button = st.button('Предсказать')
        
        # Если загружена фотография и нажата кнопка:
        if self.predict_button:
            if self.img_uploader:
                # Имя для временного файла
                user_img, pred_img = 'user_img.jpg', 'pred.jpg'
                # Сохраняем файл пользователя
                with open(user_img, 'wb') as f:
                    f.write(self.img_uploader.getbuffer())
                # Получаю первые 3 класса (жанра)
                top3, top3conf = self.model.classificate(user_img)
                # Сохраняю вывод модели 
                self.model.result.save(filename=pred_img)
                # Вывод топ 3 жанра
                st.text(top3)
                # Вывод топ 3 "уверенности" в предсказании
                st.text(top3conf)
                # Вывод изображения с классами
                st.image(pred_img)

        

if __name__ == '__main__':
    model_path = MODEL_PATH
    app = GUI(ClassificationModel(model_path))
    app.run()

