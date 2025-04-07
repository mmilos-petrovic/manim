from manim import *
import manimpango
import math
from colour import Color
from tools import Tools
from constants import Constants as C
config.disable_caching = True


# color , fill_opacity , stroke_width
class Pythagora(Scene):
    def add_with_click(self, mobject):
        self.sound(C.SOUND_CLICK_SILENT, 0.2)
        self.add(mobject)
        
    def sound(self, sound_alias, time = 0):
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
            
    def construct(self):

        # INTRO
        title1 = Text("PYTHAGOREAN THEOREM", font_size = 36, color = YELLOW).shift(1 * UP)
        title2 = Text("The simplest visual proof", font_size = 36, t2c = {"simplest": BLUE_C}).shift(0 * DOWN)
        self.add(title1)
        self.wait(0.7)
        self.play(Write(title2))
        self.add(title2)
        self.play(FadeOut(title2), FadeOut(title1, run_time = 1.5))
        self.wait(0.5)

        # STEP 1
        step1 = Text("Step 1: Draw an arbitrary right triangle.", font_size = 28, t2c = {"Step 1": YELLOW}).to_edge(UL)
        self.sound(C.SOUND_STEP, 0)
        self.play(Write(step1), run_time = 2)
        a = 1.8
        b = 1.4

        A = Dot([a/2, b,0], radius = 0.03).shift(1.4 * UP)
        B = Dot([-a/2,0,0], radius = 0.03).shift(1.4 * UP)
        CC = Dot([a/2,0,0], radius = 0.03).shift(1.4 * UP)
        triangle = Polygon(A.get_center(), B.get_center(), CC.get_center(), fill_color=BLUE, fill_opacity=0.3)
        
        la = Tools.twoPointLabel(B, CC, "A", font_size = 28)
        lb = Tools.twoPointLabel(CC, A, "B", font_size = 28)
        lc = Tools.twoPointLabel(A, B, "C", font_size = 28)
        self.sound(C.SOUND_CREATING, 0.7)
        self.play(Create(triangle))
        self.add_with_click(la)
        self.wait(0.5)
        self.add_with_click(lb)
        self.wait(0.5)
        self.add_with_click(lc)
        self.wait(1)

        # STEP 2
        step2 = Text("Step 2: Draw two squares with side lengths A + B.", font_size = 28, 
                     t2c = {"Step 2": YELLOW, "A + B":GREEN}).to_edge(UL)
        self.play(FadeOut(step1))
        self.sound(C.SOUND_STEP, 0)
        self.play(Write(step2), run_time = 2)
        self.wait(1)
        sq1 = Square(side_length = 3.2, z_index = 10, color = GREEN).shift(2.5 * LEFT + DOWN)
        sq2 = Square(side_length = 3.2, z_index = 10, color = GREEN).shift(2.5 * RIGHT + DOWN)
        line = Line(sq1.get_critical_point(DL), sq1.get_critical_point(UL))
        b1 = Brace(line, direction = line.copy().rotate(PI / 2).get_unit_vector(), buff = 1)
        b1text = b1.get_text("A + B").set_color(GREEN)
        self.play(Create(sq1))
        self.sound(C.SOUND_CREATED, 0.3)
        self.wait(0.5)
        self.play(Create(sq2))
        self.sound(C.SOUND_CREATED, 0.3)
        
        self.wait(0.5)
        self.sound(C.SOUND_CREATING, 1)
        self.play(
            AnimationGroup(Create(b1), Write(b1text.rotate(PI/2)), lag_ratio=0.7), run_time = 1
        )
        
        # STEP 3
        
        step3 = Text("Step 3: Arrange four triangles into the first square.", font_size = 28, 
                     t2c = {"Step 3": YELLOW}).to_edge(UL)
        self.play(FadeOut(step2))
        self.sound(C.SOUND_STEP, 0)
        self.play(Write(step3), run_time = 2)
        
        tGroup1 = VGroup(triangle, la, lb, lc)
        tGroup2 = VGroup(triangle.copy(), 
            la.copy().rotate(PI/2), 
            lb.copy().rotate(PI/2), 
            lc.copy().rotate(PI/2))
        tGroup3 = VGroup(triangle.copy(), 
            la.copy().rotate(PI), 
            lb.copy().rotate(PI), 
            lc.copy().rotate(PI))
        tGroup4 = VGroup(triangle.copy(), 
            la.copy().rotate(-PI/2), 
            lb.copy().rotate(-PI/2), 
            lc.copy().rotate(-PI/2))
        
        # FIRST SQUARE
        t1 = tGroup1.copy().shift(sq1.get_critical_point(DR) - CC.get_center())
        t2 = tGroup2.copy().shift(sq1.get_critical_point(DL) - CC.get_center()).rotate(-PI/2, about_point=sq1.get_critical_point(DL))
        t3 = tGroup3.copy().shift(sq1.get_critical_point(UL) - CC.get_center()).rotate(PI, about_point=sq1.get_critical_point(UL))
        t4 = tGroup4.copy().shift(sq1.get_critical_point(UR) - CC.get_center()).rotate(PI/2, about_point=sq1.get_critical_point(UR))
        self.play(Transform(tGroup1.copy(), t1))
        self.sound(C.SOUND_CLICK_LOUD)
        self.wait(1)
        self.play(Transform(tGroup2.copy(), t2))
        self.sound(C.SOUND_CLICK_LOUD)
        self.wait(1)
        self.play(Transform(tGroup3.copy(), t3))
        self.sound(C.SOUND_CLICK_LOUD)
        self.wait(1)
        self.play(Transform(tGroup4.copy(), t4))
        self.sound(C.SOUND_CLICK_LOUD)
        self.wait(1)
        t1[3].set_color(GRAY_D)
        t2[3].set_color(GRAY_D)
        t3[3].set_color(GRAY_D)
        t4[3].set_color(GRAY_D)
        self.add(t1[3], t2[3], t3[3], t4[3])
        C2 = MathTex(r"C^2", color = YELLOW, font_size = 32).shift(sq1.get_center())
        self.play(Indicate(C2))
        self.wait(1)
        con1 = Text("Black area = ", font_size=24, color = WHITE).next_to(sq1, DOWN).shift(0.5 * DOWN + 0.5*LEFT)
        C2rez = C2.copy().next_to(con1, RIGHT)
        self.play(Write(con1))
        self.play(Transform(C2.copy(), C2rez))
        self.sound(C.SOUND_CLICK_SILENT)
        self.wait(1.5)
        
        # STEP 4 => SECOND SQUARE
        
        step4 = Text("Step 4: Arrange four triangles into the second square.", font_size = 28, 
                     t2c = {"Step 4": YELLOW}).to_edge(UL)
        self.play(FadeOut(step3))
        self.sound(C.SOUND_STEP, 0)
        self.play(Write(step4), run_time = 2)
        self.wait(1)
        
        t5 = tGroup1.copy().shift(sq2.get_critical_point(DR) - CC.get_center())
        t6 = tGroup3.copy().shift(sq2.get_critical_point(DR) - CC.get_center()).rotate(PI, about_point=sq2.get_critical_point(DR)).shift(UP * b + LEFT * a)
        t7 = tGroup2.copy().rotate(-PI/2, about_point=CC.get_center()).shift(sq2.get_critical_point(UL) - CC.get_center() - (0,a,0))
        t8 = tGroup4.copy().rotate(PI/2, about_point=CC.get_center()).shift(sq2.get_critical_point(UL) - CC.get_center() + (b, 0, 0))
        self.play(Transform(tGroup1.copy(), t5))
        self.sound(C.SOUND_CLICK_LOUD)
        self.wait(1)
        self.play(Transform(tGroup3.copy(), t6))
        self.sound(C.SOUND_CLICK_LOUD)
        self.wait(1)
        self.play(Transform(tGroup2.copy(), t7))
        self.sound(C.SOUND_CLICK_LOUD)
        self.wait(1)
        self.play(Transform(tGroup4.copy(), t8))
        self.sound(C.SOUND_CLICK_LOUD)
        self.wait(1)
        t6[1].set_color(GRAY_D)
        t6[2].set_color(GRAY_D)
        t7[2].set_color(GRAY_D)
        t8[1].set_color(GRAY_D)
        A2 = MathTex(r"A^2", color = YELLOW, font_size = 32).shift(sq2.get_center() + (a/2, a/2, 0))
        self.add(t6[1], t8[1])
        self.sound(C.SOUND_CLICK_SILENT, 0.5)
        self.play(Indicate(A2), run_time = 0.8)
        
        self.wait(1)
        B2 = MathTex(r"B^2", color = YELLOW, font_size = 32).shift(sq2.get_center() - (b/2 + 0.2, b/2 + 0.2, 0))
        self.add(t6[2], t7[2])
        self.sound(C.SOUND_CLICK_SILENT, 0.5)
        self.play(Indicate(B2), run_time = 0.8)
        self.wait(2)
        con2 = Text("Black area", font_size=24, color = WHITE).next_to(sq2, DOWN).shift(0.5 * DOWN + 1.5 * LEFT)
        eq = Text("=", font_size=24, color = WHITE).next_to(con2, RIGHT)
        A2rez = A2.copy().next_to(eq, RIGHT)
        plus = Text("+", font_size=24, color = WHITE).next_to(A2rez, RIGHT)
        B2rez = B2.copy().next_to(plus, RIGHT)
        
        
         # STEP 5 => BLACK AREA
        self.play(Write(con2), Write(eq))
        self.play(ReplacementTransform(A2.copy(), A2rez))
        self.sound(C.SOUND_CLICK_SILENT)
        self.play(Write(plus))
        self.play(ReplacementTransform(B2.copy(), B2rez))
        self.sound(C.SOUND_CLICK_SILENT)
        
        step5 = Text("Step 5: The black areas of both squares are equal.", font_size = 28, 
                     t2c = {"Step 5": YELLOW}).to_edge(UL)
        self.play(FadeOut(step4))
        self.sound(C.SOUND_STEP, 0)
        self.play(Write(step5))
        self.wait(1)
        
        group = VGroup(eq, A2rez, plus, B2rez)
        self.play(FadeOut(con2))
        self.sound(C.SOUND_CREATING, 0.4)
        self.play(group.animate().next_to(C2rez, RIGHT))
        
        group2 = VGroup(C2rez, group)
        box = SurroundingRectangle(group2, color=YELLOW, buff=0.2, corner_radius=0.05, stroke_width = 2)
        self.play(Create(box))
        self.wait(3)
        