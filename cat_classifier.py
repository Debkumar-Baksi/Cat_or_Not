# cat_classifier.py
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator


import os
from PIL import Image

def clean_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            try:
                Image.open(path).verify()  # check if image can be opened
            except:
                print(f"Removing invalid file: {path}")
                os.remove(path)

clean_directory("dataset/train")
clean_directory("dataset/val")




# Define a very simple CNN
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(64,64,3)),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')  # binary classification: cat or not
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Data preprocessing
train_datagen = ImageDataGenerator(rescale=1./255)
train_data = train_datagen.flow_from_directory(
    'dataset/train',  # should have 'cats/' and 'not_cats/' folders
    target_size=(64,64),
    batch_size=32,
    class_mode='binary'
)

val_data = train_datagen.flow_from_directory(
    'dataset/val',
    target_size=(64,64),
    batch_size=32,
    class_mode='binary'
)

# Train
model.fit(train_data, validation_data=val_data, epochs=20)

print("Class indices:", train_data.class_indices)

# Save model
model.save("cat_model.h5")
print("Model saved as cat_model.h5")
