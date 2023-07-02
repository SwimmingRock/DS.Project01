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


# BEGIN: ___________DELETE A SHOW___________
def delete_subdirectory(directory_path: str, subdirectory_name: str) -> bool:
    subdirectory_path = os.path.join(directory_path, subdirectory_name)

    if os.path.exists(subdirectory_path):
        shutil.rmtree(subdirectory_path)
        print(f"Subdirectory '{subdirectory_name}' and its contents have been deleted successfully!")
    else:
        print(f"Subdirectory '{subdirectory_name}' does not exist.")

# END: ___________DELETE A SHOW___________

# ==================================================================================== END SHOWS ====================================================================================



# ==================================================================================== BEGIN SHOTS ====================================================================================

# BEGIN: ___________CREATE NEW SHOTS WITHIN A SHOW___________
def create_character_info(directory_path: str, file_name: str, character_name: str, info: Dict) -> bool:
    # Create the directory if it doesn't exist
    os.makedirs(directory_path, exist_ok=True)

    # Create the character's JSON file
    character_file = os.path.join(directory_path, f"{file_name}.json")

    # Check if the file already exists
    if os.path.exists(character_file):
        print(f"Character file '{character_file}' already exists.")
    else:
        # Create the JSON file and write the information
        with open(character_file, 'w') as file:
            json.dump(info, file, indent=4)
        print(f"Character file '{character_file}' created successfully!")

# END: ___________CREATE NEW SHOTS WITHIN A SHOW___________


# BEGIN: ___________READ A LIST OF ALL CREATED SHOTS___________
def get_json_files(directory_path: str) -> str:
    json_files = []

    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if file_name.endswith(".json") and file_name != "description.json":
            json_files.append(file_name)

    if len(json_files) > 0:
        print("The Shots in this subdirectory are:")
        for file_name in json_files:
            print(file_name)
    else:
        print("No Shots found in this subdirectory.")

# END: ___________READ A LIST OF ALL CREATED SHOTS___________


# BEGIN: ___________READ INFORMATION FOR A SINGLE SHOT___________
def get_json_file_info(directory_path: str, file_name: str) -> Dict:
    file_path = os.path.join(directory_path, file_name)

    if os.path.exists(file_path) and file_name.endswith(".json"):
        with open(file_path, 'r') as file:
            json_data = json.load(file)
        return json_data
    else:
        print(f"JSON file '{file_name}' does not exist in the specified directory.")
        return None
    
# END: ___________READ INFORMATION FOR A SINGLE SHOT___________


# BEGIN: ___________UPDATE THE DATA FOR A SHOT___________
def edit_json_file(directory_path: str, file_name: str, new_data: Dict) -> bool:
    file_path = os.path.join(directory_path, file_name)

    if os.path.exists(file_path) and file_name.endswith(".json"):
        with open(file_path, 'w') as file:
            json.dump(new_data, file, indent=4)
        print(f"JSON file '{file_name}' has been successfully updated!")
    else:
        print(f"JSON file '{file_name}' does not exist in the specified directory.")

# END: ___________UPDATE THE DATA FOR A SHOT___________