from manim import *

gradient_colors = ['#ca164c', '#40b7f0', '#1df6ad', '#e8cf61']
# #ca164c: 一个深红色
# #40b7f0: 一个亮蓝色
# #1df6ad: 一个亮青绿色
# #e8cf61: 一个亮黄色


def textmod(textmod1, textmod3, positionmod, buff, color_rect):
    # 创建文本行
    line1 = MathTex(textmod1).set_color("#40b7f0")
    line2 = Text("这种函数能写成", font="KaiTi").scale(0.6)
    line3 = MathTex(textmod3).set_color("#e8cf61")

    # 使用 VGroup 对齐文本并设置行间距
    paragraph = VGroup(line1, line2, line3)
    paragraph.arrange(DOWN, aligned_edge=ORIGIN, buff=buff)

    # 设置文本的位置
    paragraph.to_edge(positionmod)

    # 创建背景矩形
    screen_rect = Rectangle(color=color_rect, fill_opacity=0.8).surround(paragraph, buff=0.3)
    return paragraph, screen_rect


class ALL(Scene):
    def construct(self):
        self.camera.background_color = "#0e1a25"

        text1 = SingleStringMathTex("f(x+y)=f(x)+f(y)")
        text2 = SingleStringMathTex("f(x+y)=f(x)f(y)")
        text3 = SingleStringMathTex("f(xy)=f(x)+f(y)")
        text4 = SingleStringMathTex("f(xy)=f(x)f(y)")

        texts = VGroup(text1, text2, text3, text4)
        texts.arrange(DOWN, buff=0.5)  # `buff` 控制文本之间的间距
        # 设置文本的位置
        texts.move_to(ORIGIN)

        self.play(Write(texts))
        self.wait(2)

        self.play(Circumscribe(text1))
        self.wait(2)
        self.play(Circumscribe(text2))
        self.wait(2)
        self.play(Circumscribe(text3))
        self.wait(2)
        self.play(Circumscribe(text4))
        self.wait(2)
        self.play(FadeOut(texts))

        paragraph, screen_rect = textmod("f(x+y)=f(x)+f(y)", "f(x)=cx", UP,0.8,"#7ac5cd")
        self.play(Create(paragraph))
        self.wait(3)
        paragraph, screen_rect = textmod("f(x+y)=f(x)+f(y)", "f(x)=c^{n}", DOWN,0.8,"#7ac5cd")
        self.play(Create(paragraph))
        self.wait(3)



class AA(Scene):
    def construct(self):
        self.camera.background_color = "#0e1a25"

        # 原始公式
        text1 = SingleStringMathTex("f(x+y)=f(x)+f(y)")
        self.play(Write(text1))
        self.wait(2)
        text2 = SingleStringMathTex("f(0+0)=f(0)+f(0)")
        self.play(TransformMatchingShapes(text1, text2))
        self.wait(2)
        text3 = SingleStringMathTex("f(0)=0")
        self.play(TransformMatchingShapes(text2, text3))
        self.wait(2)
        self.play(FadeOut(text3))

        AA = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-5, 5, 1],
        )
        self.add(AA)
        self.wait(1)
        dot1 = Dot(color=RED)
        origin_text = MathTex('(0, 0)').next_to(dot1, DOWN)
        # 将点添加到场景中
        self.play(FadeIn(dot1, origin_text))
        self.wait(2)
        self.play(FadeOut(origin_text, AA, dot1))
        self.wait(1.5)

        self.play(Write(text1))
        self.wait(2)
        text4 = SingleStringMathTex("f(x+dx)=f(x)+f(dx)")
        self.play(TransformMatchingShapes(text1, text4))
        self.wait(2)
        text5 = SingleStringMathTex("f(x+dx)-f(x)=f(dx)")
        self.play(TransformMatchingShapes(text4, text5))
        self.wait(2)
        text6 = SingleStringMathTex(r"\frac{f(x+dx)-f(x)}{dx} =\frac{f(dx)}{dx} ")
        self.play(TransformMatchingShapes(text5, text6))
        self.wait(2)
        text7 = SingleStringMathTex(r"{f(x)}'  =\frac{f(dx)}{dx}  ")
        self.play(TransformMatchingShapes(text6, text7))
        self.wait(2)
        text8 = SingleStringMathTex(r"{f(x)}'  ={f(0)}'  ")
        self.play(TransformMatchingShapes(text7, text8))
        self.wait(2)
        self.play(FadeOut(text8))
        self.wait(2)

        start_point = np.array([0, 0, 0])  # (0, 0)
        slope = 0.5  # 固定斜率为 0.5

        # 使用 ValueTracker 控制点的 x 坐标
        x_tracker = ValueTracker(0)  # 初始位置在 x = 0

        # 动态计算移动点的位置
        moving_point = always_redraw(lambda:
                                     Dot().move_to(np.array([x_tracker.get_value(), slope * x_tracker.get_value(), 0])).set_color(RED)
                                     )

        # 动态生成线段
        line = always_redraw(lambda:
                             Line(
                                 start=start_point,
                                 end=np.array([x_tracker.get_value(), slope * x_tracker.get_value(), 0])
                             )
                             )


        # 添加坐标系、线段和移动点到场景
        self.add(AA, line, moving_point)

        # 点从左向右移动，形成直线
        self.play(x_tracker.animate.set_value(3), time=5)
        self.play(x_tracker.animate.set_value(4), time=6)
        self.play(x_tracker.animate.set_value(-1), time=4)
        self.play(x_tracker.animate.set_value(-2), time=4)
        line = always_redraw(lambda:
                             Line(
                                 start=np.array([-10, -10 * slope, 0]),  # 左侧起点
                                 end=np.array([10, 10 * slope, 0])  # 右侧终点
                             ).set_color("#c23519")
                             )
        self.remove(moving_point)
        self.play(Create(line))
        self.wait(2)

        line1 = MathTex("f(x+y)=f(x)+f(y)").set_color("#40b7f0")
        line2 = Text("这种函数能写成", font="KaiTi").scale(0.6)
        line3 = MathTex("f(x)=cx").set_color("#e8cf61")

        # 使用 VGroup 对齐文本并设置行间距
        paragraph = VGroup(line1, line2, line3)

        paragraph.arrange(DOWN, aligned_edge=ORIGIN, buff=0.3).to_edge(DOWN)  # 设置左对齐，行间距为 0.7
        screen_rect = Rectangle(color="#0e1a25").set_opacity(0.8).surround(paragraph, buff=0.3)
        # 将段落添加到场景中

        self.play(FadeIn(screen_rect), Create(paragraph))
        self.wait(3)


