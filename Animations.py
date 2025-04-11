from manim import *
import numpy as np

class PowerFiveFunction(Scene):
    def construct(self):
        text = MathTex("f(x) = x^5 + x^2 - x - 0.2" , font_size= 48, color= YELLOW)
        text.to_corner(UL)
        ax = Axes(
            x_length= 6,
            x_range=[-2, 2, 1], 
            axis_config={"include_tip": 0},
            x_axis_config={"numbers_to_include" : np.arange(-2, 2.1, 1)},  
            y_axis_config={"include_ticks" : 0})
        graph = ax.plot(lambda x : x**5+ x**2 - x -0.2, color= YELLOW)
        x0 = Dot(ax.coords_to_point(-1.193, 0), color= RED)
        
        self.add(ax, text)
        self.play(Create(graph, run_time= 4))

class AddingDots(Scene):
    def construct(self):
        text = MathTex("f(x) = x^5 + x^2 - x - 0.2" , font_size= 48, color= YELLOW)
        text.to_corner(UL)
        ax = Axes(
            x_length= 6,
            x_range=[-2, 2, 1], 
            axis_config={"include_tip": 0},
            x_axis_config={"numbers_to_include" : np.arange(-2, 2.1, 1)},  
            y_axis_config={"include_ticks" : 0})
        graph = ax.plot(lambda x : x**5+ x**2 - x -0.2, color= YELLOW)
        
        group = VGroup()
        group.add(ax, graph)
        self.add(ax, text, graph)
        self.play(group.animate.shift(RIGHT * 3), run_time=2)
        self.wait(1)
        root1 = Dot(ax.coords_to_point(-1.193, 0), color= RED, radius= 0.11)
        root2 = Dot(ax.coords_to_point(-0.1709, 0), color= RED, radius= 0.11)
        root3 = Dot(ax.coords_to_point(0.8119, 0), color= RED, radius= 0.11)
        dots = VGroup()
        dots.add(root1, root2, root3)
        self.play(Create(dots,lag_ratio= 1, run_time= 2))
        self.wait(0.5)
        root1Text = MathTex("f(-1.193) = 0", color= YELLOW, font_size= 55).shift([-4.7, 1.2, 0])
        root2Text = MathTex("f(-1.1709) = 0", color= YELLOW, font_size= 55).shift([-4.7, 0, 0])
        root3Text = MathTex("f(0.8119) = 0", color= YELLOW, font_size= 55).shift([-4.7, -1.2, 0])
        #VGroup(root1Text, root2Text, root3Text).arrange(DOWN, buff=1)
        self.add(root1.copy(), root2.copy(), root3.copy())
        self.play(FadeTransform(root1, root1Text))
        self.play(FadeTransform(root2, root2Text))
        self.play(FadeTransform(root3, root3Text))

class HowDoWeComputeThem(Scene):
    def construct(self):
       text = Tex("How do we compute them ? ", color= YELLOW, font_size= 70)
       self.wait(0.5)
       self.play(Write(text), run_time= 1.5)

