

def number_length(a: int) -> int:
    return len(str(a))


if __name__ == '__main__':
    print("Example:")
    print(number_length(10))

    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
