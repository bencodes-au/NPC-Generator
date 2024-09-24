from characters_functions import generate_character, delete_character, view_character, view_categories, save_and_exit
from characters_class import Characters

print("Welcome to your NPC Generator")


def menu():
    print("Enter 1 to Generate a Character")
    print("Enter 2 to Delete a Character")
    print("Enter 3 to View Saved Characters")
    print("Enter 4 to Learn about Generation")
    print("Enter 5 to Save and Exit")

    choice = input("Enter your choice: ")

    return choice


choice = ""

while choice != "5":
    choice = menu()

    if choice == "1":
        generate_character()
    elif choice == "2":
        delete_character()
    elif choice == "3":
        view_character()
    elif choice == "4":
        view_categories()
    elif choice == "5":
        save_and_exit()
        print("Exiting")
    else:
        print("Invalid choice")

print("See you next time!")
