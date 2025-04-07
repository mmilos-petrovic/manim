import manimpango
from manim import *
import manimpango
from colour import Color
from tools import Tools


# color , fill_opacity , stroke_width
class Arithmetic(Scene):
    def construct(self):
        title = Text("Find n-th term of a series", font_size=42, color=BLUE).to_corner(UL)
        self.add(title)

        distance = 8 * RIGHT
        txt1 = Text("2", font_size=48, color = GREEN)
        txt2 = Text("5", font_size=48, color = GREEN).next_to(txt1, distance)
        txt3 = Text("8", font_size=48, color = GREEN).next_to(txt2, distance)
        txt4 = Text("11", font_size=48, color = GREEN).next_to(txt3, distance)
        txt5 = Text("14", font_size=48, color = GREEN).next_to(txt4, distance)

        sequence = VGroup(txt1, txt2, txt3, txt4, txt5).move_to(ORIGIN).shift(1.5 * UP)
        
        triPlus = Text("+3", font_size=32)
        frame = SurroundingRectangle(triPlus, color=BLUE, buff=0.2, corner_radius=0.1) 
        box = VGroup(triPlus, frame)
        
        box1 = box.copy().next_to(sequence[0], 2*RIGHT).shift(0.5 * UP)
        box2 = box.copy().next_to(sequence[1], 2*RIGHT).shift(0.5 * UP)
        box3 = box.copy().next_to(sequence[2], 2*RIGHT).shift(0.5 * UP)
        box4 = box.copy().next_to(sequence[3], 2*RIGHT).shift(0.5 * UP)

        self.add(sequence)
        self.play(AnimationGroup(Create(box1), Create(box2), Create(box3), Create(box4), lag_ratio=0.9), run_time = 5)
        self.wait(1)

        title2 = MathTex("\\text{All distances = 3}","\\Longrightarrow", "\\text{This sequence is arithmetic.}", font_size=32, color=GREEN).next_to(sequence, DOWN * 1.5)
        title2[2].set_color(BLUE)
        self.play(AnimationGroup(
                    Create(title2[0]),  
                    Create(title2[1]), 
                    Create(title2[2]), lag_ratio=0.8),
                  run_time = 2
            )
        self.wait(0.5)
        self.play(Create(SurroundingRectangle(title2[2], color=BLUE, buff=0.1, corner_radius=0.1) ))

        self.wait(1)
        txt6 = MathTex(r"a_1 = ", font_size=42, color = GREEN).to_edge(LEFT, buff=1).shift(1.1 * DOWN)
        self.add(txt6)
        a1 = MathTex(r"2", font_size=42, color = GREEN).next_to(txt6, RIGHT)
        self.play(Transform(txt1.copy(), a1))
        

        self.wait(1)
        txt7 = MathTex(r"d = ", font_size=42, color = BLUE).next_to(txt6, DOWN * 1.5)
        self.add(txt7)
        d =MathTex("3", font_size=42, color = BLUE).next_to(txt7)
        self.play(Transform(box1[0].copy(), d))
        
        self.wait(2)
        txt8 = Text(r"GENEREAL TERM", font_size=24, color = WHITE).to_edge(LEFT, buff= 5).shift(0.4 * DOWN)
        self.play(Indicate(txt8))
        eq1 = MathTex(r"a_n = ", r"a_1"," + ", "d","(n-1)", font_size=42, color = WHITE).next_to(txt6, RIGHT * 8).to_edge(LEFT, buff= 5)
        eq1[1].set_color(GREEN)
        eq1[3].set_color(BLUE)
        eq2 = MathTex(r"a_n = ", "2", " + ", "3\cdot", "(n-1)", font_size=42, color = WHITE).next_to(eq1, DOWN * 1.2).to_edge(LEFT, buff= 5)
        eq2[1].set_color(GREEN)
        eq2[3].set_color(BLUE)
        eq3 = MathTex(r"a_n = 2 + 3n-3", font_size=42, color = WHITE).next_to(eq2, DOWN * 1.2).to_edge(LEFT, buff= 5)
        eq4 = MathTex(r"a_n = -1 + 3n", font_size=42, color = WHITE).next_to(eq3, DOWN * 1.2).to_edge(LEFT, buff= 5)
        
        equations = [eq1, eq2, eq3, eq4]
        self.wait(1)
        self.add(equations[0].copy())
        for i in range(1, len(equations)):
            self.wait(0.8)
            self.add(equations[i-1].copy())
            self.play(TransformMatchingTex(equations[i-1], equations[i]), run_time = 2)
        self.wait(2)




