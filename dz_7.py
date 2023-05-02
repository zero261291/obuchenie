x = 10

def multiply_x_by_y(y):
    x = 10
    x *= y
    return x

y = 5
result = multiply_x_by_y(y)
print(result)

assert multiply_x_by_y(y) == 50