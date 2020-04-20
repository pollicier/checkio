from typing import Iterable


def is_ascending(items: Iterable[int]) -> bool:
    if len(items) <= 1:
        return True
    else:
        i = 1
        while i <= len(items) - 1 and items[i] > items[i - 1]:
            i += 1
        return True if i == len(items) else False


if __name__ == '__main__':
    print("Example:")
    print(is_ascending([-5, 10, 99, 123456]))

    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")