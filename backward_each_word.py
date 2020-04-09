

def backward_string_by_word(text: str) -> str:
    if len(text) == 0:
        return text
    else:
        words = text.split(' ')
        new_words = [word[::-1] for word in words]
        txt = ' '.join(new_words)
        return txt


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")