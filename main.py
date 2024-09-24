from characters_functions import generate_character, delete_character, view_character, view_categories, save_and_exit
from characters_class import Characters
import inquirer

print("Welcome to your NPC Generator")

choice = ""

while choice != "Save and Exit":

    menu = [
        inquirer.List(
            "choice",
            message="What would you like to do?",
            choices=["Generate a Character", "Delete a Character",
                     "View Saved Characters", "Learn about Generation", "Save and Exit"],
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

# def menu():
#     print("Enter 1 to Generate a Character")
#     print("Enter 2 to Delete a Character")
#     print("Enter 3 to View Saved Characters")
#     print("Enter 4 to Learn about Generation")
#     print("Enter 5 to Save and Exit")

#     choice = input("Enter your choice: ")

#     return choice


# choice = ""

# while choice != "5":
#     choice = menu()

#     if choice == "1":
#         generate_character()
#     elif choice == "2":
#         delete_character()
#     elif choice == "3":
#         view_character()
#     elif choice == "4":
#         view_categories()
#     elif choice == "5":
#         save_and_exit()
#         print("Exiting...")
#     else:
#         print("Invalid choice")
