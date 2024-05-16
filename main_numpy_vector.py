import numpy
import numpy as np

if __name__ == '__main__':
    # 创建一个numpy对应的向量
    vc = np.array([1, 2, 3])
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

