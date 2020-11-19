define lana = Character("Lana", color="#8d3ab0", what_color="#8d3ab0", what_prefix = '"', what_suffix = '"')

label first_member:
    scene bg forest
    show lana
    lana "{cps=35}I saw what you did."
    n "{cps=35}I don't know what you're talking about..."
    lana "{cps=35}It's ok, I have been spying on the [gang] for a while."
    lana "{cps=35}they are hiding money in [boss]'s cabin. I can help you fight them, if I get to keep the money."
    n "{cps=35}Sounds good, we will keep in touch."
    "Lana joined your gang." with dissolve
    jump second_mission
