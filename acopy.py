from manim import *

class CubeA(ThreeDScene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#BDBCA8"

        self.set_camera_orientation(phi=75*DEGREES, theta=35*DEGREES, focal_distance=6)
        # self.begin_3dillusion_camera_rotation()

        axes = ThreeDAxes()

        n = 10
        a = 2.5/n

        # Convert RGB values to hexadecimal
        rgb_to_hex = lambda r, g, b: "#{:02X}{:02X}{:02X}".format(r, g, b)
        

        CUBES = [] 
        A = [[] for j in range(n)]
        Vgroup_A = [[] for j in range(n)]
        for k in range(n):
             for i in range(n-k):
                 for j in range(n-k):
                    A[k] += [ Cube(side_length=a, fill_opacity=1, fill_color=rgb_to_hex(126 + k*(255 - 126)//n, 49 + k*(255 - 49)//n, 55+ k*(255 - 55)//n),stroke_width=3,stroke_color="#0C0C40").move_to(i * RIGHT *a + j * UP*a + k * OUT*a)]     
                    CUBES += [ Cube(side_length=a, fill_opacity=1, fill_color=rgb_to_hex(126 + k*(255 - 126)//n, 49 + k*(255 - 49)//n, 55+ k*(255 - 55)//n),stroke_width=3,stroke_color="#0C0C40").move_to(i * RIGHT*a + j * UP*a + k * OUT*a)]

        for i in range(n):
            Vgroup_A[i] = VGroup(*A[i])


        Vgroup_CUBES=VGroup(*CUBES[i])
        self.add(axes) 
        for i in range(n): 
            self.add(Vgroup_A[i])
            self.wait()

        self.move_camera(phi=0*DEGREES, theta=90*DEGREES, focal_distance=30)


        r=0
        for i in range(n): 
            r += n-i
            self.play(Vgroup_A[i].animate.move_to([n-r,0, 0]))
            self.wait()

        # group_CUBES = VGroup(*CUBES)
        # for i in range(n):
        #     self.add(group_CUBES)
        # self.wait()

class CubeB(ThreeDScene):
    def construct(self):

        n = 5
        a = 2.5/n
        def marge(L,n):
            marge = (L - ((((n+1)*n)/2)*a))/(n-1)
            return marge
        

        # Set background color
        self.camera.background_color = "#BDBCA8"

        self.set_camera_orientation(phi=75*DEGREES, theta=35*DEGREES, focal_distance=6)
        # self.set_camera_orientation(phi=0*DEGREES, theta=90*DEGREES, focal_distance=30)
        self.begin_3dillusion_camera_rotation()

        axes = ThreeDAxes()


        # Convert RGB values to hexadecimal
        rgb_to_hex = lambda r, g, b: "#{:02X}{:02X}{:02X}".format(r, g, b)
        

        CUBES = [] 
        A = [[] for j in range(n)]
        Vgroup_A = [[] for j in range(n)]
        for k in range(n):
             for i in range(n-k):
                 for j in range(n-k):
                    A[k] += [ Cube(side_length=a, fill_opacity=1, fill_color=rgb_to_hex(126 + k*(255 - 126)//n, 49 + k*(255 - 49)//n, 55+ k*(255 - 55)//n),stroke_width=0.75,stroke_color="#0C0C40").move_to(i * RIGHT *a + j * UP*a + k * OUT*a)]     
                    CUBES += [ Cube(side_length=a, fill_opacity=1, fill_color=rgb_to_hex(126 + k*(255 - 126)//n, 49 + k*(255 - 49)//n, 55+ k*(255 - 55)//n),stroke_width=0.75,stroke_color="#0C0C40").move_to(i * RIGHT*a + j * UP*a + k * OUT*a)]

        for i in range(n):
            Vgroup_A[i] = VGroup(*A[i])


        Vgroup_CUBES=VGroup(*CUBES[i])
        self.add(axes) 
        for i in range(n): 
            self.add(Vgroup_A[i])
            self.wait()

        self.move_camera(phi=0*DEGREES, theta=90*DEGREES, focal_distance=30)


        L = 12
        x = L/2 - ((n/2)*a)
        for i in range(n):
            self.add(Vgroup_A[i].move_to([x ,0 , 0]))
            x -= (((n-i)/2) +((n-1-i)/2))*a + marge(L,n)
            self.wait()
