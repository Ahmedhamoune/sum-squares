from manim import *

class CubeExample(ThreeDScene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#BDBCA8"

        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

        axes = ThreeDAxes()

        n = 5

        # Convert RGB values to hexadecimal
        rgb_to_hex = lambda r, g, b: "#{:02X}{:02X}{:02X}".format(r, g, b)
        
        # Create a 3D grid of cubes
        """List_Cube = [
            Cube(side_length=1, fill_opacity=1, fill_color=rgb_to_hex(126 + k*(255 - 126)//n, 49 + k*(255 - 49)//n, 55+ k*(255 - 55)//n),stroke_width=3,stroke_color="#0C0C40").move_to(i * RIGHT + j * UP + k * OUT)
            for j in range(n)  # Y-axis
            for i in range(j)  # X-axis
            for k in range(j)  # Z-axis
        ]"""

        List_Cubes = []
        List_Cube1 = []
        List_Cube2 = []
        List_Cube3 = []
        List_Cube4 = []
        for j in range(n):
             for i in range(j):
                 for k in range(j):
                    if k == 0:
                        List_Cube1 += [ Cube(side_length=1, fill_opacity=1, fill_color=rgb_to_hex(126 + k*(255 - 126)//n, 49 + k*(255 - 49)//n, 55+ k*(255 - 55)//n),stroke_width=3,stroke_color="#0C0C40").move_to(i * RIGHT + j * UP + k * OUT)]
                    if k == 1:
                        List_Cube2 += [ Cube(side_length=1, fill_opacity=1, fill_color=rgb_to_hex(126 + k*(255 - 126)//n, 49 + k*(255 - 49)//n, 55+ k*(255 - 55)//n),stroke_width=3,stroke_color="#0C0C40").move_to(i * RIGHT + j * UP + k * OUT)]
                    if k == 2:
                        List_Cube3 += [ Cube(side_length=1, fill_opacity=1, fill_color=rgb_to_hex(126 + k*(255 - 126)//n, 49 + k*(255 - 49)//n, 55+ k*(255 - 55)//n),stroke_width=3,stroke_color="#0C0C40").move_to(i * RIGHT + j * UP + k * OUT)]
                    if k == 3:
                        List_Cube4 += [ Cube(side_length=1, fill_opacity=1, fill_color=rgb_to_hex(126 + k*(255 - 126)//n, 49 + k*(255 - 49)//n, 55+ k*(255 - 55)//n),stroke_width=3,stroke_color="#0C0C40").move_to(i * RIGHT + j * UP + k * OUT)]
                        
                    List_Cubes += [ Cube(side_length=1, fill_opacity=1, fill_color=rgb_to_hex(126 + k*(255 - 126)//n, 49 + k*(255 - 49)//n, 55+ k*(255 - 55)//n),stroke_width=3,stroke_color="#0C0C40").move_to(i * RIGHT + j * UP + k * OUT)]
             

        
        print(List_Cube4
              )
        Vgroup_Cube1 = VGroup(*List_Cube1)
        Vgroup_Cube2 = VGroup(*List_Cube2)
        Vgroup_Cube3 = VGroup(*List_Cube3)
        Vgroup_Cube4 = VGroup(*List_Cube4)

        Vgroup_Cubes = VGroup(Vgroup_Cube1, Vgroup_Cube2, Vgroup_Cube3, Vgroup_Cube4)

        # self.add(axes,Vgroup_Cubes)
        # self.wait()
        self.add(Vgroup_Cube1)
        self.wait()
        self.add(Vgroup_Cube2)
        self.wait()
        self.add(Vgroup_Cube3)
        self.wait()
        self.add(Vgroup_Cube4)
        self.wait()

        new_position = [2, 2, 0]  # New coordinates (x, y, z)
        self.play(Vgroup_Cubes.animate.move_to(new_position))
        self.wait(1)

        # Move the cube to another set of coordinates
        another_position = [-2, -2, 0]  # Another set of coordinates (x, y, z)
        self.play(Vgroup_Cubes.animate.move_to(another_position))
        self.wait(1)