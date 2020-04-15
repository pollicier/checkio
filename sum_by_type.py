from typing import Tuple


def sum_by_types(items: list) -> Tuple[str, int]:
    if len(items) == 0:
        return '', 0
    else:
        strings = ''
        nums = 0
        for item in items:
            if type(item) == str:
                strings += item
            else:
                nums += item
        return strings, nums


if __name__ == '__main__':
    print("Example:")
    print(sum_by_types([]))

    assert sum_by_types([]) == ('', 0)
    assert sum_by_types([1, 2, 3]) == ('', 6)
    assert sum_by_types(['1', 2, 3]) == ('1', 5)
    assert sum_by_types(['1', '2', 3]) == ('12', 3)
    assert sum_by_types(['1', '2', '3']) == ('123', 0)
    assert sum_by_types(['size', 12, 'in', 45, 0]) == ('sizein', 57)
    print("Coding complete? Click 'Check' to earn cool rewards!")