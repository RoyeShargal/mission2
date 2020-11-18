label final_fight:
    scene bg motel
    "{cps=35}You call your men and tell them to meet you at the entrance to the [gang] territory.
     You have waited long enough, it's time to end this."
    if devils:
        scene bg devils
    else:
        scene bg ghosts
