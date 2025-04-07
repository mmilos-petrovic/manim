import manimpango
from manim import *
from colour import Color
from tools import Tools

# color , fill_opacity , stroke_width
class Equilat(Scene):
    def construct(self):
        title = Text("Equilateral triangle height formula", font_size=42, color=BLUE).to_corner(UL)
        self.add(title)

        triangle = Triangle(color = BLUE, fill_opacity = 0.5, stroke_width = 10).scale(2.1).shift(4 * LEFT + 0.5 * DOWN)
        triangle_shif = [5,0,0]
        text_shift = [7,0.8,1]
        points = {}
        labels = {}
        
        points['dl']  = Dot(triangle.get_critical_point(DL))
        points['dr']  = Dot(triangle.get_critical_point(DR))
        points['up']  = Dot(triangle.get_critical_point(UP))
        points['d']  = Dot(triangle.get_critical_point(DOWN))
        labels["a1"] = Tools.twoPointLabel(points['dl'], points['dr'], "a")
        labels["a2"] = Tools.twoPointLabel(points['dr'], points['up'], "a")
        labels["a3"] = Tools.twoPointLabel(points['dl'], points['up'], "a", True)
        labels["ahalf"] = Tools.twoPointLabel(points['d'], points['dl'], "a/2", True)
        h = Line(points['d'].get_center(), points['up'].get_center(), color = ORANGE, stroke_width = 10)
        labels["h"] = Tools.lineLabel(h, "h")
        right_triangle = Polygon(points['dl'].get_center(), points['up'].get_center(), points['d'].get_center(), 
                                 color = YELLOW, fill_opacity = 0.5, stroke_width = 10)
        
        self.wait(1)
        self.play(Create(triangle))
        self.wait(1)
        self.play(Create(h))
        self.wait(1)
        self.add(*points.values())
        self.wait(1)
        self.add(*labels.values())
        self.wait(1)
        self.play(Create(right_triangle))
        
        self.play(
            AnimationGroup(
                right_triangle.animate.shift(triangle_shif),
                VGroup(
                    labels['h'].copy(),
                    labels['ahalf'].copy(),
                    labels['a3'].copy()
                    ).animate.shift(triangle_shif),
                lag_ratio = 0.1
            )
        )
        self.wait(1)
        text1=MathTex("a^2","=","\\left(\\frac{ a }{ 2 }\\right)^2","+","h^2", font_size = 42).next_to(points['up']).shift(text_shift)
        self.play(Write(text1))
        framebox1a = SurroundingRectangle(text1[0], buff = 0.2, color=GREEN, stroke_width = 5)
        framebox1b = SurroundingRectangle(labels['a3'].copy().shift(triangle_shif), buff = 0.2, color = GREEN, stroke_width = 5)
        framebox2a = SurroundingRectangle(text1[2], buff = 0.2, color = GREEN, stroke_width = 5)
        framebox2b = SurroundingRectangle(labels['ahalf'].copy().shift(triangle_shif), buff = 0.2, color = GREEN, stroke_width = 5)
        framebox3a = SurroundingRectangle(text1[4], buff = 0.2, color = GREEN, stroke_width = 5)
        framebox3b = SurroundingRectangle(labels['h'].copy().shift(triangle_shif), buff = 0.2, color = GREEN, stroke_width = 5)
        self.play(
            Create(framebox1a), Create(framebox1b),
        )
        self.wait(1)
        self.play(
            Transform(framebox1a, framebox2a),
            Transform(framebox1b, framebox2b),
            run_time = 3
        )
        self.wait(1)
        self.play(
            Transform(framebox1a, framebox3a),
            Transform(framebox1b, framebox3b),
            run_time = 3
        )
        self.wait(1)
        self.remove(framebox1a, framebox1b)
        self.wait(1)
        text2 = MathTex(r"a^2 = \frac{a^2}{4} + h^2", font_size=42, color = WHITE).next_to(text1, DOWN)
        self.play(Create(text2))
        self.wait(1)
        text3 = MathTex(r"h^2 = a^2 - \frac{a^2}{4}", font_size=42, color = WHITE).next_to(text2, DOWN)
        self.play(Create(text3))
        self.wait(1)
        text4 = MathTex(r"h^2 = \frac{3 \cdot a^2}{4}", font_size=42, color = WHITE).next_to(text3, DOWN)
        self.play(Create(text4))
        self.wait(1)
        text5 = MathTex(r"h = \frac{a \sqrt{3}}{2}", font_size=42, color = WHITE).next_to(text4, DOWN)
        self.play(Create(text5))
        self.wait(1)
        box = SurroundingRectangle(text5, color=YELLOW, buff=0.2) 
        self.play(Create(box))
        self.wait(8)
        

