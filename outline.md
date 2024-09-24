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

## Libraries
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
    - Warrior = ["the Valiant.", "the Fearless.", "the Conqueror.", "the Defiant.", "the Protector.", "the Mercenary."]
    - Expert = ["the Mastermind.", "the Viruoso.", "the Scholar.", "the Adept.", "the Prodigy.", "the Oracle."]
    - Criminal = ["the Outlaw.", "the Bandit.", "the Trickster.", "the Sinner.", "the Scoundrel.", "the Shadow."]
    - Merchant = ["the Broker.", "the Dealer.", "the Purveyor.", "the Prince.", "the Vendor.", "the Bargain Master."]
    - Wanderer = ["the Recluse.", "the Nomad.", "the Explorer.", "the Drifter.", "the Wayfarer.", "the Adventerous."]
    - Believer = ["the Faithful.", "the Devoted.", "the Seeker.", "the Zealot.", "the Prophet.", "the Enlightened."]
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




