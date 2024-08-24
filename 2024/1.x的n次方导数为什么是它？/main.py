from manim import *


class Derivative(Scene):
    def construct(self):
        text1 = MathTex(r"f'(x)=\frac{f(x+\Delta x)-f(x)}{\Delta x}")
        self.play(Create(text1))
        self.wait(2)
        self.play(text1.animate.to_edge(UP))
        self.wait(2)
        # 显示求导公式后移动到屏幕上边缘

        fx1 = MathTex(r"f(x)=x^{n}")
        self.play(Create(fx1))
        self.wait(2)
        # 显示要求的公式
        fx2 = MathTex(r"f'(x)=\frac{(x+\Delta x)^{n}-x^{n}}{\Delta x}")
        self.play(ReplacementTransform(fx1, fx2))
        self.wait(2)
        # 变化成求导

        self.play(Indicate(fx2[0][6:13]))
        self.wait(1)
        # 重点强调这一部分

        self.play(FadeOut(fx2[0][:6], fx2[0][13:]))
        fx2a = MathTex(r"(x+\Delta x)^{n}")
        self.play(ReplacementTransform(fx2[0][6:13], fx2a))
        self.wait(2)
        # 隐藏掉多余的部分

        self.play(fx2a.animate.to_edge(LEFT))
        # 移动到左屏幕

        fx2aa = MathTex(r"=(x+\Delta x)(x+\Delta x)(x+\Delta x) \cdots (x+\Delta x)").move_to(RIGHT*0.5)
        self.play(FadeIn(fx2aa))
        self.wait(2)
        # 展开
        fx2aaa = MathTex("=", r"x^n+n\Delta x\cdot x^{n-1}", r"+?x^{n-2}\Delta x^2+....").move_to(LEFT*0.5)
        self.play(ReplacementTransform(fx2aa, fx2aaa))
        self.wait(2)

        self.play(
            FadeOut(fx2aaa[0]),
            FadeOut(fx2a)
                  )

        self.wait(2)
        fx2b = MathTex(r"f'(x)=", r"\frac{x^n+n\Delta x\cdot x^{n-1}+?x^{n-2}\Delta x^2+....-x^n}{\Delta x} ")
        self.play(ReplacementTransform(fx2aaa, fx2b))
        self.wait(2)

        fx2bb = MathTex(r"f'(x)=", r"\frac{n\Delta x\cdot nx^{n-1}+?x^{n-2}\Delta x^2+....}{\Delta x}  ")
        self.play(ReplacementTransform(fx2b, fx2bb))
        self.wait(2)

        fx2bbb = MathTex(r"f'(x)=", r"nx^{n-1}", r"+?x^{n-2}\Delta x+....")
        self.play(ReplacementTransform(fx2bb, fx2bbb))
        self.wait(2)

        self.play(Indicate(fx2bbb[2][6:8]))
        self.wait(2)
        self.play((FadeOut(fx2bbb[2])))
        self.wait(2)

        end1 = MathTex(r"f(x)=", "x^n")
        end2 = MathTex(r"f'(x)=", r"nx^{n-1}")
        end = VGroup(end1, end2)
        end.arrange(DOWN, buff=1)
        self.play(
            FadeOut(text1),
            ReplacementTransform(fx2bbb, end))
        self.wait(2)






