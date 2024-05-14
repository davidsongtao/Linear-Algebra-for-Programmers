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
