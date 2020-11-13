define jason = Character("Jason", color="#b021ae", what_color="#b021ae",image = "jason")
define q = Character("????", color="#b021ae", what_color="#b021ae", image = "q")
default isJason = False

define blackFlash = Fade(0.1, 0.0, 2, color="#000000")

label second_mission:
    scene bg motel
    #play knock knock sound
    n "{cps=40}Who is this???{w=1}"

    scene darkdoor with blackFlash
    show q
    q "{cps=30}Are you %(name)s?"

    menu:
        "Yes":
            n "{cps=30}Yes, who are you and what are you doing here?"

        "No, go Away":
            q "{cps=30}I KNOW ITS YOU! cut the bullshit!"
            
    q "{cps=30}I heard about you and wanted to offer you a job."
    q "{cps=30}I will give you $10,000 to assassinate German Joe, what do you say?"

    menu:
        "Ok, give me the details":
            q "{cps=30}He will be in the local cafe tomorrow at 19:00, \n look for the guy with the white striped shirt"
            n "{cps=30}No problem, give me half now and half after his dead"
            q "{cps=30}Sure."
            $ money += 5000
            "Money increesed by $5000"
            scene bg black
            centered "{size=+50}{color=#ffffff}The next day"
            jump chose_kill

        "No, I have values":
            q "{cps=30}Values ah.."
            q "{cps=30}Good exactly what I was looking for.."
            hide q
            show jason
            jason "{cps=30}I'm Jason, nice to meet you. \n and I'm here to join you and help you defet The [gang]"
            $ Jason = True
            n "{cps=35}Awesome, I was looking for another partner"
            #jump after misson 2
            


label chose_kill:
    scene kill_joe
    n "{cps=40}Here he is!"
    menu:
        n "This is nerveracking"

        "Pull the trigger":
            n "{cps=35}Ok I can do this.{w=2}"
            #play shoot sound
            scene bg black with kill
            $ money += 5000
            centered "{size=+50}{color=#ffffff}Money incresed by $5000"
            #jump after misson 2

        "I can't do this":
            n "{cps=30}At least I have the $5000"
            #jump after misson 2