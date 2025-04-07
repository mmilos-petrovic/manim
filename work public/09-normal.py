from manim import *
import manimpango
import math
from colour import Color
from tools import Tools


# color , fill_opacity , stroke_width
class Normal(Scene):
    def construct(self):
        title1 = Tex("IQ is normally distributed with a mean of ", 
                     "100", 
                     " and a standard deviation of "," 16",
                     ".", font_size=32, color = WHITE).to_edge(UP, buff=0.2)
        title1[1].set_color(YELLOW)
        title1[3].set_color(YELLOW)
        title2 = Tex("What percentage of people have an IQ between", " 80 ", "and", " 112", "?" ,
                              color=WHITE, font_size = 32).next_to(title1, DOWN)
        title2[1].set_color(BLUE)
        title2[3].set_color(BLUE)
        self.add(title1, title2)
        self.wait(2)
        # STEP 1:
        step1 = MarkupText(f'<span fgcolor="{BLUE}">Step 1:</span> Draw a bell curve',
                            font_size = 24).next_to(title2, 3.6 * DOWN).to_edge(LEFT, buff=0.2)
        self.play(Indicate(step1))
        self.wait(1)
        miLabel = MathTex(r" \mu = ", font_size = 32).to_edge(LEFT, buff=0.5).shift(0.8 * UP)
        self.play(Write(miLabel))
        self.play(title1[1].copy().animate.next_to(miLabel, RIGHT), run_time = 2)
        sigmaLabel = MathTex(r" \sigma = ", font_size = 32).to_edge(LEFT, buff=0.5).shift(0.2 * UP)
        self.play(Write(sigmaLabel))
        self.play(title1[3].copy().animate.next_to(sigmaLabel, RIGHT), run_time = 2)

        axLeft = Axes(
            x_range=[50, 150, 10],
            y_range=[0, 10, 2],
            x_length=5,
            y_length=2,
            x_axis_config={"numbers_to_include": np.arange(60, 140.1, 40), "font_size" : 28},
            y_axis_config={"stroke_width" : 0},
            tips=False,
        ).set_z_index(10).to_edge(LEFT, buff = 0.5).shift(0.1 * DOWN)
        graph = axLeft.plot(lambda x: 400/(16*math.sqrt(2*PI)) * math.exp(-(x-100)**2/(2*16*16)) + 0.5,
                            color = BLUE, stroke_width = 3, z_index = 10)
        self.play(Create(axLeft), Create(graph, run_time = 3))

        
        # STEP 2:
        step2 = MarkupText(f'<span fgcolor="{BLUE}">Step 2:</span> Shade the area bwtween <span fgcolor="{BLUE}">80</span> and <span fgcolor="{BLUE}">112</span>.',
                            font_size = 24).next_to(title2, 3.6 * DOWN).to_edge(LEFT, buff=0.5)
        self.play(FadeOut(step1))
        self.play(Indicate(step2))
        dot1 = Dot(axLeft.coords_to_point(80, 0), color=BLUE, z_index = 20, radius=0.06)
        self.add(dot1)
        self.play(title2[1].copy().animate.next_to(dot1, DOWN), run_time = 2)
        dot2 = Dot(axLeft.coords_to_point(112, 0), color=BLUE, z_index = 20, radius=0.06)
        self.add(dot2)
        self.play(title2[3].copy().animate.next_to(dot2, DOWN), run_time = 2)
        area = axLeft.get_area(graph = graph, x_range=(80,112), color=(BLUE, BLUE_C)
                               , opacity=0.7)
        self.play(Create(area), run_time = 3)
        
        #step 3
        step3 = MarkupText(f'<span fgcolor="{BLUE}">Step 3:</span> Find the z-scores for 80 and 112. ',
                            font_size = 24).next_to(title2, 3.6 * DOWN).to_edge(LEFT, buff=0.5)
        self.play(FadeOut(step2))
        self.play(Indicate(step3))
        
        formula1 = MathTex(r"z_1 = \frac{x_1 - \mu}{ \sigma } =", font_size = 28).to_edge(LEFT, buff = 0.5).shift(2.3 * DOWN)
        formula2 = MathTex(r"\frac{80 - 100}{ 16 } =", font_size = 28).next_to(formula1, RIGHT)
        formula3 = MathTex(r"-1.25", font_size = 28).next_to(formula2, RIGHT)
        self.play(Write(formula1))
        self.play(Write(formula2))
        self.play(Write(formula3))
        self.wait(2)

        formula4 = MathTex(r"z_2 = \frac{x_2 - \mu}{ \sigma } =", font_size = 28).to_edge(LEFT, buff = 0.5).shift(3.2 * DOWN)
        formula5 = MathTex(r"\frac{112 - 100}{ 16 } =", font_size = 28).next_to(formula4, RIGHT)
        formula6 = MathTex(r"0.75", font_size = 28).next_to(formula5, RIGHT)
        self.play(Write(formula4))
        self.play(Write(formula5))
        self.play(Write(formula6))
        self.wait(1)

        #step 4
        step4 = MarkupText(f'<span fgcolor="{BLUE}">Step 4:</span> Draw a standard normal distribution (Z-Distribution) ',
                            font_size = 24).next_to(title2, 3.6 * DOWN).to_edge(LEFT, buff=0.5)
        self.play(FadeOut(step3))
        self.play(Indicate(step4))
        axRight = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 14, 20],
            x_length=5,
            y_length=2,
            x_axis_config={"numbers_to_include": np.arange(-3, 3.1, 3), "font_size" : 28},
            y_axis_config={"numbers_to_include": np.arange(0, 10, 50)},
            tips=False,
        ).to_edge(RIGHT, buff = 0.5).shift(0.1 * DOWN)
        graphRight = axRight.plot(lambda x: 35/(math.sqrt(2 * PI)) * math.exp(-x**2/2) + 0.4,
                                  color = GREEN, stroke_width = 3, z_index = 10)
        self.play(Create(axRight), Create(graphRight, run_time = 3))
        self.wait(2)

        #step 4b
        dot1right = Dot(axRight.coords_to_point(-1.25, 0), color=GREEN, z_index = 20, radius=0.06)
        dot2right = Dot(axRight.coords_to_point(0.75, 0), color=GREEN, z_index = 20, radius=0.06)
        self.add(dot1right, dot2right)
        self.play(formula3.copy().set_color(GREEN).animate().next_to(dot1right, DOWN))
        self.play(formula6.copy().set_color(GREEN).animate().next_to(dot2right, DOWN))
        areaRight = axRight.get_area(graph = graphRight, x_range=(-1.25, 0.75))
        self.play(Transform(area.copy(), areaRight), run_time = 3)

        #step 5
        step5 = MarkupText(f'<span fgcolor="{BLUE}">Step 5:</span> Find the shaded area using standard normal distribution table',
                            font_size = 24).next_to(title2, 3.6 * DOWN).to_edge(LEFT, buff=0.5)
        self.play(FadeOut(step4))
        self.play(Indicate(step5))

        eq = Text("=", font_size=35)
        minus = Text("-", font_size=50)
        areaInf1 = axRight.get_area(graph = graphRight, x_range=(-3, 0.75), color=GREEN, z_index = 30).set_opacity(0.5)
        areaInf2 = axRight.get_area(graph = graphRight, x_range=(-3, -1.25), color=GREEN, z_index = 30).set_opacity(0.5)

        areaRightTarget = areaRight.copy().set_opacity(1).scale(0.3).shift(3 * LEFT + 2.5 * DOWN)
        eq1 = eq.next_to(areaRightTarget, RIGHT)
        areaInf1Targt = areaInf1.copy().set_opacity(1).scale(0.25).next_to(eq1, RIGHT)
        minus1 = minus.next_to(areaInf1Targt, RIGHT)
        areaInf2Targt = areaInf2.copy().set_opacity(1).scale(0.35).next_to(minus1, RIGHT)
        
        self.play(Transform(areaRight.copy(), areaRightTarget), run_time = 3)
        self.add(eq1)
        self.add(areaInf1)
        self.wait(2)
        self.play(Transform(areaInf1, areaInf1Targt), run_time = 3)
        self.add(minus1)
        self.add(areaInf2)
        self.wait(2)
        self.play(Transform(areaInf2, areaInf2Targt), run_time = 3)
        eq2 = eq.copy().next_to(eq1, 2.3 * DOWN)
        self.add(eq2)

        sol1 = Text("0.7734", font_size=20).next_to(eq2, RIGHT)
        self.wait(0.5)
        minus2 = minus.copy().next_to(sol1, RIGHT)
        self.add(sol1)
        self.add(minus2)
        sol2 = Text("0.1056", font_size=20).next_to(minus2, RIGHT)
        self.wait(0.5)
        self.add(sol2)
        eq3 = eq.copy().next_to(eq2, 1.6 * DOWN)
        sol3 = Text("0.6678 = 67%", font_size=20).next_to(eq3, RIGHT)
        self.add(eq3)
        self.add(sol3)

        self.wait(6)
        
        
        
        



        

        
       
        

        

        
