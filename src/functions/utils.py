import shutil
import os
import random
import string

def copy_and_delete_folder(src, dst):
    # Copy all files and directories from src to dst
    shutil.copytree(src, dst, dirs_exist_ok=True)
    
    # Delete the source directory
    shutil.rmtree(src)

def copy_and_delete_file(source, destination):
    try:
        # Copy the file to the destination
        shutil.copy2(source, destination)
        print(f"File copied to {destination}")
        
        # Delete the file from the source
        os.remove(source)
        print(f"File deleted from {source}")
    
    except FileNotFoundError:
        print(f"The file at {source} does not exist.")
    except PermissionError:
        print(f"Permission denied. Cannot access {source} or {destination}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def generate_random_string(length=16):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string


def update_state(state, key, value):
    state[key] = value 
    return state
