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


# BEGIN: ___________DELETE A SHOT___________
def delete_json_file(directory_path: str, file_name: str) -> bool:
    file_path = os.path.join(directory_path, file_name)

    if os.path.exists(file_path) and file_name.endswith(".json"):
        os.remove(file_path)
        print(f"JSON file '{file_name}' has been successfully deleted!")
    else:
        print(f"JSON file '{file_name}' does not exist in the specified directory.")

# END: ___________DELETE A SHOT___________

# ==================================================================================== END SHOTS ====================================================================================



# ==================================================================================== BEGIN EXAMPLE USAGE SHOWS ====================================================================================

# BEGIN: ___________CREATE NEW SHOWS___________
directory_path = "D:/BCIT/Term 3/Data Structures/Assignment 1"
directory_name = "Animal_Kingdom"
subdirectories = ["Dogs", "Cats", "Birds", "Bunnys"]
create_subdirectories(directory_path, directory_name, subdirectories)

# END: ___________CREATE NEW SHOWS___________


# BEGIN: ___________READ A LIST OF ALL CREATED SHOWS___________
subdirectories_list = get_subdirectories(os.path.join(directory_path, directory_name))
print(subdirectories_list)

# END: ___________READ A LIST OF ALL CREATED SHOWS___________


# BEGIN: ___________CREATE/READ INFORMATION FOR A SINGLE SHOW___________
subdir_path = os.path.join(directory_path, directory_name, "Cats")
description = {
    "Description": "This show is about a family of Cats in the Animal Kingdom",
}
create_json_file(subdir_path, "description.json", description)

chosen_subdirectory = "Dogs"
description = get_description_file(os.path.join(directory_path, directory_name), chosen_subdirectory)
if description is not None:
    print(description)

# END: ___________CREATE/READ INFORMATION FOR A SINGLE SHOW___________

"""
# BEGIN: ___________UPDATE THE DATA FOR A SHOW___________
chosen_subdirectory = "Cats"
updated_description = {
    "Description": "This show is about a family of Cats in the Animal Kingdom. It follows their adventures and daily lives.",
}
update_description_file(os.path.join(directory_path, directory_name), chosen_subdirectory, updated_description)

# END: ___________UPDATE THE DATA FOR A SHOW___________


# BEGIN: ___________DELETE A SHOW___________
subdirectory_to_delete = "Cats"
delete_subdirectory(os.path.join(directory_path, directory_name), subdirectory_to_delete)

# END: ___________DELETE A SHOW___________
"""
# ==================================================================================== END EXAMPLE USAGE SHOWS ====================================================================================



# ==================================================================================== BEGIN EXAMPLE USAGE SHOTS ====================================================================================

# BEGIN: ___________CREATE NEW SHOTS WITHIN A SHOW___________
directory_path = "D:/BCIT/Term 3/Data Structures/Assignment 1/Animal_Kingdom/Dogs"
file_name = "character2"
character_name = "Bailey"
info = {
    "Name": "Bailey",
    "Age": 3,
    "Occupation": "Private Investigator",
    "Description": "A seasoned detective with a disturbing past.",
    "Abilities": ["Sharp Shooter", "Gun Expert", "Martial arts"],
}

create_character_info(directory_path, file_name, character_name, info)

# END: ___________CREATE NEW SHOTS WITHIN A SHOW___________


# BEGIN: ___________READ A LIST OF ALL CREATED SHOTS___________
directory_path = "D:/BCIT/Term 3/Data Structures/Assignment 1/Animal_Kingdom/Dogs"
get_json_files(directory_path)

# END: ___________READ A LIST OF ALL CREATED SHOTS___________


# BEGIN: ___________READ INFORMATION FOR A SINGLE SHOT___________
directory_path = "D:/BCIT/Term 3/Data Structures/Assignment 1/Animal_Kingdom/Dogs"
file_name = "character1.json"
json_data = get_json_file_info(directory_path, file_name)
if json_data:
    print(json_data)

# END: ___________READ INFORMATION FOR A SINGLE SHOT___________

"""
# BEGIN: ___________UPDATE THE DATA FOR A SHOT___________
directory_path = "D:/BCIT/Term 3/Data Structures/Assignment 1/Animal_Kingdom/Dogs"
file_name = "character1.json"
new_data = {
    "Name": "Charlie",
    "Age": 7,
    "Occupation": "Private Investigator",
    "Description": "A seasoned detective with a knack for solving complex cases.",
    "Abilities": ["Sharp intuition", "Expert deduction", "Martial Arts"],
}

edit_json_file(directory_path, file_name, new_data)

# END: ___________UPDATE THE DATA FOR A SHOT___________



# BEGIN: ___________DELETE A SHOT___________
directory_path = "D:/BCIT/Term 3/Data Structures/Assignment 1/Animal_Kingdom/Dogs"
file_name = "character4.json"

delete_json_file(directory_path, file_name)

# END: ___________DELETE A SHOT___________
# ==================================================================================== END EXAMPLE USAGE SHOTS ====================================================================================
"""