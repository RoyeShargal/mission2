label first_mission:
    #TODO: fix title screen
    scene bg black
    centered "{size=+50}{color=#F72C00}The Revenge" with dissolve

    if devils:
        $ gang = "Devils"
        $ other_gang = "Ghosts"
        $ boss = "Julian"
        $ other_boss = "Frank"
    else:
        $ gang = "Ghosts"
        $ other_gang = "Devils"
        $ boss = "Frank"
        $ other_boss = "Julian"

    #Ending tests
    #if chose_fight:
    #    jump ending_scene_2
    #jump ending_scene_1
    scene bg motel
    show screen stats

    n "{cps=40}Where is my gun?? I am going kill them!"
    n "{cps=40}There its is! I'll show them'"
    scene bg black
    #add walking sound
    "{cps=2}   {nw}"

    if devils:
        #scene bg devils
        scene gangs place
    else:
        #scene bg ghosts
        scene gangs place

    #Maybe add a truck image to the scene
    n "{cps=30}What is this truck?\nThis must be their bomb supply."
    n "{cps=30}That's [boss] in the window inside that cabin!"
    n "{cps=30}Shit, I only have 1 bullet, and there are too many of them inside."

    menu:
        "What to do"

        "Try to kill [boss]":
            n "{cps=30}Thats it! I'm going in to end it"
            scene bodyguards
            if devils:
                j "{cps=45}Oh look, its the thief's little friend"
                j "{cps=40}That's sweet."
                n "{cps=25}yo ... your.. your time is up!"
                j "{cps=40}HE'S ARMED! STOP HIM!!"
            else:
                f "{cps=45}Oh look, its the thief's little friend"
                f "{cps=40}That's sweet."
                n "{cps=25}yo ... your.. your time is up!"
                f "{cps=40}HE'S ARMED! STOP HIM!!"

            scene bg black with kill
            centered "{size=+50}{color=#F72C00}{cps=20}You and [boss] died" with dissolve
            jump dead


        "Destroy their supply":
            n "{cps=30}I'll shoot thier bomb supply! \n That will hurt them"
            scene bg black with flash
            n "{cps=45}Thay are coming out! I gotta go fast!"
            scene bg motel
            #jump first_guy
            #add SOUNDS

       # "Steal the truck":
        #    "You steal the truck"

jump second_mission

label dead:
