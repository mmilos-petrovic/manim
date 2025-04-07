from manim import *
import manimpango
from colour import Color
from tools import Tools



# color , fill_opacity , stroke_width
class Complex(Scene):
    def construct(self):
        title = Text("Modulus , polar form, conjugate", font_size=36, color=BLUE).to_corner(UL, buff=0.2)
        self.add(title)

        ax = Axes(
            x_range=[-1.1, 6.1, 1],
            y_range=[-3.1, 3.1, 1],
            x_length=7,
            y_length=6,
            x_axis_config={"numbers_to_include": np.arange(-1, 7, 1)},
            y_axis_config={"numbers_to_include": np.arange(-3, 4, 1)},
            tips=False,
        ).shift(DOWN * 0.7 + 3 * LEFT)
        axLabels = ax.get_axis_labels(
            x_label=Tex("Re"), 
            y_label=Tex(r"Im")
        )
        self.add(ax, axLabels)

        z = Dot(ax.coords_to_point(4, 2), color=GREEN, radius=0.1, z_index = 2)
        zLabel = MathTex("z = 4 + 2 i", font_size=36).next_to(z, UR * 0.5)
        origin = Dot(ax.coords_to_point(0, 0), color = WHITE)
        lineZ = Line(z.get_center(), origin.get_center(), color = GREEN_A, stroke_width = 4)
        self.add(z, zLabel, lineZ)

        title1 = MathTex(" \\text{ Modulus }", font_size = 32, color = BLUE).to_edge(19 * LEFT).shift(2.5 * UP)
        formula1 = MathTex("|z| = \\sqrt{ a^2 + b^2 }", font_size = 32).next_to(title1, DOWN).to_edge(20 * LEFT)
        formula2 = MathTex("|z| =\\sqrt{ 4^2 + 2^2 }", font_size = 32).next_to(formula1, DOWN).to_edge(20 * LEFT)
        formula3 = MathTex("|z| = \\sqrt{ 20 }", font_size = 32).next_to(formula2, DOWN).to_edge(20 * LEFT)
        
        self.play(Write(title1))
        self.wait(1)
        self.play(Write(formula1))
        self.wait(1)
        self.play(Write(formula2))
        self.wait(1)
        self.play(Write(formula3))
        self.wait(1)

        box = SurroundingRectangle(formula3, color=BLUE, buff=0.2) 
        self.play(Create(box))
        group = VGroup(formula3.copy(), box.copy())
        self.play(group.animate.shift(LEFT * 7.3), run_time = 1)
        self.play(group.animate.rotate(PI/7).scale(0.8), run_time = 1)
        self.wait(1)

        one = Dot(ax.coords_to_point(1, 0), color = WHITE)
        lineOrigin = Line(one.get_center(), origin.get_center())
        alpha = Angle(lineOrigin, lineZ, radius=2, quadrant = (-1,-1), other_angle=False, color = RED)
        value = MathTex(r"26^{\circ}", font_size = 32, color = RED).next_to(alpha,RIGHT * 0.1)
        self.play(Create(alpha), Write(value))

        title2 = MathTex(" \\text{ Polar Form }", font_size = 32, color = BLUE).next_to(formula3, 2.5*DOWN).to_edge(19 * LEFT)
        formula4 = MathTex(r"z = |z| \left( \sin \alpha + i \cos \alpha \right)", font_size = 32).next_to(title2, 1.5*DOWN).to_edge(20 * LEFT)
        formula5 = MathTex(r"z = \sqrt{ 20 } \left( \sin 26^{\circ} + i \cos 26^{\circ} \right)", font_size = 32).next_to(formula4, DOWN).to_edge(20 * LEFT)
        
        self.play(Write(title2))
        self.wait(1)
        self.play(Write(formula4))
        self.wait(1)
        self.play(Write(formula5))
        self.wait(1)

        box2 = SurroundingRectangle(formula5, color=BLUE, buff=0.2) 
        self.play(Create(box2))
        self.play(formula5.copy().animate.shift(4.2*LEFT + 2.5*UP))
        self.wait(1)

        zConj = Dot(ax.coords_to_point(4, -2), color=RED, radius=0.1, z_index = 2)
        zConjLabel = MathTex(" \\overline{ z } = 4  - 2 i", font_size=36, color=RED,).next_to(zConj, DR * 0.5)
        self.play(z.copy().animate.shift(zConj.get_center() - z.get_center()), run_time = 2)
        self.add(zConj)
        self.play(Create(Line(origin.get_center(), zConj.get_center(), color = RED)))
        self.add(zConjLabel)
        self.wait(4)

        
       
        

        

        
