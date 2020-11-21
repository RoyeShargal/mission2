label first_mission:
    scene bg black
    centered "{font=ARMY RUST.ttf}{size=+100}{color=#912119}The Revenge" with Dissolve(1.0)

    if devils:
        $ gang = "Devils"
        $ other_gang = "Ghosts"
        $ boss = j
        $ other_boss = f

    else:
        $ gang = "Ghosts"
        $ other_gang = "Devils"
        $ boss = f
        $ other_boss = j
        image side boss_side = "frank_side"

    scene bg motel

    "{cps=35}You get back back to your motel."
    n "{cps=35}Where is my gun?? I am going kill them!"
    #n "{cps=40}There it is! I'll show them"
    scene bg black
    play sound "fastWalking.wav"
    "{cps=2}{color=#000000}....{/color}{nw}"
    stop sound

    scene bg truck
    n "{cps=35}What is this truck? I can see bombs inside, This must be their supply."
    n "{cps=35}I'm so close to the [gang] territory, but I'm really outnumbered."
    n "{cps=35}Maybe I can hurt them without risking my life."

    menu:
        "What do you do?"

        "Try to kill [boss]":
            n "{cps=35}Thats it! I'm going to end it!"
            if devils:
                scene bg devils
            else:
                scene bg ghosts
                show frank at middle_right with dissolve
            boss "{cps=35}Oh look, its the thief's little friend."
            boss "{cps=35}That's sweet."
            n "{cps=35}Your time is up!"
            boss "{cps=35}HE'S ARMED! STOP HIM!!"

            play sound "gunshot.mp3"
            scene bg black with kill
            centered "{font=ARMY RUST.ttf}{size=+75}{color=#F72C00}{cps=20}You and [boss] died" with Dissolve(1.0)
            jump dead


        "Destroy their supply":
            n "{cps=35}I'll shoot their bomb supply!"
            play sound "explode.wav"
            scene bg black with shot
            n "{cps=35}They are coming! I gotta go fast!"
            play sound "fastWalking.wav"
            "{cps=2}{color=#000000}.....{/color}{nw}"
            stop sound
            jump first_member

label dead:
    return
