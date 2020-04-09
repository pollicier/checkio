
def checkio(first, second):
    lst_1 = first.split(',')
    lst_2 = second.split(',')
    lst_3 = []
    for i in lst_1:
        if i in lst_2:
            lst_3.append(i)

    return ','.join(sorted(lst_3))


if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"