# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


label start:
    $ name = renpy.input("Enter your name to start", "", length=20)
    scene bg black
    play music "bg music.mp3"
    #play sound "rain.mp3" fadein 2.0 fadeout 20.0

    a "{cps=30}%(name)s! Wake up!"
    scene bg room
    #will change background to transperent today
    show albert
    a "I'm in trouble, I need you to come with me to raven forest."

    scene bg forest

    #show Albert
    a "{cps=35}I fucked up %(name)s, my brother lost everything gambling and took out a huge loan."
    a "{cps=30}I accepted a job and stole guns from the gangs operating here so I can help pay the money back, but they found out."
    "{cps=40}You heard about those gangs, there are the devils, led by Julian, known for their ruthlessness and lack of honor." with flash
    "{cps=40}And the ghosts, led by Frank, they operate in the shadows. If you cross them, your only way out is death."
    a "{cps=30}No one can escape them, I don’t know what to do, please help me."

    menu:
        "What's your plan?"

        "Offer to work for the devils for protection.":
            $ devils = True
            jump chose_devils

        "Offer to work for the ghosts for protection.":
            $ ghosts = True
            jump chose_ghosts

        "Prepare to fight for your friend’s life.":
            $ chose_fight = True
            jump chose_fight

    return
