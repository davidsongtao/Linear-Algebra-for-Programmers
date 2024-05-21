"""
实现高斯约旦消元法
    - 构造方法：组织创建一个系数矩阵与结果列组成的增广矩阵，对这个矩阵进行正向高斯消元和反向约旦消元
"""
from playLA.Metrix import Metrix
from playLA.Vector import Vector


class LinearSystem:

    # DONE 构造方法，传入A系数矩阵，b右侧结果矩阵，生成增广矩阵
    def __init__(self, A, b):
        # A：系数矩阵；b:右侧结果向量
        assert A.row_num() == len(b), "Error!"  # 判断系数矩阵的行数是否等于结果向量的元素数
        self._m = A.row_num()  # 增广矩阵的行数
        self._n = A.col_num()  # 增广矩阵的列数
        self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]]) for i in range(self._m)]  # 构建增广矩阵

    def __repr__(self):
        return f"{self.Ab}"

    # DONE 返回最大主元向量的行号
    def _max_row(self, index, n):
        best, ret = self.Ab[index][index], index  # best为最大主元，ret为对应行号
        for i in range(index + 1, n):
            if self.Ab[i][index] < best:
                best, ret = self.Ab[i][index], i
        return ret

    # DONE 实现高斯消元法
    def _forward(self):
        # 排列行向量，使主元最大的行向量排列在最前面，假设循环次数为n,
        n = self._m
        # 循环n次，每次将主元消为1，将下一行主元下面对应的元素消为0
        for i in range(n):
            max_row = self._max_row(i, n)
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]
            self.Ab[i] = self.Ab[i] / self.Ab[i][i]  # TODO 如果Ab[i][i] == 0, 则有问题，需要处理
            for j in range(i + 1, n):
                self.Ab[j] = self.Ab[j] - self.Ab[j][i] * self.Ab[i]  # 将主元下面的数消为0

    # self.Ab[i][i] 做为主元

    # DONE 实现约旦消元法
    def _backward(self):
        n = self._m
        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[j][i] * self.Ab[i]

    # DONE 高斯约旦消元法求解方程式
    def gauss_jordan_elimination(self):
        self._forward()
        self._backward()

    # DONE 打结果输出
    def fancy_print(self):
        for i in range(self._m):
            print("".join(str(self.Ab[i][j]) for j in range(self._n)), end=" ")
            print("|", self.Ab[i][-1])
