

def end_zeros(num: int) -> int:
    lst = [int(i) for i in str(num)]
    a = 0
    while len(lst) != 0:
        if lst[-1] == 0:
            a += 1
            lst.pop()
        else:
            break
    return a


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")