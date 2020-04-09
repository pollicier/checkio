

def is_all_upper(text: str) -> bool:
    a = 0
    if len(text) == 0:
        return True
    for char in text:
        if char.isupper() or char.isspace() or char.isdigit():
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
    assert is_all_upper('') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")