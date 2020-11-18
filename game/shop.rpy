label shopexp:
    "You are ready to fight [boss], and heard a rumour about a black market that sells illegal weapons."
    "You follow the lead and arrive at a dark house, you knock on the door, it opens and a dark figure leads you inside."
    q "Welcome, everything here is for sale, do not try to steal and keep this place a secret."
    scene darkdoor with blackFlash
    show q

label shop:
    #maybe add an option to steal an item??
    #even keep the option but after a certain amount of items stolen you get caught and killed
    #(shopkeeper gets more suspicious every time)

    #maybe start the game with some money so the shop isn't useless to some people
    #Also maybe reduce amount of money earned from mission 2 since with 10000$ you can probably buy everything

    #options for items:
    #1. camouflage suit
    #2. mines
    #3. flash/smoke grenade
    #4. bulletproof vest
    #5. stun gun
    #6. first aid kit (maybe one of your teammates gets hurt and you can help him, or to treat yourself)
    #7. silencer
    #8. enlist the shopkeeper's help in the final fight

    menu:
        "buy item 1":
            if money >= 10000:
                #get the item
                " "
            else:
                "You don't have enough money"
                jump shop

        "buy item 2":
            if money >= 5000:
                #get the item
                " "
            else:
                "You don't have enough money"
                jump shop

        "buy item 3":
            if money >= 5000:
                #get the item
                " "
            else:
                "You don't have enough money"
                jump shop

        "finish shopping":
            jump final_fight
