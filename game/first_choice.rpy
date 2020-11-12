label chose_devils:

    scene bg devils

    #maybe explain Julian is the devils boss
    j "{cps=30}Albert! where is my money? Did you really think you could steal from me and live?"
    a "{cps=4}...{nw}"
    "{b}Julian pulls out his gun, puts it to Albert’s head and pulls the trigger.\n" with kill
    j "{cps=30}Get his friend out of here!"
    n "{cps=30}{b}{size=+5}I will make him pay for this."

    jump first_mission

label chose_ghosts:

    scene bg ghosts


    jump first_mission

label chose_fight:

    #scene bg house


    jump first_mission
