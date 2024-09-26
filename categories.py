import inquirer

how_to_blurb = (
    """
    This program is designed to generate characters for a story-world to spark inspiration.
    Select a series of options which will guide the generator into providing a dramatic prompt of a character outline.
    To get started, follow the Generate a Character option in the Menu.
    If you choose to save them, your characters will be stored here for whenever you need them.
    Have Fun!
    """
)

genre_blurb = (
    """
    Genre is the style or category that the story takes place in. These include:
    Fantasy: A typically medieval world of knights, magic and dragons.
    Sci-fi: A imagined future of advanced science, space exploration, time travel and extra-terrestrials.
    Crime: A story of detectives and investigators solving a mystery.
    Horror: A story of every day people attempting to survive a horrific threat.
    Heroes: Enhanced humans attempting to save the day from villiany.
    Western: Rootin' tootin' gunslingers in the wild west chasing down varmant.
    """
)

identity_blurb = (
    """
    Identity represents the gender identity of your character. These include:

    Male: This character identifies as Male. 
    Female: This character identifies as Female.
    Neutral: This character identifies as neither Male or Female. 
    """)

trait_blurb = (
    """
    Trait describes this character's biggest asset. The tool that defines them. These include:
    Strong: having the power to move heavy weights
    Nimble: quick and light in movement or action
    Hardy: capable of enduring difficult conditions
    Smart: quick witted or intelligent
    Wise: experienced, knowledgeable or with sound judgement
    Charming: pleasant and/or attractive
    """)
background_blurb = (
    """
    Background describes this character's origin, profession or skillset. These include:
    Warrior: someone who lives or dies by their proficiency with their weapon
    Expert: a master of a craft or trade
    Criminal: someone who makes a living breaking the law
    Merchant: a trader of goods and wares
    Hermit: a sage who lives in private studying
    Believer: a person of faith in a higher being
    """)

name_blurb = (
    """
    Name is self-explanitary. Everyone has one of those.
    Names are generated based on the choices made in prior categories.
    """)

title_blurb = (
    """
    Title refers to a nickname related to the characteristic they are best known by.
    Titles are generated based on the choices made in prior categories. 
    """)


class Categories:
    def learn_more():
        categories = [
            inquirer.List(
                "category",
                message="What would you like to know?",
                choices=["How-To", "Genre", "Identity", "Trait",
                         "Background", "Name", "Title", "Return to Menu"],
            ),

        ]

        answers = inquirer.prompt(categories)

        if answers["category"] == "How-To":
            print(how_to_blurb)
        elif answers["category"] == "Genre":
            print(genre_blurb)
        elif answers["category"] == "Identity":
            print(identity_blurb)
        elif answers["category"] == "Trait":
            print(trait_blurb)
        elif answers["category"] == "Background":
            print(background_blurb)
        elif answers["category"] == "Name":
            print(name_blurb)
        elif answers["category"] == "Title":
            print(title_blurb)
        elif answers["category"] == "Return to Menu":
            menu_nav = "Menu"
        else:
            print("Error in Categories")
