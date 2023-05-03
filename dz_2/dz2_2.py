def check_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return check_palindrome(s[1:-1])
    else:
        return False

s = input("Введите строку: ")
if check_palindrome(s):
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")

def test_check_palindrome():
    assert check_palindrome("racecar") == True
    assert check_palindrome("hello") == False
    assert check_palindrome("level") == True
    assert check_palindrome("") == True
    assert check_palindrome("a") == True
    assert check_palindrome("ab") == False
    print("All test_check_palindrome passed!")

test_check_palindrome()