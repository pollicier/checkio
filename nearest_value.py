

def nearest_value(values: set, one: int) -> int:
    lst = list(values)
    lst.append(one)
    lst = sorted(lst)
    if lst.index(one) == (len(lst) - 1):
        return lst[-2]
    elif lst.index(one) == 0:
        return lst[1]
    else:
        a = lst.index(one)
        b = lst[a-1:a+2]
        if abs(b[0] - b[1]) <= abs(b[1] - b[2]):
            return b[0]
        else:
            return b[2]


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")