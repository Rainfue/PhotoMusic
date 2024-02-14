# %%
import tensorflow as tf
from keras.applications.vgg16 import VGG16
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Dropout
from keras.layers.experimental.preprocessing import Normalization
from keras.optimizers import Adam
from keras.preprocessing import image_dataset_from_directory
import matplotlib.pyplot as plt



# classes = ['alternative', 'classical', 'electronics', 'indie', 'jazz', 'metal', 'pop', 'rap', 'rock']

#Load data lol
# %%
train_dataset = image_dataset_from_directory('D:\Project\TESTFUCK\\train',
                                             subset='training',
                                             seed=42,
                                             validation_split=0.1,
                                             batch_size=128,
                                             image_size=(128, 128))

class_names = train_dataset.class_names
print(class_names)


# %%
validation_dataset = image_dataset_from_directory('D:\Project\TESTFUCK\\train',
                                             subset='validation',
                                             seed=42,
                                             validation_split=0.1,
                                             batch_size=128,
                                             image_size=(128, 128))

# %%
plt.figure(figsize=(10, 10))
for images, labels in train_dataset.take(1):
  for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(images[i].numpy().astype("uint8"))
    plt.title(class_names[labels[i]])
    plt.axis("off")

# %%
test_dataset = image_dataset_from_directory('D:\Project\TESTFUCK\\test',
                                             shuffle=True,
                                             label_mode='int',
                                             batch_size=128,
                                             image_size=(128, 128))

print(test_dataset.class_names)

# %%
AUTOTUNE = tf.data.experimental.AUTOTUNE

train_dataset = train_dataset.prefetch(buffer_size=AUTOTUNE)
validation_dataset = validation_dataset.prefetch(buffer_size=AUTOTUNE)
test_dataset = test_dataset.prefetch(buffer_size=AUTOTUNE)

#Create NN

# %%
vgg16_net = VGG16(weights='imagenet',
                  include_top=False,
                  input_shape=(128, 128, 3))

vgg16_net.trainable = False

# %%
model = Sequential()
model.add(Normalization())
# Добавляем модель VGG16 в сеть как слой
model.add(vgg16_net)
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(9, activation='softmax'))

#Compile modelll

# %%
model.compile(loss='sparse_categorical_crossentropy',
              optimizer="adam",
              metrics=['accuracy'])

#Teaching NN

# %%
history = model.fit(train_dataset,
                    epochs=10,
                    validation_data=validation_dataset)

#Rating teaching quality

# %%
scores = model.evaluate(test_dataset, verbose=1)

print("Доля верных ответов на тестовых данных, в процентах:", round(scores[1] * 100, 4))

# %%
plt.plot(history.history['accuracy'],
         label='Доля верных ответов на обучающем наборе')
plt.plot(history.history['val_accuracy'],
         label='Доля верных ответов на проверочном наборе')
plt.xlabel('Эпоха обучения')
plt.ylabel('Доля верных ответов')
plt.legend()
plt.show()

# %%
plt.plot(history.history['loss'],
         label='Ошибка на обучающем наборе')
plt.plot(history.history['val_loss'],
         label='Ошибка на проверочном наборе')
plt.xlabel('Эпоха обучения')
plt.ylabel('Ошибка')
plt.legend()
plt.show()

#Fine-tuning the neural network

# %%
vgg16_net.trainable = True
trainable = False
for layer in vgg16_net.layers:
    if layer.name == 'block5_conv1':
        trainable = True
    layer.trainable = trainable
    
model.compile(loss='sparse_categorical_crossentropy',
              optimizer=Adam(learning_rate=1e-5),
              metrics=['accuracy'])

history = model.fit(train_dataset,
                    validation_data=validation_dataset,
                    epochs=3)

#Evaluate the quality of network training

# %%
scores = model.evaluate(test_dataset, verbose=1)

# %%
model.summary()

# %%
print("Доля верных ответов на тестовых данных, в процентах:", round(scores[1] * 100, 4))

plt.plot(history.history['accuracy'],
         label='Доля верных ответов на обучающем наборе')
plt.plot(history.history['val_accuracy'],
         label='Доля верных ответов на проверочном наборе')
plt.xlabel('Эпоха обучения')
plt.ylabel('Доля верных ответов')
plt.legend()
plt.show()

#Save what we do lol

# %%
model.save("album_image_model3.h5")

# %%
