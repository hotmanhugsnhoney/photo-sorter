# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 17:41:14 2024

@author: willh
"""

# data_types = set(type(item) for item in date_list)
# print("Data types in the list:", data_types) 

# combine tuples together into integers
# date_list_int = []
# for date in date_objects:
#     combined_num = int(''.join(map(str, date)))
#     date_list_int.append(combined_num)
# print(date_list_int)

# date_list_str = str(date_list_int)
# print(date_list_str)
    
# convert integers to dates
# date_objects = [dt.datetime.strptime(str(date), "%Y%m%d").date() for date in date_list_int]
# print(date_objects)

# data_types = set(type(item) for item in date_list_str)
# print("Data types in the list:", data_types) 

# # gather files 
# dest_folders = os.listdir(destination)
# dest_folders_2 = np.array_split(dest_folders, 16)
# for folders in dest_folders_2:
#     final_destination = f'D:\pics\{folders}'
#     print(final_destination)
#     # print(folders)
# #     for the_folders in dest_folders:
# #         os.path.join(destination, the_folders)
# #         final_destination = f'D:\pics\{dest_folders}'
# allfiles = os.listdir(source)
# # print(the_folders)
# # iterate on all files to move them to destination folder
# for pics in allfiles:
#     src_path = os.path.join(source, pics)
#     dst_path = os.path.join(final_destination, pics)
#     shutil.move(src_path, dst_path)
