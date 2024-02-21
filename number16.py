"""def f(n):
    if n == 1:
        return 2
    elif n > 1:
        return f(n - 1) + 5 * n ** 2


print(f(39))"""

"""def f(n):
    if n < 3: return n + 3
    elif n >= 3 and n % 3 == 0: return (n + 2) * f(n - 4)
    elif n >= 3 and n % 3 != 0: return n + f(n-1) + 2 * f(n - 2)


print(f(20))"""

"""def f(n):
    if n == 1:
        return 1
    return 2 * f(n - 1) + g(n - 1) - 2


def g(n):
    if n == 1:
        return 1
    return f(n - 1) + 2 * g(n - 1)


print(f(14) + g(14))"""

"""def f(n):
    k = 0
    k += 1
    if n >= 1:
        k += 2 + f(n - 1) + f(n - 3)
    return k


print(f(40))"""

"""cache = {}


def f(n):
    if n not in cache:
        if n == 1: cache[n] = 1
        else: cache[n] =  f(n - 1) + 3 * g(n - 1)
    return cache[n]


def g(n):
    if n == 1:
        return 1
    return f(n - 1) - 2 * g(n - 1)


print(f(50))"""

"""from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return f(n - 1) + 3 * g(n - 1)


def g(n):
    if n == 1:
        return 1
    return f(n - 1) - 2 * g(n - 1)


print(sum(int(x) for x in str(f(50))))"""

"""from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < -100000: return 1
    if n > 10: return f(n - 1) + 3 * f(n - 3) + 2
    return -f(n-1)


for i in range(-100000, 20):
    f(i)
print(f(20))"""

"""def f(n):
    if n < -100000: return 1
    if n > 10: return f(n - 1) + 3 * f(n - 3) + 2
    return -f(n-1)


k = 0
for i in range(1, 1001):
    if all(int(x) % 2 == 1 for x in str(f(i))):
        k += 1"""


"""def f(n):
    if n <= 5: return n
    if n % 4 == 0: return n + f(n / 2 - 1)
    return n + f(n + 2)


for n in range(1, 1000):
    try:
        print(n, f(n))
    except:
        ..."""


def f(n):
    if n <= 5: return n
    if n % 5 == 0: return n + f(n / 5 + 1)
    return n + f(n + 6)


for n in range(1, 1000):
    try:
        if f(n) > 1000:
            print(n, f(n))
    except:
        ...