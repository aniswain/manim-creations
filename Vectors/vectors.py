from manim import *
import math

class AddVector(Scene):
    def construct(self):
        plane = NumberPlane()
        vector_1 = Vector([3,0], color=RED)
        vector_2 = Vector([0,3], color=BLUE)
        vector_3 = Vector([3,3], color=YELLOW)
        # label_1 = vector_1.coordinate_label()
        # label_2 = vector_2.coordinate_label(color=YELLOW_A)
        self.add(plane)
        self.play(Create(vector_1), Create(vector_2))
        self.wait(1)
        self.play(vector_2.animate.shift((3,0,0)))
        
        
        self.play(Create(vector_3))
        # self.add(label_1, label_2)
        self.wait(2)

class Test(Scene):
    def construct(self):
        tex = MathTex("x^2")
        self.play(Write(tex))
        self.wait()

class exponential(Scene):
    def construct(self):
        plane = NumberPlane(x_range=(-10,10,1), y_range=(-10,10,1))
        curve = plane.plot(lambda x: math.e**x, color=RED)
        area = plane.get_area(curve, x_range=(-10,2))
        self.add(plane)
        self.play(Create(curve, run_time=3))
        self.play(FadeIn(area))