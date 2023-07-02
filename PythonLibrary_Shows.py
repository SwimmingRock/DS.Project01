import os
import json
import shutil
from typing import List, Dict
# ==================================================================================== BEGIN SHOWS ====================================================================================

# BEGIN: ___________CREATE NEW SHOWS/READ A LIST OF ALL CREATED SHOWS___________
def create_directory(directory_path: str, directory_name: str) -> bool:
    # Combine the directory path and name
    directory = os.path.join(directory_path, directory_name)

    # Check if the directory already exists
    if os.path.exists(directory):
        print(f"Directory '{directory}' already exists.")
    else:
        # Create the directory
        os.makedirs(directory)
        print(f"Directory '{directory}' created successfully!")

def create_subdirectories(directory_path: str, directory_name: str, subdirectories: List[str]) -> bool:
    # Create the main directory
    main_directory_path = os.path.join(directory_path, directory_name)
    create_directory(directory_path, directory_name)

# READ A LIST OF ALL CREATED SHOWS
    # Create subdirectories within the main directory
    for subdirectory in subdirectories:
        subdirectory_path = os.path.join(main_directory_path, subdirectory)
        create_directory(main_directory_path, subdirectory)

# END: ___________CREATE NEW SHOWS/READ A LIST OF ALL CREATED SHOWS___________