class AM(Scene):
    def construct(self):
        self.camera.background_color = "#0e1a25"

        # 原始公式
        text1 = SingleStringMathTex("f(x+y)=f(x)f(y)")
        self.play(Write(text1))
        self.wait(2)
        text2 = SingleStringMathTex("f(0+0)=f(0)f(0)")
        self.play(TransformMatchingShapes(text1, text2))
        self.wait(2)
        text3 = MathTex(r"f(0)=0 \,\, or \,\, f(x)=1")
        self.play(TransformMatchingShapes(text2, text3))
        self.wait(0.4)
        text3.set_color(RED)
        self.play(Wiggle(text3), run_time=1.2)
        text3.set_color(WHITE)
        text4 = SingleStringMathTex("f(x)=f(x)f(0)")
        self.wait(0.8)
        self.play(TransformMatchingShapes(text3, text4))
        self.wait(2)
        text5 = SingleStringMathTex("f(0)=1")
        self.play(TransformMatchingShapes(text4, text5))
        self.wait(2)
        self.play(FadeOut(text5))

        AM = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-5, 5, 1],
        )
        self.wait(1)
        dot1 = Dot((0, 1, 0), color=RED)
        origin_text = MathTex('(0, 1)').next_to(dot1, DOWN)
        self.play(FadeIn(origin_text, AM, dot1))
        self.wait(2)
        # 将点添加到场景中
        self.play(FadeOut(origin_text, AM, dot1))


        self.play(Write(text1))
        self.wait(2)
        text7 = SingleStringMathTex("{f(x+y)}'=f(x){f(y)}' ")
        self.play(TransformMatchingShapes(text1, text7))
        self.wait(2)
        text8 = SingleStringMathTex("{f(x)}'={f(0)}'f(x) ")
        self.play(TransformMatchingShapes(text7, text8))
        self.wait(2)
        text9 = Tex(r"if \,\, " + "${f(0)}'=1 $")
        self.play(TransformMatchingShapes(text8, text9))
        self.play(text9.animate.shift(UP))
        text10 = SingleStringMathTex("{f(x)}'=f(x) ")
        self.play(Write(text10))
        self.wait(4)
        self.play(Unwrite(text10), Unwrite(text9))
        # 定义整个公式
        text11 = MathTex(
            r"f(n) &= f(\underbrace{1+1+\cdots +1}_{\text{n}}) \\",
            r"&= \underbrace{f(1)+f(1)+\cdots+f(1)}_{\text{n}} \\",
            r"&= f(1)^{n}\\",
            r"&= c^{n}"
        )

        self.play(Write(text11[0]))
        self.wait(1)
        self.play(Write(text11[1]))
        self.wait(1)
        self.play(Write(text11[2]))
        self.wait(1)
        self.play(Write(text11[3]))
        self.wait(1)
        self.play((Unwrite(text11)))

        exp_graph = AM.plot(lambda x: np.exp(x), color=RED)
        # 添加图例
        exp_label = AM.get_graph_label(exp_graph, label='c^x')
        # 添加坐标轴和图像到场景
        self.play(FadeIn(AM))
        self.play(Create(exp_graph), Write(exp_label))
        self.wait(2)

        line1 = MathTex("f(x+y)=f(x)f(y)").set_color("#40b7f0")
        line2 = Text("这种函数能写成", font="KaiTi").scale(0.6)
        line3 = MathTex("f(x)=c^{n}").set_color("#e8cf61")

        # 使用 VGroup 对齐文本并设置行间距
        paragraph = VGroup(line1, line2, line3)

        paragraph.arrange(DOWN, aligned_edge=ORIGIN, buff=0.3).to_edge(DOWN)  # 设置左对齐，行间距为 0.7
        screen_rect = Rectangle(color="#0e1a25").set_opacity(0.8).surround(paragraph, buff=0.3)
        # 将段落添加到场景中

        self.play(FadeIn(screen_rect), Create(paragraph))
        self.wait(3)


