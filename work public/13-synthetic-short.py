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

# color , fill_opacity , stroke_width
class SyntheticShort(Scene):
    def construct(self):
        # CONST
        tableLeft = -3.2
        tableDown = 0.7
        fsMath = 44
        fsText = 22
        fsTable = 44
        dot = MathTex(r" \cdot ", font_size = 50)
        shortRun = 0.8
        longRun = 1.3
        shortWait = 0.7
        longWait = 1.2
        
        #HEADER
        title = Text('SYNTHETIC DIVISION', color=BLUE, font_size=28).to_edge(UP).shift(0.5 * DOWN)
        self.add(title)
        
        p1 = MathTex(r"(~{{ 2 }} x^3 + {{ 1 }}x^2 {{ - 2 }} x + {{ 7 }}~)", font_size = fsMath, color = GOLD)
        delSign = MathTex(r" \div ", font_size = fsMath, color = WHITE)
        p2 = MathTex(r"(x - 3)", font_size = fsMath, color = GOLD)
        task = VGroup(p1, delSign, p2).arrange(RIGHT).next_to(title, 1.5 * DOWN)
        p2copy = MathTex(r"x - 3", font_size = fsMath, color = GOLD).next_to(delSign).shift(0.1 * RIGHT + 0.05 * UP)
        self.add(task)
        l1 = Line([tableLeft, tableDown + 1 ,0], [tableLeft + 5, tableDown + 1, 0])
        l2 = Line([tableLeft + 1, tableDown ,0], [tableLeft + 1, tableDown + 3, 0])
        
        # STEP 1
        step1 = Text("Step 1:", color=YELLOW, font_size = fsText).to_corner(DL).shift(6 * UP)
        step1a = Text("Write the dividend coefficients",font_size = fsText).next_to(step1, RIGHT)
        step1b = Text("into the division table.", font_size = fsText).next_to(step1, RIGHT).shift(0.6 * DOWN)
        self = Tools.sound(self, C.SOUND_STEP, 2, 0.5)
        self.play(Write(step1), run_time = shortRun)
        self.play(Write(step1a), run_time = shortRun)
        self.play(Write(step1b), run_time = shortRun)
        self = Tools.create_with_sound(self, l1, shortWait, shortWait, shortRun)
        self = Tools.create_with_sound(self, l2, shortWait, shortWait, shortRun)
        
        t23 = MathTex("2", font_size = fsTable).move_to([tableLeft + 2 - 0.4, tableDown + 3 - 0.3, 0])
        t33 = MathTex("1", font_size = fsTable).move_to([tableLeft + 3 - 0.4, tableDown + 3 - 0.3, 0]).\
            align_to(t23, DOWN)
        t43 = MathTex("-2", font_size = fsTable).move_to([tableLeft + 4 - 0.4, tableDown + 3 - 0.28, 0]).\
            align_to(t23, DOWN)
        t53 = MathTex("7", font_size = fsTable).move_to([tableLeft + 5 - 0.4, tableDown + 3 - 0.3, 0]).\
            align_to(t23, DOWN)
        
        
        self = Tools.transform_with_pen_clikc(self, p1[1], t23, shortWait, shortRun)
        self = Tools.transform_with_pen_clikc(self, p1[3], t33, 0, shortRun)
        self = Tools.transform_with_pen_clikc(self, p1[5], t43, 0, shortRun)
        self = Tools.transform_with_pen_clikc(self, p1[7], t53, 0, shortRun)
        self.wait(shortWait)
        
        # STEP 2
        self.play(FadeOut(step1), FadeOut(step1a), FadeOut(step1b), run_time = shortRun)
        step2 = Text("Step 2:", color=YELLOW, font_size = fsText).to_corner(DL).shift(6 * UP)
        step2a = Text("Put the root of",font_size = fsText).next_to(step2, RIGHT)
        step2b = Text("in the upper left cell.", font_size = fsText).next_to(step2, RIGHT).shift(0.6 * DOWN)
        self = Tools.sound(self, C.SOUND_STEP, shortWait, 0.5)
        self.play(Write(step2), run_time = shortRun)
        self.play(Write(step2a), run_time = shortRun)
        self.play(p2copy.animate().next_to(step2a, RIGHT).shift(0.03 * UP))
        self.play(Write(step2b), run_time = shortRun)
        self.wait(shortWait)
        
        leftEq = MathTex("x - 3", font_size = fsMath).align_to(step2b, UL).shift(0.8 * DOWN)
        equal2 = MathTex("= 0", font_size= fsMath).next_to(leftEq, RIGHT)
        self.play(Create(leftEq), run_time = shortRun)
        self.play(Create(equal2), run_time = shortRun)
        
        xEqual = MathTex("x =", font_size= fsMath).next_to(leftEq, 1.5 * DOWN).align_to(leftEq, LEFT)
        three = MathTex("3", font_size= fsMath, color = RED).next_to(xEqual, RIGHT).shift(UP * 0.05)
        self.play(Create(xEqual), run_time = shortRun)
        self.play(Create(three), run_time = shortRun)
        t13 = MathTex("3", font_size = fsTable, color = RED).move_to([tableLeft + 1 - 0.5, tableDown + 3 - 0.3, 0]).\
            align_to(t23, DOWN)
        self = Tools.transform_with_move(self, three, t13, 1, shortRun)
        
        # STEP 3
        self.remove(step2, step2a, step2b, leftEq, equal2, xEqual, three, p2copy)
        step3 = Text("Step 3:", color=YELLOW, font_size = fsText).to_corner(DL).shift(6 * UP)
        step3a = Text("Move the leading coefficient to the",font_size = fsText).next_to(step3, RIGHT)
        step3b = Text("bottom row.", font_size = fsText).next_to(step3, RIGHT).shift(0.6 * DOWN)
        self = Tools.sound(self, C.SOUND_STEP, shortWait, 0.5)
        self.play(Write(step3), run_time = shortRun)
        self.play(Write(step3a), run_time = shortRun / 2)
        self.play(Write(step3b), run_time = shortRun / 2)
        t21 = MathTex("2", font_size = fsTable, color = BLUE).move_to([tableLeft + 2 - 0.5, tableDown + 1 - 0.6, 0])
        self = Tools.transform_with_move(self, t23, t21, 1, shortRun)
        
        # STEP 4
        self.remove(step3, step3a, step3b)
        step4 = Text("Step 4:", color=YELLOW, font_size = fsText).to_corner(DL).shift(6 * UP)
        step4a = Text("Multiply 2 by 3, carry the result",font_size = fsText).next_to(step4, RIGHT)
        step4a[8].set_color(BLUE)
        step4a[11].set_color(RED)
        step4b = Text("into the next column.", font_size = fsText).next_to(step4, RIGHT).shift(0.8 * DOWN)
        self = Tools.sound(self, C.SOUND_STEP, shortWait, 0.5)
        self.play(Write(step4), run_time = shortRun)
        self.play(Write(step4a), run_time = shortRun)
        self.play(Write(step4b), run_time = shortRun)
        
        g1 = t21.copy().align_to(step4b, UL).shift(0.8 * DOWN)
        self = Tools.transform_with_pen_clikc(self, t21, g1, 1, shortRun)
        self.wait(0.5)
        dot1 = dot.next_to(g1, RIGHT)
        self.add(dot1)
        g2 = t13.copy().next_to(dot1, RIGHT)
        self = Tools.transform_with_pen_clikc(self, t13, g2, 1, shortRun)
        equal = MathTex(r"=").next_to(g2, RIGHT)
        sol = MathTex(r"6").next_to(equal, RIGHT)
        self.play(Write(equal), run_time = shortRun)
        self.play(Write(sol), run_time = shortRun)
        t32 = MathTex("6", font_size = fsTable).move_to([tableLeft + 3 - 0.5, tableDown + 2 - 0.4, 0]).\
            align_to(t33, RIGHT)
        self = Tools.transform_with_pen_clikc(self, sol, t32, 0.5, shortRun)
        
        
        # STEP 5
        step5 = Text("Step 5:", color=YELLOW, font_size = fsText).to_corner(DL).shift(3.5 * UP)
        step5a = Text("Add last colum.",font_size = fsText).next_to(step5, RIGHT)
        self = Tools.sound(self, C.SOUND_STEP, shortWait, 0.5)
        self.play(Write(step5), run_time = shortRun)
        self.play(Write(step5a), run_time = shortRun)
        t31 = MathTex("7", font_size = fsTable, color = BLUE).move_to([tableLeft + 3 - 0.5, tableDown + 1 - 0.6, 0]).\
            align_to(t33, RIGHT)
        self = Tools.add_with_click_short(self, t31, shortWait)
        
        # STEP 6
        step6 = Text("Step 6:", color=YELLOW, font_size = fsText).to_corner(DL).shift(2.5 * UP)
        step6a = Text("Repeat steps 4 and 5.",font_size = fsText).next_to(step6, RIGHT)
        self = Tools.sound(self, C.SOUND_STEP, shortWait, 0.5)
        self.play(Write(step6), run_time = shortRun)
        self.play(Write(step6a), run_time = shortRun)
        
        # REPEAT 1
        t42 = MathTex("7 ", " \\cdot ", "3", font_size = fsTable).move_to([tableLeft + 4 - 0.5, tableDown + 2 - 0.5, 0]).\
            align_to(t32, DOWN).shift(0.1 * RIGHT)
        t42[0].set_color(BLUE)
        t42[2].set_color(RED)
        self = Tools.transform_with_pen_clikc(self, t31, t42[0], 1, shortRun)
        self.add(t42[1])
        self = Tools.transform_with_pen_clikc(self, t13, t42[2], 1, shortRun)
        self.wait(longWait)
        t42b = MathTex("21", font_size = fsTable).move_to([tableLeft + 4 - 0.5, tableDown + 2 - 0.6, 0]).\
            align_to(t32, DOWN).shift(0.1 * RIGHT)
        self.play(Transform(t42, t42b), run_time = shortRun)
        self.wait(shortWait)
        t41 = MathTex("19", font_size = fsTable, color = BLUE).move_to([tableLeft + 4 - 0.5, tableDown + 1 - 0.6, 0]).align_to(t31, DOWN).shift(0.1 * RIGHT)
        self = Tools.add_with_click_pen(self, t41, 1)
        
        # REPEAT 2
        t52 = MathTex("19", " \\cdot ", "3", font_size = fsTable).move_to([tableLeft + 5 - 0.5, tableDown + 2 - 0.6, 0]).\
            align_to(t42, DOWN)
        t52[0].set_color(BLUE)
        t52[2].set_color(RED)
        self = Tools.transform_with_pen_clikc(self, t41, t52[0], longWait, shortRun)
        self.add(t52[1])
        self = Tools.transform_with_pen_clikc(self, t13, t52[2], shortWait, shortRun)
        self.wait(shortWait)
        t52b = MathTex("57", font_size = fsTable).move_to([tableLeft + 5 - 0.5, tableDown + 2 - 0.6, 0]).\
            align_to(t42, DOWN)
        self.play(Transform(t52, t52b), run_time = shortRun)
        self.wait(shortWait)
        
        # STEP 8
        t51 = MathTex("64", font_size = fsTable, color = GOLD).move_to([tableLeft + 5 - 0.5, tableDown + 1 - 0.6, 0]).align_to(t31, DOWN)
        self = Tools.add_with_click_pen(self, t51, shortWait)
        self.wait(shortWait)
        self.remove(step4, step4a, step4b, g1, g2, equal, step5, step5a, step6, step6a, dot1, sol)
        
        step7 = Text("Step 7:", color=YELLOW, font_size = fsText).to_corner(DL).shift(6 * UP)
        step7a = Text("Determine the quotient ",font_size = fsText).next_to(step7, RIGHT)
        step7b = Text("and remainder.", font_size = fsText).next_to(step7, RIGHT).shift(0.8 * DOWN)
        self = Tools.sound(self, C.SOUND_STEP, shortWait, 0.5)
        self.play(Write(step7), run_time = shortRun)
        self.play(Write(step7a), run_time = shortRun)
        self.play(Write(step7b), run_time = shortRun)
        self.wait(1)
        
        # QUOTIENT
        quotientText = Text("Quotient = ", font_size= fsText).align_to(l1, LEFT).shift(2.4 * DOWN)
        remText = Text("Remainder = ", font_size= fsText).align_to(l1, LEFT).shift(3.2 * DOWN)
        self.add(quotientText, remText)
        a = t21.copy().next_to(quotientText, RIGHT)
        x2 = MathTex(r"x^2 ~ + ", color = BLUE).next_to(a, RIGHT).shift(0.05 * UP)
        b = t31.copy().next_to(x2, RIGHT)
        x = MathTex(r"x ~ + ", color = BLUE).next_to(b, RIGHT)
        c = t41.copy().next_to(x, RIGHT)
        
        self = Tools.transform_with_pen_clikc(self, t21, a, longWait, shortRun)
        self.play(Create(x2), run_time = shortRun/2)
        self = Tools.transform_with_pen_clikc(self, t31, b, shortWait, shortRun)
        self.play(Create(x), run_time = shortRun/2)
        self = Tools.transform_with_pen_clikc(self, t41, c, shortWait, shortRun)
        
        r = t51.copy().next_to(remText, RIGHT)
        self = Tools.transform_with_move(self, t51, r, 1, shortWait)
        self.wait(3)
        