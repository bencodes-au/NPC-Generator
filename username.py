import json
from colored import Fore, Back, Style

color: str = f'{Style.res_dim}{Fore.blue}'


class Username:
    def hello():
        try:
            with open('username.json', 'r') as json_file:
                save = json.load(json_file)
                username = save.get('username')

                if not username:
                    raise ValueError("No username found.")

                print(f'{color}Welcome back {username} {Style.reset}')

        except (FileNotFoundError, ValueError):
            while True:
                username = input("Please enter your username: ").strip()

                if username.isalpha() and len(username) > 0:
                    break
                else:
                    print("Use letters only and enter at least one character.")

            save = {'username': username}

            with open('username.json', 'w') as json_file:
                json.dump(save, json_file)

            print(f'{color}Welcome {username} {Style.reset}')

    def change_username():
        try:
            with open('username.json', 'r') as json_file:
                save = json.load(json_file)
                current_username = save.get('username')

                while True:
                    new_username = input(
                        "Please enter your username: ").strip()

                    if new_username.isalpha() and len(new_username) > 0:
                        break
                    else:
                        print("Use letters only and enter at least one character.")

                save['username'] = new_username

                with open('username.json', 'w') as json_file:
                    json.dump(save, json_file)

                print(
                    f'{color}Your username has been changed to {new_username} {Style.reset}')

        except FileNotFoundError:
            print("No username has been set yet. Please set your username first.")
