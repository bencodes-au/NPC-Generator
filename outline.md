# Criteria
Current Commit Count: 4/20

## 3 classes
Manager
Generator

## 6 Functions
1. Generate a Character
2. Save a Character
3. Delete a Character
4. View Saved Characters
5. Learn about Generation
6. 

## 4 External Libraries
- Inquirer
- Typer
- 

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
- Trait = ["Strong", "Agile", "Hardy", "Smart", "Wise", "Charming"]
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

### Delete a Character
- Enter character name 
- Delete the character
- Return to menu

### View Saved Characters
- Show saved characters

### Learn about Generation
What would you like to know more about? 
- genre (blurb)
- gender
- trait
- background
- return to menu
 
Upon selecting, loads a description of the category
Returns to describe category menu

### Exit
show exiting
save current state to json file




