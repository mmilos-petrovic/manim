from manim import *
from manim.opengl import *
from reactive_manim import *
import manimpango
import math
from colour import Color
from tools import Tools
from constants import Constants as C

config.disable_caching = True


# color , fill_opacity , stroke_width
class VennDiagram(Scene):
    def construct(self):
        
        C1 = BLUE
        C2 = YELLOW
        C3 = RED
        
        SurroundingRectangle.set_default(
            color = C3,
            buff = 0.1,
            corner_radius = 0.05,
            stroke_width = 2,
        )
        
        
        # INTRO
        title = Text("How to construct a Venn diagram?", font_size = 32, color = WHITE).to_corner(UL).shift(0.1 * UP)
        self.add(title)
        
        set1 = MathTex("A = ", "\{" , "~2~", ", ", "~3~", ", ","~4~", ", ","~8~", "\}", font_size = 40, color = C1)
        set2 = MathTex("B = ", "\{" , "~1~", ", ", "~4~", ", ","~5~", ", ", "~8~", ", ", "~9~", "\}", font_size = 40, color = C2)
        group = VGroup(set1, set2).arrange(1.2 * DOWN, center=False, aligned_edge=LEFT).next_to(title, DOWN).shift(LEFT + 0.2 * DOWN)
        self.add(group)
        
        circleA = Circle(radius= 1.8, fill_opacity=0.1, color = C1, stroke_width = 5).shift(LEFT + DOWN)
        circleB = Circle(radius= 1.8, fill_opacity=0.1, color = C2, stroke_width = 5).shift(RIGHT + DOWN)
        A = MathTex("A", color = BLUE).next_to(circleA, UP + LEFT).shift(0.5 * DOWN + 0.5 * RIGHT)
        B = MathTex("B", color = YELLOW).next_to(circleB, 0.5 * UP + RIGHT).shift(0.5 * DOWN + 0.5 * LEFT)
        self.add(circleA, circleB, A, B)
        
        
        # MOVE TO DIAGRAM
        setA2 = VGroup(set1[2], SurroundingRectangle(set1[2], color = C1))
        setA3 = VGroup(set1[4], SurroundingRectangle(set1[4], color = C1))
        setA4 = VGroup(set1[6], SurroundingRectangle(set1[6], color = C1))
        setA8 = VGroup(set1[8], SurroundingRectangle(set1[8], color = C1))
        
        setB1 = VGroup(set2[2], SurroundingRectangle(set2[2], color = C2))
        setB4 = VGroup(set2[4], SurroundingRectangle(set2[4], color = C2))
        setB5 = VGroup(set2[6], SurroundingRectangle(set2[6], color = C2))
        setB8 = VGroup(set2[8], SurroundingRectangle(set2[8], color = C2))
        setB9 = VGroup(set2[10], SurroundingRectangle(set2[10], color = C2))
        
        self = Tools.create_with_sound(self, [setA4[1], setB4[1]], 1, 0.5)
        self = Tools.move_to_with_click(self, [setA4, setB4], ORIGIN + 0.5 * DOWN)
        self.remove(setA4[1], setB4)
        
        self = Tools.create_with_sound(self, [setA8[1], setB8[1]], 0.5, 0.5)
        self = Tools.move_to_with_click(self, [setA8, setB8], ORIGIN + 1.5 * DOWN)
        self.remove(setA8[1], setB8)
        
        self = Tools.create_with_sound(self, setA2[1], 0.5, 0.5)
        self = Tools.move_to_with_click(self, setA2, ORIGIN + 1.3 * LEFT)
        self.remove(setA2[1])
        
        self = Tools.create_with_sound(self, setA3[1], 0.5, 0.5)
        self = Tools.move_to_with_click(self, setA3, ORIGIN + 1.8 * LEFT + 1.2 * DOWN)
        self.remove(setA3[1])
        
        self = Tools.create_with_sound(self, setB1[1], 0.5, 0.5)
        self = Tools.move_to_with_click(self, setB1, ORIGIN + 1.5 * RIGHT)
        self.remove(setB1[1])
        
        self = Tools.create_with_sound(self, setB5[1], 0.5, 0.5)
        self = Tools.move_to_with_click(self, setB5, ORIGIN + 2.1 * RIGHT + DOWN)
        self.remove(setB5[1])
        
        self = Tools.create_with_sound(self, setB9[1], 0.5, 0.5)
        self = Tools.move_to_with_click(self, setB9, ORIGIN + 1.3 * RIGHT + 2 * DOWN)
        self.remove(setB9[1])
        
        groupAll = VGroup(circleA, circleB, setA2[0], setA3[0], setA4[0], setA8[0], setB1[0], setB5[0], setB9[0], A, B)
        self.play(groupAll.animate().to_edge(LEFT))
        
        
        intersect = Intersection(circleA, circleB, color=GREEN, fill_opacity=0.5, stroke_width = 3)
        union = Union(circleA, circleB, color = GREEN, fill_opacity=0.5, stroke_width = 3)
        diffLeft = Exclusion(circleA, intersect, color=GREEN, fill_opacity=0.5, stroke_width = 3)
        diffRight = Exclusion(circleB, intersect, color=GREEN, fill_opacity=0.5, stroke_width = 3)
        
        groupInter = VGroup(intersect, setA4[0].copy(), setA8[0].copy())
        groupUnion = VGroup(union, setA2[0].copy(), setA3[0].copy(), setA4[0].copy(), setA8[0].copy(), setB1[0].copy(), setB5[0].copy(), setB9[0].copy())
        groupDiffLeft = VGroup(diffLeft, setA2[0].copy(), setA3[0].copy())
        groupDiffRight = VGroup(diffRight, setB1[0].copy(), setB5[0].copy(), setB9[0].copy())
        
        font_s = 40
        
        equal = MathTex("=", font_size = 42)
        APB = MathTex("A \cap B = ", font_size = font_s).to_edge(RIGHT, buff = 5.2).shift(0.6 * UP)
        groupInter2 = groupInter.copy().scale(0.2).next_to(APB, RIGHT)
        e1 = equal.copy().next_to(groupInter2, RIGHT)
        sol1 = MathTex("\{", "4, ", "8", "\}", font_size = font_s).next_to(e1, RIGHT)
        self = Tools.add_with_click_pen(self, APB, 1)
        self = Tools.transform_with_move(self, groupInter, groupInter2, 1, 2)
        self.wait(1)
        self.add(e1, sol1)
        
        
        AUB = MathTex("A \cup B = ", font_size = font_s).next_to(APB, 3 * DOWN).align_to(APB, LEFT)
        groupUnion2 = groupUnion.copy().scale(0.18).next_to(AUB, RIGHT)
        e2 = equal.copy().next_to(groupUnion2, RIGHT)
        sol2 = MathTex("\{", "2, ", "3, ", "4, ", "8, ", "1, ", "5, ", "9", "\}", font_size = font_s).next_to(e2, RIGHT)
        self = Tools.add_with_click_pen(self, AUB, 1)
        self = Tools.transform_with_move(self, groupUnion, groupUnion2, 2, 2)
        self.wait(1)
        self.add(e2, sol2)
        
        ADIFFB = MathTex("A \setminus B = ", font_size = font_s).next_to(AUB, 3 * DOWN).align_to(AUB, LEFT)
        groupDiffLeft2 =  groupDiffLeft.copy().scale(0.2).next_to(ADIFFB, RIGHT)
        e3 = equal.copy().next_to(groupDiffLeft2, RIGHT)
        sol3 = MathTex("\{", "2, ", "3", "\}", font_size = font_s).next_to(e3, RIGHT)
        self = Tools.add_with_click_pen(self, ADIFFB, 1)
        self = Tools.transform_with_move(self, groupDiffLeft, groupDiffLeft2, 2, 2)
        self.wait(1)
        self.add(e3, sol3)
        
        BDIFFA = MathTex("B \setminus A = ", font_size = font_s).next_to(ADIFFB, 3 * DOWN).align_to(ADIFFB, LEFT)
        groupDiffRight2 = groupDiffRight.copy().scale(0.2).next_to(BDIFFA, RIGHT)
        e4 = equal.copy().next_to(groupDiffRight2, RIGHT)
        sol4 = MathTex("\{", "1, ", "5, ", "9", "\}", font_size = font_s).next_to(e4, RIGHT)
        self = Tools.add_with_click_pen(self, BDIFFA, 1)
        self = Tools.transform_with_move(self, groupDiffRight, groupDiffRight2, 2, 2)
        self.wait(1)
        self.add(e4, sol4)
        
        self.wait(4)
        
        
        
        
        