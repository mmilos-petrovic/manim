import manimpango
from manim import *
from colour import Color
from tools import Tools
from constants import Constants as C

config.disable_caching = True
config.frame_size = (1080,1920)
config.frame_width = 8
config.frame_height = 14.22

# color , fill_opacity , stroke_width
class HexagonShort(Scene):
    def construct(self):
        self.wait(1)
        title = Text("Area of a hexagon formula", font_size = 36, color = BLUE).to_corner(UP).shift(0.5 * DOWN)
        self =  Tools.add_with_click_silent(self, title, 0)
        trinagle_shift = [-2, -2.5, 0]
        hexagon_formula_shift = [2.7, 0, 0]

        hexagon = RegularPolygon(n = 6, color = BLUE, fill_opacity = 0.5, stroke_width = 6).scale(2).next_to(title, 5 * DOWN)
        points = {}
        labels = {}
        labels2 = {}
        side = hexagon.get_critical_point(DOWN)[0] - hexagon.get_critical_point(DL)[0]
        points['dr'] = Dot(hexagon.get_critical_point(DOWN) + side * 0.5 * RIGHT, z_index = 10)
        points['dl'] = Dot(hexagon.get_critical_point(DOWN) - side * 0.5 * RIGHT, z_index = 10)
        points['r'] = Dot(hexagon.get_critical_point(RIGHT), z_index = 10)
        points['l'] = Dot(hexagon.get_critical_point(LEFT), z_index = 10)
        points['ur'] = Dot(hexagon.get_critical_point(UP) + side * 0.5 * RIGHT, z_index = 10)
        points['ul'] = Dot(hexagon.get_critical_point(UP) - side * 0.5 * RIGHT, z_index = 10)
        points['c'] = Dot(0.5 * hexagon.get_critical_point(DOWN) + 0.5 * hexagon.get_critical_point(UP), z_index = 10)
        labels["a1"] = Tools.twoPointLabel(points['dl'], points['dr'], "a")
        labels["a2"] = Tools.twoPointLabel(points['dr'], points['r'], "a")
        labels["a3"] = Tools.twoPointLabel(points['r'], points['ur'], "a")
        labels["a4"] = Tools.twoPointLabel(points['ur'], points['ul'], "a")
        labels["a5"] = Tools.twoPointLabel(points['ul'], points['l'], "a")
        labels["a6"] = Tools.twoPointLabel(points['l'], points['dl'], "a")
        labels2["a1"] = Tools.twoPointLabel(points['dl'], points['c'], "a", True).set_color(YELLOW)
        labels2["a2"] = Tools.twoPointLabel(points['dr'], points['c'], "a").set_color(YELLOW)
        labels2["a3"] = Tools.twoPointLabel(points['dr'], points['dl'], "a", True).set_color(YELLOW)
        triangle = Polygon(points['dl'].get_center(), points['dr'].get_center(), points['c'].get_center(), color = YELLOW, fill_opacity = 0.5, stroke_width = 6)

        #initial show
        self = Tools.create_with_sound(self, hexagon, 1, 0.4)
        for p in points.values():
            self = Tools.add_with_click_silent(self, p, 0.3)
        self.wait(1)
        for l in labels.values():
            self = Tools.add_with_click_silent(self, l)    
        self = Tools.create_with_sound(self, triangle.copy(), 2, 0.4)
        for l in labels2.values():
            self = Tools.add_with_click_silent(self, l, 0.5)
        
        #five triangles
        self.wait(1)
        self.play(
                AnimationGroup(
                    Create(Polygon(points['dr'].get_center(), points['r'].get_center(), points['c'].get_center(), color = YELLOW_D, fill_opacity = 0.1, stroke_width = 6)), 
                    Create(Polygon(points['ur'].get_center(), points['r'].get_center(), points['c'].get_center(), color = YELLOW_D, fill_opacity = 0.1, stroke_width = 6)), 
                    Create(Polygon(points['ur'].get_center(), points['ul'].get_center(), points['c'].get_center(), color = YELLOW_D, fill_opacity = 0.1, stroke_width = 6)), 
                    Create(Polygon(points['ul'].get_center(), points['l'].get_center(), points['c'].get_center(), color = YELLOW_D, fill_opacity = 0.1, stroke_width = 6)), 
                    Create(Polygon(points['dl'].get_center(), points['l'].get_center(), points['c'].get_center(), color = YELLOW_D, fill_opacity = 0.1, stroke_width = 6)), 
                    lag_ratio=0.8
             ),
        )
        
        Tools.sound(self, C.SOUND_CREATING, 1.5)
        # single triangle
        self.wait(1)
        self.play(
            AnimationGroup(
                triangle.animate.shift(trinagle_shift),
                VGroup(
                    labels2['a1'].copy(),
                    labels2['a2'].copy(),
                    labels2['a3'].copy()
                    ).animate.shift(trinagle_shift),
                lag_ratio = 0.1
            )
        )
        
        self.wait(1)
        tmp1 = Triangle(color = YELLOW, fill_opacity = 0.5).scale(0.4)
        tmp2 = MathTex(r"=\dfrac{a^2 \sqrt{3}}{4}", color = YELLOW, font_size = 36).next_to(tmp1, RIGHT*1.7)
        self.add(VGroup(tmp1, tmp2).next_to(triangle, 2.5 * DOWN))
        
        # solution
        sol1 = RegularPolygon(color = BLUE, fill_opacity = 0.5).scale(0.4)
        sol2 = MathTex(r"= ~ 6 \cdot", font_size = 42).next_to(sol1, RIGHT*1)
        sol3 = tmp1.copy().next_to(sol2, RIGHT*1.2)
        eq1 = VGroup(sol1, sol2, sol3).next_to(tmp1, RIGHT).shift(hexagon_formula_shift)
        self = Tools.add_with_click_silent(self, sol1, 2)
        self = Tools.add_with_click_silent(self, sol2, 1)
        self = Tools.add_with_click_silent(self, sol3, 1)
        
        sol21 = RegularPolygon(color = BLUE, fill_opacity = 0.5).scale(0.4).next_to(sol1, 4 * DOWN)
        sol22 = MathTex(r"= ~ 6 \cdot", font_size = 42, color = WHITE).next_to(sol21, RIGHT*1)
        sol23 = MathTex(r"\frac{a^2 \sqrt{ 3 }}{ 4 }", font_size = 42, color = YELLOW).next_to(sol22, RIGHT*1)
        self = Tools.add_with_click_silent(self, sol21, 1)
        self = Tools.add_with_click_silent(self, sol22, 1)
        self = Tools.add_with_click_silent(self, sol23, 1)
        
        sol31 = RegularPolygon(color = BLUE, fill_opacity = 0.5).scale(0.4).next_to(sol21, 4 * DOWN)
        sol32 = MathTex(r"= \frac{3 a^2 \sqrt{ 3 }}{ 2 }", font_size = 42, color = BLUE).next_to(sol31, RIGHT*1)
        self = Tools.add_with_click_silent(self, sol31, 1)
        self = Tools.add_with_click_silent(self, sol32, 1)
        
        eq3 = VGroup(sol31, sol32)
        box = SurroundingRectangle(eq3, color = BLUE, buff = 0.2) 
        self = Tools.create_with_sound(self, box, 1, 0.3)
        self.wait(3)
       