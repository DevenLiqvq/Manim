# Definition_area
from turtle import position

from manim import *
GR = float("1.618033988749895")


def rectangle(height, width):
    re = VGroup()
    rectangle_1 = Rectangle(height=height, width=width, color=YELLOW, fill_opacity=0.5)

    brace_1 = Brace(rectangle_1, UP)
    brace_1text = brace_1.get_text("a")
    brace_2 = Brace(rectangle_1, LEFT)
    brace_2text = brace_2.get_text("b")
    rectangle_area = Text("Area")
    # 两个括号表示a,b
    re.add(rectangle_1, brace_1, brace_1text, brace_2, brace_2text, rectangle_area)
    return re


class Area(Scene):
    # 定义黄金分隔比例

    def construct(self):

        a = ValueTracker(GR * 2)
        b = ValueTracker(2)
        rectangle_1 = always_redraw(lambda: rectangle(a.get_value(), b.get_value()))

        # 画出矩形
        self.play(Create(rectangle_1))
        self.play(rectangle_1.animate.to_edge(LEFT))

        self.play(b.animate.set_value(5), run_time=2)
        self.play(a.animate.set_value(7), run_time=2)



