default is_game_over = False
default is_win = False
default nr_wins = 0

define gui.text_color = '#402000'

init python:
    import pygame

    class GameField(renpy.Displayable):

        def __init__(self):
            super(GameField,self).__init__()
            self.bara = im.FactorScale("bar.png",0.18)
            self.indicator = im.FactorScale("indicator.png",0.063)
            self.emissioner = im.FactorScale("bec1.png",0.5)
            self.indicator_position = 810
            self.is_venire = True
            self.punct_oprire = 0
            self.width = 1920
            self.height = 1080
            self.is_win = False
            self.is_over = False
            self.indicator_movement = 5

        def render(self, width, height, st, at):
            r = renpy.Render(self.width, self.height)
            if self.is_venire:
                self.indicator_position += self.indicator_movement
            else:
                self.indicator_position -= self.indicator_movement

            if self.indicator_position >= 1170:
                self.is_venire = False
            elif self.indicator_position <= 710:
                self.is_venire = True

            text_indication = Text(f"Press the red button.")
            text_element = renpy.render(text_indication, 200, 200, st + 1, at + 1)
            r.blit(text_element, (100, 100))

            mouse_x, mouse_y = renpy.get_mouse_pos()
            mouse_text = Text(f"Mouse: x={mouse_x}, y={mouse_y}", size=28, color="#FFFFFF")
            mouse_render = renpy.render(mouse_text, 300, 50, st, at)
            r.blit(mouse_render, (100, 50))

            emiss = renpy.render(self.emissioner,896,896,st,at)
            r.blit(emiss, (485,360))
            bara_element = renpy.render(self.bara, 487, 95, st, at)
            r.blit(bara_element, (710,200))
            indicator_bara = renpy.render(self.indicator, 45, 95, st, at)
            r.blit(indicator_bara, (self.indicator_position,200))

            renpy.redraw(self, 0)
            return r

        def change_bulb(self):
            if globals() ['nr_wins'] == 1:
                self.emissioner = im.FactorScale("bec2.png",0.5)
            elif globals() ['nr_wins'] == 2:
                self.emissioner = im.FactorScale("bec3.png",0.5)
            

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONDOWN:
                x1, y1 = 704, 594
                x2, y2 = 868, 680
                
                if x1 <= x <= x2 and y1 <= y <= y2:
                    self.punct_oprire = self.indicator_position
                    if self.punct_oprire > 105 and self.punct_oprire < 1061:
                        self.is_win = True
                        globals() ['is_win'] = self.is_win
                        globals() ['nr_wins'] += 1
                        self.indicator_movement += 5
                        self.change_bulb()
                    else:
                        self.is_win = False
                        self.is_over = True

            if globals() ['nr_wins'] >= 3:
                self.is_over = True
                return self.is_over
            elif self.is_over:
                return self.is_over
            else:
                raise renpy.IgnoreEvent()


screen bar_minigame:
    default field = GameField()
    add field          



label minigame:
    call screen bar_minigame
    if nr_wins == 3:
        "Task Completed"
    else:
        "Try again"
        $ nr_wins = 0
        jump minigame

