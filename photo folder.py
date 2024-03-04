# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 21:14:32 2024

@author: willh
"""

import os 
import datetime as dt
import shutil
import numpy as np

# start folders
# path = fr"D:\pics\{folder_name_str}"

source = 'D:\photo dump'

# Reading the date of the files

start_num = 5659
end_num = 6493
date_list_dup = []
date_list_tup = []

try:
    for img_no in range(start_num, end_num):
        if img_no not in [5662, 5666]:  # Check if img_no is not in the list of excluded numbers
            image_path = os.path.join(source, f'DSC_{img_no}.jpg')
            creation_time = None  # Initialize creation_time
            if os.path.isfile(image_path):
                creation_time_seconds = os.path.getmtime(image_path)
                creation_time = dt.datetime.fromtimestamp(creation_time_seconds)
                # Append the tuple containing date components to date_list_tup
                date_list_dup.append((creation_time.year, creation_time.month, creation_time.day))
                for dates in date_list_dup:
                    if dates not in date_list_tup:
                        date_list_tup.append(dates)
            else:
                print(f"DSC_{img_no}.jpg not found.")

except Exception as e:
    print("An error occurred:", e) 

# print(date_list) 
date_objects = [dt.datetime(*date_tuple) for date_tuple in date_list_tup]
# print(date_objects)

date_format = '%Y-%m-%d'
date_list_str = [dates_obj.strftime(date_format) for dates_obj in date_objects]
# print(date_list_str)

# Create directory based on folder_name
destination = "D:\pics"
for dates in date_list_str:
    path = os.path.join(destination, dates)
    os.makedirs(path, exist_ok=True)
# print(path)
    
dest_folders = os.listdir(destination)

# Iterate over all files in the source directory
for date in date_list_str:
    for file_name in os.listdir(source):
        file_path = os.path.join(source, file_name)
    
        final_destination = os.path.join(destination, str(date_list_str))
            
        # Gather all files from the source directory
        all_files = os.listdir(source)
        
            # Move each file to the current destination folder
        try:
            for file_names in all_files:
                src_path = os.path.join(source, file_names)
                dst_path = os.path.join(final_destination, file_names)
                shutil.move(file_path, os.path.join(final_destination, file_names))
        except FileNotFoundError:
            print('Whoopsies no file here')

# Create destination folders based on dates
for date in date_list_str:
    path = os.path.join(destination, date)
    os.makedirs(path, exist_ok=True)

# Gather all destination folders
dest_folders = os.listdir(destination)

# Iterate over files in the source directory
for file_name in os.listdir(source):
    file_path = os.path.join(source, file_name)
    
    # Determine the date of the file
    # Here you need to implement logic to extract the date from the file_name
    # For example, you might use regular expressions or some other method
    
    # Assuming you have extracted the date from the file_name
    file_date = "date1"  # Placeholder for the extracted date
    
    # Construct the final destination folder path based on the file's date
    final_destination = os.path.join(destination, file_date)
    
    # Move the file to the final destination folder
    try:
        shutil.move(file_path, os.path.join(final_destination, file_name))
    except FileNotFoundError:
        print('Whoopsies no file here')