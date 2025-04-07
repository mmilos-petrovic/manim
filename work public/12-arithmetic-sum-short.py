from manim import *
from manim.opengl import *
import manimpango
import math
from colour import Color
from tools import Tools
from constants import Constants as C

config.disable_caching = True
config.frame_size = (1080,1920)
config.frame_width = 8
config.frame_height = 14.22

def squareFun(a):
        return Square(side_length = a, 
                      stroke_color = GREEN, 
                      stroke_width = 2,
                      fill_color = GREEN_E, 
                      fill_opacity = 0.5)
    

def squarePack(n, a):
    rez = VGroup()
    for i in range(n):
        rez.add(squareFun(a))
    rez.arrange(UP, buff=0)
    return rez

# color , fill_opacity , stroke_width
class ArithmeticSumShort(Scene):
    def construct(self):
        
        title = Text("Sum of first n integers formula", font_size=28, color=BLUE).to_corner(UP).shift(DOWN)
        title2 = Text("Simple visual proff", font_size=25, color=WHITE).to_corner(UP).shift(1.8 * DOWN)
        self.add(title, title2)
        
        max = 5
        a = 0.5
        group1 = VGroup()
        one = MathTex("1")
        group1.add(one)
        for i in range(1, max):
            group1.add(MathTex("+"))
            group1.add(MathTex(i + 1))
        group1.arrange(0.5 * RIGHT).to_edge(UL, buff = 0.5).shift(4 * DOWN)
        
        # 1 - 6
        for i in range(max):
            self = Tools.add_with_click_silent(self, group1[2 * i], 0.3)

        # PLUSES
        for i in range(max - 1):
            self = Tools.add_with_click_short(self, group1[2 * i + 1], 0.2)
            self.wait(0.3)
        self.wait(0.5)
        
        # = ?
        equal = MathTex("=").next_to(group1, RIGHT)
        question = MathTex("?", color = RED).next_to(equal, RIGHT)
        self = Tools.add_with_click_silent(self, equal, 0.2)
        self = Tools.add_with_click_silent(self, question, 0.2)
        
        # CREATE SQUARES
        gSquares = VGroup()
        for i in range(max):
            sqPack = squarePack(i + 1, a).next_to(group1[2 * i], 7 * DOWN)
            gSquares.add(sqPack)
            self.play(Create(sqPack))
        self.wait(1)
        
        # MOVE SQUARES
        for i in range(1,max):
            self.play(
                gSquares[i].animate().shift(gSquares[i-1].get_critical_point(UR)-gSquares[i].get_critical_point(UL)),
                run_time = 0.8
                )
            self = Tools.sound(self,  C.SOUND_CLICK_SILENT, 0)

        # SQUARES ROTATE
        gSquares2 = gSquares.copy().set_fill_color(YELLOW)
        self.wait(1)
        self = Tools.sound(self, C.SOUND_MOVE, 1)
        self.play(gSquares2.animate.shift(RIGHT * 3), run_time = 1.5)
        for i in range(3):
            self.play(gSquares2.animate().rotate(PI/3), run_time = 0.5)   
        self.play(
            gSquares2.animate().shift(gSquares.get_critical_point(UL) - [0, a, 0]  - gSquares2.get_critical_point(UL)),
            run_time = 0.8
        )
        self = Tools.sound(self, C.SOUND_CLICK_LOUD, 0)
        
        #SHIFT BIG RECTANGLE
        g = VGroup(gSquares, gSquares2)
        self.play(g.animate().shift(0.8 * RIGHT), run_time = 1)
        
        #BRACE RIGHT
        braceLeft = BraceBetweenPoints(
              gSquares.get_critical_point(UL), 
              gSquares2.get_critical_point(DL),
              buff = 0.1)
        braceLeftStr = braceLeft.get_text("5 + 1", buff=-0.2).set_color(WHITE).rotate(PI/2)
        self.play(Create(braceLeft))
        self = Tools.add_with_click_silent(self, braceLeftStr, 0.5)
        
        #BRACE DOWN
        braceDown = BraceBetweenPoints(gSquares2.get_critical_point(DL), 
                                         gSquares2.get_critical_point(DR),
                                         buff = 0.5
                                         )
        braceDownStr = braceDown.get_text("5").set_color(WHITE)
        self.play(Create(braceDown))
        self = Tools.add_with_click_silent(self, braceDownStr, 0.5)
        
        
        equal2 = MathTex("=").next_to(gSquares, 2 * RIGHT).shift(0.2 * DOWN)
        Tools.add_with_click_silent(self, equal2, 1)
        sol1 = MathTex("5 \cdot ( 5 + 1 )").next_to(equal2, 2 * RIGHT)
        self.wait(1)
        self.play(Write(sol1))
        self.wait(1)
        
        # MOVE TO TOP
        sol2 = MathTex(r"\frac{ 5 \cdot (5 + 1)}{ 2 } ").next_to(equal2, RIGHT)
        self.play(
            AnimationGroup(
                gSquares2.animate().set_opacity(0.1),
                ReplacementTransform(sol1, sol2),
                lag_ratio = 0.5
            ),
            run_time = 2.5
            )
        self.play(FadeOut(question))
        self.play(FadeOut(equal2))
        self = Tools.sound(self, C.SOUND_CLICK_LOUD, 0.8)
        self.play(sol2.animate().next_to(equal, RIGHT), run_time = 1)
        self.wait(2)
        
        # MOVE RIGHT
        groupMove = VGroup(group1[8], equal, sol2)
        self.play(groupMove.animate().shift(1.2 * RIGHT), run_time = 1)
        
        # # ADD ...
        group1[8] = MathTex(r".\,.\,.\,+")
        self = Tools.create_with_sound(self,  group1[8].next_to(group1[7], 0.5 * RIGHT), 1, 0.3, 0.4)
        self.wait(1)
        
        # REPLACE N
        sol3 = MathTex(r"\frac{ n \cdot (n + 1)}{ 2 } ").next_to(equal, 0.5 *RIGHT)
        sol3[0][0].set_color(BLUE)
        sol3[0][3].set_color(BLUE)
        self.play(FadeOut(groupMove[0]), 
                  Create(MathTex("n", color = BLUE).next_to(group1[8], 0.5 * RIGHT)),
                  ReplacementTransform(sol2, sol3)
                  ) 
        self.wait(4)
        