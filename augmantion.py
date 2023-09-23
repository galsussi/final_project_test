import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img, save_img

def augment_images(input_directory, output_directory, augmentation_types=5):
    # Ensure output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Initialize image data generator with augmentation parameters
    datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(root, file)
                img = load_img(image_path)
                x = img_to_array(img)
                x = x.reshape((1,) + x.shape)

                # Construct the filename for augmented image
                filename_without_extension, extension = os.path.splitext(file)
                
                save_dir = root.replace(input_directory, output_directory)
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)

                # .flow() generates batches of randomly transformed images
                i = 0
                for batch in datagen.flow(x, batch_size=1, save_to_dir=save_dir, save_prefix=f"{filename_without_extension}_aug", save_format='png'):
                    i += 1
                    if i >= augmentation_types:
                        break

# Example Usage
input_directory = r"C:\final_project_test\Data\class-of-data-resizing"
output_directory = r"C:\final_project_test\Data\class-of-data-resizing-augm"

augment_images(input_directory, output_directory)
