import numpy
import numpy as np

if __name__ == '__main__':
    """
    1. Numpy几个快捷的创建向量的方法
    """
    # 创建一个numpy对应的向量
    vc = np.array([1, 2, 3, 4, 5, 6])
    print(vc)
    # 创建一个零向量
    vc_zero = np.zeros(5)
    print(vc_zero)
    # 创建一个单位向量
    vc_one = np.ones(5)
    print(vc_one)
    # 创建一个多维向量，每个维度都是相同的
    vc_full = np.full(5, 666)
    print(vc_full)

    """
    2. Numpy中向量的基本属性
    """
    # 向量中有多少个元素
    print(f"{vc}向量中的元素数量是：{vc.size}个。")
    print(f"{vc}向量中的元素数量是：{len(vc)}个。")
    # 可以使用方括号索引的方式查看向量中的某个元素的值是多少,也适用python索引的方式
    print(f"{vc}向量的0号元素是：{vc[0]}")
    print(f"{vc}向量的最后一个元素是：{vc[-1]}")
    print(f"{vc}向量的1号元素到3号元素的切片是：{vc[1:3]}")  # 切片的方式，获取的是一个向量，类型是ndarray（多维数组）

    """
    3. Numpy中向量的基本运算
    """
    vc2 = np.array([7, 1, 1, 3, 5, 4])
    print(f"{vc}向量乘以5的结果是：{vc * 5}")  # 数量乘法
    print(f"{vc}向量加上{vc2}的结果是：{vc + vc2}")  # 向量加法
    print(f"{vc}向量乘以{vc2}的结果是：{vc * vc2}")  # 逐个元素的乘法， 而不是sum(),这种乘法没有数学意义
    print(f"{vc}向量点乘{vc2}的结果是：{vc.dot(vc2)}")  # 向量的点乘在NP中的使用方式
    print(f"{vc}向量求模的结果是：{np.linalg.norm(vc)}")  # 向量求模的结果，Numpy中一个linalg的子模块中，有一个norm函数用来计算向量的模
