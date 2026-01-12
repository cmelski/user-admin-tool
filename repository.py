import json
import os

JSON_FILE = 'users.json'


class Repository:

    def __init__(self):
        pass

    def append_to_user_list(self, new_user, filename=JSON_FILE):
        # Initialize data structure in case the file does not exist or is empty
        data = {"users": []}
        # 1. Read the existing data
        # Check if the file exists and has content before trying to read it
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            try:
                with open(filename, 'r') as file:
                    data = json.load(file)
                    #print(data)
            except json.JSONDecodeError:
                # Handle cases where the file exists but is not valid JSON
                print(f"Warning: Existing file {filename} is not valid JSON. Starting with a new list.")

        # Ensure the 'users' key exists as a list
        if "users" not in data or not isinstance(data["users"], list):
            data["users"] = []

        # 2. Modify the data (append the new item)
        data["users"].append(new_user)
        #print(data)

        # 3. Write the updated data back to the file
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
            print(f"Successfully appended new user to {filename}")
