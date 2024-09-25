import inquirer


class Saved_Characters:
    def __init__(self):
        self.characters = []

    def save_character(self, character):
        self.characters.append(character)

    def show_characters(self):
        if self.characters:
            print("Saved Characters:")
            for saved_character in self.characters:
                print(f"{saved_character}")
        else:
            print("There are no saved characters.")
