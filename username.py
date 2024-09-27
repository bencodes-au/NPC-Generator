import json
from colored import Fore, Back, Style

color: str = f'{Style.res_dim}{Fore.blue}'


class Username:
    def hello():
        try:
            # Attempt to read the name from the JSON file
            with open('username.json', 'r') as json_file:
                save = json.load(json_file)
                username = save.get('username')

                # Check if name is None or empty
                if not username:
                    raise ValueError("No username found.")

                print(f'{color}Welcome back {username} {Style.reset}')

        except (FileNotFoundError, ValueError):
            # If the file does not exist or name is missing, prompt for the user's name
            while True:
                username = input("Please enter your username: ").strip()

                # Validate the name
                if username.isalpha() and len(username) > 0:
                    break
                else:
                    print("Use letters only and enter at least one character.")

            # Create a dictionary to hold the name
            save = {'username': username}

            # Save the name to a JSON file
            with open('username.json', 'w') as json_file:
                json.dump(save, json_file)

            print(f'{color}Welcome {username} {Style.reset}')

    def change_username():
        try:
            # Attempt to read the name from the JSON file
            with open('username.json', 'r') as json_file:
                save = json.load(json_file)
                current_username = save.get('username')

                # Prompt for a new name
                while True:
                    new_username = input(
                        "Please enter your username: ").strip()

                    # Validate the new name
                    if new_username.isalpha() and len(new_username) > 0:
                        break
                    else:
                        print("Use letters only and enter at least one character.")

                # Update the name in the dictionary
                save['username'] = new_username

                # Save the updated name to the JSON file
                with open('username.json', 'w') as json_file:
                    json.dump(save, json_file)

                print(
                    f'{color}Your username has been changed to {new_username} {Style.reset}')

        except FileNotFoundError:
            print("No username has been set yet. Please set your username first.")
