

def sum_numbers(text: str) -> int:
    if len(text) == 0:
        return 0
    else:
        lst = text.split(' ')
        total = 0
        for elem in lst:
            if elem.isdigit():
                total += int(elem)
        return total


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
                       'painting by Danish artist Anna '
                       'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
