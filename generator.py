import inquirer
import random
from manager import Manager

male_name = ["Alex", "Ben", "Chris", "Daniel", "Elijah", "Fred", "Gabriel", "Henry", "Isaac", "John", "Kyle",
             "Lucas", "Matthew", "Nathan", "Oliver", "Patrick", "Quentin", "Ryan", "Sam", "Thomas", "Umar",
             "Victor", "William", "Xavier", "Yuri", "Zach"]

female_name = ["Abigail", "Bianca", "Charlotte", "Diana", "Emily", "Fiona", "Grace", "Hannah", "Isabella", "Julia",
               "Katherine", "Lily", "Mia", "Nora", "Olivia", "Penelope", "Quinn", "Rebecca", "Sophia", "Tessa",
               "Uma", "Victoria", "Wendy", "Xia", "Yvonne", "Zoe"]

neutral_name = ["Avery", "Blake", "Cameron", "Dakota", "Ellis", "Finley", "Gray", "Hayden", "Indigo", "Jordan",
                "Kai", "Logan", "Morgan", "Noel", "Oakley", "Phoenix", "Quinn", "Riley", "Skyler", "Taylor",
                "Ulan", "Val", "Wyatt", "Xiao", "Yi", "Zayne"]

warrior_background = ["Valiant", "Fearless",
                      "Conqueror", "Defiant", "Protector", "Mercenary"]

expert_background = ["Mastermind", "Virtuoso",
                     "the Scholar", "Adept", "Prodigy", "Oracle"]

criminal_background = ["Outlaw", "Bandit",
                       "Trickster", "Sinner", "Scoundrel", "Shadow"]

merchant_background = ["Broker", "Dealer",
                       "Purveyor", "Prince", "Vendor", "Bargain Master"]

wanderer_background = ["Recluse", "Nomad",
                       "Explorer", "Drifter", "Wayfarer", "Adventerous"]


believer_background = ["Faithful", "Devoted",
                       "Seeker", "Zealot", "Prophet", "Enlightened"]


class Generator:
    def __init__(self, manager):
        self.manager = manager

    def generate_character(self):
        print("Lets Get Started!")

        questions = [
            inquirer.List(
                "genre",
                message="What genre is the world?",
                choices=["Fantasy", "Sci-fi", "Crime",
                         "Horror", "Heroes", "Western"],
            ),

            inquirer.List(
                "identity",
                message="How does this character identify?",
                choices=["Male", "Female", "Neutral"],
            ),

            inquirer.List(
                "trait",
                message="What is this character's main trait?",
                choices=["Strong", "Nimble", "Hardy",
                         "Smart", "Wise", "Charming"],
            ),


            inquirer.List(
                "background",
                message="What is this character's background?",
                choices=["Warrior", "Expert", "Criminal",
                         "Merchant", "Hermit", "Believer"],
            ),
        ]

        answers = inquirer.prompt(questions)

        if answers["genre"] == "Fantasy":
            chosen_genre = "From a life of swords and sorcery,"
        elif answers["genre"] == "Sci-fi":
            chosen_genre = "From a life among the stars,"
        elif answers["genre"] == "Crime":
            chosen_genre = "From a life of hunting crooks,"
        elif answers["genre"] == "Horror":
            chosen_genre = "From a life that was about to take a horrific turn,"
        elif answers["genre"] == "Heroes":
            chosen_genre = "From a life as a caped crusader,"
        elif answers["genre"] == "Western":
            chosen_genre = "From a life of darn tootin' gunslinging,"
        else:
            print("An error has occurred within Genre.")

        if answers["identity"] == "Male":
            chosen_identity = "he is a"
        elif answers["identity"] == "Female":
            chosen_identity = "she is a"
        elif answers["identity"] == "Neutral":
            chosen_identity = "they are a"
        else:
            print("An error has occurred within Identity.")

        chosen_trait = answers["trait"]
        chosen_background = answers["background"]

        if answers["identity"] == "Male":
            name = male_name
        elif answers["identity"] == "Female":
            name = female_name
        elif answers["identity"] == "Neutral":
            name = neutral_name
        else:
            print("Error in Name.")
            return

        random_name = random.choice(name)

        if answers["background"] == "Warrior":
            title = warrior_background
        elif answers["background"] == "Expert":
            title = expert_background
        elif answers["background"] == "Criminal":
            title = criminal_background
        elif answers["background"] == "Merchant":
            title = criminal_background
        elif answers["background"] == "Wanderer":
            title = criminal_background
        elif answers["background"] == "Believer":
            title = criminal_background
        else:
            print("Error in Title.")
            return

        random_title = random.choice(title)

        character = (
            f"{chosen_genre} {chosen_identity} {chosen_trait} {chosen_background} called {random_name} the {random_title}.")

        print(character)

        saving = [
            inquirer.List(
                "save",
                message="Would you like to save this character?",
                choices=["Save", "Don't Save"],
            ),
        ]

        answer = inquirer.prompt(saving)

        if answer["save"] == "Save":
            self.manager.save_character(character)
            print("Character saved!")
        else:
            print("Character not saved.")


def view_categories():
    print("Learning More")