class NewtonsMethod(Scene):
    def construct(self):
        text = MathTex("f(x) = x^5 + x^2 - x - 0.2" , font_size= 48, color= YELLOW)
        text.to_corner(UL)
        ax = Axes(
            x_length= 6,
            x_range=[-2, 2, 1], 
            axis_config={"include_tip": 0},
            x_axis_config={"numbers_to_include" : np.arange(-2, 2.1, 1)},  
            y_axis_config={"include_ticks" : 0})
        graph = ax.plot(lambda x : x**5+ x**2 - x -0.2, color= YELLOW)
        
        group = VGroup()
        group.add(ax, graph)
        self.add(group.shift(RIGHT * 3), text)
        f = lambda x :  x**5 + x**2 - x -0.2
        fdiff = lambda x : 5*x**4 + 2*x - 1
        x0 = 1.3

        pointerDot = Dot(ax.coords_to_point(x0, 0), color= RED)
        pointerVector = Vector(UP, color= RED).add_updater(lambda m: m.next_to(pointerDot, DOWN))
        
        initialGuessText = MathTex("x_0 = 1.3", color= RED).next_to(text, DOWN*3)
        self.play(Create(pointerDot), Create(pointerVector), run_time=2)
        self.play(ReplacementTransform(pointerDot.copy(), initialGuessText))
        self.wait(2)
        dashedLine = DashedLine(ax.coords_to_point(1.3, 3.5, 0),ax.x_axis.n2p(1.3), color=RED)
        fx0 = MathTex("f(x_0)", color= RED).next_to(dashedLine, RIGHT)
        self.play(Create(dashedLine), Create(fx0))
        self.wait(2)
        tangent = TangentLine(graph, 0.535, length=6, color= RED)
        self.play(Create(tangent))
        self.wait(2)
        x1 = 1.3 - f(1.3)/fdiff(1.3)
        step = Line(pointerDot, ax.x_axis.n2p(x1), color= RED)
        self.play(Create(step))
        self.wait(1)
        slope = Tex("Slope = ", color= RED).shift(LEFT * 3.5)
        self.play(ReplacementTransform(tangent.copy(), slope))
        self.wait(1)
        dyOverDx = MathTex("\\frac{f(x_0)}{-Step}", color=RED).next_to(slope, RIGHT)
        self.play(ReplacementTransform(VGroup(step, dashedLine).copy(), dyOverDx))
        self.wait(1)
        stepText2 = Tex("-Step = ", color=RED).shift(LEFT * 3.5)
        dyOverDx2 = MathTex("\\frac{f(x_0)}{Slope}", color=RED).next_to(stepText2, RIGHT)
        self.play(Transform(slope, stepText2),
                  Transform(dyOverDx, dyOverDx2))
        self.wait(1)
        stepDevelopped = MathTex("- x_1 + x_0 = \\frac{f(x_0)}{f'(x_0)}", color=RED).shift(LEFT * 3.5)
        self.play(Transform(VGroup(slope, dyOverDx), stepDevelopped))
        self.wait(1)
        finalText = MathTex("x_1 = x_0 - \\frac{f(x_0)}{f'(x_0)}", color=RED).shift(LEFT *3.5)
        self.play(Transform(VGroup(slope, dyOverDx), finalText))
        self.wait(1)
        self.play(FadeOut(dashedLine),
                  FadeOut(fx0),
                  FadeOut(step))


        for i in range(1, 6):
            x0 = x0 - f(x0)/fdiff(x0)
            currentDot = Dot(ax.c2p(x0, 0), color=RED)

            initialGuessText2 = MathTex("x_" + str(i) + " = " + str(round(x0, 2)), color= RED).next_to(text, DOWN * 3)

            equation = MathTex("x_" + str(i+1) + " = x_" + str(i) + " - \\frac{f(x_" + str(i) + ")}{f'(x_" + str(i) + ")}", color=RED).shift(LEFT * 3.5)

            fx0 = f(x0)
            dx = 0.001
            pente = (f(x0 + dx) - f(x0)) / dx
            currentTangent = Line(
                start= [ax.coords_to_point(x0 - 1, fx0 - 1 * pente)],
                end= [ax.coords_to_point(x0 + 1, fx0 + 1 * pente)],
                color= RED
            ) 

            self.play(Transform(pointerDot, currentDot),
                      Transform(initialGuessText, initialGuessText2),
                      Transform(VGroup(slope, dyOverDx), equation))
            self.wait(1.5)
            self.play(Transform(tangent,
                        currentTangent))
            self.wait(1)
        self.wait(1)
        self.play(FadeOut(VGroup(slope, dyOverDx)),
                    FadeOut(tangent),
                    FadeOut(pointerDot),
                    FadeOut(initialGuessText),
                    FadeOut(pointerVector))
        self.wait(1)

        graph2 = ax.plot(lambda x : x**5+ x**2 - x + 1 , color= YELLOW)
        newFctText = MathTex("f(x) = x^5 + x^2 - x + 1" , font_size= 48, color= YELLOW)
        newFctText.to_corner(UL)
        self.play(ReplacementTransform(graph, graph2),
                    Transform(text, newFctText))
        self.wait(1)
        
        x0 = 1.3

        pointerDot = Dot(ax.coords_to_point(x0, 0), color= RED)
        pointerVector = Vector(UP, color= RED).add_updater(lambda m: m.next_to(pointerDot, DOWN))
        
        initialGuessText = MathTex("x_0 = 1.3", color= RED).next_to(text, DOWN*3)

        iterationsText = MathTex("x_1 = x_0 - \\frac{f(x_0)}{f'(x_0)}", color=RED).shift(LEFT *3.5)

        self.play(Create(pointerDot),
                    Create(pointerVector),
                    Create(initialGuessText),
                    Create(iterationsText),
                    run_time= 2)
        self.wait(1)

        f = lambda x :  x**5 + x**2 - x + 1
        fdiff = lambda x : 5*x**4 + 2*x - 1 
        fx0 = f(x0)
        dx = 0.00001
        pente = (f(x0 + dx) - f(x0)) / dx
        newTangent = Line(
            start=[ax.coords_to_point(x0 - 1, fx0 - 1 * pente)],
                end= [ax.coords_to_point(x0 + 1, fx0 + 1 * pente)],
                color= RED
            )
        self.play(Create(newTangent))

        for i in range(1, 12):
            x0 = x0 - f(x0)/fdiff(x0)
            currentDot = Dot(ax.c2p(x0, 0), color=RED)

            initialGuessText2 = MathTex("x_{" + str(i) + "} = " + str(round(x0, 2)), color= RED).next_to(text, DOWN * 3)

            equation = MathTex("x_{" + str(i+1) + "} = x_{" + str(i) + "} - \\frac{f(x_{" + str(i) + "})}{f'(x_{" + str(i) + "})}", color=RED).shift(LEFT * 3.5)

            fx0 = f(x0)
            dx = 0.001
            pente = (f(x0 + dx) - f(x0)) / dx
            currentTangent = Line(
                start= [ax.coords_to_point(x0 - 2, fx0 - 2 * pente)],
                end= [ax.coords_to_point(x0 + 2, fx0 + 2 * pente)],
                color= RED
            ) 

            self.play(Transform(pointerDot, currentDot),
                      Transform(initialGuessText, initialGuessText2),
                      Transform(iterationsText, equation),
                      run_time= 0.5)
            self.wait(0.5)
            self.play(Transform(newTangent,
                        currentTangent))
            self.wait(0.5)
        self.wait(2)
        
        

        
            
         
