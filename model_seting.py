import os
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Step 1: Image Normalization

def normalize_images_in_directory(directory):
    for subdir, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(subdir, file)
                
                # Open the image and normalize
                with Image.open(img_path) as img:
                    normalized_img = np.asarray(img) / 255.0
                    normalized_image = Image.fromarray((normalized_img * 255).astype(np.uint8))
                    normalized_image.save(img_path)

# Normalize images in relevant directories
directories_to_normalize = [
    r'C:\final_project_test\Data\class-of-data-originals',
    r'C:\final_project_test\Data\class-of-data-resizing\64x64',
    r'C:\final_project_test\Data\class-of-data-resizing\32x32',
    r'C:\final_project_test\Data\class-of-data-resizing-augm'
]

for directory in directories_to_normalize:
    normalize_images_in_directory(directory)

# Step 2: Data Preparation and Loading

base_dir = r'C:\final_project_test\Data'
training_dir = os.path.join(base_dir, 'Training')
validation_dir = os.path.join(base_dir, 'Validation')
test_dir = os.path.join(base_dir, 'Test')

BATCH_SIZE = 32
TARGET_SIZE = (299, 299)  # For Inception V3

train_datagen = ImageDataGenerator(
    rescale=1./255, 
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

val_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    training_dir,
    target_size=TARGET_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

val_generator = val_datagen.flow_from_directory(
    validation_dir,
    target_size=TARGET_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=TARGET_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    shuffle=False
)

print("Images normalized and data generators are ready!")
