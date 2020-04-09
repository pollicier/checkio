def split_pairs(a):
    lst = []
    s = '_'

    if len(a) % 2 == 0:
        lst = [a[x:x + 2] for x in range(0, len(a), 2)]
        return lst

    if len(a) % 2 != 0:
        lst = [a[x:x + 2] for x in range(0, len(a), 2)]
        lst[-1] += s
        return lst

    if len(a) == 0:
        return lst


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
