screen stats(text_size = 20):
    vbox:
        xalign 0.1
        yalign 0.1
        spacing 5
        #text "{color=#fc0324}[health]HP"
        text "{color=#4dff3d}$[money]"
        #text "{color=#ffffff}[attack]/5 attack"
        #text "{color=#ffffff}[defence]/5 defence"
        #text "{color=#30fff8}[fame] fame"

screen ending_credits(text_size = 100, font = "ARMY RUST.ttf"):
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 50
        text "{color=#912119}{u}Game Designers:" xalign 0.5
        text "{color=#912119}Niv Nissanov" xalign 0.5
        text "{color=#912119}Nitsan Caduri" xalign 0.5
        text "{color=#912119}Roye Shargal" xalign 0.5
        text "{color=#912119}{u}Graphic Designer:" xalign 0.5
        text "{color=#912119}Hagar Nahari" xalign 0.5
