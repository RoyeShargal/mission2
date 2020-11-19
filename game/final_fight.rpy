label final_fight:
    scene bg motel
    play sound "knockknock.wav"
    show screen stats
    $ renpy.pause(1.0)
    show lana
    #reason for them leaving
    lana "{cps=35}%(name)s, I just set the [gang] drug supply on fire, they are all looking for me.
    They only left one bodyguard to protect [boss]."
    lana "{cps=35}They will find me sooner or later, we have to do something."
    menu:
        "What do you do?"

        "Go after [boss]":
            jump confrontation

        "Lock the door and prepare for the [gang] to arrive":
            "{cps=35}You and Lana take turns watching the window while the other rests"
            "{cps=35}It's 4 in the morning, when you see five armed men walking to the door."
            n "{cps=20}LANA! RUN!"
            "{cps=35}Lana quickly climbs out of the window."
            hide lana with dissolve
            "{cps=35}You try to escape as well, but it's too late, the door blasts open."
            if ghosts:
                show frank with dissolve
            else:
                #show julian
                " "
            boss "You shouldn't have fucked with me" with dissolve
            play sound "gunshot.mp3"
            with kill
            scene bg black
            centered "{font=ARMY RUST.ttf}{size=+100}{color=#F72C00}{cps=20}You died" with Dissolve(1.0)


label confrontation:
    if Jason:
        "{cps=35}Get your gun and tell Jason to meet us there, it's time to end this."
    else:
        "{cps=35}Get your gun, it's time to end this."

    if devils:
        scene bg devils
    else:
        scene bg ghosts

    show bodyguard at right
    "{cps=35}You see the bodyguard, and [boss]'s cabin behind it"
    if Jason:
        show jason at left with dissolve
        n "{cps=35}Jason, can you neutralize that guard?"
        jason "{cps=35}I got this"
        #maybe change
        "{cps=35}Jason sneaks up behind the bodyguard and chokes him unconcious.\n
        The path is clear."
        hide bodyguard with dissolve
        hide jason with dissolve
    else:
        "{cps=35}You walk up to the guard, and offer him 10000$ to look the other way."
        bodyguard "{cps=35}Deal, I never saw you"
        hide bodyguard with dissolve
    if chose_fight:
        "{cps=35}You open the cabin door.\nThere is no one inside, but the phone on the wall is ringing..."
        #maybe ringing sound
        boss "{cps=35}Did you think it would be that easy? Meet me at the Bendix Diner tommorow at 8pm, we need to talk."
    else:
        if ghosts:
            show frank
        else:
            " "
            #show julian
        "{cps=35}You open the cabin door, and see [boss] try to reach for his weapon."
        play sound "gunshot.mp3"
        "You shoot him in the leg and drag him outside." with shot

    if chose_fight:
        jump ending_scene_2
    jump ending_scene_1
