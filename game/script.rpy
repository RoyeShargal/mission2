label start:
    $ name = renpy.input("Enter your name to start", "", length=20)
    scene bg black
    play music "bg music.mp3"
    #play sound "rain.mp3" fadein 2.0 fadeout 20.0

    a "{cps=30}%(name)s! Wake up!"
    scene bg room
    show albert at middle_right
    a "{cps=35}I'm in trouble, I need you to come with me to raven forest."

    scene bg forest

    show albert at middle_right
    a "{cps=35}I fucked up %(name)s, my brother lost everything while gambling and took out a huge loan."
    a "{cps=35}I accepted a job and stole guns from the gangs operating here so I can help pay the money back, but they found out."
    "{cps=35}You heard about those gangs, there are {b}the Devils, led by Julian{/b}, known for their ruthlessness and lack of honor." with flash
    "{cps=35}And {b}the Ghosts, led by Frank{/b}, they operate in the shadows. If you cross them, your only way out is death."
    a "{cps=35}No one can escape them, I don’t know what to do, please help me."

    menu:
        "What's your plan?"

        "Prepare to fight for your friend’s life.":
            $ chose_fight = True
            jump chose_fight

        "Offer to work for the Devils for protection.":
            $ devils = True
            jump chose_devils

        "Offer to work for the Ghosts for protection.":
            $ ghosts = True
            jump chose_ghosts
