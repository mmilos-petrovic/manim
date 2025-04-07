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
class TrapezoidAreaShort(Scene):
    def construct(self):
       
        Polygon.set_default(
            fill_color=RED,
            fill_opacity = 0.9, 
            stroke_opacity = 1, 
            stroke_color = WHITE, 
            stroke_width = 6
            )
        Line.set_default(
            stroke_width = 6,
            z_index = 20
        )
        up = 1
        left = 1
        # CONST
        A = np.array((-2.2 - left, -2.3 + up, 0.0))
        B = np.array((2.2 - left, -2.3 + up, 0.0))
        CC = np.array((1 - left, 0.5 + up, 0.0))
        D = np.array((-1 - left, 0.5 + up, 0.0))
        H = np.array((-1 - left, -2.3 + up, 0.0))
        H2 = D * 0.5 + H * 0.5
        M1 = A * 0.5 + D * 0.5
        M2 = B * 0.5 + CC * 0.5
        R = B + CC - D
        R2 = R + M1 - A
        FIX1 = np.array((0.15, 0, 0))
        dotM2 = Dot(M2, color=WHITE, radius = 0.08)
        
        
        # INTRO
        title1 = Text("Area of a trapezoid", font_size = 36, color = BLUE).to_corner(UL, buff = 1)
        self.add(title1)
        
        # TRAPEZOID
        aStr = Tools.twoPointLabel(A, B , "a", False, 60)
        bStr = Tools.twoPointLabel(CC, D , "b", False, 60)
        trapezoid = Polygon(*[A, B, CC, D])
        self = Tools.create_with_sound(self, trapezoid, 1, 1)
        self = Tools.add_with_click_pen(self, aStr, 0.5)
        self = Tools.add_with_click_pen(self, bStr, 0.5)
        
        #QUESTION
        solution= Tex(r'\text{Area = }', r'$\dfrac{h}{2}$', r'$~\cdot~$', r'(a+b)', font_size=50, color = YELLOW).to_corner(UL, buff = 1).shift(1.5 * DOWN)
        self = Tools.add_with_click_pen(self, solution[0], 1)
        
        # H
        h = Line(H, D)
        hStr = Tools.twoPointLabel(H, D , "h", True, 60).set_color(WHITE).set_z_index(20)   
        self = Tools.create_with_sound(self, h, 1, 0.5)
        self = Tools.add_with_click_pen(self, hStr, 0.5)
        
        
        # CUT TRAPEZOID
        self = Tools.add_with_click_pen(self, dotM2, 1)
        cut1 = Line(D, M2)
        self = Tools.create_with_sound(self, cut1, 1, 0.5)
        part1 = Polygon(*[A, B, M2, D])
        part2 = Polygon(*[M2, CC, D + FIX1])
        self.add(part1)
        self.add(part2)
        self.remove(trapezoid, cut1)
        self.play(
            Rotate(
                VGroup(part2, bStr),
                angle=-PI,
                about_point=M2,
                rate_func=linear,
            ),
            run_time = 2
            )
        self = Tools.sound(self, C.SOUND_CLICK_SHORT, 0.2)
        self.play(
            Rotate(
                bStr,
                angle=PI,
                about_point=bStr.get_center(),
                rate_func=linear,
            ),
            run_time = 1
            )
        self.remove(dotM2)
        
        
        # CREATE TRIANGLE
        triangle = Polygon(*[A, R, D])
        self.play(FadeIn(triangle), run_time = 1)
        self.play(FadeOut(part1), FadeOut(part2), run_time = 1)
        
        
        # CUT AND ROTATE TRIANGLE
        part1 = Polygon(*[A, R - FIX1/2, M2, M1])
        part2 = Polygon(*[M1, M2, D])
        cut2 = Line(M1, M2)
        self = Tools.create_with_sound(self, cut2, 0, 0.5)
        self.wait(1)
        self.add(part1)
        self.add(part2)
        self.remove(triangle)
        self.remove(cut2)
        h2 = Line(H2, H, stroke_width = 7 ,z_index = 20)
        self.remove(h, hStr)
        h2Str = Tools.twoPointLabel(H, H2 , "\\frac{ h }{ 2 }", True, 40).set_color(WHITE).set_z_index(20)
        self.add(h2, h2Str)
        self.play(
            Rotate(
                part2,
                angle = -PI,
                about_point = M2,
                rate_func = linear,
            ),
            run_time = 2
            )
        self = Tools.sound(self, C.SOUND_CLICK_SHORT, 0.2)
        self.wait(1)
        
        
        # CREATE PARALELOGRAM
        paralelogram = Polygon(*[A, R, R2, M1])
        self.remove(part1)
        self.remove(part2)
        self.add(paralelogram)
        
        # CUT PARALELOGRAM AND TRANSLATE
        cut3 = Line(R, R + H2 - H)
        self = Tools.create_with_sound(self, cut3, 1, 0.5)
        part1 = Polygon(*[A, R, R + H2 - H, M1])
        part2 = Polygon(*[R, R2, R + H2 - H])
        self.remove(paralelogram)
        self.add(part1)
        self.add(part2)
        self.wait(1)
        self.play(
            part2.animate().shift(A-R), run_time = 2
        )
        self = Tools.sound(self, C.SOUND_CLICK_SHORT)
        self.wait(1)
        
        # CREATE RECTANGLE
        rectange = Polygon(*[A, R, R + H2 - H, A + H2 - H])
        self.remove(part1)
        self.remove(part2)
        self.remove(cut3)
        self.add(rectange)
        rectangleGroup = VGroup(rectange, aStr, bStr, h2, h2Str)
        self.play(
            rectangleGroup.animate().shift(-A/8 + R/8, LEFT).shift(UP), run_time = 1
        )
        
        # BRACKET 
        horisontal = Line(rectangleGroup.get_critical_point(DL), rectangleGroup.get_critical_point(DR))
        b2 = Brace(horisontal, direction = horisontal.copy().rotate(-PI/2).get_unit_vector(), buff = 0.3)
        b2text = b2.get_text("(a + b)").set_color(WHITE)
        self = Tools.create_with_sound(self, b2, 0.5, 0.5)
        self = Tools.add_with_click_short(self, b2text, 0.5)
        
        self = Tools.sound(self, C.SOUND_CLICK_PEN, 1, 1)
        self.play(ReplacementTransform(h2Str.copy(), solution[1]), run_time = 1)
        self = Tools.add_with_click_pen(self, solution[2], 1)
        
        self = Tools.sound(self, C.SOUND_CLICK_PEN, 1, 1)
        self.play(ReplacementTransform(b2text.copy(), solution[3]), run_time = 1)
        self.wait(3)
        
        