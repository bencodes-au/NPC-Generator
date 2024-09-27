from generator import Generator
from manager import Manager
from categories import Categories

import inquirer
import emoji
from colored import Fore, Back, Style

color: str = f'{Style.res_dim}{Fore.red}'
print(f'{color}Welcome to the Character Generator{Style.reset}')

manager = Manager()
generator = Generator(manager)
categories = Categories

menu_nav = ""

while menu_nav != "Exit Program":

    menu = [
        inquirer.List(
            "menu_nav",
            message="What would you like to do?",
            choices=["Generate a Character", "Delete a Character",
                     "View Saved Characters", "Learn More About Generation", "Exit Program"],
        ),

    ]

    answers = inquirer.prompt(menu)

    if answers["menu_nav"] == "Generate a Character":
        generator.generate_character()
    elif answers["menu_nav"] == "Delete a Character":
        manager.delete_character()
    elif answers["menu_nav"] == "View Saved Characters":
        manager.show_characters()
    elif answers["menu_nav"] == "Learn More About Generation":
        categories.learn_more()
    elif answers["menu_nav"] == "Exit Program":
        menu_nav = "Exit Program"
    else:
        print("Error Occurred: Returning to Menu")


print(emoji.emojize("See you next time :red_heart:", variant="emoji_type"))
