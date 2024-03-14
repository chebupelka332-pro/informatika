from functools import lru_cache


"""def f(curr, end):  # простейший вариант
    if curr > end: return 0
    if curr == end: return 1
    if curr < end: return f(curr + 1, end) + f(curr * 2, end)"""


"""def f(curr, end):  # исключение 4
    if curr > end or curr == 4: return 0
    if curr == end: return 1
    if curr < end: return f(curr + 1, end) + f(curr * 2, end)"""


"""def f(curr, end):  # прохидя через 8
    if curr > end: return 0
    if curr == end: return 1
    if curr < end: return f(curr + 1, end) + f(curr * 2, end)


print(f(2, 8) * f(8, 20))"""


"""def f(curr, end):  # предпоследняя команда 2
    if curr > end: return 0
    if curr == end: return 1
    if curr < end: return f(curr + 1, end) + f(curr + 2, end)


print(f(3, 15) + f(3, 14))"""


"""def f(curr, end):  # движение от большего к меньшему
    if curr < end: return 0
    if curr == end: return 1
    if curr > end: return f(curr + 1, end) + f(curr * 2, end)
"""


"""def f(curr, end):  # двоичные числа
    if curr > end: return 0
    if curr == end: return 1
    if curr < end: return f(curr + 1, end) + f(curr * 2, end) + f(curr * 2 + 1, end)


print(f(int('100', 2), int('11011', 2)))"""


"""def f(curr, end):  # конечное число
    if curr > end: return 0
    if curr == end: return 1
    if curr < end: return f(curr + 1, end) + f(curr + 5, end) + f(curr * 3, end)


for i in range(2, 200):
    if f(1, i) == 175:
        print(i)"""


"""def f(curr, end, step):  # ровно за 6 команд
    if curr > end: return 0
    if curr == end and step == 6: return 1
    if curr == end and step != 6: return 1
    if curr < end: return f(curr + 1, end, step + 1) + f(curr * 2, end, step + 1) + f(curr + 2, end, step + 1)


print(f(1, 20, 0))"""


"""@lru_cache(None)
def f(curr, end, step):  # минимальная команда
    if curr > end: return 10 ** 8
    if curr == end: return step
    if curr < end: return min(f(curr + 1, end, step + 1), f(curr + 5, end, step + 1), f(curr * 3, end, step + 1))


print(f(1, 227, 0))"""


"""@lru_cache(None)
def f(curr, end, step):  # максимальная команда
    if curr > end: return -10 ** 8
    if curr == end: return step
    if curr < end: return max(f(curr + 1, end, step + 1), f(curr + 5, end, step + 1), f(curr * 3, end, step + 1))


print(f(1, 227, 0))"""


"""k = set()


def f(curr, step):  # нет конечного числа
    global k
    if step == 4:
        k.add(curr)
    else:
        f(curr + 1, step + 1)
        f(curr + 5, step + 1)
        f(curr * 3, step + 1)


f(1, 0)
print(len(k))"""


"""d = set()
def f(curr):  # нет конечного числа и числа шагов
    if curr >= 100: return 0
    if curr < 100 and curr % 2 == 0: d.add(curr)
    if curr < 100:
        f(curr + 3)
        f(curr * 3)


f(3)
print(len(d))"""


"""def f(c, e, count): # количество определенных команд
    if c > e: return 0
    if c == e: return count == 1
    if c < e: return f(c + 1, e, count) + f(c + 2, e, count) + f(c * 2, e, count + 1)


print(f(2, 12, 0))"""


"""@lru_cache(None)
def f(c, e, k): # траектороия вычисления содержит какое-либо число
    if c % 2 != 0: k += 1
    if c > e: return 0
    if c == e: return k == 1
    return f(c + 1, e, k) + f(c + 2, e, k) + f(c * 2, e, k)


print(f(2, 40, 0))"""


def f(c, e, k):
    if c % 2 == 0: k += 1
    if c > e: return 0
    if c == e: return k == 6
    return f(c + 1, e, k) + f(c + 3, e, k) + f(c + 5, e, k)


print(f(3, 25, 0))


