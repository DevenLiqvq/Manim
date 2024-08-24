from manim import *


class Deltoid1(Scene):
    def construct(self):
        triangle_height = 6

        triangle = []
        for i in range(triangle_height):
            # 用来控制杨辉三角的每一行。
            # i 取0, 1, 2, 3, 4, 5
            row = [1]  # 每行的第一个元素为1
            for j in range(1, i + 1):
                # 一行几个元素。
                # j 取[1],[1, 2],[1, 2, 3]...[1, 2, 3, 4, 5, 6]
                val = triangle[i - 1][j - 1] + triangle[i - 1][j] if j < len(triangle[i - 1]) else 1
                # 如果当前元素不在当前行的边界上 val=上面两个数字相加
                # 如果当前元素在当前行的边界上 val=1
                row.append(val)
            triangle.append(row)
        # 将杨辉三角的数据储存到triangle中
        # triangle = [
        #     [1],
        #     [1, 1],
        #     [1, 2, 1],
        #     [1, 3, 3, 1],
        #     [1, 4, 6, 4, 1],
        #     [1, 5, 10, 10, 5, 1]
        # ]

        texs = []
        for i, row in enumerate(triangle):
            tex_row = []
            for j, val in enumerate(row):
                tex = Tex(str(val)).scale(0.7)
                tex.move_to(((2 * j - len(row) + 1) / 2) * RIGHT + (i - triangle_height / 2) * DOWN)
                tex_row.append(tex)
            texs.append(tex_row)

        for i in range(triangle_height):
            for j in range(len(triangle[i])):
                self.play(Write(texs[i][j]), run_time=0.1)

        self.wait(2)

        text = MathTex(r"(x+y)^{n}=x^n+nx^{n-1}y+?x^{n-2}y^2+....+?x^2y^{n-2}+nxy^{n-1}+y^n")
        texs_group = VGroup(*[tex for tex_row in texs for tex in tex_row])

        # 对场景中的所有 Tex 对象进行转换
        self.play(Transform(texs_group, text))

        # 等待 2 秒后结束场景
        self.wait(2)


"""
        # Highlight the first two columns
        for i in range(triangle_height):
            if len(texs[i]) > 0:
                self.play(texs[i][0].animate.set_color(YELLOW), run_time=0.1)
            if len(texs[i]) > 1:
                self.play(texs[i][1].animate.set_color(YELLOW), run_time=0.1)
                
        self.wait(2)

"""

