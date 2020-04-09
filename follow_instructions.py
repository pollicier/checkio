

def follow(instructions):
    a = 0
    b = 0
    lst = [x for x in instructions]
    for i in lst:
        if i == 'f':
            a += 1
        elif i == 'b':
            a -= 1
        elif i == 'l':
            b -= 1
        else:
            b += 1
    return b, a


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")