

def second_index(text: str, symbol: str) -> [int, None]:
    lst = [x for x in text]
    if lst.count(symbol) > 1:
        first_index = lst.index(symbol)
        second = lst.index(symbol, first_index + 1)
        return second
    else:
        return None


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
