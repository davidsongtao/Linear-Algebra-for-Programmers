from playLA.Metrix import Metrix
from playLA.Vector import Vector
from playLA.LinearSystem import LinearSystem

# from playLA.LinearSystem import LinearSystem

if __name__ == '__main__':
    A = Metrix([
        [1, 2, 4],
        [3, 7, 2],
        [2, 3, 3]
    ])

    b = Vector([7, -11, 1])

    ls = LinearSystem(A, b)
    ls.gauss_jordan_elimination()
    ls.fancy_print()


