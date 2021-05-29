from manim import *
import math

class UnitSinCos(Scene):
    def construct(self):

        grid = NumberPlane().set_opacity(0.3).scale(2)

        radius = 2
        circle = Circle(radius).set_color(WHITE)

        angle = math.pi
        dot = Dot(point=[radius*math.cos(angle), radius*math.sin(angle), 0]).set_color(GRAY_B)

        radiusU = VMobject()
        cosU = VMobject()
        sinU = VMobject()
        
        sin = DecimalNumber(0, num_decimal_places=3, include_sign=True, unit=None).move_to([-3.5, 2, 0]).set_color(YELLOW)
        sin.add_updater(lambda d: d.set_value(dot.get_center()[1]/2.0))
        cos = DecimalNumber(0, num_decimal_places=3, include_sign=True, unit=None).move_to([-3.5, 1, 0]).set_color(RED)
        cos.add_updater(lambda d: d.set_value(dot.get_center()[0]/2.0))
        sinText = Text("Sen = ").set_color(YELLOW).next_to(sin, LEFT)
        cosText = Text("Cos = ").set_color(RED).next_to(cos, LEFT)

        self.add(grid, circle, cosU, sinU, radiusU, dot, sin, cos, sinText, cosText)
        radiusU.add_updater(lambda x: x.become(Line(ORIGIN, dot.get_center()).set_color(GRAY)))
        cosU.add_updater(lambda x: x.become(Line(ORIGIN, [dot.get_center()[0], 0, 0]).set_color(RED)))
        sinU.add_updater(lambda x: x.become(Line([dot.get_center()[0], 0, 0], [dot.get_center()[0], dot.get_center()[1], 0]).set_color(YELLOW)))
        self.play(MoveAlongPath(dot, circle), rate_func=linear, run_time=10)
