# %%
# Importing the necessary modules
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.applications import VGG16
from keras.optimizers import Adam
import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping

# %%
# Catalog with data for training
train_dir = 'D:\\Project\\Dataset\\train'
# Catalog with data for validation
val_dir = 'D:\\Project\\Dataset\\val'
# Catalog with data for testing
test_dir = 'D:\\Project\\Dataset\\test'
# Размеры изображения
img_width, img_height = 128, 128
# The dimension of an image-based tensor for input data to a neural network
# backend Tensorflow, channels_last
input_shape = (img_width, img_height, 3)
# The size of the mini-sample
batch_size = 64
# Number of images to training
nb_train_samples = 70000
# Number of images to validation
nb_validation_samples = 7000
# Number of images to test
nb_test_samples = 7000

# %%
# Augmented image generator
train_datagen = ImageDataGenerator(rescale=1. / 255,
                                  rotation_range=40,
                                  width_shift_range=0.2,
                                  height_shift_range=0.2,
                                  zoom_range=0.2,
                                  zca_epsilon=1e-06,
                                  horizontal_flip=True,
                                  vertical_flip = True,
                                  fill_mode='nearest')

# %%
# Preliminary work with the data
# Upload image 
image_file_name = train_dir + '\\metal\metal.8465.jpg'
img = image.load_img(image_file_name, target_size=(128, 128))
plt.imshow(img)

# %%
# Augmented image generator in work
x = image.img_to_array(img)
x = x.reshape((1,) + x.shape)
i = 0
for batch in train_datagen.flow(x, batch_size=1):
    plt.figure(i)
    imgplot = plt.imshow(image.array_to_img(batch[0]))
    i += 1
    if i % 7 == 0:
        break
plt.show()

# %%

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')

# %%
train_generator.class_indices

# %%
test_datagen = ImageDataGenerator(rescale=1. / 255)

# %%
val_generator = test_datagen.flow_from_directory(
    val_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')

# %%
test_generator = train_datagen.flow_from_directory(
    test_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')
# %%
# Adding the pre-trained VG 16 model
vgg16_net = VGG16(weights='imagenet', include_top=False, input_shape=(128, 128, 3))

# %%
# Disabling the learning ability of the model used
vgg16_net.trainable = False

# %%
vgg16_net.summary()

# %%
model = Sequential()
# Adding a VG 16 network to the model instead of a layer
model.add(vgg16_net)
model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(7))
model.add(Activation('sigmoid'))

# %%
model.summary()

# %%
# Compile model
model.compile(loss='categorical_crossentropy',
              optimizer=Adam(), 
              metrics=['accuracy'])
# %%
# Adding a callback
early_stop = EarlyStopping(monitor='val_accuracy', 
                           patience=10, verbose=1,  
                           mode='auto', 
                           restore_best_weights=True)
# %%
# Training the model
model.fit(
    train_generator,
    steps_per_epoch=100,
    epochs=30,
    callbacks=early_stop,
    validation_data=val_generator,
    validation_steps=25)

# %%
# Rating the model learning quality
scores = model.evaluate_generator(test_generator)
print("Аккуратность на тестовых данных: %.2f%%" % (scores[1]*100))

# %%
# Enabling the VG 16 model to be trained
vgg16_net.trainable = True
trainable = False
for layer in vgg16_net.layers:
    if layer.name == 'block5_conv1':
        trainable = True
    layer.trainable = trainable 

# %%
# Сheck the number of parameters to be trained
model.summary()
# %%
model.compile(loss='categorical_crossentropy',
              optimizer=Adam(learning_rate=1e-5), 
              metrics=['accuracy'])
# %%
model.fit(
    train_generator,
    epochs=4,
    validation_data=val_generator)
# %%
# Rating the model final learning quality
scores = model.evaluate(test_generator)
print("Аккуратность на тестовых данных: %.2f%%" % (scores[1]*100))
# %%
# Save model
model.save("album_image_model5.h5")
# %%
