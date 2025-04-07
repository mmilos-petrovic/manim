from manim import *
from manim.opengl import *
import manimpango
import math
from colour import Color
from tools import Tools
from constants import Constants as C
config.disable_caching = True

# color , fill_opacity , stroke_width
class Test2(Scene):


    
            
    def construct(self):
        circle = Circle(radius = 1)
        self = Tools.add_with_click_silent(self, circle, 1)
        self.wait(1)
        

       
        

