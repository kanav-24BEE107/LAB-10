print("Name : Kanav ShahPatel , Roll No.: 24BEE107")


import os
import shutil

# Define the path to the new subdirectory
new_subdirectory = "new_subdir"

# Create the new subdirectory
try:
    os.mkdir(new_subdirectory)
    print(f"Directory '{new_subdirectory}' created successfully.")
except FileExistsError:
    print(f"Directory '{new_subdirectory}' already exists.")

# Define the source file path
source_file_path = "source_dir/source_file.txt"

# Define the destination file path
destination_file_path = os.path.join(new_subdirectory, "source_file.txt")

# Copy the file
try:
    shutil.copy(source_file_path, destination_file_path)
    print(f"File copied successfully to '{destination_file_path}'.")
except FileNotFoundError:
    print(f"Source file '{source_file_path}' not found.")



