import inquirer


def generate_character():
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
            choices=["Strong", "Agile", "Hardy", "Smart", "Wise", "Charming"],
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

    print(f"{chosen_genre} {chosen_identity} {chosen_trait} {chosen_background}.")

    print("Returning to Menu")

# if answers["identity"] == "Male"
#     print name from


def delete_character():
    print("Deleting Character")


def view_character():
    print("View Characters")


def view_categories():
    print("Learning More")


def save_and_exit():
    print("Saving...")
