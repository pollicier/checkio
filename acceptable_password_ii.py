

def is_acceptable_password(password: str) -> bool:
    lst = [x for x in password]
    a = 0
    for elem in lst:
        if elem.isdigit():
            a += 1
        else:
            a += 0
    if len(lst) > 6 and a >= 1:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")