class ComplexPart(Scene):
    def construct(self):
        planeSquare1 = Square(side_length=4).move_to(LEFT * 3).shift(UP * 1)
        plane1 = ComplexPlane(
            x_range=(-2,2,0.5),
            y_range=(-2,2,0.5),
            x_length=4,
            y_length=4
        ).move_to(LEFT * 3).shift(UP * 1)
        planeSquare2 = Square(side_length=4).move_to(RIGHT * 3).shift(UP * 1)
        plane2 = ComplexPlane(
            x_range=(-2,2,0.5),
            y_range=(-2,2,0.5),
            x_length=4,
            y_length=4
        ).move_to(RIGHT * 3).shift(UP * 1)
        planeText1 = MathTex("z", color= YELLOW).next_to(plane1, DOWN)
        planeText2 = MathTex("f(z)", color= YELLOW).next_to(plane2, DOWN)
        inputText = Text("Input", color= YELLOW).next_to(plane1, UP * 0.7)
        outputText = Text("Output", color= YELLOW).next_to(plane2, UP * 0.7)
        self.play(Create(VGroup(plane1, planeSquare1, planeText1, inputText)), Create(VGroup(plane2, planeSquare2, planeText2, outputText)), run_time= 4)
        self.wait(1)

        f = lambda x :  x**5 + x**2 - x + 1
        fdiff = lambda x : 5*x**4 + 2*x - 1
        z0 = complex(-0.5, 0.5)
        fz0 = f(z0)
        z0Dot =Dot(plane1.n2p(z0), radius= 0.15, color= RED)
        fz0Dot =  Dot(plane2.n2p(fz0), radius= 0.15, color= YELLOW)

        z0Label = MathTex("z_0", color= RED).add_updater(lambda m: m.next_to(z0Dot, UP))
        fz0Label = MathTex("f(z_0)", color= YELLOW).add_updater(lambda m: m.next_to(fz0Dot, UP))

        z0guess = MathTex("z_0 = " + str(z0), color= RED).next_to(plane1, DOWN * 4)
        fz0guess = MathTex("f(z_0) = " + str(f(z0)), color= YELLOW).next_to(plane2, DOWN * 4)
       
        z0Path = TracedPath(z0Dot.get_center, dissipating_time=0.5, stroke_color= RED, stroke_opacity=[0, 1], stroke_width= 6)
        fz0Path = TracedPath(fz0Dot.get_center, dissipating_time=1, stroke_color= YELLOW, stroke_opacity=[0, 1], stroke_width= 6)

        self.play(
            Create(VGroup(z0Dot, z0Label, z0Path)),
            Create(VGroup(fz0Dot, fz0Label, fz0Path)),
            Create(VGroup(z0guess,fz0guess)))


        self.wait(3)
        for i in range(1, 6):
            z0 = z0 - f(z0) / fdiff(z0)
            fz0 = f(z0)
            
            z1Label = MathTex("z_" + str(i), color= RED).add_updater(lambda m: m.next_to(z0Dot, UP))
            fz1Label = MathTex("f(z_" + str(i) + ")", color= YELLOW).add_updater(lambda m: m.next_to(fz0Dot, UP))
            
            z1guess = MathTex("z_" + str(i) + " = " +
            str(round(z0.real, 2) + round(z0.imag, 2) * 1j),
            color= RED).next_to(plane1, DOWN * 4)
            fz1guess = MathTex("f(z_" + str(i)+ ") = " + 
            str(round(fz0.real, 2) + round(fz0.imag, 2) * 1j),
            color= YELLOW).next_to(plane2, DOWN * 4)

            z1Dot = Dot(plane1.n2p(z0), radius= 0.15, color= RED)
            fz1Dot = Dot(plane2.n2p(fz0), radius= 0.15, color= YELLOW)

            self.play(
                Transform(z0Dot, z1Dot),
                Transform(fz0Dot, fz1Dot),
                Transform(z0guess, z1guess),
                Transform(fz0guess, fz1guess),
                Transform(z0Label, z1Label),
                Transform(fz0Label, fz1Label)
            )
            self.wait(1)

