# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:53:43 2024

@author: willh
"""

import os
import shutil
import time

source_directory = 'D:\photo dump'
destination_directory = "D:\pics"

# Get list of files in the source directory
files = os.listdir(source_directory)

# Create a list of tuples containing (filename, modification_time)
files_with_modification_time = [(file, os.path.getmtime(os.path.join(source_directory, file))) for file in files]

# Sort the list of tuples based on modification time
files_with_modification_time.sort(key=lambda x: x[1])

# Extract sorted list of filenames
sorted_files = [file[0] for file in files_with_modification_time]

# Create destination folders based on dates
for file_name in sorted_files:
    # Get modification time of the file
    modification_time = os.path.getmtime(os.path.join(source_directory, file_name))
    
    # Convert modification time to a readable date format (adjust this according to your needs)
    file_date = time.strftime("%Y-%m-%d", time.localtime(modification_time))
    
    # Create destination folder if it doesn't exist
    destination_folder = os.path.join(destination_directory, file_date)
    os.makedirs(destination_folder, exist_ok=True)
    
    # Move the file to the corresponding destination folder
    try:
        source_path = os.path.join(source_directory, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(source_path, destination_path)
    except FileNotFoundError:
        print('Whoopsies no file here')