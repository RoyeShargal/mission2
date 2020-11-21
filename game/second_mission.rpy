define jason = Character("Jason", color="#b021ae", what_color="#b021ae",image = "jason_side", what_prefix = '"', what_suffix = '"')
define q = Character("????", color="#b021ae", what_color="#b021ae", image = "q_side", what_prefix = '"', what_suffix = '"')
default Jason = False
define blackFlash = Fade(0.1, 0.0, 2, color="#000000")

label second_mission:
    scene bg black
    centered "{size=+50}{color=#ffffff}A few days later" with dissolve
    scene bg motel
    play sound "knockknock.wav"
    $ renpy.pause(1.0)
    n "{cps=35}Who is this???"

    "{cps=35}The lights turn off, you hear the door open"
    scene darkdoor with blackFlash
    show q
    q "{cps=35}Are you %(name)s?"

    menu:
        "Yes":
            n "{cps=35}Yes, who are you and what are you doing here?"

        "No, go Away":
            q "{cps=35}I KNOW ITS YOU! cut the bullshit!"

    q "{cps=35}I'm Lana's friend, she told me what you did to the [gang]. I might have a job for you."
    q "{cps=35}I will give you $10,000 to assassinate German Joe, what do you say?"

    menu:
        "Ok, give me the details":
            q "{cps=35}He will be in the local cafe tomorrow at 19:00,\nlook for the guy with the white striped shirt."
            scene bg black
            centered "{size=+50}{color=#ffffff}The next day" with dissolve
            jump chose_kill

        "No, I have values":
            q "{cps=35}Values ah.."
            hide q
            show jason
            jason "{cps=35}I'm Jason, nice to meet you.\n I had to make sure you are not some ruthless killer."
            jason "{cps=35}I have been fighting the [gang] with Lana for months. I can help you defeat them."
            $ Jason = True
            n "{cps=35}Good, I was looking for another partner."
            "Jason joined your gang." with dissolve
            jump third_mission

label chose_kill:
    scene bg sniper
    n "{cps=35}Here he is!"
    menu:
        n "{cps=35}This is nerveracking"

        "Pull the trigger":
            n "{cps=35}Ok I can do this."
            play sound "sniperre.mp3"
            scene bg black with kill
            scene darkdoor
            show q
            q "{cps=35}I knew I could count on you."
            $ money += 10000
            "Money increased by $10000" with dissolve

        "I can't do this":
            scene motel
            show jason
            q "{cps=35}What happened man?"
            n "{cps=35}I couldn't do it."
            q "{cps=35}Then why the hell are you in this business anyway?"
            n "{cps=35}The [gang] killed my friend, I can't just let them get away with it."
            hide q
            show jason
            jason "{cps=35}I respect that, I'm Jason by the way, I hate those sons of bitches too, if you ever need backup, let me know."
            $ Jason = True
            "Jason joined your gang." with dissolve

    scene bg black
    centered "{size=+50}{color=#ffffff}The day after" with dissolve
    jump third_mission
