transform middle_right:
    xalign 0.85
    yalign 1.0

label final_fight:
    scene bg motel
    play sound "knockknock.wav"
    show screen stats
    $ renpy.pause(1.0)
    show lana with dissolve
    #reason for them leaving
    lana "{cps=35}%(name)s, I just set the [gang] drug supply on fire, they are all looking for me.
    They only left one bodyguard to protect [boss]."
    lana "{cps=35}They will find me sooner or later, we have to do something."
    menu:
        "What do you do?"

        "Go after [boss]":
            jump confrontation

        "Stay and defend yourself when the [gang] arrive":
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
            jump dead


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
        menu:
            "Ask Jason to neutralize the guard":
                n "{cps=35}Jason, can you neutralize that guard?"
                jump neutralize

            "Ask Jason to kill the guard":
                n "{cps=35}Jason, can you kill that guard?"
                jason "{cps=35}I'm not getting my hands dirty for you, do it yourself."
                menu:
                    "Kill the guard yourself":
                        play sound "gunshot.mp3"
                        hide bodyguard with kill
                        "You sneak up on the guard and shoot him from behind. You feel sick, you can't recognize yourself anymore." with dissolve
                        n "{cps=35}It had to be done."
                        jason "{cps=20}Did it?"
                        "{cps=35}the path to [boss] is clear."
                        jump after_guard

                    "Let Jason handle it":
                        n "{cps=35}Okay Jason, let's try things your way."

    else:
        menu:
            "Bribe the guard":
                "{cps=35}You walk up to the guard, and offer him 10000$ to look the other way."
                bodyguard "{cps=35}Deal, I never saw you"
                hide bodyguard with dissolve
                "{cps=35}the path to [boss] is clear."
                jump after_guard

            "Kill the guard":
                play sound "gunshot.mp3"
                hide bodyguard with kill
                "You sneak up on the guard and shoot him from behind. You feel sick, you can't recognize yourself anymore." with dissolve
                n "{cps=35}It had to be done"
                lana "{cps=20}Did it?"
                "{cps=35}the path to [boss] is clear."
                jump after_guard

label neutralize:

    jason "{cps=35}I got this"
    #maybe change
    hide jason with dissolve
    show jason at middle_right with dissolve
    "{cps=35}Jason sneaks up on the bodyguard and chokes him unconcious, the path to [boss] is clear."
    hide bodyguard with dissolve
    hide jason with dissolve

label after_guard:
    scene bg cabin
    if chose_fight:
        play sound "phone.mp3"
        "{cps=35}You open the cabin door. There is no one inside, but the phone on the wall is ringing..."
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
