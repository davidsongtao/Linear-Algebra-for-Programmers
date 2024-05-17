from playLA.Vector import Vector


class Metrix:

    # DONE 定义一个矩阵，传入一个二维数组
    def __init__(self, lst2d):
        self._values = [row[:] for row in lst2d]  # 将引用者传进来的lst2d每行进行复制，使其不可更改

    # DONE 返回一个R行C列的零矩阵
    @classmethod
    def zero(cls, r, c):
        return cls([
            [0] * c for _ in range(r)
        ])

    # DONE 复写矩阵的打印方法
    def __repr__(self):
        return f"Metrix({self._values})"

    __str__ = __repr__

    # DONE 获取矩阵是几行几列的（有几个元素代表有几行，第一个元素有几个值代表有几列）
    def shape(self):
        return len(self._values), len(self._values[0])

    # DONE 获取矩阵的行数
    def row_num(self):
        return self.shape()[0]

    __len__ = row_num

    # DONE 获取矩阵的列数
    def col_num(self):
        return self.shape()[1]

    # DONE 获取矩阵中有多少个元素
    def size(self):
        r, c = self.shape()
        return r * c

    # DONE 获取矩阵中的某个元素(用r,c表示position)
    def __getitem__(self, pos):
        r, c = pos
        return self._values[r][c]

    # DONE 获取矩阵中某一行的行向量是谁
    def row_vector(self, index):
        return Vector(self._values[index])

    # DONE 获取矩阵中某一列的列向量是谁
    def col_vector(self, index):
        return Vector(row[index] for row in self._values)

    """
    矩阵的基本运算
        1. 矩阵加法/减法
        2. 矩阵数量乘法
    """

    # DONE 矩阵加法
    def __add__(self, another):
        # 返回两个矩阵的加法结果
        assert self.shape() == another.shape(), \
            "Error in adding. Shape of matrix must be same"
        return Metrix([
            [a + b for a, b in zip(self.row_vector(i),
                                   another.row_vector(i))] for i in range(self.row_num())
        ])

    # DONE 矩阵减法
    def __sub__(self, another):
        assert self.shape() == another.shape(), \
            "Error in subtraction. Shape of matrix must be same"
        return Metrix([
            [a - b for a, b in zip(self.row_vector(i),
                                   another.row_vector(i))] for i in range(self.row_num())
        ])

    # DONE 矩阵的数量乘法
    def __mul__(self, k):
        return Metrix([
            [a * k for a in self.row_vector(i)] for i in range(self.row_num())
        ])

    # DONE 矩阵的右乘的结果
    def __rmul__(self, k):
        return self * k

    # DONE 矩阵取正的结果
    def __pos__(self):
        return 1 * self

    # DONE 矩阵取负的结果
    def __neg__(self):
        return -1 * self

    # DONE 矩阵的数量除法
    def __truediv__(self, k):
        return (1 / k) * self

    # TODO 矩阵和向量的乘法操作
