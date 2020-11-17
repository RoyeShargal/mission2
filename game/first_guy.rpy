define dan = Character("Dan", color="#8d3ab0", what_color="#8d3ab0", what_prefix = '"', what_suffix = '"')

label first_guy:
    scene bg forest
    dan "{cps=40}I saw what you did."
    n "{cps=20}I don't know what you're talking about..."
    dan "{cps=35}It's ok, the [gang] have been threatning my family so I deliver their bombs. I want to hurt them too."
    n "{cps=30}If you get into this, there is no going back, are you sure?"
    dan "{cps=30}Yes, I want them dead."
    n "{cps=30}Good, we will keep in touch."
    "Dan joined your gang." with dissolve
    jump second_mission
