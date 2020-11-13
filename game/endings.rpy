label ending_scene_1:

    if devils:
        scene bg devils
    else:
        scene bg ghosts
    hide screen stats

    "{cps=40}You and your men surround [boss], he looks at you in distress"
    boss "{cps=40}Albert knew what would happen if he stole from me, he brought it on himself, all I did was pull the trigger."
    "{cps=40}You pull out your gun and point it at his head. [boss] falls to his knees and begs."
    boss "{cps=40}Killing me won’t bring your friend back, it will only make you as bad as me."

    menu:

        "Kill [boss]":
            jump ending_1

        "Spare [boss]":
            "das"

label ending_1:

    play sound "gunshot.mp3"
    "You close your eyes and pull the trigger, everything is silent
    but the sound of the shot and [boss]'s body falling to the ground." with kill
    "{cps=40}You thought you would feel something, but the emptiness you have been feeling since you started this still remains."
    "{cps=40}Maybe the boss was right, maybe you did become as bad as him,
     but at least you know he won't do what he did to Albert to anyone else."
    "{cps=30}{b}{size=+5}{color="#F72C00"}At least you got your revenge."

    return

label ending_2:

    "{cps=40}You look into the boss’s eyes, his face is filled with tears."
    "{cps=40}You close your eyes for a moment, and holster your gun. "
    "{cps=40}Maybe he deserves death, but killing him won’t bring Albert back, it will only make you feel worse."
    n "If I ever see you again, you will wish I shot you today."
    'One of your men asks "Are you sure boss? You’re really going to forgive him after what he did?"'
    n "No, but I won't become like him, it’s not what Albert would have wanted."
    "{cps=40}He gives you a small nod, and you all walk away."

    return

label ending_scene_2:

    scene bg diner
    hide screen stats

    "{cps=35}[boss] asks you to meet him at the Bendix diner, you see him sitting alone with a cup of coffee,
    he looks anxious.\nYou and your men sit in front of him."
    boss "{cps=35}You don’t have to kill me, [other_boss] killed Albert, and he is planning on getting to you before you get to him."
    "{cps=35}You look outside and see the other gang armed and heading to the diner."
    scene bg dinerParking
    "You and your men pull out your guns and go outside, [other_boss] faces you."
    other_boss "I killed Albert because he deserved it. You are outnumbered, we will let you go if you will not come after us."

    menu:

        "Signal your men and shoot the [other_gang]":
            jump ending_3

        "Agree to stop the violence":
            jump ending_4

label ending_3:
    "{cps=35}You shake [other_boss]'s hand, and tell him you will let it go."
    "{cps=35}You walk back to your men, stand beside them and whisper"
    n "{b}{size=+5}Kill them"
    #shooting sounds
    "{cps=35}You and your men start shooting, the other gang is caught by surprise and has no time to react, it’s a massacre."
    "{cps=35}You stand in the dark parking lot, shaking.
    There are bodies all around you."
    "{cps=35}Blood is dripping down your face, but it is not your blood."
    "{cps=35}You finally got revenge."
    "{b}{color="#F72C00"}Was it worth it?" with dissolve

    return

label ending_4:

    return
