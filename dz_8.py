def filter_capitalized_words(strings):
    capitalized_strings = []
    for string in strings:
        if string[0].isupper():
            capitalized_strings.append(string)
    return capitalized_strings

assert filter_capitalized_words(["Apple", "Banana", "cherry"]) == ["Apple", "Banana"]
assert filter_capitalized_words(["Python", "java", "C++"]) == ["Python"]
assert filter_capitalized_words(["Red", "green", "Blue"]) == ["Red", "Blue"]

# У вас здесь ошибка в проверке