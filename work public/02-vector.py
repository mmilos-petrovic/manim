import manimpango
from manim import *


class Vector2(Scene):
    def construct(self):
        a = [3,0.5,0]
        b = [1,2,0]
        scaleFactor = 0.8
        ax = Axes(x_range=[-0.9, 10, 1], 
                  y_range=[-0.9, 6, 1], 
                  x_length = 10.9, 
                  y_length = 6.9, 
                  ).add_coordinates().scale(scaleFactor).to_edge(DOWN, buff = 0.2)
        
        title = MathTex(r"\text{Find } ~ 3 \cdot \vec{a} + 2 \cdot \vec{b}", font_size=42, color = WHITE).to_edge(UP)
        aVec = Arrow(buff = 0, 
                     start = ax.coords_to_point(0,0,0), 
                     end=ax.coords_to_point(a[0],a[1],0), 
                     color=BLUE, stroke_width = 5, 
                     z_index = 2,
                     max_tip_length_to_length_ratio=0.1)
        txtA = MathTex(r"\vec{a}", font_size=42, color = BLUE).move_to(ax.coords_to_point(1.2,0.5)).rotate(PI/12)
        aGroup = VGroup(aVec, txtA, z_index = 2,)

        bVec = Arrow(buff = 0, start = ax.coords_to_point(0,0,0), end=ax.coords_to_point(b[0],b[1],0), color=PURPLE, stroke_width = 5, max_tip_length_to_length_ratio=0.1)
        txtB = MathTex(r"\vec{b}", font_size=42, color = PURPLE).move_to(ax.coords_to_point(0.3,1.3))
        bGroup = VGroup(bVec, txtB)

        rez = Arrow(buff=0, z_index = 0, start = ax.coords_to_point(0,0,0), end = ax.coords_to_point(3*a[0] + 2*b[0], 3*a[1] + 2*b[1],0), stroke_width = 7, color = GREEN,  max_tip_length_to_length_ratio=0.03)
        rezTxt = MathTex(r"3\vec{a} + 2\vec{b}", font_size = 42, color = GREEN).move_to(ax.coords_to_point(5,3.2)).rotate(PI/6)

        self.add(title, ax, aGroup, bGroup)
        self.wait(1)
        self.play(aGroup.copy().animate.shift(1 * a[0] * scaleFactor * RIGHT, 1 * a[1] * scaleFactor * UP))
        self.play(aGroup.copy().animate.shift(2 * a[0] * scaleFactor * RIGHT, 2 * a[1] * scaleFactor * UP))
        self.play(bGroup.copy().animate.shift(1 * b[0] * scaleFactor * RIGHT, 1 * b[1] * scaleFactor * UP))
        self.wait(1)

        line1 = DashedLine(ax.coords_to_point(0,0,0), ax.coords_to_point(3*a[0],3*a[1],0), color = GREEN, stroke_width = 1)
        self.play(line1.animate.shift(2 * b[0] * scaleFactor * RIGHT, 2 * b[1] * scaleFactor * UP))
        self.wait(1)
        
        line2 = DashedLine(ax.coords_to_point(0,0,0), ax.coords_to_point(2*b[0],2*b[1],0), color = GREEN, stroke_width = 1)
        self.play(line2.animate.shift(3 * a[0] * scaleFactor * RIGHT, 3 * a[1] * scaleFactor * UP))
        self.wait(1)

        self.play(Create(rez))
        self.play(Write(rezTxt))

        self.wait(5)
    
        

