label chose_devils:

    show albert_flip at left
    scene bg devils
    a "{cps=35}That's Julian, their boss."
    #show julian and Albert
    j "{cps=35}Albert! where is my money? Did you really think you could steal from me and live?"
    a "{cps=4}...{nw}"
    play sound "gunshot.mp3"
    hide albert_flip with kill
    "{b}Julian pulls out his gun, puts it to Albert’s head and pulls the trigger.\n" with kill
    j "{cps=35}Get his friend out of here!"
    #maybe change screen here
    n "{size=+5}I will make him pay for this." with dissolve
    jump first_mission

label chose_ghosts:

    scene bg ghosts
    #show Frank and Albert
    show albert_flip at left
    "{cps=35}Three men come out of the woods and surround you."
    show frank at right
    a "{cps=35}That's Frank, their boss."
    a "{cps=35}I'm sorry I stole from you, what can I do to make it right?"
    f "{cps=35}This isn't personal Albert, if we let you live, everyone will steal from us"
    "{cps=35}He puts his hand inside his jacket, you and Albert run to the car."
    play sound "gunshot.mp3"
    hide albert_flip with kill
    "You hear a gunshot and see Albert fall to the ground" with kill
    "{cps=35}When you turn around the woods are empty once again."
    n "{size=+5}I will make him pay for this." with dissolve
    hide frank
    jump first_mission

label chose_fight:

    show albert
    scene bg house
    "{cps=35}You get to Albert's house and go to the phone to call for help,
    Albert is staring out of the window, he is terrified."
    play sound "sniper.mp3"
    hide albert with kill
    "You hear a loud gunshot, see the window breaking and Albert falling to the ground." with kill
    "{cps=35}You run to Albert, but he is already dead."
    n "{cps=35}This must have been one of the gangs."
    n "{size=+5}I will make them pay for this." with dissolve

    menu:
        "who do you go after first?"

        "Go after the devils first.":
            $ devils = True

        "Go after the ghosts first.":
            $ ghosts = True

    jump first_mission
