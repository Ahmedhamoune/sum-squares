from manim import *
from matplotlib import mathtext

class CubeExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

        axes = ThreeDAxes()
        cube = Cube(side_length=3, fill_opacity=0.7, fill_color=BLUE)
        self.add(cube)
        self.wait()


        List_Cubes = []
        Listtt = []
        for j in range(n):
             kkk = []
             for i in range(j):  
                 for k in range(j):
                    List_Cubes += [ Cube(side_length=1, fill_opacity=1, fill_color=rgb_to_hex(126 + k*(255 - 126)//n, 49 + k*(255 - 49)//n, 55+ k*(255 - 55)//n),stroke_width=3,stroke_color="#0C0C40").move_to(i * RIGHT + j * UP + k * OUT)]
                    kkk += [ Cube(side_length=1, fill_opacity=1, fill_color=rgb_to_hex(126 + k*(255 - 126)//n, 49 + k*(255 - 49)//n, 55+ k*(255 - 55)//n),stroke_width=3,stroke_color="#0C0C40").move_to(i * RIGHT + j * UP + k * OUT)]
             Listtt += [kkk]
       # Vgroup_Cube = VGroup(*List_Cubes)
        Vgroup_Cube = VGroup(*Listtt[0])

        self.add(Vgroup_Cube)
        self.wait()

class SquareWithMeasurement(Scene):
    def construct(self):
        # Create a square
        square = Square(side_length=2, fill_opacity=0.7, fill_color="#7E3137")

        # Calculate bottom-left and bottom-right points
        bottom_left = square.get_bottom() + square.get_left()
        bottom_right = square.get_bottom() + square.get_right()

        # Create a line representing the side length
        side_length_line = DashedLine(bottom_left-1*UP, bottom_right-1*UP, color=YELLOW)


        # Create a text to display the length
        # length_text = mathtext("2", color=YELLOW).next_to(side_length_line, DOWN)

        # Add square, line, and text to the scene
        self.add(square)
        self.add(side_length_line)
