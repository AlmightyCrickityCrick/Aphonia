default is_game_over = False

init python:
    import pygame

    class GameField(renpy.Displayable):

        def __init__(self):
            super(GameField,self).__init__()
            self.bara = im.FactorScale("bar.png",0.18)
            self.indicator = im.FactorScale("indicator.png",0.063)
            self.indicator_position = 810
            self.is_venire = True
            self.punct_oprire = 0
            self.width = 1920
            self.height = 1080
            self.is_win = False
            self.is_over = False

        def render(self, width, height, st, at):
            r = renpy.Render(self.width, self.height)
            if self.is_venire:
                self.indicator_position += 10
            else:
                self.indicator_position -= 10

            if self.indicator_position >= 1170:
                self.is_venire = False
            elif self.indicator_position <= 710:
                self.is_venire = True

            bara_element = renpy.render(self.bara, 487, 95, st, at)
            r.blit(bara_element, (710,200))
            indicator_bara = renpy.render(self.indicator, 45, 95, st, at)
            r.blit(indicator_bara, (self.indicator_position,200))

            renpy.redraw(self, 0)
            return r

        def event(self, ev, x, y, st):
            pass

screen bar_minigame:
    default field = GameField()
    add field

label minigame:
    call screen bar_minigame
    if is_win == True:
        "Task Completed"
    else:
        "Try again"

