from playLA.Vector import Vector
from playLA.Metrix import Metrix
import matplotlib.pyplot as plt
import math

if __name__ == "__main__":
    points = [
        [0, 0],
        [0, 5],
        [3, 5],
        [3, 4],
        [1, 4],
        [1, 3],
        [2, 3],
        [2, 2],
        [1, 2],
        [1, 0]
    ]

    x = [point[0] for point in points]
    y = [point[1] for point in points]

    plt.figure(figsize=(5, 5))  # 设置绘图窗口的尺寸为5英尺 x 5英尺
    plt.xlim(-10, 10)  # 设置x轴的范围为-10到10
    plt.ylim(-10, 10)  # 设置y轴的范围为-10到10
    plt.plot(x, y)  # 将x,y坐标数据传入plot
    # plt.show()  # 显示图形

    # DONE 应用矩阵，将原图像横坐标扩大2倍，纵坐标扩大1.5倍
    p = Metrix(points)  # 用点坐标创建矩阵
    # 定义一个变换矩阵，使原矩阵横坐标扩大2倍，纵坐标扩大1.5倍（2列，）
    T = Metrix([
        [2, 0],
        [0, 1.5]
    ])
    # 将坐标矩阵转置，使其可以合法与变换矩阵点乘。变换矩阵列数必须等于坐标矩阵的行数
    # p2 = p.T()
    # 用变换矩阵点乘每个点的坐标向量
    p3 = T.dot(p.T())
    # 取出每个点坐标的X值与Y值
    # x = [p3.col_vector(i)[0] for i in range(p3.col_num())]
    # y = [p3.col_vector(i)[1] for i in range(p3.col_num())]
    # 将数据传入plot绘图
    plt.plot([p3.col_vector(i)[0] for i in range(p3.col_num())], \
             [p3.col_vector(i)[1] for i in range(p3.col_num())])
    # plt.show()

    # DONE 应用变换矩阵矩阵，对图像进行X轴翻转（x坐标不变，y左边变为-1)
    # 定义一个变换矩阵
    T2 = Metrix([
        [1, 0],
        [0, -1]
    ])
    # 对坐标数据进行处理，绘制图像
    p4 = T2.dot(p.T())
    plt.plot([p4.col_vector(i)[0] for i in range(p4.col_num())],
             [p4.col_vector(i)[1] for i in range(p4.col_num())])
    # plt.show()

    # DONE 应用变换矩阵,实现旋转操作
    theta = math.pi / 3  # 定义旋转角度，用弧度制表示

    # 对图形沿着原点旋转theta度的变换矩阵
    T = Metrix([
        [math.cos(theta), math.sin(theta)],
        [-math.sin(theta), math.cos(theta)]
    ])

    p6 = T.dot(p.T())
    plt.plot(
        [p6.col_vector(i)[0] for i in range(p6.col_num())],
        [p6.col_vector(i)[1] for i in range(p6.col_num())]
    )
    plt.show()
