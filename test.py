from playLA.Vector import Vector

#
if __name__ == "__main__":
    vec = Vector([5, 2])

    vec2 = Vector([1, 2])
    result = vec + vec2
    print(result)

    result2 = 3 * vec2
    print(result2)

    result3 = vec2 - vec
    print(result3)

    result4 = -vec
    print(result4)

    zer0_vec = Vector.zero(4)
    print(zer0_vec)

    result5 = vec * 0
    print(result5)

    result6 = vec.norm()
    print(result6)

    try:
        print(zer0_vec.normalize())
    except ZeroDivisionError:
        print(f"can not divide by zero: Vector{zer0_vec}")

    s1 = Vector([2, 5])
    s2 = Vector([5, 2])

    print(s1.dot(s2))

    point = s1.get_pro_point(s2)
    print(f"{s1}向量在{s2}向量上的投影点的坐标是：{point}")




