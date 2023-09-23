import os
from PIL import Image

def resize_images():
    base_dir = r'C:\final_project_test\Data\class-of-data-originals'
    target_dir = r'C:\final_project_test\Data\class-of-data-resizing'

    sizes = {
        '64x64': (64, 64),
        '32x32': (32, 32),
        '299x299': (299, 299)  # New size added here
    }

    # Create target directories
    os.makedirs(target_dir, exist_ok=True)

    for size_name, size in sizes.items():
        os.makedirs(os.path.join(target_dir, size_name), exist_ok=True)

        for bleeding_type in os.listdir(base_dir):
            type_dir = os.path.join(base_dir, bleeding_type)
            type_target_dir = os.path.join(target_dir, size_name, bleeding_type)

            if os.path.isdir(type_dir):
                os.makedirs(type_target_dir, exist_ok=True)
                
                for patient in os.listdir(type_dir):
                    patient_source_dir = os.path.join(type_dir, patient)
                    patient_target_dir = os.path.join(type_target_dir, patient)
                    os.makedirs(patient_target_dir, exist_ok=True)

                    for category in ['brain', 'bone']:
                        category_source_dir = os.path.join(patient_source_dir, category)
                        category_target_dir = os.path.join(patient_target_dir, category)
                        os.makedirs(category_target_dir, exist_ok=True)

                        if os.path.exists(category_source_dir):
                            for image_name in os.listdir(category_source_dir):
                                if image_name.endswith(('.png', '.jpg', '.jpeg')):
                                    image_path = os.path.join(category_source_dir, image_name)
                                    target_image_path = os.path.join(category_target_dir, image_name)

                                    # Open the image and resize it
                                    with Image.open(image_path) as img:
                                        img_resized = img.resize(size)
                                        img_resized.save(target_image_path)

    print("Images resized and saved!")

# Call the function
resize_images()
