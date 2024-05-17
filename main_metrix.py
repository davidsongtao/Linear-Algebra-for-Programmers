from playLA.Metrix import Metrix
from playLA.Vector import Vector


if __name__ == '__main__':
    metrix = Metrix([
        [1, 2],
        [3, 4]
    ])

    metrix2 = Metrix([
        [4, 6],
        [7, 8]
    ])

    vec = Vector([1, 2])

    print(metrix)

    print(f"{metrix}矩阵中的第二行第一列是：{metrix[1,0]}")
    print(f"{metrix}矩阵中第二行的行向量是：{metrix.row_vector(1)}")
    print(f"{metrix}矩阵中第一列的列向量是：{metrix.col_vector(0)}")
    print(f"{metrix}矩阵加上{metrix2}矩阵的结果是：{metrix + metrix2}")
    print(f"{metrix}矩阵减去{metrix2}矩阵的结果是：{metrix - metrix2}")
    print(f"{metrix}矩阵乘以3的结果是：{metrix * 3}")
    print(f"3乘以{metrix}矩阵的结果是：{3 * metrix}")
    print(f"{metrix}矩阵除以3的结果是：{metrix / 2}")
    print(f"创建一个有两行三列的零矩阵：{Metrix.zero(2,3)}")
    print(f"{metrix}矩阵与{vec}向量相乘的结果是{metrix.metrix_mul(vec)}")

