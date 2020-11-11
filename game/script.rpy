# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Albert", color="#0e64e6", what_color="#0e64e6")
define j = Character("Julian", color="#995f03", what_color="#995f03")
define f = Character("Frank", color="#d48506", what_color="#d48506")
define n = Character("[name]", color="#F72C00", what_color="#F72C00")
define b = Character("[boss]")
default ghosts = False
default devils = False
default stole_drugs = False
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

label start:

    $ name = renpy.input("Enter your name to start", "", length=20)
    scene bg room

    a "{cps=30} %(name)s Wake up!
    you open your eyes and see Albert,
    your childhood friend. He asks you to come with him to raven forest."

    scene bg forest

    "{cps=40}You heard about those gangs, there are the devils,\n known for their ruthlessness and lack of honor.\nAnd the ghosts, they prefer to operate in the shadows,\n
    if you cross them, your only way out is death"
    screen hello():
        text "dasda":
            at transform:
                align(0.2,0.5) alpha 0.0
                linear 0.5 alpha 1.0

    "{cps=30}You make eye contact with Albert, he looks distressed,\n
    he says with a shaking voice" with flash
    a "{cps=30}No one can escape them, I don’t know what to do, please help me."

    menu:
        "You have 3 choices"

        "Offer to work for the devils":
            $ devils = True
            jump chose_devils

        "Offer to work for the ghosts":
            $ ghosts = True
            jump chose_ghosts

        "Prepare to fight for your friend’s life.":
            "you chose 1"
            jump chose_gather_troop


    label first_mission:
        #TODO: fix title screen
        scene bg black
        "The Revenge" with fade

        if devils:
            #gang = "Devils"
            $ boss = "Julian"
        else:
            #gang = "Ghosts"
            $ boss = "Frank"

        scene bg motel

        n "Where is my gun?? I am going kill them!"

        #scene gang's location

        n "What is this truck?\nThis must be their bomb supply."
        n "That's [boss] in the window inside that cabin!"
        n "Shit, I only have 1 bullet left, and there are too many of them"

        menu:
            "What to do"

            "Try to kill [boss]":
                "death"
                #death

            "Destroy their supply":
                "You shoot the truck"
                #FLASH STUFF AND SOUND


    return
