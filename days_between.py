import datetime


def days_diff(a, b):
    a = [x for x in a]
    b = [x for x in b]
    first = datetime.date(a[0], a[1], a[2])
    second = datetime.date(b[0], b[1], b[2])
    delta = abs(first - second)
    return delta.days


if __name__ == '__main__':
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")
