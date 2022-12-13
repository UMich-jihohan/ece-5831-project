# ! REFERENCE: https://medium.com/mlearning-ai/training-yolov5-custom-dataset-with-ease-e4f6272148ad

import os
import shutil
import random

from tqdm import tqdm

# clear screen before running the program
os.system('cls' if os.name == 'nt' else 'clear')

full_data_path = 'data/Howl/obj_train_data/'
image_type = '.png'
train_test_ratio = 95

# create necesarry directories
images_path = 'data/images/'
if os.path.exists(images_path):
    shutil.rmtree(images_path)
os.mkdir(images_path)
    
labels_path = 'data/labels/'
if os.path.exists(labels_path):
    shutil.rmtree(labels_path)
os.mkdir(labels_path)
    
train_images_path = images_path + 'training/'
test_images_path = images_path + 'test/'
train_labels_path = labels_path + 'training/'
test_labels_path = labels_path +'test/'
    
os.mkdir(train_images_path)
os.mkdir(test_images_path)
os.mkdir(train_labels_path)
os.mkdir(test_labels_path)


files = []

ext_len = len(image_type)

for r, d, f in os.walk(full_data_path):
    for file in f:
        if file.endswith(image_type):
            strip = file[0:len(file) - ext_len]      
            files.append(strip)

# shuffle the orders of the files, and split them based on the percentage provided.
random.shuffle(files)
split = int(train_test_ratio * len(files) / 100)

print("Copying data for train...")
for i in tqdm(range(split)):
    strip = files[i]
    
    image_file = strip + image_type
    src_image = full_data_path + image_file
    shutil.copy(src_image, train_images_path) 
    
    annotation_file = strip + '.txt'
    src_label = full_data_path + annotation_file
    shutil.copy(src_label, train_labels_path) 

print("Copying data for test...")
for i in tqdm(range(split, len(files))):
    strip = files[i]
    
    image_file = strip + image_type
    src_image = full_data_path + image_file
    shutil.copy(src_image, test_images_path) 
    
    annotation_file = strip + '.txt'
    src_label = full_data_path + annotation_file
    shutil.copy(src_label, test_labels_path) 

print("All dataset is split and prepared for training process. Please run train.py with arguments.")