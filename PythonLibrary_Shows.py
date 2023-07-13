import os
import json
import shutil
from typing import List, Dict

# ==================================================================================== BEGIN SHOWS ====================================================================================

class ShowManager:
    def __init__(self, directory_path: str, directory_name: str):
        self.directory_path = directory_path
        self.directory_name = directory_name

    def create_directory(self, directory_path: str, directory_name: str) -> bool:
        directory = os.path.join(directory_path, directory_name)
        if os.path.exists(directory):
            print(f"Directory '{directory}' already exists.")
        else:
            os.makedirs(directory)
            print(f"Directory '{directory}' created successfully!")

    def create_subdirectories(self, subdirectories: List[str]) -> bool:
        main_directory_path = os.path.join(self.directory_path, self.directory_name)
        self.create_directory(self.directory_path, self.directory_name)

        for subdirectory in subdirectories:
            subdirectory_path = os.path.join(main_directory_path, subdirectory)
            self.create_directory(main_directory_path, subdirectory)

    def get_subdirectories(self) -> List[str]:
        subdirectories = []
        for entry in os.scandir(os.path.join(self.directory_path, self.directory_name)):
            if entry.is_dir():
                subdirectories.append(entry.name)
        return subdirectories

    def create_json_file(self, subdir_name: str, filename: str, data: Dict) -> bool:
        subdir_path = os.path.join(self.directory_path, self.directory_name, subdir_name)
        file_path = os.path.join(subdir_path, filename)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"JSON file '{filename}' created successfully!")

    def get_description_file(self, subdir_name: str) -> Dict:
        subdir_path = os.path.join(self.directory_path, self.directory_name, subdir_name)
        description_file = os.path.join(subdir_path, "description.json")

        if os.path.exists(description_file):
            with open(description_file, 'r') as file:
                description = json.load(file)
            return description
        else:
            print(f"Description file does not exist in '{subdir_name}' subdirectory.")
            return None

    def update_description_file(self, subdir_name: str, description: Dict) -> bool:
        subdir_path = os.path.join(self.directory_path, self.directory_name, subdir_name)
        description_file = os.path.join(subdir_path, "description.json")

        if os.path.exists(description_file):
            with open(description_file, 'w') as file:
                json.dump(description, file, indent=4)
            print(f"Description file in '{subdir_name}' subdirectory updated successfully!")
        else:
            print(f"Description file does not exist in '{subdir_name}' subdirectory.")

    def delete_subdirectory(self, subdirectory_name: str) -> bool:
        subdirectory_path = os.path.join(self.directory_path, self.directory_name, subdirectory_name)

        if os.path.exists(subdirectory_path):
            shutil.rmtree(subdirectory_path)
            print(f"Subdirectory '{subdirectory_name}' and its contents have been deleted successfully!")
        else:
            print(f"Subdirectory '{subdirectory_name}' does not exist.")

# ==================================================================================== END SHOWS ====================================================================================


# ==================================================================================== BEGIN SHOTS ====================================================================================

class ShotManager:
    def __init__(self, directory_path: str, subdirectory_name: str):
        self.directory_path = directory_path
        self.subdirectory_name = subdirectory_name

    def create_character_info(self, file_name: str, character_name: str, info: Dict) -> bool:
        os.makedirs(self.directory_path, exist_ok=True)
        character_file = os.path.join(self.directory_path, f"{file_name}.json")

        if os.path.exists(character_file):
            print(f"Character file '{character_file}' already exists.")
        else:
            with open(character_file, 'w') as file:
                json.dump(info, file, indent=4)
            print(f"Character file '{character_file}' created successfully!")

    def get_json_files(self) -> bool:
        json_files = []
        for file_name in os.listdir(self.directory_path):
            file_path = os.path.join(self.directory_path, file_name)
            if file_name.endswith(".json") and file_name != "description.json":
                json_files.append(file_name)

        if len(json_files) > 0:
            print("The Shots in this subdirectory are:")
            for file_name in json_files:
                print(file_name)
        else:
            print("No Shots found in this subdirectory.")

    def get_json_file_info(self, file_name: str) -> Dict:
        file_path = os.path.join(self.directory_path, file_name)

        if os.path.exists(file_path) and file_name.endswith(".json"):
            with open(file_path, 'r') as file:
                json_data = json.load(file)
            return json_data
        else:
            print(f"JSON file '{file_name}' does not exist in the specified directory.")
            return None

    def edit_json_file(self, file_name: str, new_data: Dict) -> bool:
        file_path = os.path.join(self.directory_path, file_name)

        if os.path.exists(file_path) and file_name.endswith(".json"):
            with open(file_path, 'w') as file:
                json.dump(new_data, file, indent=4)
            print(f"JSON file '{file_name}' has been successfully updated!")
        else:
            print(f"JSON file '{file_name}' does not exist in the specified directory.")

    def delete_json_file(self, file_name: str) -> bool:
        file_path = os.path.join(self.directory_path, file_name)

        if os.path.exists(file_path) and file_name.endswith(".json"):
            os.remove(file_path)
            print(f"JSON file '{file_name}' has been successfully deleted!")
        else:
            print(f"JSON file '{file_name}' does not exist in the specified directory.")


# ==================================================================================== END SHOTS ====================================================================================



# ==================================================================================== BEGIN EXAMPLE USAGE SHOWS ====================================================================================

# Example usage
show_manager = ShowManager("D:/BCIT/Term 3/Data Structures/Assignment 1_Classes", "Animal_Kingdom")
show_manager.create_subdirectories(["Dogs", "Cats", "Birds", "Bunnys"])

subdirectories_list = show_manager.get_subdirectories()
print(subdirectories_list)

subdir_name = "Dogs"
description = {
    "Description": "This show is about a family of Dogs in the Animal Kingdom",
}
show_manager.create_json_file(subdir_name, "description.json", description)

description = show_manager.get_description_file(subdir_name)
if description is not None:
    print(description)

# show_manager.update_description_file("Cats", {"Description": "This show is a Comedy series about Cats in the Animal Kingdom"})
# show_manager.delete_subdirectory("Dogs")

# ==================================================================================== END EXAMPLE USAGE SHOWS ====================================================================================

# ==================================================================================== BEGIN EXAMPLE USAGE Shots ====================================================================================

shot_manager = ShotManager("D:/BCIT/Term 3/Data Structures/Assignment 1_Classes/Animal_Kingdom/Dogs", "character1")
shot_manager.create_character_info("character2", "Charlie", {"name": "Charlie", "age": 3, "breed": "Labrador"})
shot_manager.get_json_files()
print(shot_manager.get_json_file_info("character1.json")) 
# shot_manager.edit_json_file("character1.json", {"name": "Charlie", "age": 4, "breed": "Golden Retriever"})
# shot_manager.delete_json_file("character2.json")

# ==================================================================================== END EXAMPLE USAGE SHOTS ====================================================================================
