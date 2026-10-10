from manim import *
import math
class Mesopotamia(Scene):
    def construct(self):
        points=[
            1*LEFT+3*UP,
            2.5*RIGHT+3*UP,
            3*RIGHT+3*DOWN,
            2.5*LEFT+3*DOWN,
            1*LEFT+3*UP
        ]
        line=VMobject()
        line.set_points_as_corners(points)
        self.add(line)
        angle=Arc(1,0,math.radians(75)).shift(3*DOWN+2.5*LEFT)
        alpha=Typst("$alpha$",font_size=70).shift(2*LEFT,2.7*DOWN)
        crown=Typst("$a$",font_size=70).shift(3.3*UP+RIGHT)
        self.add(angle,alpha,crown)
        