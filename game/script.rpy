# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Albert")
define j = Character("Julian")
define f = Character("Frank")
define n = Character("[name]")
define gui.text_color = "#F72C00"
default ghosts = False
default devils = False
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

label start:

    $ name = renpy.input("Enter your name to start", "", length=20)
    scene bg room

    a "{cps=30} %(name)s Wake up!
    you open your eyes and see Albert,
    your childhood friend.\n
    He asks you to come with him to raven forest."

    scene bg forest

    "{cps=40}You heard about those gangs, there are the devils,\n known for their ruthlessness and lack of honor.\nAnd the ghosts, they prefer to operate in the shadows,\n
    if you cross them, your only way out is death"

    "{cps=30}You make eye contact with Albert, he looks distressed,\n
    he says with a shaking voice" with flash
    a "{cps=30}No one can escape them, I don’t know what to do, please help me."

    menu:
        "You have 3 choices"

        "Offer the devils information about the ghosts in exchange for peace and protection":
            $ devils = True
            jump chose_devils

        "Offer the ghosts information about the devils in exchange for peace and protection":
            $ ghosts = True
            jump chose_ghosts

        "Start gathering troops and prepare to fight for your friend’s life.":
            "you chose 1"
            jump chose_gather_troops


    label create_gang:



    return
