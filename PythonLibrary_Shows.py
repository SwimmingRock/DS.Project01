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


# BEGIN: ___________CREATE/READ INFORMATION FOR A SINGLE SHOW___________
def create_json_file(directory_path: str, filename: str, data: Dict) -> List[str]:
    file_path = os.path.join(directory_path, filename)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"JSON file '{filename}' created successfully!")

def get_subdirectories(directory_path: str) -> List[str]:
    subdirectories = []

    for entry in os.scandir(directory_path):
        if entry.is_dir():
            subdirectories.append(entry.name)

    return subdirectories

def get_description_file(directory_path: str, subdir_name: str) -> Dict:
    subdir_path = os.path.join(directory_path, subdir_name)
    description_file = os.path.join(subdir_path, "description.json")

    if os.path.exists(description_file):
        with open(description_file, 'r') as file:
            description = json.load(file)
        return description
    else:
        print(f"Description file does not exist in '{subdir_name}' subdirectory.")
        return None

# END: ___________CREATE/READ INFORMATION FOR A SINGLE SHOW___________


# BEGIN: ___________UPDATE THE DATA FOR A SHOW___________
def update_description_file(directory_path: str, subdir_name: str, description: Dict) -> bool:
    subdir_path = os.path.join(directory_path, subdir_name)
    description_file = os.path.join(subdir_path, "description.json")

    if os.path.exists(description_file):
        with open(description_file, 'w') as file:
            json.dump(description, file, indent=4)
        print(f"Description file in '{subdir_name}' subdirectory updated successfully!")
    else:
        print(f"Description file does not exist in '{subdir_name}' subdirectory.")

# END: ___________UPDATE THE DATA FOR A SHOW___________