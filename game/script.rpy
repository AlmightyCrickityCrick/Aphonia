define gui.text_font = "SourceSansPro-Regular.ttf"

# define gui.text_color = '#402000'


define lira = Character("Lira", color = "#fff")
define kael = Character("Kael", color = "#fff")
define darin = Character("Darin", color = "#ffff")
define james = Character("James", color = "#fff")

image lira = im.FactorScale("lira.png",0.4)
image kael = im.FactorScale("kael.png",0.42)
image darin = im.FactorScale("darin.png", 1.7)
image james = im.FactorScale("james.png",0.34)

image center = im.Scale("bg_center.png",1920,1080)
image argon = im.Scale("bg_argon.png",1920,1080)
image virelia = im.Scale("bg_virelia.png",1920,1080)
image noctis = im.Scale("bg_noctis.png",1920,1080)
image room = im.Scale("bg_room.png",1920,1080)
image catastrophe = im.FactorScale("bg_catastrophe.png",1.25)
image darkness = im.Scale("bg_darkness.png",1920,1080)
image hall_kid = im.Scale("bg_lira_kid.png",1920,1080)

label start:
    jump prologue

    # call minigame

    # show lira at Position(xpos = 500, ypos = 1050)

    # show kael at Position(xpos = 1200, ypos = 980)

    # show james at Position(xpos = 1200, ypos = 980)

    # show darin at Position(xpos = 780, ypos = 990)

    # These display lines of dialogue.

    return
