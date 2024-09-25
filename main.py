from generator import Generator
from manager import Manager

import inquirer
import typer

print("Welcome to your NPC Generator")

manager = Manager()
generator = Generator(manager)

choice = ""

while choice != "Exit Program":

    menu = [
        inquirer.List(
            "choice",
            message="What would you like to do?",
            choices=["Generate a Character", "Delete a Character",
                     "View Saved Characters", "Learn More About Generation", "Exit Program"],
        ),

    ]

    answers = inquirer.prompt(menu)

    if answers["choice"] == "Generate a Character":
        generator.generate_character()
    elif answers["choice"] == "Delete a Character":
        manager.delete_character()
    elif answers["choice"] == "View Saved Characters":
        manager.show_characters()
    elif answers["choice"] == "Learn More About Generation":
        # view_categories()
        print("Viewing Categories")
    elif answers["choice"] == "Exit Program":
        choice = "Exit Program"
    else:
        print("Error in Menu")


print("See you next time!")

# typer
# if __name__ == "__main__":
#     typer.run(main)
