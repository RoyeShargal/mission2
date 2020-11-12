#characters
define a = Character("Albert", color="#0e64e6", what_color="#0e64e6")
define j = Character("Julian", color="#995f03", what_color="#995f03")
define f = Character("Frank", color="#d48506", what_color="#d48506")
define n = Character("[name]", color="#F72C00", what_color="#F72C00")
define boss = Character("[boss]")
define other_boss = Character("[other_boss]")
define gang = Character("[gang]")
define other_gang = Character("[other_gang]")
image bg black = "#000"

#Booleans
default ghosts = False
default devils = False
default chose_fight = False
default stole_drugs = False

#Transitions
define flash = Fade(0.1, 0.0, 0.1, color="#fff")
define kill = Fade(0.1, 0.0, 2, color="#b00000")
