"""
实现输入自己的图形变换库：
    - 用点绘制出一个长方形或圆形
    - 定义变换矩阵，使用矩阵变换方法变换图形
    - 利用矩阵形成自己的图形变换库
"""
import matplotlib.pyplot as plt
from playLA.Metrix import Metrix
from playLA.Vector import Vector


# DONE 将图形按照传入的参数进行放大或缩小，参数小于1时缩小，参数大于1时放大
def zoom(points, zoom_x, zoom_y):
    """
    本方法实现了将图形按照参数放大或缩小
    :param points: 要缩放的图形坐标列表（二元列表）
    :param zoom_x: 各个坐标X轴放大的倍数
    :param zoom_y: 各个坐标Y轴放大的倍数
    :return: 返回缩放后的坐标
    """
    # 把传入的点坐标(二维列表)实例化成一个矩阵对象P
    p = Metrix(points)
    # 定义一个变换矩阵T，实现将x轴放大x倍，y轴放大y倍
    assert zoom_x > 0 and zoom_y > 0, \
        "Zoom parameters must be greater than 0"
    T = Metrix([[zoom_x, 0], [0, zoom_y]])
    # 变换矩阵T点乘坐标矩阵P，获得zoom后的矩阵
    p2 = T.dot(p.T())
    # 获取缩放后的所有X值和所有Y值并组成新矩阵
    x = [p2.col_vector(i)[0] -
         (points[0][0] * zoom_x - points[0][0]) for i in range(p2.col_num())]
    y = [p2.col_vector(i)[1] -
         (points[0][1] * zoom_y - points[0][1]) for i in range(p2.col_num())]
    # 将更新后的坐标重新组织并返回
    return [list(pair) for pair in zip(x, y)]


# DONE 将图形按照传入的参数沿X轴翻转
def flip_x(points):
    p = Metrix(points)
    T = Metrix([
        [1, 0],
        [0, -1]
    ])
    P = T.dot(p.T())
    x = [P.col_vector(i)[0] for i in range(P.col_num())]
    y = [P.col_vector(i)[1] for i in range(P.col_num())]
    return [list(pair) for pair in zip(x, y)]


# DONE 将图形按照传入的参数沿Y轴翻转
def flip_y(points):
    p = Metrix(points)
    T = Metrix([
        [-1, 0],
        [0, 1]
    ])
    P = T.dot(p.T())
    x = [P.col_vector(i)[0] for i in range(P.col_num())]
    y = [P.col_vector(i)[1] for i in range(P.col_num())]
    return [list(pair) for pair in zip(x, y)]


if __name__ == '__main__':
    rectangle_points = [
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

    # DONE 绘制一个原图形
    x = [points[0] for points in rectangle_points]
    y = [points[1] for points in rectangle_points]

    plt.figure(figsize=(5, 5))
    plt.xlim(-15, 15)
    plt.ylim(-15, 15)
    plt.plot(x, y)
    # plt.show()

    # DONE 测试长方形的放大缩小
    updated_points = zoom(rectangle_points, 2, 1.5)

    x_new = [points[0] for points in updated_points]
    y_new = [points[1] for points in updated_points]

    plt.plot(x_new, y_new)
    # plt.show()

    # DONE 测试图形沿X轴进行翻转
    flip_x_points = flip_x(rectangle_points)
    flip_x_x = [points[0] for points in flip_x_points]
    flip_x_y = [points[1] for points in flip_x_points]

    plt.plot(flip_x_x, flip_x_y)
    # plt.show()

    # DONE 测试图形沿Y轴进行翻转
    flip_y_points = flip_y(rectangle_points)
    flip_y_x = [points[0] for points in flip_y_points]
    flip_y_y = [points[1] for points in flip_y_points]

    plt.plot(flip_y_x, flip_y_y)
    plt.show()
