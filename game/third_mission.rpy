#define jason = Character("Jason", color="#b021ae", what_color="#b021ae",image = "jason")
#define f = Character("????", color="#b021ae", what_color="#b021ae", image = "frank")
define spy = Character("SPY", color="#b021ae", image="spy.png")

label third_mission:
    scene bg black
    #centered "{size=+50}{color=#ffffff}MISSION #3"
    #centered "{size=+50}{color=#ffffff}The Spy."
    #scene spied_car_pic
    #play sound "horror.wav"
    $ renpy.pause(1.0)
    scene black_car
    n "{cps=30}I think I saw a car, a black one, wandering by the street,\nfor a bit too long."
    n  "Someone is definitely spying on me"

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
        n "{cps=30}What should I do?"

        "Put a gps tracker the vehicle":
            n "{cps=30}The car is the black SKODA, the windows are shadowed."
            n "{cps=30}This is your moment, all you have been practicing for, you got this."

            lana "{cps=25}Rumors say that when putting a gps tracker, there are 50 precent of peing your pants, becareful."
            jump chose_gps

        "Kidnap the spy":
            lana "{cps=30}Once the deed is done, there will be no regrets."
            n "{cps=30}Regrets are not what we're here for, huh?"
            show spy
            spy "{cps=30}Am i dreaming, or noises are being heared?"
            n "{cps=30}Walk slowly, he might be listening"
            spy "{cps=30} LEAVE ME ALONE!, YOU DON'T KNOW WHO I AM!"
            n "{cps=35} That's right, this is not the reason i am here for."
            jump chose_kidnap
            #jump after misson 2
label chose_gps:
    #maybe change
    n"{cps=20}The tracker has been successfully planted"
    n"{cps=20}Good Job."
    "+1,500$" with dissolve
    $ money+=1500
    #END

label chose_kidnap:
    scene intero
    spy "{cps=20}I am prepared to be tortured, no information will be getting out of my mouth, FUCKER."
    menu:
        "Kill":
            n"{cps=10}Alright then,\nUp you go."
            play sound "gunshot.mp3"
            n"{cps=20}Mission failed,\n-5 Fame."
            $ fame -=5

        "Interrogate":
            n"{cps=20}Lets play a small game.\nPick a Number from 1-6,\nI am serious."
            $ num = renpy.input("","",allow="123456")
            if  num>=3:
                n"{cps=10}Seems like your lucky day lad.\nWait for my call,\nWe will be in touch when I need you."
                $ fame+=10
                "+10 Fame" with dissolve
            else:
                n"{cps=10}Not today,\nSorry."
                play sound "gunshot.mp3"
            jump final_fight


        #END
