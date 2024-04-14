def div(x):  # стандартная функция для 25
    d = set()
    for i in range(1, int(x ** 0.5) + 1):  # менять 1 на 2 если не нужно делители 1 и само число
        if x % i == 0:
            d.add(i)
            d.add(x // i)
            # d |= {i, x // i}
    return sorted(d)


"""def prostoe(x):  # определение простого числа
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))"""

"""for x in range(193136, 193223 + 1):
    d = div(x)
    if len(d) == 6:
        print(*d)"""


"""for x in range(25000, 250200 + 1):  # фильтрация делителей
    d = [i for i in div(x) if i % 2 == 0]
    if len(d) == 6:
        print(d[4], d[5])"""



from fnmatch import *  # макси для чисел


"""for x in range(0, 10 ** 9, 17):  # ? - любое число; * любое кол-во чисел; [] - любое число из набора
    if fnmatch(str(x), '23?456?89'):
        print(x, x // 17)"""


"""for x in range(0, 10 ** 9, 169):
    if fnmatch(str(x), '345*789?'):
        print(x, x // 169)"""

for x in range(0, 10 ** 8, 2023):
    if fnmatch(str(x), '11[02468]??[13579]11'):
        print(x, x // 2023)