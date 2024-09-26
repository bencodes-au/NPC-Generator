import inquirer


class Categories:
    def __init__(self):
        self.how_to_blurb = """This program is designed to generate characters for a story-world to spark inspiration. Select a series of options which will guide the generator into providing a dramatic prompt of a character outline.
To get started, follow the Generate a Character option in the Menu. If you choose to save them, your characters will be stored here for whenever you need them.
Have Fun :)
        """
        self.genre_blurb = "Genres include Fantasy, Sci-fi, etc."
        self.identity_blurb = "Identities are Male, Female, or Neutral."
        self.trait_blurb = "Traits define your character's abilities."
        self.background_blurb = "Backgrounds give context to your character."
        self.name_blurb = "Names are randomly generated based on identity."
        self.title_blurb = "Titles are added based on the background."

    def learn_more(self):
        categories = [
            inquirer.List(
                "category",
                message="What would you like to know?",
                choices=["How-To", "Genre", "Identity", "Trait",
                         "Background", "Name", "Title", "Return to Menu"],
            ),
        ]

        answers = inquirer.prompt(categories)

        if answers["category"] == "How-To":
            print(self.how_to_blurb)
        elif answers["category"] == "Genre":
            print(self.genre_blurb)
        elif answers["category"] == "Identity":
            print(self.identity_blurb)
        elif answers["category"] == "Trait":
            print(self.trait_blurb)
        elif answers["category"] == "Background":
            print(self.background_blurb)
        elif answers["category"] == "Name":
            print(self.name_blurb)
        elif answers["category"] == "Title":
            print(self.title_blurb)
        elif answers["category"] == "Return to Menu":
            print("Returning to the main menu...")
        else:
            print("Error in Categories")


# To test this in a main program:
categories_instance = Categories()
categories_instance.learn_more()
