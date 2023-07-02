Project Description:
The provided code represents a project that manages and organizes information about shows and shots within those shows. It allows for the creation, retrieval, modification, and deletion of shows and shots by utilizing directories and JSON files to store the relevant data. The project provides functions to create new shows and shots, read information for a single show or shot, update the data for a show or shot, and delete shows or shots.

As an example I have create a main directory called "Animal Kingdom" and subdirectories(Shows) called "Dogs","Cats","Bunnys" and "Birds". Each show as a description.json file which gives you information on what the show is about. For this example I have only created shots (Character info about the characters in the show) for the Dogs Show, but you can use the same code to create shots for different shows by making changes to values the variables hold.

The code is broken down into 4 main sections:
1. Begin Shows: It contains all the functions to create directories, subdirectories, list all created subdirectories...etc
2. Begin Shots: It contain all the functions to create json files to store info about a shot (character), update, delete..etc
3. Begin Example Usage Shows: Here are the example usage code on how to run the functions created in the Begin Shows section.
4. Begin Example Usage Shots: Here are the example usage code on how to run the functions created in the Begin Shots section.


To Run Examples:
To run the examples, follow these steps: 
(Note: These example code block for your understanding)

1. Set up the project structure: 
   - Make sure you have a suitable directory on your system where you want to create the project. Update the `directory_path` variable in the code examples with the desired path.
   - Create the necessary subdirectories for shows and shots using the `create_subdirectories` function. Modify the `directory_name` and `subdirectories` variables to suit your needs.

2. Working with Shows:
   - Example 1: Creating new shows

      ## Example Code block
      ## BEGIN: ___________CREATE NEW SHOWS___________
      # directory_path = "D:/BCIT/Term 3/Data Structures/Assignment 1"
      # directory_name = "Animal_Kingdom"
      # subdirectories = ["Dogs", "Cats", "Birds", "Bunnys"]
      # create_subdirectories(directory_path, directory_name, subdirectories)

      ## END: ___________CREATE NEW SHOWS___________

     - Uncomment the code block under the comment "CREATE NEW SHOWS" and modify the `directory_path`, `directory_name`, and `subdirectories` variables to specify the desired directory and show names.
     - Run the code block to create the new shows.

   - Example 2: Reading a list of all created shows

      ## Example Code block
      ## BEGIN: ___________READ A LIST OF ALL CREATED SHOWS___________
      # subdirectories_list = get_subdirectories(os.path.join(directory_path, directory_name))
      # print(subdirectories_list)

      ## END: ___________READ A LIST OF ALL CREATED SHOWS___________

     - Uncomment the code block under the comment "READ A LIST OF ALL CREATED SHOWS."
     - Run the code block to retrieve a list of all the created shows.

   - Example 3: Creat/Read information for a single show

      ## Example Code block
      ## BEGIN: ___________CREATE/READ INFORMATION FOR A SINGLE SHOW___________
      # subdir_path = os.path.join(directory_path, directory_name, "Dogs")
      # description = {
      #     "Description": "This show is about a family of Dogs in the Animal Kingdom",
      # }
      # create_json_file(subdir_path, "description.json", description)

      # chosen_subdirectory = "Dogs"
      # description = get_description_file(os.path.join(directory_path, directory_name), chosen_subdirectory)
      # if description is not None:
      #     print(description)

      ## END: ___________CREATE/READ INFORMATION FOR A SINGLE SHOW___________

     - Uncomment the code block under the comment "CREATE/READ INFORMATION FOR A SINGLE SHOW."
     - Modify the `subdir_path` and `description` variable to specify the desired show and subdirectory.
     - Run the code block to create a description.json file.
     - Modify the `chosen_subdirectory` variable to specify the show description you want to read.
     - Run the code block to retrieve the description for the chosen show.

   - Example 4: Updating the data for a show

      ## Example Code block
      ## BEGIN: ___________UPDATE THE DATA FOR A SHOW___________
      # chosen_subdirectory = "Cats"
      # updated_description = {
      #     "Description": "This show is about a family of Dogs in the Animal Kingdom. It follows their adventures and daily lives.",
      # }
      # update_description_file(os.path.join(directory_path, directory_name), chosen_subdirectory, updated_description)

      ## END: ___________UPDATE THE DATA FOR A SHOW___________

     - Uncomment the code block under the comment "UPDATE THE DATA FOR A SHOW."
     - Modify the `chosen_subdirectory`and `updated_description` variable to include the desired changes to the description.
     - Run the code block to update the description for the chosen show.

   - Example 5: Deleting a show

      ## Example Code block
      ## BEGIN: ___________DELETE A SHOW___________
      # subdirectory_to_delete = "Cats"
      # delete_subdirectory(os.path.join(directory_path, directory_name), subdirectory_to_delete)

      ## END: ___________DELETE A SHOW___________

     - Uncomment the code block under the comment "DELETE A SHOW."
     - Modify the `subdirectory_to_delete` variable to specify the subdirectory you want to delete.
     - Run the code block to delete the chosen show.

