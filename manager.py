import inquirer
import json


class Manager:
    def __init__(self, file_name="saved_characters.json"):
        self.characters = []
        self.file_name = file_name
        self.load_characters()

    def save_character(self, character):
        self.characters.append(character)
        self.save_to_file()

    def save_to_file(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.characters, file, indent=4)
        print(f"Your progress has been saved.")

    def show_characters(self):
        if self.characters:
            print("Saved Characters:")
            for saved_character in self.characters:
                print(f"{saved_character}")
        else:
            print("There are no saved characters.")

    def load_characters(self):
        try:
            with open(self.file_name, 'r') as file:
                self.characters = json.load(file)
            print(f"Loaded characters from {self.file_name}.")
        except FileNotFoundError:
            print(f"No existing file found.")

    def delete_character(self):
        if not self.characters:
            print("No characters available to delete.")
            return

        questions = [
            inquirer.List(
                'character',
                message="Select a character to delete:",
                choices=self.characters + ["Return to Menu"]
            )
        ]

        answer = inquirer.prompt(questions)

        character_to_delete = answer['character']

        if character_to_delete == "Return to Menu":
            menu_nav = "Menu"

        if character_to_delete in self.characters:
            self.characters.remove(character_to_delete)
            self.save_to_file()
            print(f"Character deleted.")
        else:
            print(f"Character not found.")
