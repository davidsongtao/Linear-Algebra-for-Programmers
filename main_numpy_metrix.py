import numpy as np

if __name__ == '__main__':
    A = np.array([
        [1, 2],
        [3, 4]
    ])

    # print(A)
    # print(A.shape)
    #
    # # 获取矩阵的转置
    # print(A.T)
    #
    # # 获取矩阵的元素
    # print(A[1, 1])
    #
    # # 获取矩阵的行向量
    # print(A[0])
    #
    # # 获取矩阵中的列向量
    # print(A[:, 1])

    B = np.array([
        [5, 6],
        [7, 8]
    ])

    print(A + B)
    print(A - B)
    print(A * 10)
    print(f"矩阵{A}乘以矩阵{B}的结果是：{A.dot(B)}")
    print(f"矩阵{B}乘以矩阵{A}的结果是：{B.dot(A)}")

    p = np.array([10, 100])
    f = np.array([2, 5])

    print(f.dot(p))
