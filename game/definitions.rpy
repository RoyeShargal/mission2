#characters
define a = Character("Albert", color="#0e64e6", what_color="#0e64e6", what_prefix = '"', what_suffix = '"')
define j = Character("Julian", color="#995f03", what_color="#995f03", what_prefix = '"', what_suffix = '"')
define f = Character("Frank", color="#d48506", what_color="#d48506", what_prefix = '"', what_suffix = '"')
define n = Character("[name]", color="#F72C00", what_color="#F72C00", what_prefix = '"', what_suffix = '"')
define boss = Character("[boss]")
define other_boss = Character("[other_boss]")
define gang = Character("[gang]")
define other_gang = Character("[other_gang]")
image bg black = "#000"

#Image resizing
image bg room = im.Scale("bg room.png", 1920, 1080, bilinear=True)
image bg devils= im.Scale("bg devils.png", 1920, 1080, bilinear=True)
image bg ghosts= im.Scale("bg ghosts.png", 1920, 1080, bilinear=True)
image bg diner= im.Scale("bg diner.png", 1920, 1080, bilinear=True)
image bg dinerParking= im.Scale("bg dinerParking.png", 1920, 1080, bilinear=True)
image bg forest= im.Scale("bg forest.png", 1920, 1080, bilinear=True)
image bg motel= im.Scale("bg motel.png", 1920, 1080, bilinear=True)

#Booleans
default ghosts = False
default devils = False
default chose_fight = False
default stole_drugs = False

#Transitions
define flash = Fade(0.1, 0.0, 0.1, color="#fff")
define kill = Fade(0.5, 0.0, 1, color="#b00000")

#Stats
define health = 2
define money = 0
define attack = 1
define defence = 1

define honor = 20 #Invisible, every bad action reduces honor and good ones increase it
                    #Can tell the player how he played at the end.

define endings_discovered = 0 #If there is a way to save stats between games(shown after ending)
