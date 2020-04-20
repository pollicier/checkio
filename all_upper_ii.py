

def is_all_upper(text: str) -> bool:
    lst = text.split(' ')
    a = 0
    for elem in lst:
        if elem.isupper():
            a += 0
        else:
            a += 1
    if a == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")