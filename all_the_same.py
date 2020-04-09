from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    if len(elements) <= 1:
        return True
    else:
        a = 0
        for i in range(len(elements) - 1):
            if elements[i] == elements[i + 1]:
                a += 0
            else:
                a += 1
        if a == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
