label final_fight:
    scene bg motel
    play sound "knockknock.wav"
    show screen stats
    $ renpy.pause(1.0)
    show lana
    #reason for them leaving
    lana "Boss, I just came back from the [gang] territory,
     there's probably something important downtown, there is only one bodyguard there right now."
    if Jason:
        "Get your gun and tell Jason to meet us there, it's time to end this."
    else:
        "Get your gun, it's time to end this."

    if devils:
        scene bg devils
    else:
        scene bg ghosts

    "You see the bodyguard, and [boss]'s cabin behind it"
    if Jason:
        n "Jason, can you neutralize that guard?"
        show jason
        jason "I got this"
        #maybe change
        "Jason sneaks up on the bodyguard and chokes him"
    else:
        "You bribe the bodyguard"
    if chose_fight:
        "You open the cabin door, but there is no one inside. The phone on the wall starts ringing..."
        boss "You thought it would be that easy? Meet me at the Bendix Diner tommorow at 8pm, we need to talk."
    else:
        "You open the cabin door, and see [boss] try to reach for his weapon."
        play sound "gunshot.mp3"
        "You shoot him in the leg and he falls to his knees" with flash

    if chose_fight:
        jump ending_scene_2
    jump ending_scene_1
