define jason = Character("Jason", color="#b021ae", what_color="#b021ae",image = "jason")
define q = Character("????", color="#b021ae", what_color="#b021ae", image = "q")
default isJason = False

define blackFlash = Fade(0.1, 0.0, 2, color="#000000")

label second_mission:
    scene bg black
    centered "{size=+50}{color=#ffffff}A few days later"
    scene bg motel
    play sound "knockknock.wav"
    $ renpy.pause(1.0)
    n "{cps=40}Who is this???{w=1}"

    scene darkdoor with blackFlash
    show q
    q "{cps=30}Are you %(name)s?"

    menu:
        "Yes":
            n "{cps=30}Yes, who are you and what are you doing here?"

        "No, go Away":
            q "{cps=30}I KNOW ITS YOU! cut the bullshit!"

    q "{cps=30}I heard about what you did to the [gang] and wanted to offer you a job."
    q "{cps=30}I will give you $10,000 to assassinate German Joe, what do you say?"

    menu:
        "Ok, give me the details":
            q "{cps=30}He will be in the local cafe tomorrow at 19:00,\nlook for the guy with the white striped shirt."
            scene bg black
            centered "{size=+50}{color=#ffffff}The next day"
            jump chose_kill

        "No, I have values":
            q "{cps=30}Values ah.."
            hide q
            show jason
            jason "{cps=30}I'm Jason, nice to meet you.\n I had to make sure you are not some ruthless killer."
            jason "{cps=30}I have been fighting the [gang] for months. I could help you beat them."
            $ Jason = True
            n "{cps=35}Good, I was looking for another partner."
            "Jason joined your gang." with dissolve
            #jump after misson 2
            jump third_mission

label chose_kill:
    scene bg sniper
    n "{cps=40}Here he is!"
    menu:
        n "This is nerveracking"

        "Pull the trigger":
            n "{cps=35}Ok I can do this.{w=2}"
            play sound "gunshot.mp3"
            scene bg black with kill
            scene bg motel
            show jason
            jason "{cps=35}I knew I could count on you."
            $ money += 10000
            "Money increased by $10000" with dissolve

        "I can't do this":
            scene bg motel
            show jason
            jason "{cps=35}What happened man?"
            n "{cps=35}I couldn't do it."
            jason "{cps=35}Then why the hell are you in this business anyway?"
            n "{cps=35}The [gang] killed my friend, I can't let them get away with it."
            jason "{cps=35}I respect that, I hate those sons of bitches too, if you wont get your hands dirty, this might help."
            "Earned tranquilizer gun" with dissolve

        #jump after misson 2
    jump third_mission

    jump ending_scene_2
