from typing import Iterable


def replace_last(items: list) -> Iterable:
    if len(items) <= 1:
        return items
    else:
        a = [items[-1]]
        items.pop()
        for i in items:
            a.append(i)
        return a


if __name__ == '__main__':
    print("Example:")
    print(list(replace_last([2, 3, 4, 1])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_last([2, 3, 4, 1])) == [1, 2, 3, 4]
    assert list(replace_last([1])) == [1]
    assert list(replace_last([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