class Intro(Scene):
    def construct(self):
        
        title = Tex("Newton's", color= YELLOW, font_size= 160).shift(UP*1)
        fractal = Tex(r"Fractals", color= YELLOW, font_size= 110).next_to(title, DOWN*0.5).shift(RIGHT*2)
        
        self.play(
            Write(title), 
            Write(fractal),
            run_time= 3
        )
        self.wait(1)

        text1 = Tex("Presented By: ", font_size= 35, color=YELLOW).next_to(title, DOWN * 5 ).shift(LEFT * 3.2)
        text2 = Tex("Taha Barakat ", font_size= 35, color=YELLOW).next_to(text1, DOWN)
        text3 = Tex("Supervised By: ", font_size= 35, color=YELLOW).next_to(title, DOWN * 5).shift(RIGHT * 3.5)
        text4 = Tex("Dr. Wassim Al-Falou ", font_size= 35, color=YELLOW).next_to(text3, DOWN)

        self.play(
            Write(text1),
            Write(text2),
            Write(text3),
            Write(text4)
        )

class FunPart(Scene):
    def construct(self):
        text = Tex("Now here's the fun part", color= YELLOW, font_size= 70)
        self.wait(0.5)
        self.play(Write(text), run_time=2)


class Fractal(Scene):
    



    def construct(self):
        plane2 = ComplexPlane(
            x_range=(-2,2,1),
            y_range=(-2,2,1),
            x_length=8,
            y_length=8
        ).shift(RIGHT*3).add_coordinates()
        plane1 = ComplexPlane(
            x_range=(-2,2,0.2),
            y_range=(-2,2,0.2),
            x_length=8,
            y_length=8,
            background_line_style={
                "stroke_opacity": 0.4
            }
        ).shift(RIGHT*3)
        square = Square(8, color= BLUE).shift(RIGHT*3)

        function = MathTex("f(x) = x^5 + x^2 - x + 1",
            color= YELLOW,
            font_size= 50
        ).to_corner(UL)

        self.play(
            Create(VGroup(plane1, plane2, square)),
            Create(function),
            run_time= 3
        )
        self.wait(2)

        manySeeds = Tex("Many Initial points: ", font_size=40).next_to(function, DOWN * 4)
        z0tex = MathTex("z_0", color= YELLOW, font_size= 40).next_to(manySeeds, RIGHT)

        self.play(Create(VGroup(manySeeds, z0tex)))
        self.wait(1)

        
        #Small Resolution 

        x = np.linspace(-2, 2, 21)
        y = np.linspace(-2, 2, 21)
        x_1, y_1 = np.meshgrid(x, y)  
        smallDots = list()
        smallDotsGroup = VGroup()

        for i in range(len(x_1)):
            for j in range(len(y_1)):
                z = complex(x_1[i][j], y_1[i][j])
                currentDot = Dot(plane1.n2p(z), color=WHITE, radius= 0.05)
                smallDots.append(currentDot)
                smallDotsGroup.add(currentDot)
        self.wait(2)
        self.play(ReplacementTransform(z0tex.copy(), smallDotsGroup), run_time= 2.5)
        self.wait(3)

        z0Text = MathTex(
            "z_1 = z_0 - \\frac{f(z_0)}{f'(z_0)}",
            color= YELLOW,
            font_size=60
            ).next_to(manySeeds, DOWN * 3)
        self.play(Create(z0Text))
        self.wait(1)

        z0 = list()
        #z0Path = VGroup()
        for i in range(len(smallDots)):
            coord = plane1.point_to_coords(smallDots[i].get_center())
            z0.append(complex(coord[0], coord[1]))
            #path = TracedPath(smallDots[i].get_center, dissipating_time=0.8, stroke_color= WHITE, stroke_opacity=[0, 1], stroke_width= 2)
            #z0Path.add(path)
        #self.add(z0Path)

        f = lambda x: x**5 + x**2 - x + 1
        fdiff = lambda x: 5*x**4 + 2*x - 1
        roots = [-1.3247 + 0.0000j,
                 0.0000 + 1.0000j,
                 0.0000 - 1.0000j,
                 0.6624 + 0.5623j,
                 0.6624 - 0.5623j]
        colors = [YELLOW, BLUE, RED, PURPLE, GREEN]
        self.play(Create(Dot(plane1.n2p(roots[0]), color= colors[0],    radius=0.1)), 
                  Create(Dot(plane1.n2p(roots[1]), color= colors[1], radius=0.1)),
                  Create(Dot(plane1.n2p(roots[2]), color= colors[2], radius=0.1)),
                  Create(Dot(plane1.n2p(roots[3]), color= colors[3], radius=0.1)),
                  Create(Dot(plane1.n2p(roots[4]), color= colors[4], radius=0.1)))
        self.wait(2)

        bigDotsGroup = list()
        bigDotsGroup.append(smallDotsGroup.copy())
        for i in range(1, 16):
            #text
            z1Text = MathTex(
            "z_{" + str(i+1) + "} = z_{" + str(i) + "} - \\frac{f(z_{" + str(i) + "})}{f'(z_{" + str(i) + "})}",
            color= YELLOW,
            font_size=60
            ).next_to(manySeeds, DOWN * 3)
            

            #Dots
            bigDots = VGroup()
            for j in range(len(smallDots)):
                z0[j] = z0[j] - f(z0[j]) / fdiff(z0[j])
                currentDot = Dot(plane1.n2p(z0[j]), radius= 0.05)
                bigDots.add(currentDot)

            bigDotsGroup.append(bigDots)
            self.play(*[
                    Transform(smallDots[dot1], bigDots[dot1])
                    for dot1 in range(len(smallDots))
                ],
                
                Transform(z0Text, z1Text)
            )
            self.wait(0.35)

        z = list()
        for i in range(len(smallDots)):
            currentZ = plane1.p2n(smallDots[i].get_center())
            z.append(currentZ)
        
        def FindClosestRoot(roots, z):
                closestTo = list()
                for i in range(len(z)):
                    initial = abs(z[i] - roots[0])
                    closestTo.append(0)
                    for k in range(1, len(roots)):
                        if abs(z[i] - roots[k]) < initial :
                            initial = abs(z[i] - roots[k])
                            closestTo[i] = k
                return closestTo

        closestTo = FindClosestRoot(roots, z)

        
        self.play(*[smallDots[i].animate.set_color(colors[closestTo[i]]) for i in range(len(smallDots))])

        for j in reversed(range(len(bigDotsGroup))):
            z1Text = MathTex(
            "z_{" + str(j+1) + "} = z_{" + str(j) + "} - \\frac{f(z_{" + str(j) + "})}{f'(z_{" + str(j) + "})}",
            color= YELLOW,
            font_size=60
            ).next_to(manySeeds, DOWN * 3)

            self.play(*[smallDots[i].animate.move_to(
                        bigDotsGroup[j][i]) 
                        for i in range(len(smallDots))
                        ],
                        Transform(z0Text, z1Text), 
                        run_time= 0.5)
        self.wait(4)
        self.remove(z0Text)
        self.remove(*[smallDots[i] for i in range(len(smallDots))])


        #Big Resolution


        x = np.linspace(-2, 2, 41)
        y = np.linspace(-2, 2, 41)
        x_1, y_1 = np.meshgrid(x, y)  
        smallDots = list()
        smallDotsGroup = VGroup()
        #test = Dot(plane1.n2p(complex(x_1[0][2], y_1[2][4])), color=RED, radius= 0.1)
        #self.add(test)
        for i in range(len(x_1)):
            for j in range(len(y_1)):
                z = complex(x_1[i][j], y_1[i][j])
                currentDot = Dot(plane1.n2p(z), color=WHITE, radius= 0.05)
                smallDots.append(currentDot)
                smallDotsGroup.add(currentDot)
        self.wait(2)
        self.play(ReplacementTransform(z0tex.copy(), smallDotsGroup), run_time= 2.5)
        self.wait(3)

        z0Text = MathTex(
            "z_1 = z_0 - \\frac{f(z_0)}{f'(z_0)}",
            color= YELLOW,
            font_size=60
            ).next_to(manySeeds, DOWN * 3)
        self.play(Create(z0Text))
        self.wait(1)

        z0 = list()
        #z0Path = VGroup()
        for i in range(len(smallDots)):
            coord = plane1.point_to_coords(smallDots[i].get_center())
            z0.append(complex(coord[0], coord[1]))
            #path = TracedPath(smallDots[i].get_center, dissipating_time=0.3, stroke_color= WHITE, stroke_opacity=[0, 1], stroke_width= 2)
            #z0Path.add(path)
        #self.add(z0Path)

        f = lambda x: x**5 + x**2 - x + 1
        fdiff = lambda x: 5*x**4 + 2*x - 1
        roots = [-1.3247 + 0.0000j,
                 0.0000 + 1.0000j,
                 0.0000 - 1.0000j,
                 0.6624 + 0.5623j,
                 0.6624 - 0.5623j]
        colors = [YELLOW, BLUE, RED, PURPLE, GREEN]
        self.play(Create(Dot(plane1.n2p(roots[0]), color= colors[0],    radius=0.1)), 
                  Create(Dot(plane1.n2p(roots[1]), color= colors[1], radius=0.1)),
                  Create(Dot(plane1.n2p(roots[2]), color= colors[2], radius=0.1)),
                  Create(Dot(plane1.n2p(roots[3]), color= colors[3], radius=0.1)),
                  Create(Dot(plane1.n2p(roots[4]), color= colors[4], radius=0.1)))
        self.wait(2)

        bigDotsGroup = list()
        bigDotsGroup.append(smallDotsGroup.copy())
        for i in range(1, 16):
            #text
            z1Text = MathTex(
            "z_{" + str(i+1) + "} = z_{" + str(i) + "} - \\frac{f(z_{" + str(i) + "})}{f'(z_{" + str(i) + "})}",
            color= YELLOW,
            font_size=60
            ).next_to(manySeeds, DOWN * 3)
            

            #Dots
            bigDots = VGroup()
            for j in range(len(smallDots)):
                z0[j] = z0[j] - f(z0[j]) / fdiff(z0[j])
                currentDot = Dot(plane1.n2p(z0[j]), radius= 0.05)
                bigDots.add(currentDot)

            bigDotsGroup.append(bigDots)
            self.play(*[
                    Transform(smallDots[dot1], bigDots[dot1])
                    for dot1 in range(len(smallDots))
                ],
                
                Transform(z0Text, z1Text), 
                run_time= 0.5
            )

        z = list()
        for i in range(len(smallDots)):
            currentZ = plane1.p2n(smallDots[i].get_center())
            z.append(currentZ)

        closestTo = FindClosestRoot(roots, z)

        self.play(*[smallDots[i].animate.set_color(
            colors[closestTo[i]]) for i in range(len(smallDots))])

        for j in reversed(range(len(bigDotsGroup))):
            z1Text = MathTex(
            "z_{" + str(j+1) + "} = z_{" + str(j) +
             "} - \\frac{f(z_{" + str(j) + "})}{f'(z_{" + str(j) + "})}",
            color= YELLOW,
            font_size=60
            ).next_to(manySeeds, DOWN * 3)

            self.play(*[smallDots[i].animate.move_to(
                        bigDotsGroup[j][i]) 
                        for i in range(len(smallDots))
                        ],
                        Transform(z0Text, z1Text), 
                        run_time= 0.5)
        self.wait(2)
            

class ManimLogo(Scene):
    def construct(self):
         banner = ManimBanner()
         self.play(banner.expand())