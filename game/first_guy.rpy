define lana = Character("Lana", color="#8d3ab0", what_color="#8d3ab0", what_prefix = '"', what_suffix = '"')

label first_guy:
    scene bg forest
    show lana
    lana "{cps=40}I saw what you did."
    n "{cps=20}I don't know what you're talking about..."
    #add reason for spying on the gang
    lana "{cps=35}It's ok, I have been spying on the [gang] for a while, I can help you fight them."
    n "{cps=30}Good, we will keep in touch."
    "Lana joined your gang." with dissolve
    jump second_mission
