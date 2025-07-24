
define lira = Character("Lira", color = "#fff")
image lira = im.FactorScale("lira.png",0.4)
image argon = im.Scale("bg_argon.png",1920,1080)

label start:

    scene argon

    show lira at Position(xpos = 500, ypos = 1050)

    # These display lines of dialogue.

    lira "You've created a new Ren'Py game."

    lira "Once you add a story, pictures, and music, you can release it to the world!"

    return
