import os
import shutil

def copy_static_to_public(static_dir, public_dir):
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    copy_directories(static_dir, public_dir)

def copy_directories(origin_directory, target_directory):
    if os.path.exists(origin_directory):
        directories = os.listdir(origin_directory)
    else:
        raise ValueError("Origin directory does not exist")
    if not os.path.exists(target_directory):
        os.mkdir(target_directory)
    for directory in directories:
        full_path = os.path.join(origin_directory, directory)
        expected_path = os.path.join(target_directory, directory)
        if os.path.isfile(full_path):
            shutil.copy(full_path, expected_path)
        else:
            copy_directories(full_path, expected_path)