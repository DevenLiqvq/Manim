from manim import *


class Deltoid2(Scene):
    def construct(self):
        row = VGroup(*[MathTex(f"(x+y)^{{{i}}}") for i in range(6)])
        row.arrange(DOWN, buff=0.5)
        self.play(Create(row), run_time=6)
        self.wait(2)

        self.play(
            ReplacementTransform(row[0], MathTex(r"1").move_to(row[0])),
            ReplacementTransform(row[1], MathTex(r"1x+1y").move_to(row[1])),
            ReplacementTransform(row[2], MathTex(r"1x^2+2xy+1y^2").move_to(row[2])),
            ReplacementTransform(row[3], MathTex(r"1x^3+3x^2y+3xy^2+1y^3").move_to(row[3])),
            ReplacementTransform(row[4], MathTex(r"1x^4+4x^3y+6x^2y^2+4xy^3+1y^4").move_to(row[4])),
            ReplacementTransform(row[5], MathTex(r"1x^5+5x^4y+10 x^3y^2+10x^2y^3+5xy^4+1y^5").move_to(row[5])),
            run_time=2
        )
        self.wait(2)
        self.play(FadeOut(row))
"""
        #for a in row:
            # (x+y)^0
            # (x+y)^1
            # (x+y)^2....
            for b in a:
                for c in b:
                    self.play(Indicate(c), run_time=5)

        self.wait(2)
"""