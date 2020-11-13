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

    scene bg motel
    show screen stats

    n "Where is my gun?? I am going kill them!"

    if devils:
        scene bg devils
    else:
        scene bg ghosts

    #Maybe add a truck image to the scene
    n "What is this truck?\nThis must be their bomb supply."
    n "That's [boss] in the window inside that cabin!"
    n "Shit, I only have 1 bullet, and there are too many of them."

    menu:
        "What to do"

        "Try to kill [boss]":
            "death"

        "Destroy their supply":
            "You shoot the truck"
            #FLASH STUFF AND SOUNDS

        "Steal the truck":
            "You steal the truck"

jump second_mission