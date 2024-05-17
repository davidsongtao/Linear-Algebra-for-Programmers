from playLA.Vector import Vector


class Metrix:

    # 定义一个矩阵，传入一个二维数组
    def __init__(self, lst2d):
        self._values = [row[:] for row in lst2d]  # 将引用者传进来的lst2d每行进行复制，使其不可更改

    def __repr__(self):
        return f"Metrix({self._values})"

    __str__ = __repr__

    # 矩阵是几行几列的：有几个元素代表有几行，第一个元素有几个值代表有几列
    def shape(self):
        return len(self._values), len(self._values[0])

    # 获取矩阵的行数
    def row_num(self):
        return self.shape()[0]

    __len__ = row_num

    # 获取矩阵的列数
    def col_num(self):
        return self.shape()[1]

    # 获取矩阵中有多少个元素
    def size(self):
        r, c = self.shape()
        return r * c

    # 获取矩阵中的某个元素(用r,c表示position)
    def __getitem__(self, pos):
        r, c = pos
        return self._values[r][c]

    # 获取矩阵中某一行的行向量是谁
    def row_vector(self, index):
        return Vector(self._values[index])

    # 获取矩阵中某一列的列向量是谁
    def col_vector(self, index):
        return Vector(row[index] for row in self._values)
