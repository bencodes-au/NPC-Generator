# Criteria
Current Commit Count: 11/20

## 3 classes
Manager
Generator
Categories

## 6 Functions
1. Generate a Character
2. Save a Character
3. Delete a Character
4. Show a Character
5. Save to File
6. Load from File
7. Learn More
+ init functions

## 4 External Libraries
1. Inquirer
2. Typer
3.  
4. 

## Read Me

## App flow
What would you like to do? 
- Generate a Character
- Delete a Character
- View Saved Characters
- Learn about Generation
- Exit Application

### Generate a Character
- Genre = ["Fantasy", "Sci-fi", "Crime", "Horror", "Heroes", "Western"]
- Identity = ["Male", "Female", "Neutral"]
- Trait = ["Strong", "Nimble", "Hardy", "Smart", "Wise", "Charming"]
- Background = ["Warrior", "Expert", "Criminal", "Merchant", "Hermit", "Believer"]
- Name (from identity)
    - Male = ["Alex", "Ben", "Chris", "Daniel", "Elijah", "Fred", "Gabriel", "Henry", "Isaac", "John", "Kyle", "Lucas", "Matthew", "Nathan", "Oliver", "Patrick", "Quentin", "Ryan", "Sam", "Thomas", "Umar", "Victor", "William", "Xavier", "Yuri", "Zach"]
    - Female = ["Abigail", "Bianca", "Charlotte", "Diana", "Emily", "Fiona", "Grace", "Hannah", "Isabella", "Julia", "Katherine", "Lily", "Mia", "Nora", "Olivia", "Penelope", "Quinn", "Rebecca", "Sophia", "Tessa", "Uma", "Victoria", "Wendy", "Xia", "Yvonne", "Zoe"]
    - Neutral = ["Avery", "Blake", "Cameron", "Dakota", "Ellis", "Finley", "Gray", "Hayden", "Indigo", "Jordan", "Kai", "Logan", "Morgan", "Noel", "Oakley", "Phoenix", "Quinn", "Riley", "Skyler", "Taylor", "Ulan", "Val", "Wyatt", "Xiao", "Yi", "Zayne"]
- title (from background)
warrior_background = ["Valiant", "Fearless", "Conqueror", "Defiant", "Protector", "Mercenary."]
expert_background = ["Mastermind", "the Viruoso", "the Scholar", "Adept", "Prodigy", " Oracle"]
criminal_background = ["Outlaw", "Bandit", "Trickster", "Sinner", "Scoundrel", "Shadow"]
merchant_background = ["Broker", "Dealer", "Purveyor", "Prince", "Vendor", "Bargain Master"]
wanderer_background = ["Recluse", "Nomad", "Explorer", "Drifter", "Wayfarer", "Adventerous"]
believer_background = ["Faithful", "Devoted", "Seeker", "Zealot", "Prophet", "Enlightened"]
- save y/n
- if y, save to json

### Delete a Character
- Press Delete Character
- Shows all saved characters
- Choose to delete one or return to menu
- Shows "Successfully Deleted"
- Save Json

### View Saved Characters
- Show saved characters

### Learn about Generation
What would you like to know more about? 
- genre (blurb)
- gender
- trait
- background
- name
- title
- return to menu
 
Upon selecting, loads a description of the category
Returns to menu

### Exit
show exiting




