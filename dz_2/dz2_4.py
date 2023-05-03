def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)


def test_sum_of_digits():
    assert sum_of_digits(0) == 0
    assert sum_of_digits(5) == 5
    assert sum_of_digits(10) == 1
    assert sum_of_digits(12345) == 15
    assert sum_of_digits(999999999999999) == 135
    print("All test_sum_of_digits pass")

test_sum_of_digits() # Название проверочной функции было не верно написано