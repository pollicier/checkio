

def is_acceptable_password(password: str) -> bool:
    if len(password) > 9:
        return True
    elif len(password) < 6:
        return False
    else:
        a = 0
        b = 0
        for char in password:
            if char.isdigit():
                a += 1
            else:
                b += 1
        if a > 0 and b > 0:
            return True
        else:
            return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
