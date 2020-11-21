#define jason = Character("Jason", color="#b021ae", what_color="#b021ae",image = "jason")
#define f = Character("????", color="#b021ae", what_color="#b021ae", image = "frank")
define spy = Character("SPY", color="#b021ae", image="spy_side")
image side spy_side = "spy side.png"

label third_mission:
    #scene bg black
    #centered "{size=+50}{color=#ffffff}MISSION #3"
    #centered "{size=+50}{color=#ffffff}The Spy."
    #scene spied_car_pic
    #play sound "horror.wav"
    #$ renpy.pause(1.0)
    scene black_car
    n "{cps=35}I think I saw a car, a black one, wandering by the street for a bit too long."
    n  "{cps=35}Someone is definitely spying on me."

    #menu:
    #    "Yes":
    #        n "{cps=30}Let's hope you are brave enough."
    #
    #    "No, too busy":
    #        n "{cps=30}See you in hell."
    #        n "{cps=15}Mission Failed."
    #
    #n "{cps=30} Take into consideration these concequences, being spied isn't lovely."

    menu:
        n "{cps=35}What should I do?"

        "Put a GPS tracker on the vehicle":
            "{cps=35}The car is the black SKODA, the windows are shadowed."
            #"{cps=35}This is your moment, all you have been practicing for, you got this."
            #lana "{cps=35}Rumors say that when putting a gps tracker, there are 50 percent of peing your pants, be careful."
            lana "{cps=35}Be careful, whoever is inside could be dangerous."
            jump chose_gps

        "Kidnap the spy":
            lana "{cps=35}Once the deed is done, there will be no regrets."
            n "{cps=35}Regrets are not what we're here for, huh?"
            #show spy
            spy "{cps=35}Am i dreaming, or can I hear noises?"
            n "{cps=35}Walk slowly, he might be listening."
            spy "{cps=35} LEAVE ME ALONE!, YOU DON'T KNOW WHO I AM!"
            #n "{cps=35} That's right, this is not the reason i am here for."
            jump chose_kidnap

label chose_gps:
    "{cps=35}You successfully planted the tracker."
    "{cps=35}After a few hours of waiting, the spy drives away, he stops when he gets to the [gang] territory."
    n "{cps=35}They know we are coming after them, we have to act now."
    jump final_fight

label chose_kidnap:
    scene intero
    spy "{cps=35}I am prepared to be tortured, you won't get any information out of me, FUCKER."
    menu:
        "Kill the spy":
            n"{cps=20}Alright then, up you go."
            play sound "gunshot.mp3"
            "The spy's body falls to the floor, he won't be spying on you again." with kill
            jump final_fight

        "Interrogate":
            n "{cps=35}Lets play a small game.\nPick a Number from 1-6.\nI am serious."
            $ num = renpy.input("","",allow="123456")
            if  num>=3:
                n "{cps=35}Seems like your lucky day lad.\nWait for my call, We will be in touch when we need you."
            else:
                n"{cps=35}Not today.\nSorry."
                play sound "gunshot.mp3"
                with kill
            jump final_fight
