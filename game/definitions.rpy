#characters
define a = Character("Albert", color="#0e64e6", what_color="#0e64e6", what_prefix = '"', what_suffix = '"')
define j = Character("Julian", color="#995f03", what_color="#995f03", what_prefix = '"', what_suffix = '"')
define f = Character("Frank", color="#d48506", what_color="#d48506", what_prefix = '"', what_suffix = '"')
define n = Character("[name]", color="#F72C00", what_color="#F72C00", what_prefix = '"', what_suffix = '"')
define boss = Character("[boss]", color="#ff530f", what_color="#ff530f", what_prefix = '"', what_suffix = '"')
define police = Character("Police", color="#0e64e6", what_color="#0e64e6", what_prefix = '"', what_suffix = '"')
define other_boss = Character("[other_boss]", color="#ff530f", what_color="#ff530f", what_prefix = '"', what_suffix = '"')
define driver = Character("Driver", color="#0e64e6", what_color="#0e64e6", what_prefix = '"', what_suffix = '"')
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
image frank = im.Scale("frank.png",1500, 833, bilinear=True)
image bg black = "#000"

#Booleans
default ghosts = False
default devils = False
default chose_fight = False
default stole_drugs = False

#Transitions
define flash = Fade(0.1, 0.0, 0.1, color="#fff")
define kill = Fade(0.4, 0.0, 1, color="#b00000")
define blue = Fade(0.2, 0.0, 0.2, color="#5e9cff")
define red = Fade(0.2, 0.0, 0.2, color="#ff2445")

#Stats
define health = 2
define money = 0
define attack = 1
define defence = 1
define ending = 1

define honor = 20 #Invisible, every bad action reduces honor and good ones increase it
                    #Can tell the player how he played at the end.

define fame = 0 #can increase as you do missions, to explain how people have heard about you

define endings_discovered = 0 #If there is a way to save stats between games(shown after ending)
