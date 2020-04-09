

def index_power(array: list, n: int) -> int:
    if n > (len(array) - 1):
        return -1
    else:
        a = array[n]
        result = a ** n
        return result


if __name__ == '__main__':
    print('Example:')
    print(index_power([1, 2, 3, 4], 2))

    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")