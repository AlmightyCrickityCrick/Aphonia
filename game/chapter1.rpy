

label base:

scene room with Dissolve(2.0)

"The sound of the base's ventilation system hummed overhead, a dull mechanical
rhythm that filled the silence of the morning."
"The light filtering through the
metal blinds was cold and sterile, casting pale lines on the floor."
"The team was already awake, though no one spoke much."
"The air was thick with the
unspoken weight of their mission {w}— and the growing awareness that there were
only two days left to clean up the sectors."

show james at Position(xpos = 1200, ypos = 980)

"James stood in the central corridor of the base, {w}his arms folded as he looked
over the small screen that displayed their remaining energy levels and
available credits."
james "Some echo-credits. {w}Enough for a single battery. {w}Enough for one
sector."
hide james

show lira at Position(xpos = 500, ypos = 1050)

"Lira leaned against the doorway, arms crossed."
"She looked tired. {w} Or maybe just wary."
lira "Well {w}what's the plan, Commander?"
hide lira

#спрат под вопросом
#show Darin
"Darin chimed in from the other room, voice light"
darin "I vote for going shopping.{w} Who doesn't love retail therapy in a fallout
zone?"
 
"Kael, already checking his worn utility belt, muttered"
show Kael at Position(xpos = 1200, ypos = 980)
"We can’t clean anything without batteries. So it’s not really a vote, is
it."
menu:
    "Where should we go first?":
        "Shop"
        #block of code to run
        "Sector":
            scene virelia with dissolve  

        #block of code to run
    
            
        








