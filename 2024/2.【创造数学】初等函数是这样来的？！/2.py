from manim import *


def textmod(textmod1, textmod3, positionmod):
    # 创建文本行
    line1 = MathTex(textmod1).set_color("#40b7f0")
    line2 = Text("这种函数能写成", font="KaiTi").scale(0.6)
    line3 = MathTex(textmod3).set_color("#e8cf61")

    # 使用 VGroup 对齐文本并设置行间距
    paragraph = VGroup(line1, line2, line3)
    paragraph.arrange(DOWN, aligned_edge=ORIGIN, buff=0.3)

    # 设置文本的位置
    paragraph.to_edge(positionmod)

    # 创建背景矩形
    screen_rect = Rectangle(color="#0e1a25", fill_opacity=0.8).surround(paragraph, buff=0.3)
    return paragraph, screen_rect


class ALL(Scene):
    def construct(self):
        self.camera.background_color = "#0e1a25"

        # 调用 textmod 函数创建文本和矩形
        paragraph, screen_rect = textmod("f(x+y)=f(x)+f(y)", "f(x)=cx", UP)

        # 显示背景矩形和文本
        self.play(Create(screen_rect))
        self.play(FadeIn(paragraph))
        self.wait(3)
