from manim import *
from manim.opengl import *
from reactive_manim import *
import manimpango
import math
from colour import Color
from tools import Tools
from constants import Constants as C

config.disable_caching = True
config.frame_size = (1080,1920)
config.frame_width = 8
config.frame_height = 14.22

# color , fill_opacity , stroke_width
class ArithmeticSumShort(Scene):
    def construct(self):
        Square.set_default(
            fill_color=RED,
            fill_opacity = 0.9, 
            stroke_opacity = 1, 
            stroke_color = WHITE, 
            stroke_width = 2
            )
        Rectangle.set_default(
            fill_color=BLUE,
            fill_opacity = 0.9, 
            stroke_opacity = 1, 
            stroke_color = WHITE, 
            stroke_width = 2
            )
        a = VGroup(
            Square(side_length = 0.5), 
            Text("a", color=WHITE, font_size = 20, weight = BOLD, slant=ITALIC)
            )
        d = VGroup(
            Rectangle(width=0.8, height=0.5), 
            Text("d", color=WHITE, font_size = 20, weight = BOLD, slant=ITALIC)
            )
        
        # TITLE
        title = Text("Sum of arithmetic progression", font_size = 32, color = BLUE).to_edge(UP, buff = 1.5)
        self.add(title)
        
        # SUBTITLE
        sum = MathTex('S_4', '~=~', 'a', '~+~' , '(a + d)', '~+~', '(a + 2d)', '~+~', '(a+3d)', font_size=36, color = YELLOW)\
                .next_to(title, 3.2 * DOWN)
        sum[0].set_color(WHITE)
        sum[1].set_color(WHITE)
        sum[3].set_color(WHITE)
        sum[5].set_color(WHITE)
        sum[7].set_color(WHITE)
        
        for i in [2, 4, 6, 8]:
            self.add(sum[i])
        self.wait(2)
        for i in [0, 1, 3, 5, 7]:
            self = Tools.add_with_click_pen(self, sum[i])
            self.wait(0.4)
        gap = 0.6
        a1 = a.copy()
        a2 = a.copy().next_to(a1, gap * DOWN)
        a3 = a.copy().next_to(a2, gap * DOWN)
        a4 = a.copy().next_to(a3, gap * DOWN)
        d21 = d.copy().next_to(a2, gap * RIGHT)
        d31 = d.copy().next_to(a3, gap * RIGHT)
        d32 = d.copy().next_to(d31, gap * RIGHT)
        d41 = d.copy().next_to(a4, gap * RIGHT)
        d42 = d.copy().next_to(d41, gap * RIGHT)
        d43 = d.copy().next_to(d42, gap * RIGHT)
        
        G1 = VGroup(a1, a2, a3, a4, d21, d31, d32, d41, d42, d43).next_to(sum, 5 * DOWN)
        G1A = VGroup(a1, a2, a3, a4)
        G1D = VGroup(d21, d31, d32, d41, d42, d43)
        S4str = MathTex("S_4 =", font_size = 40).next_to(G1, 3 * LEFT)
        
        # CREATE GROUP 1
        self = Tools.transform_with_pen_clikc(self, sum[0], S4str, 0.5, 0.8)
        self = Tools.transform_with_move(self, sum[2], a1, 0.5, 0.8)
        self = Tools.transform_with_move(self, sum[4], VGroup(a2, d21), 0.5, 0.8)
        self = Tools.transform_with_move(self, sum[6], VGroup(a3, d31, d32), 0.5, 0.8)
        self = Tools.transform_with_move(self, sum[8], VGroup(a4, d41, d42, d43), 0.5, 0.8)
        
        # COPY 
        plus = Text("+", font_size = 40, weight = BOLD).next_to(G1, RIGHT)
        G2 = G1.copy().next_to(G1, 2 * DOWN)
        self = Tools.add_with_click_pen(self, plus, 1)
        self = Tools.transform_with_pen_clikc(self, G1.copy(), G2, 1, 1)
        S4str2 = MathTex("2 \cdot S_4 =", font_size = 40).next_to(G1, 3 * LEFT)
        self = Tools.transform_with_pen_clikc(self, S4str, S4str2, 1, 1)
        self.remove(S4str)
        self = Tools.delete_with_sound(self, plus, 1)
        
        # REARANGE
        G2A = VGroup(G2[0], G2[1], G2[2], G2[3])
        G2D = VGroup(G2[4], G2[5], G2[6], G2[7], G2[8], G2[9])
        G2AM = G2A.copy().next_to(G1, gap * LEFT)
        self = Tools.move(self, G2A, G2AM, 2, 1.5)
        
        self.play(Rotate(G2D, PI), run_time = 1.2)
        for e in G2D:
             e[1].rotate(PI)
        G2DM = G2D.copy().shift(a1.get_critical_point(UR) - G2D.get_critical_point(UL)).shift(0.15 * RIGHT)
        self = Tools.move_with_clik(self, G2D, G2DM, 1, 1.5)
        self.remove(G2D)
        self.remove(G2A)
        groupVisible = VGroup(S4str2, G1A, G1D, G2AM, G2DM, a1, a2, a3, a4, d21, d31, d32)
        self.play(groupVisible.animate().move_to(ORIGIN).shift(0.8 * UP))
        
        # BRACKET 1
        line1 = Line(groupVisible[3].get_critical_point(DL), groupVisible[1].get_critical_point(DR)).set_color(ORANGE)
        b1 = Brace(line1)
        b1Text = VGroup(MathTex("2 \cdot 4", font_size = 32), a.copy().scale(0.7)).arrange(RIGHT).next_to(b1, DOWN)
        self.add(b1)
        self = Tools.add_with_click_pen(self, b1Text, 1)
        
        # BRACKET 2
        self.wait(1)
        line2 = Line(G1[7].get_critical_point(DL), G1[9].get_critical_point(DR)).set_color(ORANGE)
        b2 = Brace(line2)
        b2Text = VGroup(MathTex("4 \cdot (4-1)", font_size = 32), d.copy().scale(0.7) ).arrange(RIGHT).next_to(b2, DOWN)
        self.add(b2)
        self = Tools.add_with_click_pen(self, b2Text, 1)
        
        # FORMULA TRANSFORMTION
        two, four, a, d, n, dot = MathTex("2", "4", "a", "d", "n", "\\cdot",)
        n.set_color(ORANGE)
        a.set_color(BLUE)
        d.set_color(BLUE)
        two1 = two.copy()
        four1 = four.copy()
        four2 = four.copy()
        S4 = MathTex("S", "_", "4")
        SN = MathTex("S",  "_", "n")
        SN[2].set_color(BLUE)
        
        # 2 * S4 = 2 * 4 * a + 4(4-1)d
        tex = MathTex([two, S4], "=", [ [two1, dot, four, dot, a], "+", [four1, "(", four2, "-", "1", ")", d ]], font_size = 42).shift(3.2 * DOWN)
        self = Tools.move_with_clik(self, groupVisible[0].copy(), tex[0], 1.5, 0.5)
        self.add(tex[1])
        self = Tools.move_with_clik(self, b1Text.copy(), tex[2][0], 1, 0.5)
        self.add(tex[2][1])
        self = Tools.move_with_clik(self, b2Text.copy(), tex[2][2], 1, 0.5)
        self.remove(self.mobjects[-1])
        self.remove(self.mobjects[-1])
        self.remove(self.mobjects[-1])
        self.remove(self.mobjects[-1])
        self.remove(self.mobjects[-1])
        self.remove(self.mobjects[-1])
        self.remove(self.mobjects[-1])
        self.add(tex).wait(1)
        
        # S4 = (2 * 4 * a)/2 + (4(4-1)d)/2
        tex.LHS = S4
        tex.RHS = [ 
                   Fraction([ two1, dot, four, dot, a ], two.pop()), 
                   "+", 
                   Fraction([four1, "(", four2, "-", "1", ")", d ], "2")
                   ]
        self.play(TransformInStages.progress(tex), run_time = 2)
        
        # S4 = 4 * a + (4(4-1)d)/2
        self.wait(1)
        tex.RHS = [ [four, dot, a] , "+", Fraction([four1, "(", four2, "-", "1", ")", d ], "2") ]
        self.play(TransformInStages.progress(tex), run_time = 2)

        # Sn = n * a + (n(n-1)d)/2
        tex.LHS[2] = n
        tex.RHS[0][0] = n
        tex.RHS[2].numerator[0] = n
        tex.RHS[2].numerator[2] = n
        self.play(TransformInStages.progress(tex), run_time = 1.5)
        self.wait(1)
        
        # BOX
        box = SurroundingRectangle(tex, color=YELLOW, buff=0.2, fill_opacity = 0.0, stroke_color = YELLOW)
        self = Tools.create_with_sound(self, box, 0, 0.6)
        self.wait(3)
        