import manimpango
from manim import *
from colour import Color



def twoPointLabel(dot1: Dot, dot2: Dot, label: str, changeDirection = False) -> MathTex:
    line = Line(dot1, dot2)
    return lineLabel(line, label, changeDirection)


def lineLabel(line: Line, label: str, changeDirection = False) -> MathTex:
    label = MathTex(label, font_size = 46).move_to(midpoint(line.end, line.start))
    vecX = round(line.copy().rotate(PI/2).get_unit_vector()[0],2)
    vecY = round(line.copy().rotate(PI/2).get_unit_vector()[1],2)
    if changeDirection:
        vecX = -vecX
        vecY = -vecY
    label.shift(LEFT * vecX * 0.3 + DOWN * vecY * 0.3)
    return label

# color , fill_opacity , stroke_width
class Equilat2(Scene):
    def construct(self):
        triangle = Triangle(color = BLUE, fill_opacity = 0.5, stroke_width = 10).scale(2.1).shift(4 * LEFT)
        triangle_shif = [5,0,1]
        text_shif = [7,1,1]
        points = {}
        labels = {}
        
        points['dl']  = Dot(triangle.get_critical_point(DL))
        points['dr']  = Dot(triangle.get_critical_point(DR))
        points['up']  = Dot(triangle.get_critical_point(UP))
        points['d']  = Dot(triangle.get_critical_point(DOWN))
        labels["a1"] = twoPointLabel(points['dl'], points['dr'], "a")
        labels["a2"] = twoPointLabel(points['dr'], points['up'], "a")
        labels["a3"] = twoPointLabel(points['dl'], points['up'], "a", True)
        labels["ahalf"] = twoPointLabel(points['d'], points['dl'], "a/2", True)
        h = Line(points['d'].get_center(), points['up'].get_center(), color = ORANGE, stroke_width = 10)
        labels["h"] = lineLabel(h, "h")

        right_triangle = Polygon(points['dl'].get_center(), points['up'].get_center(), points['d'].get_center(), 
                                 color = YELLOW, fill_opacity = 0.5, stroke_width = 10)
        
        title = Text("Equilateral triangle height formula", font_size=42, color=BLUE).to_corner(UL)
        self.add(title)

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
            right_triangle.animate.shift(triangle_shif),
            labels['h'].copy().animate.shift(triangle_shif),
            labels['ahalf'].copy().animate.shift(triangle_shif),   
            labels['a3'].copy().animate.shift(triangle_shif)    
        )
        self.wait(1)
        text1=MathTex("a^2","=","\\left(\\frac{ a }{ 2 }\\right)^2","+","h^2", font_size = 42).next_to(points['up']).shift(text_shif)
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
        


class AnimationMechanisms(Scene):
    def construct(self):
        c = Circle()
        
        c.generate_target()
        c.target.set_fill(color=GREEN, opacity=0.5)
        c.target.shift(2*RIGHT + UP).scale(0.5)
        
        self.add(c)
        self.wait()
        self.play(MoveToTarget(c))
        
        s = Square()
        s.save_state()
        self.play(FadeIn(s))
        self.play(s.animate.set_color(PURPLE).set_opacity(0.5).shift(2*LEFT).scale(3))
        self.play(s.animate.shift(5*DOWN).rotate(PI/4))
        self.wait()
        self.play(Restore(s), run_time=2)

        self.wait()

class Test(Scene):
    def construct(self):
        squares = VGroup(*[Square(color = Color(hue = j/20, saturation = 1, luminance = 0.5), fill_opacity=0.8) for j in range(20)])
        squares.arrange_in_grid(4, 5).scale(0.5)
        self.play(AnimationGroup(*[FadeIn(s) for s in squares], lag_ratio=0.15))

class BasicAnimations(Scene):
    def construct(self):
        polys = VGroup(
            *[RegularPolygon(n = 6, radius = 1, color = Color(hue = j/5, saturation = 1, luminance = 0.5), fill_opacity = 0.5) for j in range(5)]
        ).arrange(RIGHT)
        self.play(DrawBorderThenFill(polys), run_time = 3)
        self.play(
            Rotate(polys[0], PI, rate_func = lambda t:t),
            Rotate(polys[1], PI, rate_func = lambda t: np.sin(t*PI)),
            Rotate(polys[2], PI, rate_func = smooth),
            run_time = 3
        )
        self.wait(3)