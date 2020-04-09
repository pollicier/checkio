def split_list(items: list) -> list:
    a, b, c = [], [], []
    if len(items) == 0:
        c = [a, b]
        return c
    elif len(items) == 1:
        c = [items, a]
        return c
    else:
        half = len(items) // 2
        if len(items) % 2 == 0:
            a = items[:half]
            b = items[half:]
            c = [a, b]
            return c
        else:
            a = items[:half+1]
            b = items[half+1:]
            c = [a, b]
            return c


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")