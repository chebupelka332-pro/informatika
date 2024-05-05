"""def f(x): # число
    return (x & 107 == 0) <= ((x & 55 != 0) <= (x & a != 0))


for a in range(1, 1000):
    if all(f(x) == 1 for x in range(1, 100000)):
        print(a)"""


"""def f(x, y): # числовая плоскость
    return (x ** 2 - 10 * x + 16 > 0) or (y ** 2 - 10 * y + 21 > 0) or (x * y < 2 * a)


for a in range(1, 1000):
    if all(f(x, y) == 1 for x in range(1, 1000) for y in range(1, 1000)):
        print(a)"""


"""a = set()  # множества мин


def f(x):
    A = x in a
    D = x in list(range(17, 59))
    C = x in list(range(29, 81))
    return D <= (((not C) and A))


for x in range(1000):
    if f(x) == 0:
        a.add(x)
print(a)"""



"""a = set(range(1000))  # множества макс


def f(x):
    A = x not in a
    P = x in {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    Q = x in {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
    R = x in {12, 24, 36, 48, 60}
    return A <= ((P or Q) <= R)


for x in range(1000):
    if f(x) == 0:
        a.remove(x)
print(a)"""


"""from itertools import * #  отрезки


def f(x):
    B = 18 <= x <= 52
    C = 16 <= x <= 41
    A = a1 <= x < a2
    return (B <= A) and ((not C) or A)


OX = [i / 4 for i in range(16 * 4, 53 * 4 + 1)]
m = []

for a1, a2 in combinations(OX, 2):
    if all(f(x) == 1 for x in OX):
        m.append(a2 - a1)
print(min(m))
"""


"""from itertools import * # восмибитовые цепочки


d = [''.join(i) for i in product('01', repeat=8)]

a = set()


def f(x):
    P = x in {i for i in d if i[:2] == '11'}
    Q = x in {i for i in d if i[-1] == '0'}
    A = x in a
    return (not A) <= ((not P) and (not Q))


for x in d:
    if f(x) == 0:
        a.add(x)
print(len(a))"""