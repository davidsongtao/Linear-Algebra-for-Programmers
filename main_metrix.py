from playLA.Metrix import Metrix


if __name__ == '__main__':
    metrix = Metrix([
        [1, 2],
        [3, 4]
    ])

    print(metrix)

    print(f"{metrix}矩阵中的第二行第一列是：{metrix[1,0]}")
    print(f"{metrix}矩阵中第二行的行向量是：{metrix.row_vector(1)}")
    print(f"{metrix}矩阵中第一列的列向量是：{metrix.col_vector(0)}")