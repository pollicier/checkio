from typing import Iterable


def except_zero(items: list) -> Iterable:
    b = []
    for elem in items:
        if elem != 0:
            b.append(elem)
    b.sort(reverse=False)
    if items.count(0) > 0:
        c = 0
        for i in range(len(items) - 1):
            if items[i] != 0:
                items[i] = b[c]
                c += 1
        return items
    else:
        return b


if __name__ == '__main__':
    print("Example:")
    print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

    assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
    assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
    assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
    assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
    assert list(except_zero([0, 0])) == [0, 0]
    print("Coding complete? Click 'Check' to earn cool rewards!")