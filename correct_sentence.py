

def correct_sentence(text: str) -> str:
    if not text.endswith('.'):
        text += '.'
    if text[0].islower():
        text = text.replace(text[0], text[0].upper(), 1)
    return text


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")