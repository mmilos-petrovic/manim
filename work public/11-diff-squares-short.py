from manim import *
from manim.opengl import *
import manimpango
import math
from colour import Color
from constants import Constants as C
from tools import Tools

config.disable_caching = True
config.frame_size = (1080,1920)
config.frame_width = 8
config.frame_height = 14.22


# color , fill_opacity , stroke_width
class DiffSquaresShort(Scene):
    def construct(self):

        # INTRO
        title1 = Text("Difference of squares", font_size = 32, color = BLUE).to_edge(UP, buff = 0.7)
        title2 = Text("The simple visual proof", font_size = 28).next_to(title1, DOWN)
        self.add(title1)
        Tools.add_with_click_silent(self, title2, 1)
        
        a = 3.2
        b = 1.3
        
        # SQUARE A
        A = RoundedRectangle(
                   corner_radius=0.02,
                   width = a,
                   height = a,
                   fill_opacity = 0.9, 
                   fill_color=RED,
                   stroke_opacity = 1, 
                   stroke_color = WHITE, 
                   stroke_width = 7).shift(0 * DOWN)
        self = Tools.create_with_sound(self, A, 0.5, 0.5, 1)
        
        
        # BRACKET A
        line = Line(A.get_critical_point(DR), A.get_critical_point(UR))
        b1 = Brace(line, direction = line.copy().rotate(-PI/2).get_unit_vector(), buff = 0.7)
        b1text = b1.get_text("A").set_color(WHITE)
        self.play(Create(b1), run_time = 1)
        self = Tools.add_with_click_silent(self, b1text, 0)
        
        # A square + move
        A2 = MathTex(r"A^2", color = WHITE, font_size = 50)
        self = Tools.add_with_click_silent(self, A2, 1.5)
        self.wait(1)
        self.play(A2.animate().shift(2.5 * LEFT + 4 * UP))
        Tools.sound(C.SOUND_CLICK_SILENT, 0)
        minus = MathTex("-", font_size=48).next_to(A2)
        self.wait(1)
        
        # SQUARE B
        B = RoundedRectangle(
                   corner_radius=0.02,
                   width = b,
                   height = b,
                   fill_opacity = 0.9, 
                   fill_color=BLUE,
                   stroke_opacity = 1, 
                   stroke_color = WHITE, 
                   stroke_width = 7)
        B.shift(A.get_critical_point(DL) - B.get_critical_point(DL))
        self = Tools.create_with_sound(self, B, 0, 0.9, 1)
        
        #Bracket  B
        line3 = Line(B.get_critical_point(DL), B.get_critical_point(UL))
        b3 = Brace(line3, direction = line.copy().rotate(PI/2).get_unit_vector(), buff = 0.7)
        b3text = b3.get_text("B").set_color(WHITE)
        self.add(b3)
        self = Tools.add_with_click_silent(self, b3text, 1)
                
        # B Square move
        B2 = MathTex("B^2", color = WHITE, font_size = 50).shift(B.get_center())
        self = Tools.add_with_click_silent(self, B2, 1.5)
        self.wait(0.5)
        self.play(B2.animate().next_to(minus, RIGHT))
        Tools.sound(C.SOUND_CLICK_SILENT, 0)
        
        # # Bracket A - B
        line4 = Line(B.get_critical_point(UL), A.get_critical_point(UL))
        b4 = Brace(line4, direction = line4.copy().rotate(PI/2).get_unit_vector(), buff = 0.7)
        b4text = b4.get_text("A-B").set_color(WHITE)
        self.play(Create(b4), run_time = 0.5)
        self = Tools.add_with_click_silent(self, b4text, 1)
        
        # Bracket B top
        line5 = Line(A.get_critical_point(UL), A.get_critical_point(UL) + (b, 0 ,0))
        b5 = Brace(line5, direction = line5.copy().rotate(PI/2).get_unit_vector(), buff = 0.7)
        b5text = b5.get_text("B").set_color(WHITE)
        self.wait(0.5)
        self.play(Create(b5), run_time = 0.5)
        self = Tools.add_with_click_silent(self, b5text, 1)
        
        points = [
            A.get_critical_point(UR), 
            A.get_critical_point(DR),
            B.get_critical_point(DR),
            B.get_critical_point(UR),
            B.get_critical_point(UL),
            A.get_critical_point(UL),
        ]
        lShape = Polygon(*points, 
                   fill_opacity = 0.9, 
                   fill_color=RED,
                   stroke_opacity = 1, 
                   stroke_color = WHITE, 
                   stroke_width = 7)
        self.add(lShape)
        self = Tools.delete_withot_sound(self, A, 1)
        self = Tools.delete_with_sound(self, B, 1, 0)
        self.play(Create(minus))
        
        dotLine = DashedLine(B.get_critical_point(UR), B.get_critical_point(UR) + (0, a-b, 0),
                             color = WHITE,
                             dash_length=0.2,
                             z_index = 10)
        self = Tools.create_with_sound(self, dotLine, 1, 0.5, 0.5)
        
        self.wait(2)
        rightRect = Polygon(
            A.get_critical_point(UR),
            A.get_critical_point(DR),
            B.get_critical_point(DR),
            B.get_critical_point(UR) + (0, a-b, 0),
            fill_opacity = 0.9, 
            fill_color=RED,
            stroke_opacity = 1, 
            stroke_color = WHITE, 
            stroke_width = 7
            )
        diff = Difference(lShape, rightRect,
                          fill_opacity = 0.9, 
                          fill_color=RED,
                          stroke_opacity = 1, 
                          stroke_color = WHITE, 
                          stroke_width = 7,
                          )
        self.add(diff)
        self.remove(lShape)
        
        rotationCenter = Dot(B.get_critical_point(UR) + (0, a-b, 0) + ((a-b)/2, -(a-b)/2, 0))
        group = VGroup(rightRect, b1, b1text)
        self.play(group.animate().rotate(PI/2, about_point = rotationCenter.get_center()))
        Tools.sound(C.SOUND_CLICK_LOUD, 0)
        self.play(group[2].animate().rotate(-PI/2))
        self.play(FadeOut(b3), FadeOut(b3text))
         
        groupRemoveBrackest = VGroup(b5, group[1])
        line6 = Line(A.get_critical_point(UL), group[0].get_critical_point(UR))
        b6 = Brace(line6, direction = line6.copy().rotate(PI/2).get_unit_vector(), buff = 0.7)
        
        createBrackets = b6
        self.play(Transform(groupRemoveBrackest, createBrackets), run_time = 1.3)
        plus = MathTex("+", font_size = 50).move_to(0.5 * b5text.get_center() + 0.5 * group[2].get_center())
        self = Tools.add_with_click_silent(self, plus, 2)
        
        jednako = MathTex("=", font_size = 50).next_to(B2, RIGHT)
        self = Tools.add_with_click_silent(self, jednako, 1)
        
        self.wait(1)
        aMinusBrez = MathTex("(A-B)", font_size = 50).next_to(jednako, RIGHT)
        self = Tools.sound(self, C.SOUND_CLICK_LOUD, 1)
        self.play(ReplacementTransform(b4text.copy(), aMinusBrez), run_time = 1.2)
        self.wait(1)
        aPlusBrez = MathTex("(A+B)", font_size = 50).next_to(aMinusBrez, RIGHT)
        self = Tools.sound(self, C.SOUND_CLICK_LOUD, 1)
        self.play(ReplacementTransform(VGroup(b5text, plus, group[2]).copy(), aPlusBrez), run_time = 1.2)
        
        
        group2 = VGroup(A2, minus, B2, jednako, aMinusBrez, aPlusBrez)
        self.play(group2.animate().shift(LEFT * 0.5))
        box = SurroundingRectangle(group2, color = YELLOW, stroke_width = 3, buff= 0.2, corner_radius=0.05)
        self = Tools.sound(self, C.SOUND_CREATING, 0.5)
        self.play(Create(box))
        group2.set_color(YELLOW)
        self.wait(2)
        
        
        
        

       
        

