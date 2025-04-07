from manim import *
import manimpango
from colour import Color
from tools import Tools



# color , fill_opacity , stroke_width
class Probability(Scene):
    def construct(self):
        # left side
        title = Text("The addition rule",  font_size=36, color=WHITE).to_edge(UL).to_edge(LEFT, buff=0.3)

        # sets circles
        setA = Circle(radius=1.6, fill_opacity=0.5, color=BLUE, stroke_width=7).move_to(1.4 * LEFT)
        setB = Circle(radius=1.6, fill_opacity=0.5, color=GREEN, stroke_width=7).move_to(0 * LEFT)
        labelA = Text("A", font_size = 32).move_to(setA, UL)
        labelB = Text("B", font_size = 32).move_to(setB, UR)
        self.add(setA, setB, labelA, labelB)


        # sets input data
        pA = Text("P(A) =", font_size=28, color=BLUE).to_edge(LEFT, buff=0.2).shift(-1.5 * DOWN)
        pAval = Text("0.7", font_size = 28, color=BLUE).next_to(pA, RIGHT)
        pB = Text("P(B) =", font_size=28, color=GREEN).to_edge(LEFT, buff=0.2).shift(-0.5 * DOWN)
        pBval = Text("0.5", font_size=28, color=GREEN).next_to(pB, RIGHT)
        pAandB = Text("P(A and B) = ", font_size=28, color=RED).to_edge(LEFT, buff=0.2).shift(0.5 * DOWN)
        pAandBVal = Text("0.3", font_size=28, color=RED).next_to(pAandB, RIGHT)
        pAorB = Text("P(A or B) = ??", font_size=28, color=WHITE).to_edge(LEFT, buff=0.2).shift(1.5 * DOWN)
        self.add(title)
        self.wait(1)
        self.play( AnimationGroup(
            Write(pA), Write(pAval), Write(pB), Write(pBval), Write(pAandB), Write(pAandBVal), Write(pAorB),
                                  lag_ratio = 1),run_time = 6)
        
        # intersection 
        self.wait(3)
        i = Intersection(setA, setB, color=RED_E, fill_opacity=0.5, stroke_width = 7)
        self.add(i)
        pAandB.set_color(RED)
        pAandBVal.set_color(RED)
        pAandBValCenter = pAandBVal.copy().shift(RIGHT * 3.2 + 0.5 * UP)
        self.play(Transform(pAandBVal.copy(), pAandBValCenter), run_time = 2)

        # compute pAmoon
        self.wait(2)
        eA = Exclusion(setA, i, color=BLUE, fill_opacity=0.5, stroke_width = 7)
        eAtarget = eA.copy().shift(RIGHT * 4.6 + 2 * UP).scale(0.3)
        self.play(Transform(eA, eAtarget), run_time = 2)
        eq = Text("=", font_size=28, color=WHITE)
        minus = Text("-", font_size=58, color = WHITE)
        eq1 = eq.copy().next_to(eAtarget, RIGHT)
        self.add(eq1)
        setAtarget = setA.copy().scale(0.3).next_to(eq1, RIGHT)
        self.play(Transform(setA.copy(), setAtarget), run_time = 2)
        minus1 = minus.copy().next_to(setAtarget, RIGHT)
        self.add(minus1)
        i1Target = i.copy().scale(0.3).next_to(minus1, RIGHT)
        self.play(Transform(i.copy(), i1Target), run_time = 2)
        
        eq2 = eq1.copy().next_to(eq1, 5 * DOWN)
        self.add(eq2)
        pAvalTarget = pAval.copy().next_to(eq2, RIGHT)
        self.play(Transform(pAval.copy(), pAvalTarget), run_time = 2)
        minus2 = minus.copy().next_to(pAvalTarget, RIGHT)
        self.add(minus2)
        pAandBValTarget = pAandBVal.copy().next_to(minus2, RIGHT)
        self.play(Transform(pAandBVal.copy(), pAandBValTarget), run_time = 2)
        eq3 = eq.copy().next_to(pAandBValTarget, RIGHT)
        self.add(eq3)
        pAmoon = Text("0.4", font_size=28, color=BLUE).next_to(eq3, RIGHT)
        self.add(pAmoon)
        self.play(pAmoon.copy().animate.shift(9 * LEFT + 0.7 * DOWN), run_time = 2)
        
        # compute pBmoon
        self.wait(2)
        eB = Exclusion(setB, i, color=GREEN, fill_opacity=0.5, stroke_width = 7)
        eBtarget = eB.copy().shift(RIGHT * 2.4 - UP).scale(0.3)
        self.play(Transform(eB, eBtarget), run_time = 2)
        eq4 = eq.copy().next_to(eBtarget, RIGHT)
        self.add(eq4)
        setBtarget = setB.copy().scale(0.3).next_to(eq4, RIGHT)
        self.play(Transform(setB.copy(), setBtarget), run_time = 2)
        minus3 = minus.copy().next_to(setBtarget, RIGHT)
        self.add(minus3)
        i2Target = i.copy().scale(0.3).next_to(minus3, RIGHT)
        self.play(Transform(i.copy(), i2Target), run_time = 2)
        eq5 = eq.copy().next_to(eq4, 5 * DOWN)
        self.add(eq5)
        pBvalTarget = pBval.copy().next_to(eq5, RIGHT)
        self.play(Transform(pBval.copy(), pBvalTarget), run_time = 2)
        minus4 = minus.copy().next_to(pBvalTarget, RIGHT)
        self.add(minus4)
        pAandBValTarget2 = pAandBVal.copy().next_to(minus4, RIGHT)
        self.play(Transform(pAandBVal.copy(), pAandBValTarget2), run_time = 2)
        eq6 = eq.copy().next_to(pAandBValTarget2, RIGHT)
        self.add(eq6)
        pBmoon = Text("0.2", font_size=28, color=GREEN).next_to(eq6, RIGHT)
        self.add(pBmoon)
        self.play(pBmoon.copy().animate.shift(6 * LEFT + 2.35 * UP), run_time = 2)
        
        self.wait(2)
        i = Union(setA, setB, color=YELLOW, fill_opacity=0.4, stroke_width = 7)
        self.play(Create(i), run_time = 1)
        solution = Text("P(A or B) = 0.4 + 0.3 + 0.2 = 0.9", font_size=28, color=YELLOW).shift(3*DOWN)
        self.play(Write(solution), run_time = 2)
        

        self.wait(4)


        



        

        
       
        

        

        
