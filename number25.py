def div(x):  # стандартная функция для 25
    d = set()
    for i in range(1, int(x ** 0.5) + 1):  # менять 1 на 2 если не нужно делители 1 и само число
        if x % i == 0:
            d.add(i)
            d.add(x // i)
            # d |= {i, x // i}
    return sorted(d)


"""for x in range(193136, 193223 + 1):
    d = div(x)
    if len(d) == 6:
        print(*d)"""


"""for x in range(25000, 250200 + 1):  # фильтрация делителей
    d = [i for i in div(x) if i % 2 == 0]
    if len(d) == 6:
        print(d[4], d[5])"""


def prostoe(x):  # определение простого числа
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))


for x in range(1_000_000_000):
    if prostoe(x):
        print(x)
