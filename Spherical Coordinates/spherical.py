from manim import *
from manim.opengl import *
import math

def projection(vector:np.array, target:np.array):
    return (np.dot(vector, target)/np.dot(target, target))*target

# vectors
ARB_VECTOR = np.array([1,1,1])
THETA = np.arccos(np.dot(ARB_VECTOR, Z_AXIS)/(np.linalg.norm(ARB_VECTOR))*np.linalg.norm(Z_AXIS))
E_R = np.array([1/math.sqrt(3)]*3)
E_THETA = np.array([1/2, 1/2, -1/math.sqrt(2)])
E_PHI = np.array([-1/math.sqrt(2), 1/math.sqrt(2), 0])


class SphericalSetup(Scene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=(-3, 3),
            y_range=(-3, 3),
            z_range=(0, 2),
            z_length=2
            )
        x_label = axes.get_x_axis_label("X")
        y_label = axes.get_y_axis_label("Y")
        z_label = axes.get_z_axis_label("Z")
        self.add(axes, x_label, y_label, z_label)

        self.play(self.camera.animate.set_euler_angle(phi=70*DEGREES, theta=15*DEGREES))

        # Added arbitrary vector and add the projection of arb vector onto z-axis
        vector1 = Arrow(ORIGIN, ARB_VECTOR)
        vector1_dup = Arrow3D(ORIGIN, ARB_VECTOR, color=WHITE)
        self.add(vector1, vector1_dup)
        ARB_RPOJ_ZAXIS = projection(vector1_dup.get_end(), Z_AXIS)
        self.play(ReplacementTransform(vector1_dup, Arrow3D(ORIGIN, ARB_RPOJ_ZAXIS, color=PURPLE)))
        theta = ArcBetweenPoints(Z_AXIS*0.25, ARB_VECTOR*0.25,  stroke_color=YELLOW).rotate(-90*DEGREES, axis=ARB_VECTOR*0.25 - Z_AXIS*0.25)
        self.play(Create(theta))
        self.wait(1)


        # # Create unit vector e_r
        v_r_hat = Arrow3D(ORIGIN, E_R, color=RED).shift(ARB_VECTOR)
        v_r_hat_dup= Arrow3D(ORIGIN, E_R, color=RED).shift(ARB_VECTOR)
        # Create unit vector e_theta
        v_t_hat = Arrow3D(ORIGIN, E_THETA, color=BLUE).shift(ARB_VECTOR)
        v_t_hat_dup = Arrow3D(ORIGIN, E_THETA, color=BLUE).shift(ARB_VECTOR)
        # Create unit vector e_phi
        v_p_hat = Arrow3D(ORIGIN, E_PHI, color=GREEN).shift(ARB_VECTOR)
        v_p_hat_dup = Arrow3D(ORIGIN, E_PHI, color=GREEN).shift(ARB_VECTOR)
        self.play(Create(v_r_hat), Create(v_t_hat), Create(v_p_hat), Create(v_r_hat_dup))
        self.wait(2)
        # Remove the unit vectors
        self.play(FadeOut(v_t_hat), FadeOut(v_p_hat))

        #BEGIN ANIMATIONS TRANSLATIONS
        V_R_PROJXY = np.array([ARB_VECTOR[0], ARB_VECTOR[1], 0])
        v_r_hat.generate_target()
        v_r_hat.target.shift([0, 0, -1])
        self.play(MoveToTarget(v_r_hat))
        arrow_end = projection(v_r_hat.get_end(), V_R_PROJXY)
        vert_line = Arrow3D(ARB_VECTOR, v_r_hat.get_start() + V_R_PROJXY, color=PURPLE)
        self.add(v_r_hat)
        

        self.play(ReplacementTransform(v_r_hat, Arrow3D(V_R_PROJXY, arrow_end+V_R_PROJXY, color=RED)))
        join_line = Arrow3D(ARB_VECTOR, arrow_end+V_R_PROJXY, color=PURPLE)
        self.add(vert_line, join_line)

        self.play(Animation(self.begin_ambient_camera_rotation(rate=PI/2), run_time=4))

        # self.play(Rotate(v_r_hat_dup, angle=45*DEGREES, about_point=v_r_hat_dup.get_start(), axis=np.cross(v_r_hat_dup.get_end(), v_r_hat.get_end())+v_r_hat_dup.get_start()))
        theta2 = ArcBetweenPoints(v_r_hat.get_end()*0.25, v_r_hat_dup.get_end()*0.25)

        # theta2 = ArcBetweenPoints(Z_AXIS*0.25, ARB_VECTOR*0.25,  stroke_color=YELLOW).rotate(-90*DEGREES, axis=ARB_VECTOR*0.25 - Z_AXIS*0.25)
        # self.play(Transform(v_r_hat, Arrow3D(np.array([1,1,0]), np.array([1,1,0]) + V_R_PROJXY, color=RED)))
        # vertical_z = Arrow3D(ARB_VECTOR, np.array([1,1,0]))
        # r_to_projection = Arrow(ARB_VECTOR, np.array([1,1,0]) + V_R_PROJXY)
        # self.play(Create(vertical_z), Create(r_to_projection))
        # self.wait(1)
        self.interactive_embed()