label ending_scene_1:

    if devils:
        scene bg devils
    else:
        scene bg ghosts
        show frank at right
    hide screen stats

    "{cps=40}You and your men surround [boss], he looks at you in distress"
    boss "{cps=40}Albert knew what would happen if he stole from me, he brought it on himself, all I did was pull the trigger."
    "{cps=40}You pull out your gun and point it at his head. [boss] falls to his knees and begs."
    boss "{cps=40}Killing me won’t bring your friend back, it will only make you as bad as me."

    menu:

        "Kill [boss]":
            jump ending_1

        "Spare [boss]":
            jump ending_2

label ending_1:

    play sound "gunshot.mp3"
    hide frank with kill
    "You close your eyes and pull the trigger, everything is silent
    but the sound of the shot and [boss]'s body falling to the ground." with dissolve
    play music "ending_music.mp3" fadein 2.0
    "{cps=30}You thought you would feel something, but the emptiness you have been feeling since you started this still remains."
    "{cps=30}Maybe [boss] was right, maybe you did become as bad as him,
     but at least you know he won't do what he did to Albert to anyone else."
    "{size=+5}At least you got your revenge." with Dissolve(1.0)

    $ ending = 1
    jump credits

label ending_2:

    play music "ending_music.mp3" fadein 2.0
    "{cps=30}You look into [boss]'s eyes, his face is filled with tears."
    "{cps=30}You close your eyes for a moment, and holster your gun. "
    "{cps=30}Maybe he deserves death, but killing him won’t bring Albert back, it will only make you feel worse."
    n "{cps=30}If I ever see you again, you will wish I shot you today."
    dan "{cps=30} Are you sure boss? You’re really going to forgive him after what he did?"
    n "{cps=30}No, but I won't become like him, it’s not what Albert would have wanted."
    "{cps=30}He gives you a small nod, and you all walk away."

    $ ending = 2
    jump credits

label ending_scene_2:

    scene bg diner
    hide screen stats
    if ghosts:
        show frank at right
    "{cps=35}You find [boss] at the Bendix diner, he is sitting alone with a cup of coffee."

    menu:
        "Kill [boss]":
            jump ending_5

        "Listen to what [boss] has to say":
            "{cps=35}You and your men sit in front of the boss"

label ending_scene_3:

    boss "{cps=35}You don’t have to kill me, [other_boss] killed Albert,
    and he is planning on getting to you before you get to him."
    "{cps=35}You look outside and see the other gang armed and heading to the diner."
    scene bg dinerParking
    if devils:
        show frank
    "{cps=35}You and your men pull out your guns and go outside, [other_boss] faces you."
    other_boss "{cps=35}I killed Albert because he deserved it. You are outnumbered,
     we will let you go if you will not come after us."

    menu:

        "Signal your men and shoot the [other_gang]":
            jump ending_3

        "Agree to stop the violence":
            jump ending_4

label ending_3:
    play music "ending_music.mp3"
    "{cps=30}You shake [other_boss]'s hand, and tell him you will let it go."
    "{cps=30}You walk back to your men, stand beside them and whisper"
    n "{size=+5}Kill them." with dissolve
    #shooting sounds
    "{cps=30}You and your men start shooting, the other gang is caught by surprise and has no time to react, it’s a massacre."
    "{cps=30}You stand in the dark parking lot, shaking. There are bodies all around you."
    #"{cps=30}Blood is dripping down your face, but it is not your blood."
    "{cps=30}You finally got revenge."
    "{size=+5}Was it worth it?" with Dissolve(1.0)

    $ ending = 3
    jump credits

label ending_4:

    play music "ending_music.mp3"
    $ ending = 4
    jump credits

label ending_5:
    play music "ending_music.mp3"
    play sound "gunshot.mp3"
    "You pull out your gun and shoot [boss] in his chest" with dissolve
    "{cps=35}Everyone in the diner starts screaming, they are all scared of you."
    "{cps=35}Red and blue lights flash through the window"
    "{cps=35}You look down at [boss] lying on the ground, he says softly as he struggles to breath"
    boss "{cps=35}I didn't kill Albert, it was [other_boss]."
    boss "{cps=35}You killed me for nothing, you are just as bad as him"
    police "{cps=35}This is the police! get out with your hands on your head!"
    scene bg dinerParking
    "{cps=35}As soon as you leave the diner, they handcuff you and put you in the police car."
    "The driver looks back at you and says"
    driver "{cps=30}That's fucked up, shooting a man in front of all those people... how does anyone do something like that?"
    n "{cps=3}I....{nw}"
    n "{cps=20}I though he deserved it."
    n "{size=+5}I lost control." with Dissolve(1.0)

    $ ending = 5
    jump credits
    return

label credits:
    scene bg black
    centered "{font=ARMY RUST.ttf}{size=+100}{color=#912119}Ending no. [ending]\nout of 5" with Dissolve(2.0)
    show screen ending_credits with Dissolve(2.0)
    pause (40)
    return
