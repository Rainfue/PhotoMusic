# Импортирование библиотек
import os

import numpy as np
from ultralytics import YOLO

# Класс для работы с моделью классификации
class ClassificationModel():
    # Конструктор класса
    def __init__(self, model_path: str):
        # Проверка формата путя к модели
        if not isinstance(model_path, str):
            raise TypeError(f'Путь к модели должен быть в формате str, а не {type(model_path)}')
        # Проверка, существует ли путь
        if not os.path.exists(model_path):
            raise TypeError(f'Путь к модели не найден')

        try:
            # Инициализация модели
            self.model = YOLO(model_path)       
        except Exception as e:
            print(f'Модель не найдена, проверьте путь\nОШибка: {e}')
        # Путь к модели
        self.model_path = model_path
        # Словарь классов
        self.classes = self.model.names    
        # Последний предикт
        self.result = None 
        

    # Функция для классификации
    def classificate(self, img: str):
        # Получение топ 3 класса (жанра)
        result = self.model.predict(img, 
                                    verbose=False,
                                    show=False,
                                    save=False)[0]
        self.result = result

        # Получаем топ 3 уверенности
        confidences = self.result.probs.top5conf[:3].cpu().numpy().astype(np.float32)

        return (
            [self.classes[i] for i in result.probs.top5[:3]],
            confidences
        )
    
    def __str__(self):
        return self.model_path
    

if __name__ == '__main__':
    model = ClassificationModel('/home/mar/PhotoMusic/main/model/model_10ep/weights/best.pt')

    print(model.classificate(r'/home/mar/PhotoMusic/main/downloads/marrainfue_None.jpg'))
