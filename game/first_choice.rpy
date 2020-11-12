label chose_devils:

    scene bg devils

    #maybe explain Julian is the devils boss
    j "{cps=30}Albert! where is my money? Did you really think you could steal from me and live?"
    a "{cps=4}...{nw}"
    "{b}Julian pulls out his gun, puts it to Albert’s head and pulls the trigger.\n" with kill
    j "{cps=30}Get his friend out of here!"
    #maybe change screen here
    n "{cps=30}{b}{size=+5}I will make him pay for this."

    jump first_mission

label chose_ghosts:

    scene bg ghosts

    "{cps=30}Three men come out of the woods and surround you"
    a "{cps=30}I'm sorry I stole from you, what can I do to make it right?"
    f "{cps=30}This isn't personal Albert, if we let you live, everyone will steal from us"
    "{cps=30}He puts his hand inside his jacket, you and Albert run to the car"
    "{b}You hear a gunshot and see Albert falling to the ground" with kill
    "{cps=30}When you turn around the woods are empty once again"
    n "{cps=30}{b}{size=+5}I will make him pay for this."

    jump first_mission

label chose_fight:

    #scene bg house

    "You get to Albert's house and call your brother to ask for help,\n
    Albert is staring out of the window, he is terrified"
    scene bg black with flash
    "The lights turn off"
    #scene bg house
    "When they turn back on, you see Albert lying dead on the ground"
    "There is a note beside him, it reads: You don't steal from us and live"
    n "{cps=30}{b}{size=+5}I will make them pay for this."

    menu:
        "who do you go after first"

        "Go after the devils first":
            $ devils = True

        "Go after the ghosts first":
            $ ghosts = True

    jump first_mission