3. Working with Shots:
   - Example 1: Creating new shots within a show

      ## Example Code block
      ## BEGIN: ___________CREATE NEW SHOTS WITHIN A SHOW___________
      # directory_path = "D:/BCIT/Term 3/Data Structures/Assignment 1/Animal_Kingdom/Dogs"
      # file_name = "character3"
      # character_name = "Coco"
      # info = {
      #     "Name": "Coco",
      #     "Age": 2,
      #     "Occupation": "Software Engineer",
      #     "Description": "A brilliant and accomplished software engineer.",
      #     "Abilities": ["Problem-solving", "Strong Debugging and Troubleshooting"],
      # }

      # create_character_info(directory_path, file_name, character_name, info)

      ## END: ___________CREATE NEW SHOTS WITHIN A SHOW___________

     - Uncomment the code block under the comment "CREATE NEW SHOTS WITHIN A SHOW."
     - Modify the `directory_path`, `file_name`, `character_name`, and `info` variables to specify the desired directory and shot information.
     - Run the code block to create a new shot.

   - Example 2: Reading a list of all created shots within a show

      ## Example Code block
      ## BEGIN: ___________READ A LIST OF ALL CREATED SHOTS___________
      # directory_path = "D:/BCIT/Term 3/Data Structures/Assignment 1/Animal_Kingdom/Dogs"
      # get_json_files(directory_path)

      ## END: ___________READ A LIST OF ALL CREATED SHOTS___________

     - Uncomment the code block under the comment "READ A LIST OF ALL CREATED SHOTS."
     - Modify the `directory_path` variable to specify the desired show and subdirectory.
     - Run the code block to retrieve a list of all the created shots within the chosen show.

   - Example 3: Reading information for a single shot

      ## Example Code block
      ## BEGIN: ___________READ INFORMATION FOR A SINGLE SHOT___________
      # directory_path = "D:/BCIT/Term 3/Data Structures/Assignment 1/Animal_Kingdom/Dogs"
      # file_name = "character1.json"
      # json_data = get_json_file_info(directory_path, file_name)
      # if json_data:
      #     print(json_data)

      ## END: ___________READ INFORMATION FOR A SINGLE SHOT___________

     - Uncomment the code block under the comment "READ INFORMATION FOR A SINGLE SHOT."
     - Modify the `directory_path` and `file_name` variables to specify the desired show, subdirectory, and shot file.
     - Run the code block to retrieve the information for the chosen shot.

   - Example 4: Updating the data for a shot

      ## Example Code block
      ## BEGIN: ___________UPDATE THE DATA FOR A SHOT___________
      # directory_path = "D:/BCIT/Term 3/Data Structures/Assignment 1/Animal_Kingdom/Dogs"
      # file_name = "character1.json"
      # new_data = {
      #     "Name": "Charlie",
      #     "Age": 7,
      #     "Occupation": "Private Investigator",
      #     "Description": "A seasoned detective with a knack for solving complex cases.",
      #     "Abilities": ["Sharp intuition", "Expert deduction", "Martial arts"],
      # }

      # edit_json_file(directory_path, file_name, new_data)

      ## END: ___________UPDATE THE DATA FOR A SHOT___________

     - Uncomment the code block under the comment "UPDATE THE DATA FOR A SHOT."
     - Modify the `directory_path`, `file_name`, and `new_data`(values), variables to specify the desired show, subdirectory

, shot file, and updated data.
     - Run the code block to update the data for the chosen shot.

   - Example 5: Deleting a shot

      ## Example Code block
      # BEGIN: ___________DELETE A SHOT___________
      # directory_path = "D:/BCIT/Term 3/Data Structures/Assignment 1/Animal_Kingdom/Dogs"
      # file_name = "character2.json"

      # delete_json_file(directory_path, file_name)

      ## END: ___________DELETE A SHOT___________

     - Uncomment the code block under the comment "DELETE A SHOT."
     - Modify the `directory_path` and `file_name` variables to specify the desired show, subdirectory, and shot file.
     - Run the code block to delete the chosen shot.

Remember to uncomment the desired code blocks(if commented) and modify the variables as instructed to perform the desired operations on shows and shots.