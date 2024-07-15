import os
import shutil

def clear_temp_directory(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)

temp_directory = "./temp"

if os.path.exists(temp_directory):
    clear_temp_directory(temp_directory)
    print(f"All files and folders within {temp_directory} have been deleted.")
else:
    print(f"The directory {temp_directory} does not exist.")
