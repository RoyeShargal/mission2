# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


label start:
    $ name = renpy.input("Enter your name to start", "", length=20)
    scene bg room

    a "{cps=30} %(name)s! Wake up!"
    "{cps=30}You open your eyes and see Albert, your childhood friend.
     He asks you to come with him to raven forest."

    scene bg forest

    a "{cps=30}I fucked up %(name)s, I have been stealing money from the gangs operating here and they found out."
    "{cps=40}You heard about those gangs, there are the devils,\n known for their ruthlessness and lack of honor." with flash
    "{cps=40}And the ghosts, they operate in the shadows.\n If you cross them, your only way out is death"
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
            $ chose_fight = True
            jump chose_fight

    return
