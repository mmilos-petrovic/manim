
import manimpango
from manim import *
from colour import Color
from constants import Constants as C
import collections.abc

class Tools:
    
    @staticmethod
    def add_step_with_sound(self, stepNo, text, pos, shift = (0,0,0), waitBefore = 0.0):
        lastStepIndex = -1
        for i in range(len(self.mobjects)):
            if isinstance(self.mobjects[i], Text):
                if "Step" in self.mobjects[i].text: 
                    lastStepIndex = i
        
        if waitBefore > 0:
            self.wait(waitBefore)
        step1 = Text("Step " + str(stepNo) + ": " + text, 
                     font_size = 26, 
                     t2c = {"Step " + str(stepNo): YELLOW},
                     line_spacing = 1.3
                     ).to_edge(pos).shift(shift)
        self = Tools.sound(self, C.SOUND_STEP, 0.5)
        if lastStepIndex > 0:
            self.play(
                AnimationGroup(
                    FadeOut(self.mobjects[lastStepIndex]),
                    Write(step1),
                    lag_ratio=0.5
                ),
                run_time = 2
                )
        else:
            self.play(Write(step1), run_time = 1)
        return self
    
    @staticmethod
    def create_with_sound(self, mobject, secBefore = 0.0, secRunTime = 1):
        self = Tools.sound(self, C.SOUND_CREATING, secBefore, secRunTime * 0.9)
        if not isinstance(mobject, collections.abc.Sequence):
            mobject = [mobject]
        anims = []
        for e in mobject:
            anims.append(Create(e))
        self.play(*anims, run_time = secRunTime)    
        return self
    
    @staticmethod
    def transform_with_move(self, mobjectFrom, mobjectTo, secBefore = 0.0, secRunTime = 1):
        self = Tools.sound(self, C.SOUND_CREATING, secBefore, secRunTime * 0.8)
        self.play(TransformFromCopy(mobjectFrom, mobjectTo), run_time = secRunTime)
        return self
    
    @staticmethod
    def move(self, mobjectFrom, mobjectTo, secBefore = 0.0, secRunTime = 1):
        self = Tools.sound(self, C.SOUND_CREATING, secBefore, secRunTime * 0.8)
        self.play(Transform(mobjectFrom, mobjectTo), run_time = secRunTime)
        return self
    
    @staticmethod
    def move_with_clik(self, mobjectFrom, mobjectTo, secBefore = 0.0, secRunTime = 1):
        self = Tools.sound(self, C.SOUND_CLICK_PEN, secBefore, secRunTime * 1)
        self.play(Transform(mobjectFrom, mobjectTo), run_time = secRunTime)
        return self
    
    @staticmethod
    def move_to_with_click(self, mobjectFrom, destination, secBefore = 0.0, secRunTime = 1):
        self = Tools.sound(self, C.SOUND_CLICK_PEN, secBefore, secRunTime * 1)
        if not isinstance(mobjectFrom, collections.abc.Sequence):
            mobjectFrom = [mobjectFrom]
        anims = []
        for e in mobjectFrom:
            anims.append(e.animate().move_to(destination))    
        self.play(*anims,
                  run_time = secRunTime
                  )
        return self
    
    @staticmethod
    def transform_with_pen_clikc(self, mobjectFrom, mobjectTo, secBefore = 0.0, secRunTime = 1):
        self = Tools.sound(self, C.SOUND_CLICK_PEN, secBefore, secRunTime * 0.9)
        self.play(TransformFromCopy(mobjectFrom, mobjectTo), run_time = secRunTime)
        return self
    
    @staticmethod
    def add_with_click_silent(self, mobject, secBefore = 0.0):
        if secBefore > 0:
            self.wait(secBefore)
        self = Tools.sound(self, C.SOUND_CLICK_SILENT, 0.2)
        self.add(mobject)
        return self
    
    @staticmethod
    def add_with_click1(self, mobject, secBefore = 0.0):
        if secBefore > 0:
            self.wait(secBefore)
        self = Tools.sound(self, C.SOUND_CLICK_LOUD, 0.2)
        self.add(mobject)
        return self
    
    @staticmethod
    def add_with_click_short(self, mobject, secBefore = 0.0):
        if secBefore > 0:
            self.wait(secBefore)
        self = Tools.sound(self, C.SOUND_CLICK_SHORT, 0.2)
        self.add(mobject)
        return self
    
    @staticmethod
    def add_with_click_pen(self, mobject, secBefore = 0.0):
        if secBefore > 0:
            self.wait(secBefore)
        self = Tools.sound(self, C.SOUND_CLICK_PEN, 0.3)
        self.add(mobject)
        return self
    
    @staticmethod
    def delete_withot_sound(self, mobject, secBefore = 0.0):
        if secBefore > 0:
            self.wait(secBefore)
        self.remove(mobject)
        return self
    
    
    @staticmethod
    def delete_with_sound(self, mobject, secBefore = 0.0, secSoundWait = 0.2):
        if secBefore > 0:
            self.wait(secBefore)
        self = Tools.sound(self, C.SOUND_DELETE, secSoundWait)
        self.remove(mobject)
        return self
                
    @staticmethod    
    def sound(self, sound_alias, secBefore = 0.0, soundOffset = 0.0):
        if secBefore > 0:
            self.wait(secBefore)
        if sound_alias == C.SOUND_CLICK_LOUD:
            self.add_sound('sounds/click_loud.mp3', time_offset = soundOffset)
        if sound_alias == C.SOUND_CLICK_SILENT:
            self.add_sound('sounds/click_silent.mp3', time_offset = soundOffset)
        if sound_alias == C.SOUND_CLICK_SHORT:
            self.add_sound('sounds/click-pen.mp3', time_offset = soundOffset)
        if sound_alias == C.SOUND_CLICK_PEN:
            self.add_sound('sounds/click-short.wav', time_offset = soundOffset)
        if sound_alias == C.SOUND_CREATED:
            self.add_sound('sounds/created.wav', time_offset = soundOffset)
        if sound_alias == C.SOUND_CREATING:
            self.add_sound('sounds/creating-03.wav', time_offset = soundOffset)
        if sound_alias == C.SOUND_STEP:
            self.add_sound('sounds/step2.mp3', time_offset = soundOffset)
        if sound_alias == C.SOUND_DELETE:
            self.add_sound('sounds/delete.mp3', time_offset = soundOffset)
        if sound_alias == C.SOUND_MOVE:
            self.add_sound('sounds/move.wav', time_offset = soundOffset)

        return self
        
    @staticmethod
    def twoPointLabel(dot1: Dot, dot2: Dot, label: str, changeDirection = False, font_size = 46) -> MathTex:
        line = Line(dot1, dot2)
        return Tools.lineLabel(line, label, changeDirection, font_size)


    @staticmethod
    def lineLabel(line: Line, label: str, changeDirection = False, font_size = 46) -> MathTex:
        label = MathTex(label, font_size = font_size).move_to(midpoint(line.end, line.start))
        vecX = round(line.copy().rotate(PI/2).get_unit_vector()[0],2)
        vecY = round(line.copy().rotate(PI/2).get_unit_vector()[1],2)
        if changeDirection:
            vecX = -vecX
            vecY = -vecY
        label.shift(LEFT * vecX * 0.3 + DOWN * vecY * 0.3)
        return label

    