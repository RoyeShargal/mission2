label first_mission:
    #TODO: fix title screen
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

    #Ending tests
    #if chose_fight:
        #jump ending_scene_2
    #jump ending_scene_1
    scene bg motel
    show screen stats

    n "{cps=40}Where is my gun?? I am going kill them!"
    #n "{cps=40}There it is! I'll show them"
    scene bg black
    play sound "fastWalking.wav"
    "{cps=2}{color=#000000}.....{/color}{nw}"
    stop sound

    scene bg truck
    n "{cps=30}What is this truck?\nI can see bombs inside, This must be their supply."
    n "{cps=30}I'm so close to the [gang] territory, but I'm really outnumbered."
    n "{cps=30}Maybe I can hurt them without risking my life."

    menu:
        "What do you do?"

        "Try to kill [boss]":
            n "{cps=30}Thats it! I'm going to end it!"
            if devils:
                scene bg devils
            else:
                scene bg ghosts
                boss "{cps=45}Oh look, its the thief's little friend."
                boss "{cps=40}That's sweet."
                n "{cps=25}Your time is up!"
                boss "{cps=40}HE'S ARMED! STOP HIM!!"

            scene bg black with kill
            play sound "gunshot.mp3"
            centered "{font=ARMY RUST.ttf}{size=+50}{color=#F72C00}{cps=20}You and [boss] died" with Dissolve(1.0)
            jump dead


        "Destroy their supply":
            n "{cps=30}I'll shoot their bomb supply!"
            play sound "explode.wav"
            scene bg black with flash
            n "{cps=45}They are coming out! I gotta go fast!"
            play sound "fastWalking.wav"
            "{cps=2}{color=#000000}.....{/color}{nw}"
            stop sound
            jump first_guy

label dead:
    return
