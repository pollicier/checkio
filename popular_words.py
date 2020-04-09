

def popular_words(text: str, words: list) -> dict:
    txt = text.replace('\n', ' ').strip().lower().split(' ')
    a = []
    for i in range(0, len(words)):
        if words[i] in txt:
            a.append(txt.count(words[i]))
        else:
            a.append(0)
    dictionary = dict(zip(words, a))
    return dictionary


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
