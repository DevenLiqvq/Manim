# tangent_function
from manim import *
from sympy import *


class PolygonOnAxes(Scene):

    def construct(self):
        x = symbols('x')
        # 定义自变量
        f = cos(x)
        derivative_f = diff(f, x)

        # 定义函数
        t = ValueTracker(5)
        # ValueTracker 的值发生变化时
        # 所有依赖于这个值的动画元素会自动更新以反映新的值。这种机制允许创建平滑的过渡和动态效果。

        func = lambdify(x, f, 'numpy')
        derivative_func = lambdify(x, derivative_f, 'numpy')
        # 将 SymPy 符号表达式转换为一个 lambda 函数，这个 lambda 函数可以用数值参数调用，并返回数值结果

        ax = Axes(
            x_range=[0, 10],
            y_range=[0, 10],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False},  # 坐标轴的两端不会有尖端显示
        )
        # 创建一个 Axes 对象，表示坐标轴。

        graph = ax.plot(
            func,
            color=YELLOW_D,
            x_range=[0, 10, 0.01],
        )
        # 画出sin函数图像
        dot = Dot()
        dot.add_updater(
            lambda x: x.move_to(
                ax.c2p(t.get_value(), func(t.get_value()))
            )
        )
        dot.set_z_index(10)

        def line_func(x):
            return derivative_func(t.get_value()) * (x - t.get_value()) + func(t.get_value())

        # 绘制直线
        line = always_redraw(lambda: ax.plot(line_func, color=RED, x_range=[0, 10]))

        self.add(ax, graph, dot, line)
        self.play(t.animate.set_value(3))
        self.play(t.animate.set_value(5))
        self.play(t.animate.set_value(8))
        self.play(t.animate.set_value(2))


