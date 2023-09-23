import xlsxwriter
import os
import math
import numpy as np
from PIL import Image
from numpy import array
import re


def data_mapping(path_to_walk, file_name):
    workbook = xlsxwriter.Workbook("{}.xlsx".format(file_name))
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "No.")
    worksheet.write(0, 1, "Image Path")
    worksheet.write(0, 2, "Classification") 
    """
        Classification: 
        0 - No bleeding
        1 - Epidural
        2 - Intraparenchymal
        3 - Intraventricular
        4 - Subarachnoid
        5 - Subdural
    """
    worksheet.write(0, 3, "Uses (train/test)")

    col = 0
    row = 0
    #classes = ["Epidural", "Intraparenchymal", "Intraventricular", "Subarachnoid", "Subdural"]

    for root, directories, files in os.walk(path_to_walk):
        for path in os.listdir(root):
            if "bone" not in path: 
                full_path = os.path.join(root, path)
                print(full_path)
        
        # for directory in directories:
        #     if directory != "bone":
        #         print(directory)
        # for file in files:
        #     print(file)
        
    
    # for dir in walk:
    #     print(dir)
        # for path in os.listdir(root):
        #     full_path = os.path.join(root, path)
        #     if os.path.isfile(full_path):
        #         print(full_path)
                
                # row += 1
                # worksheet.write(row, col, row)  # row No.
                # worksheet.write(row, col + 1, full_path)  # full path
                # worksheet.write(row, col + 2, full_path.split(os.path.sep)[len(full_path.split(os.path.sep)) - 2])  # malware family
                
                
                # if file_name != "mapped-original-data":

                #    print(r"{}. Vectorize images for {}".format(row, file_name))
                #    img_vector = vectorize_img(full_path)
                #    for i in range(len(img_vector)):
                #        worksheet.write(row, col + 4 + i, img_vector[i] / 255)

#     number_of_images_for_testing = math.ceil((row / 100) * 10)  # rounds up
#     number_of_images_for_learning = math.floor((row / 100) * 90)  # rounds down

#     image_count = row
#     row = 0
#     testing = 0
#     training = 0
#     for i in range(image_count):
#         row += 1
#         if row % 10 < 9:
#             worksheet.write(row, 3, "training")
#             training += 1
#         else:
#             worksheet.write(row, 3, "testing")
#             testing += 1
#     workbook.close()
#     print(f"testing: {testing} / {number_of_images_for_testing} images")
#     print(f"training: {training} / {number_of_images_for_learning} images")
#     print(f"Total images == {testing + training}")


# def vectorize_img(path):
#     img = Image.open(path)
#     img_vector = np.ravel(array(img))
#     return img_vector

path = os.path.join("Data", "class-of-data-originals")
data_mapping(path=path, 
             file_name="mapped-original-data")
