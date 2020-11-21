label ending_scene_1:

    if devils:
        scene bg devils
        #show julian
    else:
        scene bg ghosts
        show frank at middle_right
    hide screen stats

    "{cps=35}He looks at you in distress."
    boss "{cps=35}Albert knew what would happen if he stole from me, he brought it on himself, all I did was pull the trigger."
    "{cps=35}You pull out your gun and point it at his head. [boss] starts to beg"
    boss "{cps=35}Killing me won’t bring your friend back, it will only make you as bad as me."

    menu:
        "Kill [boss]":
            jump ending_1

        "Spare [boss]":
            jump ending_2

label ending_1:

    play sound "gunshot.mp3"
    if ghosts:
        hide frank with kill
    #else:
        #hide julian with kill
    stop music
    "You close your eyes and pull the trigger, everything is silent
    but the sound of the shot and [boss]'s body falling to the ground." with Dissolve(0.5)
    play music "ending_music.mp3" fadein 2.0
    "{cps=35}You thought you would feel something, but the emptiness you have been feeling since you started this still remains."
    "{cps=35}Maybe [boss] was right, maybe you did become as bad as him,
     but at least you know he won't do what he did to Albert to anyone else."
    "{size=+5}At least you got your revenge." with Dissolve(1.0)

    $ ending = 1
    jump credits

label ending_2:

    stop music
    play music "ending_music.mp3" fadein 2.0
    "{cps=35}You look into [boss]'s eyes, his face is filled with tears."
    "{cps=35}You close your eyes for a moment, and holster your gun. "
    "{cps=35}Maybe he deserves death, but killing him won’t bring Albert back, it will only make you feel worse."
    n "{cps=35}If I ever see you again, you will wish I shot you today."
    lana "{cps=35} Are you sure boss? You’re really going to forgive him after what he did?"
    n "{cps=35}No, but I won't become like him, it’s not what Albert would have wanted."
    "{cps=35}He gives you a small nod, and you all walk away."

    $ ending = 2
    jump credits

label ending_scene_2:

    scene bg diner
    hide screen stats
    if ghosts:
        show frank at middle_right
    #else:
        #show julian
    "{cps=35}You find [boss] at the Bendix diner, he is sitting alone with a cup of coffee."

    menu:
        "Kill [boss] while you have the chance":
            jump ending_5

        "Listen to what [boss] has to say":
            "{cps=35}You and your men sit in front of [boss]."

label ending_scene_3:

    boss "{cps=35}You don’t have to kill me, [other_boss] killed Albert,
    and he is planning on getting to you before you get to him."
    "{cps=35}You look outside and see the [other_gang] armed and heading to the diner."
    scene bg dinerParking
    if devils:
        show frank at middle_right
    #else:
        #show julian
    if jason:
        show jason at left
    show lana at middle_left
    "{cps=35}You and your men pull out your guns and go outside, [other_boss] faces you."
    other_boss "{cps=35}I killed Albert because he deserved it. You are outnumbered,
     we will let you go if you will not come after us."

    menu:

        "Signal your men and shoot the [other_gang]":
            jump ending_3

        "Agree to stop the violence":
            jump ending_4

label ending_3:
    stop music
    play music "ending_music.mp3" fadein 2.0
    "{cps=35}You shake [other_boss]'s hand, and tell him you will let it go."
    "{cps=35}You walk back to your men, stand beside them and whisper:"
    n "{size=+5}Kill them." with dissolve
    play sound "shooting.mp3"
    if devils:
        hide frank with kill
    #else:
        #hide julian with kill
    "You and your men start shooting, the other gang is caught by surprise and has no time to react, it’s a massacre." with dissolve
    hide lana with dissolve
    hide jason with dissolve
    "{cps=30}You stand in the dark parking lot, shaking. There are bodies all around you."
    "{cps=20}You finally got revenge."
    "{size=+5}Was it worth it?" with Dissolve(1.0)

    $ ending = 3
    jump credits

label ending_4:
    stop music
    play music "ending_music.mp3" fadein 2.0
    "{cps=35}You shake [other_boss]'s hand, and tell him you will let it go."
    "{cps=35}Both sides are still pointing weapons at each other, when several police cars arrive."
    police "{cps=35}This is the police! put down your weapons!"
    menu:
        "Give in":
            jump ending_6
        "Run":
            n "RUN!!" with dissolve
    "{cps=35}You run away, but the [other_gang] starts shooting at the police."
    "{cps=35}You hide behind a trash can and see Lana running towards you."
    play sound "gunshot.mp3"
    hide lana with shot
    "{cps=35}She gets shot, two policemen handcuff her and put her in the car."
    scene bg forest
    "{cps=35}There is nothing you can do to help her, you run and stop when you get to the woods, tears fill your eyes."
    n "{cps=35}This is all my fault." with dissolve
    $ ending = 4
    jump credits

label ending_6:
    "{cps=35}You put your hands on your head and fall to your knees."
    play sound "shooting.mp3"
    if devils:
        hide frank with kill
    #else:
        #hide julian with kill
    "[other_boss] tries to run away and gets shot multiple times." with dissolve
    "{cps=35}The police take everyone into seperate police cars."
    n "{cps=35}Am I going to jail?"
    driver "{cps=35}Well, that depends on whether your men will talk."
    n "{cps=35}They won't."
    driver "{cps=35}I have been doing this job for a very long time."
    driver "I wouldn't be so sure" with Dissolve(1.0)

    $ ending = 6
    jump credits

label ending_5:
    play music "ending_music.mp3"
    play sound "gunshot.mp3"
    "You pull out your gun and shoot [boss] in his chest" with shot
    "{cps=35}Everyone in the diner starts screaming, they are all scared of you."
    "{cps=35}Red and blue lights flash through the window."
    "{cps=35}You look down at [boss] lying on the ground, he says softly as he struggles to breath"
    boss "{cps=35}I didn't kill Albert, it was [other_boss]."
    boss "{cps=35}You killed me for nothing, you are just as bad as him."
    police "{cps=35}This is the police! get out with your hands on your head!"
    scene bg dinerParking
    "{cps=35}As soon as you leave the diner, the police handcuff you and put you in the police car."
    "The driver looks back at you and says"
    driver "{cps=35}That's fucked up, shooting a man in front of all those people... how does anyone do something like that?"
    n "{cps=3}I...{nw}"
    n "{cps=15}I though he deserved it."
    n "{size=+5}I lost control." with Dissolve(1.0)

    $ ending = 5
    jump credits

label credits:
    scene bg black
    centered "{font=ARMY RUST.ttf}{size=+100}{color=#912119}Ending no. [ending]\nout of 6" with Dissolve(2.0)
    show screen ending_credits with Dissolve(2.0)
    pause (40)
    return
