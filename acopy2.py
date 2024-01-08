from manim import *


class CubeA(ThreeDScene):
    def construct(self):

        n = 5
        a = 2.5/n
        def marge(L,n):
            marge = (L - ((((n+1)*n)/2)*a))/(n-1)
            return marge
        

        # Set background color
        self.camera.background_color = "#203343"

        self.set_camera_orientation(phi=75*DEGREES, theta=35*DEGREES, focal_distance=6)
        # self.set_camera_orientation(phi=0*DEGREES, theta=90*DEGREES, focal_distance=30)
        self.begin_3dillusion_camera_rotation(0.2)

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


class CubeB(ThreeDScene):
    def construct(self):

        n = 5
        a = 2.5/n
        def marge(L,n):
            marge = (L - ((((n+1)*n)/2)*a))/(n-1)
            return marge
        

        # Set background color
        self.camera.background_color = "#203343"

        self.set_camera_orientation(phi=75*DEGREES, theta=35*DEGREES, focal_distance=6)
        # self.set_camera_orientation(phi=0*DEGREES, theta=90*DEGREES, focal_distance=30)
        self.begin_3dillusion_camera_rotation(0.2)

        axes = ThreeDAxes()


        # Convert RGB values to hexadecimal
        rgb_to_hex = lambda r, g, b: "#{:02X}{:02X}{:02X}".format(r, g, b)
        

        CUBES = [] 
        B = [[] for j in range(n)]
        Vgroup_B = [[] for j in range(n)]
        for k in range(n):
             for i in range(n-k):
                 for j in range(n-k):
                    B[j] += [ Cube(side_length=a, fill_opacity=1, fill_color=rgb_to_hex(126 + j*(255 - 126)//n, 49 + j*(255 - 49)//n, 55+ j*(255 - 55)//n),stroke_width=0.75,stroke_color="#0C0C40").move_to(i * RIGHT *a + j * UP*a + k * OUT*a)]     
                    CUBES += [ Cube(side_length=a, fill_opacity=1, fill_color=rgb_to_hex(126 + j*(255 - 126)//n, 49 + j*(255 - 49)//n, 55+ j*(255 - 55)//n),stroke_width=0.75,stroke_color="#0C0C40").move_to(i * RIGHT*a + j * UP*a + k * OUT*a)]

        for i in range(n):
            Vgroup_B[i] = VGroup(*B[i])


        Vgroup_CUBES=VGroup(*CUBES[i])
        self.add(axes) 
        for i in range(n): 
            self.add(Vgroup_B[i])
            # self.wait()

        # self.move_camera(phi=0*DEGREES, theta=90*DEGREES, focal_distance=30)

        L = 12
        y = -L/2 + ((n/2)*a)

        # Create animations for each object in the VGroup
        animations = [Vgroup_B[i].animate.move_to([0, y + 3*i*a , a*(n-1-i)/2]) for i in range(n)]

        # Play all animations simultaneously
        self.play(*animations)
            
        self.wait(8)


class CubeC(ThreeDScene):
    def construct(self):

        n = 5
        a = 2.5/n
        def marge(L,n):
            marge = (L - ((((n+1)*n)/2)*a))/(n-1)
            return marge
        

        # Set background color
        self.camera.background_color = "#203343"

        self.set_camera_orientation(phi=50*DEGREES, theta=25*DEGREES, focal_distance=6)
        # self.set_camera_orientation(phi=0*DEGREES, theta=90*DEGREES, focal_distance=30)
        self.begin_ambient_camera_rotation(about="theta",rate=0.02)

        axes = ThreeDAxes()


        # Convert RGB values to hexadecimal
        rgb_to_hex = lambda r, g, b: "#{:02X}{:02X}{:02X}".format(r, g, b)



        L = []
        K = []

        for i in range(n):
            l1 = VGroup()
            l2 = VGroup()
            for j in range(i, n):
                for k in range(n - j):
                    cube1 = Cube(
                        side_length=a,
                        fill_opacity=1,
                        fill_color=rgb_to_hex(
                            126 + i * (255 - 126) // n,
                            49 + i * (255 - 49) // n,
                            55 + i * (255 - 55) // n,
                        ),
                        stroke_width=0.75,
                        stroke_color="#0C0C40"
                    ).move_to(i * RIGHT * a + j * UP * a + k * OUT * a)

                    l1.add(cube1)

                    if i != 0:
                        cube2 = Cube(
                            side_length=a,
                            fill_opacity=1,
                            fill_color=rgb_to_hex(
                                24 + i * (255 - 24) // n,
                                108 + i * (255 - 108) // n,
                                110 + i * (255 - 110) // n,
                            ),
                            stroke_width=0.75,
                            stroke_color="#0C0C40"
                        ).move_to(j * RIGHT * a + (i-1) * UP * a + k * OUT * a)

                        l2.add(cube2)

            L.append(l1)
            if i != 0:
                K.append(l2)

        # VGroup for each row
        Vgroup_C = VGroup(*L)

        # Remove the first row if it exists
        # K.remove(K[0])

        # VGroup for each additional row
        Vgroup_K = VGroup(*K)


        # You can add Vgroup_C and Vgroup_K to the scene as needed
        self.add(axes,Vgroup_C,Vgroup_K)


        y = -6
        x = 6

        self.move_camera(phi=0*DEGREES, theta=90*DEGREES, focal_distance=10, zoom=0.8, gamma=45*DEGREES)

        # Create animations for each object in Vgroup_K
        animations1 = [Vgroup_K[i].animate.move_to([0, (-n+i+1)*a*2, 0.5*a*(n-i-1)]) for i in range(len(Vgroup_K))]

        # Create animations for each object in Vgroup_C
        animations2 = [Vgroup_C[i].animate.move_to([(-n+i) * a* 2 , 0, 0.5*a*(n-i)]) for i in range(len(Vgroup_C))]

        self.move_camera(phi=-10*DEGREES, theta=90*DEGREES, focal_distance=10, zoom=0.8, gamma=45*DEGREES)

        # Play all animations simultaneously
        self.play(*animations1, *animations2)

        # self.stop_ambient_camera_rotation()
        # Set the final camera orientation
        

        # self.begin_ambient_camera_rotation()

        self.wait(4)
