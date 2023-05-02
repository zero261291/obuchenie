def prime_numbers(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i**2, n+1, i):
                primes[j] = False
    for i in range(2, n+1):
        if primes[i]:
            print(i)

prime_numbers(int(input('Введите число: ')))

assert prime_numbers(10) == [2, 3, 5, 7]
assert prime_numbers(20) == [2, 3, 5, 7, 11, 13, 17, 19]
assert prime_numbers(5) == [2, 3, 5]