#characters
define a = Character("Albert", color="#0e64e6", what_color="#0e64e6",image="albert_side", what_prefix = '"', what_suffix = '"')
define j = Character("Julian", color="#995f03", what_color="#995f03", what_prefix = '"', what_suffix = '"')
define f = Character("Frank", color="#d48506", what_color="#d48506",image="frank_side", what_prefix = '"', what_suffix = '"')
define n = Character("[name]", color="#F72C00", what_color="#F72C00", what_prefix = '"', what_suffix = '"')
define boss = Character("[boss]", color="#ff530f", what_color="#ff530f",image="boss_side", what_prefix = '"', what_suffix = '"')
define police = Character("Police", color="#0e64e6", what_color="#0e64e6", what_prefix = '"', what_suffix = '"')
define other_boss = Character("[other_boss]", color="#ff530f", what_color="#ff530f", what_prefix = '"', what_suffix = '"')
define driver = Character("Driver", color="#0e64e6", what_color="#0e64e6", what_prefix = '"', what_suffix = '"')
define bodyguard = Character("Bodyguard", color="#0e64e6", what_color="#0e64e6",image="bodyguard_side", what_prefix = '"', what_suffix = '"')

define gang = "gang"
define other_gang = "other_gang"

#Image resizing
image bg room = im.Scale("bg room.png", 1920, 1080, bilinear=True)
image bg devils= im.Scale("bg devils.png", 1920, 1080, bilinear=True)
image bg ghosts= im.Scale("bg ghosts.png", 1920, 1080, bilinear=True)
image bg diner= im.Scale("bg diner.png", 1920, 1080, bilinear=True)
image bg dinerParking= im.Scale("bg dinerParking.png", 1920, 1080, bilinear=True)
image bg forest= im.Scale("bg forest.png", 1920, 1080, bilinear=True)
image bg motel= im.Scale("bg motel.png", 1920, 1080, bilinear=True)
image bg house= im.Scale("bg house.png", 1920, 1080, bilinear=True)
image bg sniper= im.Scale("bg sniper.png", 1920, 1080, bilinear=True)
image bg truck= im.Scale("bg truck.png", 1920, 1080, bilinear=True)
image bg cabin= im.Scale("bg cabin.png", 1920, 1080, bilinear=True)
image frank = im.Scale("frank.png",1500, 833, bilinear=True)
image side frank_side:
    "frank side.png"
    xzoom -1
image firstGuy = im.Scale("first_guy.png",805, 1209, bilinear=True)
image albert = im.Scale("Albert.png", 600, 823, bilinear=True)
image side albert_side:
    "Albert side.png"
    xzoom -1
image albert_flip:
    im.Scale("Albert.png", 600, 823, bilinear=True)
    xzoom -1
image lana = im.Scale("lana.png", 300, 798, bilinear=True)
image side lana_side = "lana side.png"
image q = im.Scale("q.png", 230, 813, bilinear=True)
image side q_side = "q side.png"
image jason = im.Scale("jason.png", 230, 813, bilinear=True)
image side jason_side = "jason side.png"
image side bodyguard_side:
    "bodyguard side"
image bg black = "#000"

#Booleans
default ghosts = False
default devils = False
default chose_fight = False
default stole_drugs = False
default info = False

#Transitions
define flash = Fade(0.1, 0.0, 0.1, color="#fff")
define kill = Fade(0.4, 0.0, 1, color="#b00000")
define shot = Fade(0.3, 0.0, 0.3, color="#fff")

#Stats
define money = 0
define ending = 1
