"""
创造一个向量类，向量其实就是一组有序的数字，python中用数组表示一组有序的数字
"""
import math
from playLA._global import EPSILON

# 定义一个向量类,传入一个list
class Vector:
    def __init__(self, lst):
        self._values = list(lst)  # 将引用者传进来的lst进行复制，使其不可更改

    # 返回向量的模
    def norm(self):
        return math.sqrt(sum(e ** 2 for e in self))  # 将向量的所有元素平方后相加，和开根号

    # 返回向量的单位向量
    def normalize(self):
        if self.norm() < EPSILON:    # 浮点数和0比较，不能直接使用==，要定义一个精度
            raise ZeroDivisionError("Normalization cannot be zero")
        return Vector(self._values) / self.norm()

    # 返回一个N维的零向量
    @classmethod
    def zero(cls, dim):
        return cls([0] * dim)

    # 向量的加法
    def __add__(self, other):
        # 判断两个向量的维度是否相等
        assert len(self) == len(other), "Error in Adding. Length must be same."
        return Vector([a + b for a, b in zip(self, other)])

    # 向量的减法
    def __sub__(self, other):
        assert len(self) == len(other), "Error in Subtracting. Length must be same."
        return Vector([a - b for a, b in zip(self, other)])

    # 返回向量的数量乘法
    def __mul__(self, k):
        return Vector([a * k for a in self])

    # 返回向量的数量除法
    def __truediv__(self, k):  # 向量运算使用浮点数，所以覆盖truediv，python3中区分了整数和浮点数的除法
        return Vector([1 / k * a for a in self])

    # 向量的右乘
    def __rmul__(self, k):
        return Vector([k * a for a in self])

    # 返回两个向量的点乘的结果，返回一个标量
    def dot(self, another):
        assert len(self) == len(another),\
            "Error in Dotting. Length must be same."
        return sum(a * b for a, b in zip(self, another))

    # 返回一个向量在另一个向量上的投影点的坐标

    # 1. 计算投影点的距离：d = U向量点乘V向量除U向量的模
    # 2. 计算投影点的方向：u = U向量的单位向量
    # 3. 计算投影点的坐标：Pv = d * u

    def get_pro_point(self, another):
        return self.normalize() * self.dot(another) / self.norm()

    # 返回向量取正的结果
    def __pos__(self):
        return 1 * self

    # 返回向量取负的结果
    def __neg__(self):
        return -1 * self

    # 返回向量的迭代器，模拟_value不可被访问或修改
    def __iter__(self):
        return iter(self._values).__iter__()

    # 取出向量中的第index个向量元素
    def __getitem__(self, index):
        return self._values[index]

    # 返回向量的长度，即维度(有多少个元素)
    def __len__(self):
        return len(self._values)

    def __repr__(self):
        return f"Vector({self._values})"

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))
