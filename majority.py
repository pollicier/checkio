

def is_majority(items: list) -> bool:
    if len(items) < 1:
        return False
    else:
        t = 0
        f = 0
        for i in items:
            if i == True:
                t += 1
            else:
                f += 1
        if t > f:
            return True
        else:
            return False


if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, True, False]))

    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")