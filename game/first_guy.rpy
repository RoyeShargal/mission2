define dan = Character("Dan", color="#8d3ab0", what_color="#8d3ab0", what_prefix = '"', what_suffix = '"')


label first_guy:
    scene bg forest
    dan "{cps=40}I saw what you did."
    n "{cps=20}I don't know what you're talking about..."
    dan "{cps=35}It's ok I want to hurt the [gang] too"
    n "{cps=30}I'm looking for revange, will you assist me?"
    dan "{cps=30}Yes, I want them dead"
    n "{cps=30}Good, we will keep in touch"
    jump second_mission
