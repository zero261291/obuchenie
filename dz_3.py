def is_pythagorean_triple(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    elif a**2 + c**2 == b**2:
        return True
    elif b**2 + c**2 == a**2:
        return True
    else:
        return False

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if is_pythagorean_triple(a, b, c):
    print(True)
else:
    print(False)

assert is_pythagorean_triple(3, 4, 5) == True
assert is_pythagorean_triple(5, 12, 13) == True
assert is_pythagorean_triple(7, 8, 9) == False