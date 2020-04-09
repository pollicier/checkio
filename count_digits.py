

def count_digits(text: str) -> int:
    a = 0
    for char in text:
        if char.isdigit():
            a += 1
        else:
            a += 0
    return a


if __name__ == '__main__':
    print("Example:")
    print(count_digits('hi'))

    assert count_digits('hi') == 0
    assert count_digits('who is 1st here') == 1
    assert count_digits('my numbers is 2') == 1
    assert count_digits('This picture is an oil on canvas '
                        'painting by Danish artist Anna '
                        'Petersen between 1845 and 1910 year') == 8
    assert count_digits('5 plus 6 is') == 2
    assert count_digits('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
