import re


def between_markers(text: str, begin: str, end: str) -> str:
    a, b = text.count(begin), text.count(end)
    if (a == b == 1) and (text.index(begin) < text.index(end)):
        pattern = re.escape(begin) + r'(.*?)' + re.escape(end)
        return ''.join(re.findall(pattern, text, flags=re.DOTALL))
    elif b == a == 0:
        return text
    elif b == 0:
        pattern = re.escape(begin) + r'(\w*.*?)'
        return ''.join(re.findall(pattern, text, flags=re.DOTALL))
    elif a == 0:
        pattern = r'(.*?)' + re.escape(end)
        return ''.join(re.findall(pattern, text, flags=re.DOTALL))
    else:
        s = ''
        return s


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')