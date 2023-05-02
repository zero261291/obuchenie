def unique_words(text):
    words = text.split()
    unique = set(words)
    return list(unique)

text = input("Введите предложение: ")
print(unique_words(text))

assert unique_words("hello world") == ["hello", "world"]
assert unique_words("apple apple banana cherry") == ["apple", "banana", "cherry"]
assert unique_words("Python is great, isn't it?") == ["Python", "is", "great", "isn't", "it"]