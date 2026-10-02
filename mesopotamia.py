from manim import *
import math
class Mesopotamia(Scene):
    def construct(self):
        img = ImageMobject(r"C:\Users\juliu\Downloads\YBC-7289-OBV-REV.jpg")
        img.width = 10  # or img.height = 3, etc.
        img.shift(RIGHT*0.2+UP*0.5)
        #img.rotate(math.radians(-1.5))
        points=[
            3.4*UP,
            3.4*RIGHT,
            3.4*DOWN,
            3.4*LEFT,
            3.4*UP
        ]
        numbers1=Typst("30",font_size=70).rotate(math.radians(45)).shift(2.1*UP+2.6*LEFT)
        numbers2=VGroup(
            Typst("1;",font_size=70).shift(LEFT*1.8),
            Typst("24,",font_size=70).shift(LEFT*0.9),
            Typst("51,",font_size=70).shift(RIGHT*0.8),
            Typst("10",font_size=70).shift(RIGHT*1.7)
            ).rotate(math.radians(5))
        numbers3=VGroup(
            Typst("42;",font_size=70).shift(LEFT*0.9),
            Typst("25, ",font_size=70).shift(RIGHT*0.8),
            Typst("35",font_size=70).shift(RIGHT*2)
        ).rotate(math.radians(15)).shift(DOWN*1.1)
        line=VMobject(stroke_width=5)
        line.set_points_as_corners(points)
        diagonal1=Line(3.4*DOWN,3.4*UP,stroke_width=5)
        diagonal2=Line(3.4*LEFT,3.4*RIGHT,stroke_width=5)
        new_numbers1=Typst("30",font_size=60).rotate(math.radians(45)).shift(1.6*UP+2.2*LEFT)
        new_numbers2=Typst("1,4142129",font_size=60).rotate(math.radians(5))
        new_numbers3=Typst("42,426",font_size=60).rotate(math.radians(15)).shift(DOWN*1.1)
        kathete1=Typst("s",font_size=60).shift(2*UP+1.9*LEFT)
        kathete2=Typst("s",font_size=60).shift(1.6*DOWN+2.2*LEFT)
        hypotenuse=Typst("d",font_size=60).shift(0.3*RIGHT+0.7*UP)
        arc=Arc(radius=0.8,start_angle=math.radians(-45),angle=math.radians(90)).shift(3.4*LEFT)
        point=Dot(3*LEFT,0.04)
        # self.play(
        #     FadeOut(img),
        #     FadeIn(
        #         line,
        #         diagonal1,
        #         diagonal2
        #     ),
        #     run_time=5
        # )
        picture=VGroup(
            line,
            diagonal1,
            diagonal2,
            numbers1,
            numbers2,
            numbers3,
            
        )  
        picture2=VGroup(
            new_numbers2,
            new_numbers1,
            new_numbers3,
            kathete1,
            kathete2,
            hypotenuse,
            arc,
            point
        ).shift(3*RIGHT)
        self.add(img) 
        self.play(
            Create(numbers1),
            Create(numbers2),
            Create(numbers3),
            run_time=5
        )
        self.wait(2)
        self.play(
            
                
            Create(line),
            Create(diagonal1),
            Create(diagonal2),
            run_time=3
            
        )
        
        self.play(FadeOut(img))
        self.play(
            picture.animate.shift(RIGHT*3)
            )
        
        calculation1=[]
        calculation1.append(Typst("$30$",font_size=40).to_corner(UL))
        calculation1.append(Typst("$=30 * 60^0$",font_size=40).next_to(calculation1[0],RIGHT))
        calculation1.append(Typst("$=30$",font_size=40).next_to(calculation1[1],RIGHT))
        calculation2=[]
        calculation2.append(Typst("$1;24,51,10$",font_size=40).to_corner(UL).align_to(calculation1[0],LEFT))
        calculation2.append(Typst("$= 1*60^0 + 24/(60^1) + 51/(60^2) + 10/(60^3)$",font_size=33).next_to(calculation2[0],DOWN).align_to(calculation1[0],LEFT))
        calculation2.append(Typst("$= 1,4142129$",font_size=40).next_to(calculation2[1],DOWN).align_to(calculation1[0],LEFT))
        calculation3=[]
        calculation3.append(Typst("$42;25,35$",font_size=40).to_corner(UL).align_to(calculation1[0],LEFT))
        calculation3.append(Typst("$= 42*60^0 + 24/(60^1) + 35/(60^2)$",font_size=37).next_to(calculation2[0],DOWN).align_to(calculation1[0],LEFT))
        calculation3.append(Typst("$= 42,426$",font_size=40).next_to(calculation2[1],DOWN).align_to(calculation1[0],LEFT))
        
        
        self.play(Transform(numbers1,calculation1[0]),run_time=1)
        
        self.play(Create(calculation1[1]),run_time=2)
        self.play(Create(calculation1[2]),run_time=2)
        self.play(ReplacementTransform(calculation1[2],new_numbers1),run_time=1)
        self.play(FadeOut(numbers1,calculation1[1]),run_time=1)

        self.play(Transform(numbers2,calculation2[0]),run_time=1)
        self.wait(1)
        self.play(Create(calculation2[1]),run_time=4)
        self.play(Create(calculation2[2]),run_time=2)
        self.wait(1)
        self.play(ReplacementTransform(calculation2[2],new_numbers2),run_time=1)
        self.play(FadeOut(numbers2,calculation2[1]),run_time=1)

        self.play(Transform(numbers3,calculation3[0]),run_time=1)
        self.wait(1)
        self.play(Create(calculation3[1]),run_time=3)
        self.play(Create(calculation3[2]),run_time=2)
        self.wait(1)
        self.play(ReplacementTransform(calculation3[2],new_numbers3),run_time=1)
        self.play(FadeOut(numbers3,calculation3[1]),run_time=1)

        
        self.play(
            new_numbers1.animate.set_opacity(0.15),
            new_numbers2.animate.set_opacity(0.15),
            new_numbers3.animate.set_opacity(0.15),
            FadeOut(diagonal2),
            run_time=3
        )
        
        
        self.wait(3)
        self.play(
            Create(arc),
            Create(point),
            run_time=2
        )
        self.play(
            Create(kathete1),
            Create(kathete2),
            run_time=2
            
        )
        self.play(
            Create(hypotenuse), 
            run_time=2
        )
        self.wait(4)
        title=Typst("Satz des Pythagoras",font_size=60).to_corner(UL)
        formula1=Typst("$d^2 =$",font_size=50).next_to(title,DOWN).align_to(title,LEFT)
        formula2=Typst("$s^2 +$",font_size=50).next_to(formula1,RIGHT)
        formula3=Typst("$s^2$",font_size=50).next_to(formula2,RIGHT)
        self.play(Write(title))
        self.play(
            TransformFromCopy(hypotenuse,formula1),run_time=1
        )
        self.wait(1)
        self.play(TransformFromCopy(kathete1,formula2),run_time=1)
        self.play(TransformFromCopy(kathete2,formula3),run_time=1)
        self.wait(2)
        formula4=Typst("$d^2 = 2 * s^2$").next_to(formula1,DOWN).align_to(title,LEFT)
        formula5=Typst("$d = sqrt(2 * s^2)$").next_to(formula4,DOWN).align_to(title,LEFT)
        formula6=Typst("$d = sqrt(2) * s$").next_to(formula5,DOWN).align_to(title,LEFT)
        formula7=Typst("$sqrt(2) * s= d$").to_corner(UL).align_to(title,LEFT)
        self.play(Write(formula4),run_time=2)
        self.play(Write(formula5),run_time=2)
        self.play(Write(formula6),run_time=2)
        self.wait(2)
        self.play(
            FadeOut(
                title,
                formula1,
                formula2,
                formula3,
                formula4,
                formula5,
            ),
            Transform(formula6,formula7),
            run_time=2
        )
        self.wait(2)
        formula8=Typst("$ s = 30 $").next_to(formula7,DOWN).align_to(title,LEFT)
        formula9=Typst("$ sqrt(2) approx 1,4142129 $").next_to(formula8,DOWN).align_to(title,LEFT)
        formula10=Typst("$1,4142129 *30 approx 42,426$").next_to(formula9,DOWN).align_to(title,LEFT)
        formula11=Typst("$sqrt(2) * s= d$").next_to(formula10,DOWN).align_to(title,LEFT)
        self.play(
            Write(formula8[0:2]),
            
        )
        self.play(
            new_numbers1.animate.set_opacity(1),
        )
        self.play(
            Indicate(new_numbers1)
        )
        self.play(
            TransformFromCopy(new_numbers1,formula8[2:4])
        )

        self.play(
            Write(formula9[0:4]),
            #new_numbers1.animate.set_ty(0.15),opaci
            
        )
        self.play(
            new_numbers2.animate.set_opacity(1),
        )
        self.play(
            Indicate(new_numbers2),
            run_time=3
        )
        self.play(
            TransformFromCopy(new_numbers2,formula9[4:13])
        )
        
        self.wait(3)
        self.play(
            Write(formula10[0:13]),
            run_time=3
        )
        
        self.play(
            Write(formula10[13:19]),
            new_numbers3.animate.set_opacity(1),
            run_time=2
        )
        
        self.play(
            Indicate(formula10[13:19]),
            Indicate(new_numbers3),
            run_time=3
        )

        numbers1.set_opacity(0)
        numbers2.set_opacity(0)
        numbers3.set_opacity(0)
        diagonal2.set_opacity(0)
        self.play(
            FadeOut(
                formula8,
                formula6,
                formula9,
                formula10,
            ),
            picture.animate.shift(3*LEFT),
            picture2.animate.shift(3*LEFT),
            run_time=2
        )
        self.play(
            FadeOut(
                hypotenuse,
                kathete1,
                kathete2,
                arc,
                point
            ),
            new_numbers2.animate.shift(3*UP+3*LEFT).rotate(math.radians(-5)),
            new_numbers3.animate.shift(RIGHT+UP*0.5).rotate(math.radians(-15)),
            run_time=3
        )






        self.wait(3)
        