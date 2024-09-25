from characters_functions import generate_character, delete_character, view_character, view_categories, save_and_exit
from Saved_Characters_class import Saved_Characters
import inquirer
import typer

print("Welcome to your NPC Generator")

choice = ""

while choice != "Save and Exit":

    menu = [
        inquirer.List(
            "choice",
            message="What would you like to do?",
            choices=["Generate a Character", "Delete a Character",
                     "View Saved Characters", "Learn More About Generation", "Save and Exit"],
        ),

    ]

    answers = inquirer.prompt(menu)

    if answers["choice"] == "Generate a Character":
        generate_character()
    elif answers["choice"] == "Delete a Character":
        delete_character()
    elif answers["choice"] == "View Saved Characters":
        view_character()
    elif answers["choice"] == "Learn More About Generation":
        view_categories()
    elif answers["choice"] == "Save and Exit":
        save_and_exit()
        choice = "Save and Exit"
    else:
        print("Error in Menu")


print("See you next time!")

# typer
# if __name__ == "__main__":
#     typer.run(main)
