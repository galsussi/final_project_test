import os
import pandas as pd
import numpy as np
from PIL import Image

def data_mapping_gal():
    directories = [
        r'C:\final_project_test\Data\class-of-data-originals',
        r'C:\final_project_test\Data\class-of-data-resizing\64x64',
        r'C:\final_project_test\Data\class-of-data-resizing\32x32',
        r'C:\final_project_test\Data\class-of-data-resizing-augm\64x64',  # Added path for augmented data
        r'C:\final_project_test\Data\class-of-data-resizing-augm\32x32'   # Added path for augmented data
    ]

    image_paths = []
    patient_numbers = []
    slice_numbers = []
    bleedings = []
    datasets = []
    image_sizes = []

    for base_dir in directories:
        # Navigate through each directory.
        for bleeding_type in os.listdir(base_dir):
            type_dir = os.path.join(base_dir, bleeding_type)
            
            if os.path.isdir(type_dir) and bleeding_type in ['Epidural', 'Intraparenchymal', 'Intraventricular', 'subarachnoid', 'Subdural']:
                for patient in os.listdir(type_dir):
                    brain_dir = os.path.join(type_dir, patient, 'brain')
                    
                    if os.path.exists(brain_dir):
                        images = os.listdir(brain_dir)
                        
                        for image in images:
                            slice_num = image.split('.')[0].replace('_HGE_Seg', '')
                            
                            if "_HGE_Seg" in image:
                                bleeding_status = bleeding_type
                            else:
                                bleeding_status = 'No Bleeding'
                            
                            # Open the image and get its size
                            with Image.open(os.path.join(brain_dir, image)) as img:
                                width, height = img.size
                                img_size = f"{width}x{height}"

                            image_paths.append(os.path.join(brain_dir, image))
                            patient_numbers.append(patient)
                            slice_numbers.append(slice_num)
                            bleedings.append(bleeding_status)
                            image_sizes.append(img_size)

    # Randomly splitting data for training and testing
    num_samples = len(image_paths)
    train_indices = np.random.choice(num_samples, size=int(0.7 * num_samples), replace=False)
    test_indices = list(set(range(num_samples)) - set(train_indices))

    for i in range(num_samples):
        if i in train_indices:
            datasets.append("Training")
        else:
            datasets.append("Test")

    # Creating a DataFrame
    df = pd.DataFrame({
        'Image Path': image_paths,
        'Patient Number': patient_numbers,
        'Slice Number': slice_numbers,
        'Bleeding Type': bleedings,
        'Image Size': image_sizes,
        'Dataset': datasets
    })

    # Save to Excel
    excel_path = r'C:\final_project_test\Data\mapping.xlsx'
    df.to_excel(excel_path, index=False)

    print(f"Mapping saved to {excel_path}")

# Call the function
data_mapping()
