
# Show and Shot Manager Examples

The project consists of two classes: `ShowManager` and `ShotManager`. These classes provide functionality for managing shows and shots within a directory structure.

## ShowManager

The `ShowManager` class is responsible for creating and managing show directories. It provides methods to:

- Create the main directory.
- Create subdirectories within the main directory.
- Create JSON files within subdirectories.
- Retrieve the description file of a subdirectory.
- Update the description file.
- Delete subdirectories.

### Example Usage

```python
import os
import json
import shutil
from typing import List, Dict

# ShowManager class implementation...

# Example usage
show_manager = ShowManager("C:/MyShows", "Animal_Kingdom")
show_manager.create_subdirectories(["Dogs", "Cats", "Birds", "Bunnys"])

subdirectories_list = show_manager.get_subdirectories()
print(subdirectories_list)

subdir_name = "Cats"
description = {
    "Description": "This show is about a family of Cats in the Animal Kingdom",
}
show_manager.create_json_file(subdir_name, "description.json", description)

description = show_manager.get_description_file(subdir_name)
if description is not None:
    print(description)

show_manager.update_description_file("Cats", {"Description": "This show is a Comedy series about Cats in the Animal Kingdom"})
show_manager.delete_subdirectory("Cats")
```

In this example:

1. A `ShowManager` object is created with the main directory path set to `"C:/MyShows"` and the main directory name set to `"Animal_Kingdom"`.
2. The `create_subdirectories` method is called to create the subdirectories: `"Dogs"`, `"Cats"`, `"Birds"`, and `"Bunnys"`.
3. The `get_subdirectories` method is called to retrieve a list of subdirectories.
4. The `create_json_file` method is used to create a description file for the `"Cats"` subdirectory.
5. The `get_description_file` method is called to retrieve the description from the created file.
6. The `update_description_file` method is used to update the description of the `"Cats"` subdirectory.
7. The `delete_subdirectory` method is called to delete the `"Cats"` subdirectory.

## ShotManager

The `ShotManager` class is responsible for managing shot files within a subdirectory. It provides methods to:

- Create character information files.
- Retrieve the list of shot files within a subdirectory.
- Retrieve information from a shot file.
- Update a shot file.
- Delete a shot file.

### Example Usage

```python
import os
import json
from typing import Dict

# ShotManager class implementation...

# Example usage
shot_manager = ShotManager("C:/MyShows/Animal_Kingdom/Dogs", "character1")

shot_manager.create_character_info("character2", "Charlie", {"name": "Charlie", "age": 3, "breed": "Labrador"})
shot_manager.get_json_files()
print(shot_manager.get_json_file_info("character1.json")) 

shot_manager.edit_json_file("character1.json", {"name": "Charlie", "age": 4, "breed": "Golden Retriever"})
shot_manager.delete_json_file("character1.json")
```

In this example:

1. A `ShotManager` object is created with the directory path set to `"C:/MyShows/Animal_Kingdom/Dogs"` and the subdirectory name set to `"character1"`.
2. The `create_character_info` method is called to create a character information file for `"character2"`.
3. The `get_json_files` method is used to retrieve the list of shot files within the subdirectory.
4. The `get_json_file_info` method is called to retrieve information from a specific shot file.
5. The `edit_json_file` method is used to update the information in a shot file.
6. The `delete_json_file` method is called to delete a specific shot file.

---

By following the instructions and modifying the code snippets accordingly, you can create different directory structures, update show descriptions, delete subdirectories, create character information files with different details, and delete specific shot files, resulting in different outcomes based on your modifications.