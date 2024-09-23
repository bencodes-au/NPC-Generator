# Pseudo-Code
## Menu
print("Welcome to your Character Manager")

def menu
    print ("Enter 1 to Generate a Character")
    print ("Enter 2 to Delete a Character")
    print ("Enter 3 to View Saved Characters")
    print ("Enter 4 to Learn about Generation)
    print ("Enter 5 to Save and Exit")
    
    choice = input("Enter your choice: ")

    return choice

choice = ""

while choice != "5":
    choice = menu()

    if choice == "1":
        generate_character(characters)
    elif choice == "2":
        delete_character(characters)
    elif choice == "3":
        view_character(characters)
    elif choice == "4":
        view_categories(characters)
    elif choice == "5":
        save_and_exit(characters)
        print "Exiting"
    else:
        print ("Invalid choice")

print("See you next time!")


## Character Generator
### Character Questions
What genre? 
1. Fantasy
2. Sci-fi
3. Modern

questions = [
    inquirer.List(
        "genre",
        message="What genre is your world?",
        choices=["Fantasy", "Sci-fi", "Crime", "Horror", "Heroes", "Western"],
    ),
]

answers = inquirer.prompt(questions)
finished_character = Character Generator

## Generation
if genre == "Fantasy":
    chosen_genre == "From a life of swords and sorcery, "
elif genre == "Sci-fi"
    chosen_genre == "From a life living amongst the stars, "
etc etc

answers = inquirer.prompt(questions)
<!-- finished_character = Generator -->

(f"{chosen_genre} {chosen_gender} {chosen_trait} {chosen_background} named {chosen_name} {chosen_title}.")

finished_character = (f"{chosen_genre} {chosen_gender} {chosen_trait} {chosen_background} named {chosen_name} {chosen_title}.") 
print finished_character

choice = input("Would you like to save your character?: ")
    if choice == "y":
        save function
    elif choice == "n":
        menu()
    else:
        print("Invalid Choice")





### Save a Character
def save_character(characters)
    save_name = finished_character
    saved_character = characters(save_name)
    characters.save_character(saved_character)
    print("Character saved")

in characters class
def saved_character(self, save_name)
    self.saved_character.append(save_name)

## Delete a Character
use characters class 

def delete_character(manager):
    save_name = input("Enter the save name: ")
    
    if ? reference character class to delete it ? 
        print("Character successfully deleted")
    else: 
        print("This save name does not exist")


## View Characters
use .get on manager class to show current save names
select a save name to see the full character

def show_characters(characters)
    saved_characters = characters.show_character()
    if not saved_characters
        print("There are no characters saved)
    for save_name in saved_characters
        print(save_name)

in character class
def show_characters(self):
    return self.saved_characters

## Characters Class functions
### Save a character
def saved_character(self, save_name)
    self.saved_character.append(save_name)

### Delete saved characters
tba

### Show saved characters
def show_characters(self):
    return self.saved_characters

## Generate Class Function

