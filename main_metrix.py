from playLA.Metrix import Metrix
from playLA.Vector import Vector

if __name__ == '__main__':
    # metrix = Metrix([
    #     [2, 3, 5],
    #     [2, 4, 2]
    # ])
    #
    # metrix2 = Metrix([
    #     [1, 2],
    #     [2, 3],
    #     [3, 5]
    # ])
    #
    # vec = Vector([6, 8])
    # vec2 = Vector([2, 3, 5])
    #
    # print(metrix)
    #
    # print(f"{metrix}矩阵中的第二行第一列是：{metrix[1,0]}")
    # print(f"{metrix}矩阵中第二行的行向量是：{metrix.row_vector(1)}")
    # print(f"{metrix}矩阵中第一列的列向量是：{metrix.col_vector(0)}")
    # # print(f"{metrix}矩阵加上{metrix2}矩阵的结果是：{metrix + metrix2}")
    # # print(f"{metrix}矩阵减去{metrix2}矩阵的结果是：{metrix - metrix2}")
    # print(f"{metrix}矩阵乘以3的结果是：{metrix * 3}")
    # print(f"3乘以{metrix}矩阵的结果是：{3 * metrix}")
    # print(f"{metrix}矩阵除以3的结果是：{metrix / 2}")
    # print(f"创建一个有两行三列的零矩阵：{Metrix.zero(2,3)}")
    # print(f"{metrix}矩阵与{vec}向量相乘的结果是{metrix.dot(vec)}")
    # print(f"{metrix}矩阵与{metrix2}矩阵相乘的结果是{metrix.dot(metrix2)}")
    # print(f"{metrix}乘以{vec2}的结果是:{metrix.dot(vec2)}")
    #
    # # print(f"{vec}乘以{vec2}的结果是：{vec.dot(vec2)}")

    T = Metrix([
        [1.5, 0],
        [0, 2]
    ])

    P = Vector([5, 3])

    F = Metrix([
        [0, 4, 5],
        [0, 0, 3]
    ])

    # print(f"T.dot(p)的结果是：{T.dot(P)}")
    # print(f"T.dot(F)的结果是：{T.dot(F)}")
    # print(f"F.dot(T)的结果是：{F.dot(T)}")

    print(F.T())