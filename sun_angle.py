

def sun_angle(time):
    lst = time.split(":")
    lst = [int(x) for x in lst]
    grad = ((lst[0] - 6) * 60 + lst[1]) * 0.25
    if grad > 180 or grad < 0:
        return "I don't see the sun!"
    else:
        return round(grad, 2)


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")