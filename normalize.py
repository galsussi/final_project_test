import os
import numpy as np
from PIL import Image

def normalize_image(image_path, save_path):
    # Load image
    image = Image.open(image_path)
    image_array = np.asarray(image)

    # Normalize image
    normalized_image_array = image_array / 255.0
    
    # Convert back to PIL Image and save
    normalized_image = Image.fromarray((normalized_image_array * 255).astype(np.uint8))
    normalized_image.save(save_path)

def normalize_images_in_directory(directory):
    for subdir, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(subdir, file)
                normalize_image(image_path, image_path)  # Overwrite the original image

# Normalize images in the following directories:
directories = [
    r'C:\final_project_test\Data\class-of-data-originals',
    r'C:\final_project_test\Data\class-of-data-resizing\64x64',
    r'C:\final_project_test\Data\class-of-data-resizing\32x32',
    r'C:\final_project_test\Data\class-of-data-resizing-augm\64x64',
    r'C:\final_project_test\Data\class-of-data-resizing-augm\32x32',
    r'C:\final_project_test\Data\class-of-data-resizing-augm\299x299'  # Added based on the previous resizing requirement
]

for directory in directories:
    normalize_images_in_directory(directory)

print("All images have been normalized!")
