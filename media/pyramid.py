from manim import *

class PyramidScene(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes()

        self.camera.background_color = "#203343"

        self.set_camera_orientation(phi=75*DEGREES, theta=35*DEGREES, gamma=35*DEGREES, zoom=0.5)

        self.add(axes)
        lab = axes.get_z_axis_label(Tex("$z$-label"))
        self.add(lab)
        pyramid = self.create_pyramid(n=8, a=0.3, OUT_XY=False, DOWN_XZd=True)

        self.add(pyramid)


        new_pyramid = self.create_pyramid(n=7, a=0.3)
        #self.play(ReplacementTransform(pyramid, new_pyramid))
        self.wait()
    def create_pyramid(self, n, a,
                    OUT_XY=True, OUT_XdY=False, OUT_XYd=False, OUT_XdYd=False,
                    IN_XY=False, IN_XdY=False, IN_XYd=False, IN_XdYd=False,
                    UP_XZ=False, UP_XdZ=False, UP_XZd=False, UP_XdZd=False,
                    DOWN_XZ=False, DOWN_XdZ=False, DOWN_XZd=False, DOWN_XdZd=False,
                    RIGHT_YZ=False, RIGHT_YdZ=False, RIGHT_YZd=False, RIGHT_YdZd=False,
                    LEFT_YZ=False, LEFT_YdZ=False, LEFT_YZd=False, LEFT_YdZd=False
                    ):
        rgb_t_hex = lambda r, g, b: "#{:02X}{:02X}{:02X}".format(r, g, b)
        pyramid = VGroup()
        for k in range(n):
            for i in range(n - k):
                for j in range(n - k):
                    cube = Cube(
                        side_length=a,
                        fill_opacity=1,
                        fill_color=rgb_t_hex(
                            126 + i * (255 - 126) // n,
                            49 + i * (255 - 49) // n,
                            55 + i * (255 - 55) // n,
                        ),
                        stroke_width=0.75,
                        stroke_color="#0C0C40",
                    )

                    position = None

                    if OUT_XY:
                        position = i * RIGHT * a + j * UP * a + k * OUT * a
                    elif OUT_XdY:
                        position = -i * RIGHT * a + j * UP * a + k * OUT * a
                    elif OUT_XYd:
                        position = i * RIGHT * a  - j * UP * a + k * OUT * a
                    elif OUT_XdYd:
                        position = -i * RIGHT * a - j * UP * a + k * OUT * a
                    elif IN_XY:
                        position = i * RIGHT * a  + j * UP * a - k * OUT * a
                    elif IN_XdY:
                        position = -i * RIGHT * a + j * UP * a - k * OUT * a
                    elif IN_XYd:
                        position = i * RIGHT * a - j * UP * a - k * OUT * a
                    elif IN_XdYd:
                        position = -i * RIGHT * a - j * UP * a - k * OUT * a
                    elif UP_XZ:
                        position = j * RIGHT * a + k * UP * a + i * IN * a
                    elif UP_XdZ:
                        position = -j * RIGHT * a + k * UP * a + i * IN * a
                    elif UP_XZd:
                        position = j * RIGHT * a - k * UP * a + i * IN * a
                    elif UP_XdZd:
                        position = -j * RIGHT * a - k * UP * a + i * IN * a
                    elif DOWN_XZ:
                        position = j * RIGHT * a + k * UP * a - i * IN * a
                    elif DOWN_XdZ:
                        position = -j * RIGHT * a + k * UP * a - i * IN * a
                    elif DOWN_XZd:
                        position = j * RIGHT * a - k * UP * a - i * IN * a
                    elif DOWN_XdZd:
                        position = -j * RIGHT * a - k * UP * a - i * IN * a
                    elif RIGHT_YZ:
                        position = k * RIGHT * a + i * UP * a + j * OUT * a
                    elif RIGHT_YdZ:
                        position =  -k * RIGHT * a + i * UP * a + j * OUT * a
                    elif RIGHT_YZd:
                        position =  k * RIGHT * a - i * UP * a + j * OUT * a
                    elif RIGHT_YdZd:
                        position =  -k * RIGHT * a - i * UP * a + j * OUT * a
                    elif LEFT_YZ:
                        position =  k * RIGHT * a + i * UP * a - j * OUT * a
                    elif LEFT_YdZ:
                        position =  -k * RIGHT * a + i * UP * a - j * OUT * a
                    elif LEFT_YZd:
                        position =  k * RIGHT * a - i * UP * a - j * OUT * a
                    elif LEFT_YdZd:
                        position =  -k * RIGHT * a - i * UP * a - j * OUT * a

                    if position is not None:
                        cube.move_to(position)
                        pyramid.add(cube)

        return pyramid
