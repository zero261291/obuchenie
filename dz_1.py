def multiply(a, b):
    return a * b

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

result = multiply(a, b)
print(result)

assert multiply(2, 3) == 6
assert multiply(10, 5) == 50
assert multiply(7, -3) == -21