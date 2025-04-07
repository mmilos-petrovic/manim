from manim import *
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
class PythagoraShort(Scene):
    def construct(self):
        # constants
        a = 1.8
        b = 1.4
        stepBuff = 2.5
        # INTRO
        title1 = Text("PYTHAGOREAN THEOREM", font_size = 32, color = BLUE).to_edge(UP, buff = 0.7)
        title2 = Text("The simplest visual proof", font_size = 28).next_to(title1, DOWN)
        Tools.add_with_click_silent(self, title1)
        Tools.add_with_click_silent(self, title2, 1)
        
        
        # # STEP 1
        self = Tools.add_step_with_sound(self, 1, "Draw a right triangle.", UP, stepBuff)
        A = Dot([a/2, b,0] + 0.6 * DOWN, radius = 0.03).shift(2.5 * UP)
        B = Dot([-a/2,0,0] + 0.6 * DOWN, radius = 0.03).shift(2.5 * UP)
        CC = Dot([a/2,0,0] + 0.6 * DOWN, radius = 0.03).shift(2.5 * UP)
        triangle = Polygon(A.get_center(), B.get_center(), CC.get_center(), fill_color=BLUE, fill_opacity=0.3)
        
        la = Tools.twoPointLabel(B, CC, "A", font_size = 28)
        lb = Tools.twoPointLabel(CC, A, "B", font_size = 28)
        lc = Tools.twoPointLabel(A, B, "C", font_size = 28)
        self = Tools.create_with_sound(self, triangle, 0.1)
        self = Tools.add_with_click_silent(self, la, 0.2)
        self = Tools.add_with_click_silent(self, lb, 0.2)
        self = Tools.add_with_click_silent(self, lc, 0.2)

        # STEP 2
        self.play(FadeOut(self.mobjects[3]))
        self = Tools.add_step_with_sound(self, 2, "Draw two squares with \n sides A + B.", UP, stepBuff)
        lastStepTitleIndex = len(self.mobjects) - 1
        sq1 = Square(side_length = 3.2, z_index = 10, color = GREEN).shift(2 * LEFT + 1 * DOWN)
        sq2 = Square(side_length = 3.2, z_index = 10, color = GREEN).shift(2 * RIGHT + 1 * DOWN)
        line = Line(sq1.get_critical_point(DL), sq1.get_critical_point(UL))
        b1 = Brace(line, direction = line.copy().rotate(PI / 2).get_unit_vector(), buff = 1)
        b1text = b1.get_text("A + B").set_color(GREEN)
        self = Tools.create_with_sound(self, sq1, 1)
        self = Tools.create_with_sound(self, sq2, 1)
        
       
        
        # STEP 3
        # for o in self.mobjects: print(o)
        self.play(FadeOut(self.mobjects[lastStepTitleIndex]))
        self = Tools.add_step_with_sound(self, 3, "Arrange four triangles into the \n first square.", UP, stepBuff)
        lastStepTitleIndex = len(self.mobjects) - 1
        
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
        Tools.sound(self, C.SOUND_CLICK_LOUD)
        self.wait(0.5)
        self.play(Transform(tGroup2.copy(), t2))
        Tools.sound(self, C.SOUND_CLICK_LOUD)
        self.wait(0.5)
        self.play(Transform(tGroup3.copy(), t3))
        Tools.sound(self, C.SOUND_CLICK_LOUD)
        self.wait(0.5)
        self.play(Transform(tGroup4.copy(), t4))
        Tools.sound(self, C.SOUND_CLICK_LOUD)
        self.wait(0.5)
        t1[3].set_color(GRAY_D)
        t2[3].set_color(GRAY_D)
        t3[3].set_color(GRAY_D)
        t4[3].set_color(GRAY_D)
        self.add(t1[3], t2[3], t3[3], t4[3])
        C2 = MathTex(r"C^2", color = YELLOW, font_size = 32).shift(sq1.get_center())
        self.play(Indicate(C2))
        self.wait(0.5)
        con1 = Text("Black area = ", font_size=24, color = WHITE).next_to(sq1, DOWN).shift(1 * DOWN + 0.5*LEFT)
        C2rez = C2.copy().next_to(con1, RIGHT)
        self.play(Write(con1))
        self.play(Transform(C2.copy(), C2rez))
        Tools.sound(self, C.SOUND_CLICK_LOUD)
        self.wait(1)
        
        
        # # STEP 4 => SECOND SQUARE
        self.play(FadeOut(self.mobjects[lastStepTitleIndex]))
        self = Tools.add_step_with_sound(self, 4, "Arrange four triangles into the \n second square.", UP, stepBuff)
        lastStepTitleIndex = len(self.mobjects) - 1
        
        t5 = tGroup1.copy().shift(sq2.get_critical_point(DR) - CC.get_center())
        t6 = tGroup3.copy().shift(sq2.get_critical_point(DR) - CC.get_center()).rotate(PI, about_point=sq2.get_critical_point(DR)).shift(UP * b + LEFT * a)
        t7 = tGroup2.copy().rotate(-PI/2, about_point=CC.get_center()).shift(sq2.get_critical_point(UL) - CC.get_center() - (0,a,0))
        t8 = tGroup4.copy().rotate(PI/2, about_point=CC.get_center()).shift(sq2.get_critical_point(UL) - CC.get_center() + (b, 0, 0))
        self.play(Transform(tGroup1.copy(), t5))
        Tools.sound(self, C.SOUND_CLICK_LOUD)
        self.wait(0.5)
        self.play(Transform(tGroup3.copy(), t6))
        Tools.sound(self, C.SOUND_CLICK_LOUD)
        self.wait(0.5)
        self.play(Transform(tGroup2.copy(), t7))
        Tools.sound(self, C.SOUND_CLICK_LOUD)
        self.wait(0.5)
        self.play(Transform(tGroup4.copy(), t8))
        Tools.sound(self, C.SOUND_CLICK_LOUD)
        self.wait(0.5)
        t6[1].set_color(GRAY_D)
        t6[2].set_color(GRAY_D)
        t7[2].set_color(GRAY_D)
        t8[1].set_color(GRAY_D)
        A2 = MathTex(r"A^2", color = YELLOW, font_size = 32).shift(sq2.get_center() + (a/2, a/2, 0))
        self.add(t6[1], t8[1])
        Tools.sound(self, C.SOUND_CLICK_SILENT, 0.5)
        self.play(Indicate(A2), run_time = 0.8)
        self.wait(1)
        B2 = MathTex(r"B^2", color = YELLOW, font_size = 32).shift(sq2.get_center() - (b/2 + 0.2, b/2 + 0.2, 0))
        self.add(t6[2], t7[2])
        Tools.sound(self, C.SOUND_CLICK_SILENT, 0.5)
        self.play(Indicate(B2), run_time = 0.8)
        self.wait(2)
        con2 = Text("Black area", font_size=24, color = WHITE).next_to(sq2, DOWN).shift(1 * DOWN + 1.5 * LEFT)
        eq = Text("=", font_size=24, color = WHITE).next_to(con2, RIGHT)
        A2rez = A2.copy().next_to(eq, RIGHT)
        plus = Text("+", font_size=24, color = WHITE).next_to(A2rez, RIGHT)
        B2rez = B2.copy().next_to(plus, RIGHT)
        
        
        # STEP 5 => BLACK AREA
        self.play(Write(con2), Write(eq))
        self.play(ReplacementTransform(A2.copy(), A2rez))
        Tools.sound(self, C.SOUND_CLICK_SILENT)
        self.play(Write(plus))
        self.play(ReplacementTransform(B2.copy(), B2rez))
        Tools.sound(self, C.SOUND_CLICK_SILENT)
        
        
        self.play(FadeOut(self.mobjects[lastStepTitleIndex]))
        self = Tools.add_step_with_sound(self, 5, "The black areas of both squares \nare equal.", UP, stepBuff)
        group = VGroup(eq, A2rez, plus, B2rez)
        self.play(FadeOut(con2))
        Tools.sound(self, C.SOUND_CREATING, 0.4)
        self.play(group.animate().next_to(C2rez, RIGHT))
        
        group2 = VGroup(C2rez, group)
        box = SurroundingRectangle(group2, color=YELLOW, buff=0.2, corner_radius=0.05, stroke_width = 2)
        self.play(Create(box))
        self.wait(3)
        
        