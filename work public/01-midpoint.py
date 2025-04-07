import manimpango
from manim import *



class Midpoint(Scene):
    def construct(self):
        # objects
        ax = Axes(x_range=[-0.9, 7, 1], 
                  y_range=[-0.9, 6, 1], 
                  x_length = 7.9, 
                  y_length = 6.9, 
                  ).add_coordinates().scale(0.8).to_edge(LEFT, buff=0.5)
        dotA = Dot(ax.coords_to_point(1, 5), color=GREEN, radius=0.1, z_index = 2)
        dotB = Dot(ax.coords_to_point(7, 1), color=GREEN, radius=0.1, z_index = 2)
        mid = Dot(ax.coords_to_point(4, 3), color = RED_C, radius = 0.1, z_index = 2)
        line = Line(dotA.get_center(), dotB.get_center(), color = BLUE, stroke_width = 5)

        # text
        title = Text("How to find midpoint?", font_size=36, color=BLUE).to_corner(UL)
        txtA = MathTex(r"A(1,5)", font_size=32, color = GREEN).next_to(dotA, UP * 0.5)
        txtB = MathTex(r"B(7, 1)", font_size=32, color = GREEN).next_to(dotB, UR * 0.5)
        txtMid = MathTex(r"M(?,?)", font_size=32, color = RED_C).next_to(mid, UR * 0.5)

        # anim
        self.add(title)
        self.play(Write(ax), run_time = 1)
        self.wait(1)
        self.play(FadeIn(dotA), FadeIn(txtA), run_time = 0.5)
        self.play(FadeIn(dotB), FadeIn(txtB), run_time = 0.5)
        self.play(Write(line), run_time = 0.5)
        self.play(FadeIn(mid), FadeIn(txtMid), run_time = 0.5)
        self.wait(1)

        # solution
        text1 = Tex(r"$M \left( \dfrac{x_1+x_2}{2}, \dfrac{y_1+y_2}{2} \right)$", font_size=32, color = WHITE).to_edge(UR)
        text2 = Tex(r"$M \left( \dfrac{1+7}{2}, \dfrac{5+1}{2} \right)$", font_size=32, color = WHITE).next_to(text1, DOWN)
        text3 = Tex(r"$M \left( \dfrac{8}{2}, \dfrac{6}{2} \right)$", font_size=32, color = WHITE).next_to(text2, DOWN)
        text4 = Tex(r"$M \left( 4, 3 \right)$", font_size=32, color = WHITE).next_to(text3, DOWN)
        box = SurroundingRectangle(text4, color=YELLOW, buff=0.2) 
        text4box = VGroup(box, text4)

        # anim solution
        self.play(Write(text1), run_time = 0.5)
        self.wait(1)
        self.play(Write(text2), run_time = 1)
        self.wait(1)
        self.play(Write(text3), run_time = 1)
        self.wait(1)
        self.play(Indicate(text4box))
        mid.color = YELLOW
        self.play(FadeOut(txtMid),
                  text4box.copy().animate.next_to(mid, UR * 0.2),
                  run_time = 0.5
                  )
        self.wait(3)
    
    

