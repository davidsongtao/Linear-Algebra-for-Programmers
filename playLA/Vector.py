"""
创造一个向量类，向量其实就是一组有序的数字，python中用数组表示一组有序的数字
"""


# 定义一个向量类,传入一个list
class Vector:
    def __init__(self, lst):
        self._values = list(lst)  # 将引用者传进来的lst进行复制，使其不可更改

    # 向量的加法
    def __add__(self, other):
        # 判断两个向量的维度是否相等
        assert len(self) == len(other), "Error in Adding. Length must be same."
        return Vector([a + b for a, b in zip(self, other)])

    # 向量的减法
    def __sub__(self, other):
        assert len(self) == len(other), "Error in Subtracting. Length must be same."
        return Vector([a - b for a, b in zip(self, other)])

    # 向量的数量乘法
    def __mul__(self, k):
        return Vector([a * k for a in self])

    # 向量的右乘运算
    def __rmul__(self, k):
        return Vector([k * a for a in self])

    # 向量取正的结果
    def __pos__(self):
        return 1 * self

    # 向量取负的结果
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
