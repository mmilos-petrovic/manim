from manim import *
import manimpango
from colour import Color
from tools import Tools
from constants import Constants as C
config.disable_caching = True

# color , fill_opacity , stroke_width
class LCM(Scene):
    def construct(self):
        title = MarkupText(f'Find <span fgcolor="{YELLOW}">LCM(70, 84, 150)</span> by prime factorisation.',  
                           font_size=24, 
                           color=BLUE).to_edge(UL).shift(0.2 * DOWN)
        self.add(title)
        
        font_size = 26
        dot_size = 50
        two = Text("2", font_size=font_size, color=WHITE)
        three = Text("3", font_size=font_size)
        five = Text("5", font_size=font_size)
        seven = Text("7", font_size=font_size)
        empty = Text("x", font_size=font_size, color=BLACK)
        dot = MathTex(r"\cdot", font_size=dot_size)
        eq = Text("=", font_size=font_size)
        n84 = Text("84", font_size=font_size)
        n150 = Text("150", font_size=font_size)
        n70 = Text("70", font_size=font_size)
        LCM = Text("LCM", font_size=font_size, color = BLUE)
        
        # step 1
        self = Tools.add_step_with_sound(self, 1, "write each number as a product of prime factors.", UL, 1.4 * DOWN, 1)
        
        allNumbers1 = VGroup(
            n70.copy(), eq.copy(), two.copy(), dot.copy(), five.copy(), dot.copy(), seven.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(),
            n84.copy(), eq.copy(), two.copy(), dot.copy(), two.copy(), dot.copy(), three.copy(), dot.copy(), seven.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(),
            n150.copy(), eq.copy(), two.copy(), dot.copy(), three.copy(), dot.copy(), five.copy(), dot.copy(), five.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(),
            empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(),
        ).arrange_in_grid(4, 13, buff=0.5).shift(0.1 * DOWN)
        self.wait(1)
        self.add(allNumbers1[0])
        self.add(allNumbers1[1])
        self.wait(0.5)
        self.add(allNumbers1[13])
        self.add(allNumbers1[14])
        self.wait(0.5)
        self.add(allNumbers1[26])
        self.add(allNumbers1[27])
        self.wait(1)
        for i in range(2, 7):
            self = Tools.add_with_click_silent(self, allNumbers1[i], 0.1)
        self.wait(1)
        for i in range(15, 22):
            self = Tools.add_with_click_silent(self, allNumbers1[i], 0.1)
        self.wait(1)
        for i in range(28, 35):
            self = Tools.add_with_click_silent(self, allNumbers1[i], 0.1)
        
        
        # # step 2
        self = Tools.add_step_with_sound(self, 2, "match primes vertically.", UL, 1.4 * DOWN, 1)
        allNumbers2 = VGroup(
            n70.copy(), eq.copy(), two.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), dot.copy(), five.copy(), empty.copy(), empty.copy(), dot.copy(), seven.copy(),
            n84.copy(), eq.copy(), two.copy(), dot.copy(), two.copy(), dot.copy(), three.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), dot.copy(), seven.copy(),
            n150.copy(), eq.copy(), empty.copy(), empty.copy(), two.copy(), dot.copy(), three.copy(), dot.copy(), five.copy(), dot.copy(), five.copy(), empty.copy(), empty.copy(),
            empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(), empty.copy(),
        ).arrange_in_grid(4, 13, buff=0.5).shift(0.1 * DOWN)
        
        self.wait(1)
        self.play(Transform(allNumbers1, allNumbers2), run_time = 2)
        self.wait(2)

        #step 3
        self = Tools.add_step_with_sound(self, 3, "bring down numbers in each column.", UL, 1.4 * DOWN, 1)
        box_time = 0.3
        num_time = 0.2
        
        self.add(LCM.copy().set_color(BLUE).move_to(allNumbers2[39].get_center()))
        self.add(eq.copy().set_color(BLUE).move_to(allNumbers2[40].get_center()))
        box1 = SurroundingRectangle(VGroup(allNumbers2[2], allNumbers2[41]), color=BLUE)
        self.add(box1)
        self = Tools.sound(self, C.SOUND_CLICK_SILENT, num_time + 0.1)
        self.play(allNumbers2[2].copy().set_color(BLUE).animate().move_to(allNumbers2[41].get_center()), run_time = num_time)

        box2 = SurroundingRectangle(VGroup(allNumbers2[3], allNumbers2[42]), color=BLUE)
        self.play(Transform(box1, box2, replace_mobject_with_target_in_scene=True), run_time = box_time)
        self.play(allNumbers2[16].copy().animate().move_to(allNumbers2[42].get_center()), run_time = num_time)
        
        box3 = SurroundingRectangle(VGroup(allNumbers2[4], allNumbers2[43]), color=BLUE)
        self.play(Transform(box2, box3, replace_mobject_with_target_in_scene=True), run_time = box_time)
        self = Tools.sound(self, C.SOUND_CLICK_SILENT, num_time + 0.1)
        self.play(allNumbers2[17].copy().set_color(BLUE).animate().move_to(allNumbers2[43].get_center()), run_time = num_time)

        box4 = SurroundingRectangle(VGroup(allNumbers2[5], allNumbers2[44]), color=BLUE)
        self.play(Transform(box3, box4, replace_mobject_with_target_in_scene=True), run_time = box_time)
        self.play(allNumbers2[18].copy().animate().move_to(allNumbers2[44].get_center()), run_time = num_time)

        box5 = SurroundingRectangle(VGroup(allNumbers2[6], allNumbers2[45]), color=BLUE)
        self.play(Transform(box4, box5, replace_mobject_with_target_in_scene=True), run_time = box_time)
        self = Tools.sound(self, C.SOUND_CLICK_SILENT, num_time + 0.1)
        self.play(allNumbers2[19].copy().set_color(BLUE).animate().move_to(allNumbers2[45].get_center()), run_time = num_time)

        box6 = SurroundingRectangle(VGroup(allNumbers2[7], allNumbers2[46]), color=BLUE)
        self.play(Transform(box5, box6, replace_mobject_with_target_in_scene=True), run_time = box_time)
        self.play(allNumbers2[33].copy().animate().move_to(allNumbers2[46].get_center()), run_time = num_time)

        box7 = SurroundingRectangle(VGroup(allNumbers2[8], allNumbers2[47]), color=BLUE)
        self.play(Transform(box6, box7, replace_mobject_with_target_in_scene=True), run_time = box_time)
        self = Tools.sound(self, C.SOUND_CLICK_SILENT, num_time + 0.1)
        self.play(allNumbers2[8].copy().set_color(BLUE).animate().move_to(allNumbers2[47].get_center()), run_time = num_time)

        box8 = SurroundingRectangle(VGroup(allNumbers2[9], allNumbers2[48]), color=BLUE)
        self.play(Transform(box7, box8, replace_mobject_with_target_in_scene=True), run_time = box_time)
        self.play(allNumbers2[35].copy().animate().move_to(allNumbers2[48].get_center()), run_time = num_time)

        box9 = SurroundingRectangle(VGroup(allNumbers2[10], allNumbers2[49]), color=BLUE)
        self.play(Transform(box8, box9, replace_mobject_with_target_in_scene=True), run_time = box_time)
        self = Tools.sound(self, C.SOUND_CLICK_SILENT, num_time + 0.1)
        self.play(allNumbers2[36].copy().set_color(BLUE).animate().move_to(allNumbers2[49].get_center()), run_time = num_time)

        box10 = SurroundingRectangle(VGroup(allNumbers2[11], allNumbers2[50]), color=BLUE)
        self.play(Transform(box9, box10, replace_mobject_with_target_in_scene=True), run_time = box_time)
        self.play(allNumbers2[11].copy().animate().move_to(allNumbers2[50].get_center()), run_time = num_time)

        box11 = SurroundingRectangle(VGroup(allNumbers2[12], allNumbers2[51]), color=BLUE)
        self.play(Transform(box10, box11, replace_mobject_with_target_in_scene=True), run_time = box_time)
        self = Tools.sound(self, C.SOUND_CLICK_SILENT, num_time + 0.1)
        self.play(allNumbers2[12].copy().set_color(BLUE).animate().move_to(allNumbers2[51].get_center()), run_time = num_time)
        self.play(FadeOut(box11))
        
        #step 4
        self = Tools.add_step_with_sound(self, 4, "multiply last row.", UL, 1.4 * DOWN, 1)
        rez = Text("LCM = 2100", font_size=font_size, color = BLUE).next_to(allNumbers2, 3.3 * DOWN)
        box = SurroundingRectangle(rez, buff=0.3, color=BLUE)
        self.wait(1)
        self.add(rez)
        self = Tools.create_with_sound(self, box, 0, 0.5, 1)
        self.wait(3)

        