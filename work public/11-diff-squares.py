from manim import *
from manim.opengl import *
import manimpango
import math
from colour import Color
from constants import Constants as C
from tools import Tools
config.disable_caching = True


# color , fill_opacity , stroke_width
class DiffSquares(Scene):
    
    def add_with_click(self, mobject, w = 0.0):
        if w > 0:
            self.wait(w)
        self.sound(C.SOUND_CLICK_SILENT, 0.2)
        self.add(mobject)

    def delete_with_sound(self, mobject, w = 0.0):
        if w > 0:
            self.wait(w)
        self.sound(C.SOUND_DELETE, 0.2)
        self.remove(mobject)
                
    def sound(self, sound_alias, time = 0.0):
        if sound_alias == C.SOUND_CLICK_LOUD:
            self.add_sound('sounds/click1.mp3', time_offset = time)
        if sound_alias == C.SOUND_CLICK_SILENT:
            self.add_sound('sounds/click2.mp3', time_offset = time)
        if sound_alias == C.SOUND_CREATED:
            self.add_sound('sounds/created.wav', time_offset = time)
        if sound_alias == C.SOUND_CREATING:
            self.add_sound('sounds/creating-03.wav', time_offset = time)
        if sound_alias == C.SOUND_STEP:
            self.add_sound('sounds/step.wav', time_offset = time)
        if sound_alias == C.SOUND_DELETE:
            self.add_sound('sounds/delete.mp3', time_offset = time)
    
    def construct(self):

        # INTRO
        title1 = MathTex("A^2-B^2 = (A-B)(A+B)", font_size = 52, color = YELLOW).shift(1 * UP)
        title2 = Text("Simple Visual Proof", font_size = 32, t2c = {"simplest": BLUE}).shift(0 * DOWN)
        self.wait(1)
        self.play(Write(title1), run_time = 1) 
        self.add_with_click(title2, 1)
        self.wait(2)
        self.play(FadeOut(title1, title2), run_time = 3)
        self.wait(1)
        
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
                   stroke_width = 7).shift(DOWN)
        self.sound(C.SOUND_CREATING, 0.8)
        self.play(Create(A), run_time = 1)
        
        
        # BRACKET A
        line = Line(A.get_critical_point(DR), A.get_critical_point(UR))
        b1 = Brace(line, direction = line.copy().rotate(-PI/2).get_unit_vector(), buff = 0.7)
        b1text = b1.get_text("A").set_color(WHITE)
        self.play(Create(b1))
        self.add_with_click(b1text)
        self.wait(2)
        
        # A square + move
        A2 = MathTex(r"A^2", color = WHITE, font_size = 50).shift(A.get_center())
        self.sound(C.SOUND_CREATED, 0.7)
        self.play(Indicate(A2))
        self.wait(1)
        self.play(A2.animate().to_edge(UP).shift(2*LEFT))
        self.sound(C.SOUND_CLICK_SILENT, 0)
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
        self.sound(C.SOUND_CREATING, 0.8)
        self.play(Create(B), run_time = 1)
        
        #Bracket  B
        self.wait(1)
        line3 = Line(B.get_critical_point(DL), B.get_critical_point(UL))
        b3 = Brace(line3, direction = line.copy().rotate(PI/2).get_unit_vector(), buff = 0.7)
        b3text = b3.get_text("B").set_color(WHITE)
        self.add(b3)
        self.add_with_click(b3text, 1)
                
        # B Square move
        self.wait(1)
        B2 = MathTex("B^2", color = WHITE, font_size = 50).shift(B.get_center())
        self.sound(C.SOUND_CREATED, 0.7)
        self.play(Indicate(B2))
        self.wait(1)
        self.play(B2.animate().next_to(minus, RIGHT))
        self.sound(C.SOUND_CLICK_SILENT, 0)
        self.wait(1)
        
        # # Bracket A - B
        line4 = Line(B.get_critical_point(UL), A.get_critical_point(UL))
        b4 = Brace(line4, direction = line4.copy().rotate(PI/2).get_unit_vector(), buff = 0.7)
        b4text = b4.get_text("A-B").set_color(WHITE)
        self.play(Create(b4))
        
        self.add_with_click(b4text,1 )
        self.wait(2)
        
        # Bracket B top
        line5 = Line(A.get_critical_point(UL), A.get_critical_point(UL) + (b, 0 ,0))
        b5 = Brace(line5, direction = line5.copy().rotate(PI/2).get_unit_vector(), buff = 0.7)
        b5text = b5.get_text("B").set_color(WHITE)
        self.play(Create(b5))
        self.add_with_click(b5text,1 )
        self.wait(1)
        

        
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
        
        self.delete_with_sound(A)
        self.delete_with_sound(B)
        self.play(Create(minus))
        
        dotLine = DashedLine(B.get_critical_point(UR), B.get_critical_point(UR) + (0, a-b, 0),
                             color = WHITE,
                             dash_length=0.2,
                             z_index = 10)
        
        self.play(Create(dotLine))
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
        self.sound(C.SOUND_CLICK_LOUD, 0)
        self.play(group[2].animate().rotate(-PI/2))
        self.play(FadeOut(b3), FadeOut(b3text))
         
        groupRemoveBrackest = VGroup(b5, group[1])
        line6 = Line(A.get_critical_point(UL), group[0].get_critical_point(UR))
        b6 = Brace(line6, direction = line6.copy().rotate(PI/2).get_unit_vector(), buff = 0.7)
        
        createBrackets = b6
        self.play(Transform(groupRemoveBrackest, createBrackets), run_time = 2)
        self.wait(2)
        
        plus = MathTex("+", font_size = 50).move_to(0.5 * b5text.get_center() + 0.5 * group[2].get_center())
        self.add_with_click(plus)
        jednako = MathTex("=", font_size = 50).next_to(B2, RIGHT)
        self.add_with_click(jednako, 1)
        self.wait(1)
        
        aMinusBrez = MathTex("(A-B)", font_size = 50).next_to(jednako, RIGHT)
        self.play(ReplacementTransform(b4text.copy(), aMinusBrez), run_time = 2)
        self.sound(C.SOUND_CLICK_LOUD)
        self.wait(1)
        aPlusBrez = MathTex("(A+B)", font_size = 50).next_to(aMinusBrez, RIGHT)
        self.play(ReplacementTransform(VGroup(b5text, plus, group[2]).copy(), aPlusBrez), run_time = 2)
        self.sound(C.SOUND_CLICK_LOUD)
        
        group2 = VGroup(A2, minus, B2, jednako, aMinusBrez, aPlusBrez)
        self.play(group2.animate().shift(LEFT * 0.5))
        self.wait(1)
        box = SurroundingRectangle(group2, color = YELLOW, stroke_width = 3, buff= 0.2, corner_radius=0.05)
        self.sound(C.SOUND_CREATING, 0.6)
        self.play(Create(box))
        group2.set_color(YELLOW)
        self.wait(5)
        
        
        
        

       
        

