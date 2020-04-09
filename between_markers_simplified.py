

def between_markers(text: str, begin: str, end: str) -> str:
    lst = [x for x in text]
    a = lst.index(begin)
    b = lst.index(end)
    c = ""
    if a == (b-1):
        return c
    else:
        d = lst[a+1:b]
        txt = ''
        for char in d:
            txt += char
        return txt


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')