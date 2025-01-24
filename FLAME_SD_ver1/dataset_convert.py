# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 10:06:05 2025

@author: hao9
"""

import os
from PIL import Image
from tqdm import tqdm

def convert_png_to_jpg(input_dir, output_dir):
    # Check if the output directory exists, create it if not
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List all PNG files in the input directory
    png_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.png')]

    # Use tqdm to display progress
    for file_name in tqdm(png_files, desc="Converting PNG to JPG"):
        input_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, os.path.splitext(file_name)[0] + '.jpg')

        try:
            # Open the PNG file and convert it to JPG
            with Image.open(input_path) as img:
                rgb_image = img.convert('RGB')
                rgb_image.save(output_path, 'JPEG')
        except Exception as e:
            print(f"Failed to convert {file_name}: {e}")

# input_directory = "./FLAME_D/FLAME_D/" 
# output_directory = "./FLAME_SD/FLAME_SD/" 

input_directory = "./FLAME_D/mask/" 
output_directory = "./FLAME_SD/mask/" 

convert_png_to_jpg(input_directory, output_directory)


