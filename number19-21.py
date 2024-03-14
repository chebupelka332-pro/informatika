"""def f(s, m): # простой вариант
    if s > 33: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 1, m - 1), f(s + 2, m - 1), f(s + 3, m - 1), f(s * 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19)', [s for s in range(1, 34) if f(s, 2)])
print('20)', [s for s in range(1, 34) if not f(s, 1) and f(s, 3)])
print('20)', [s for s in range(1, 34) if not f(s, 2) and f(s, 4)])"""


"""def f(s, m): # двойное условие
    if 45 <= s <= 112: return m % 2 == 0
    if s > 112: return m % 2 != 0
    if m == 0: return 0
    h = [f(s + 2, m - 1), f(s * 3, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19)', [s for s in range(1, 45) if f(s, 2)])
print('20)', [s for s in range(1, 45) if not f(s, 1) and f(s, 3)])
print('21)', [s for s in range(1, 45) if not f(s, 2) and f(s, 4)])"""


"""def f(s1, s2, m): # две кучи
    if s1 + s2 >= 59: return m % 2 == 0
    if m == 0: return 0
    h = [f(s1 + 1, s2, m - 1), f(s1 * 2, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1, s2 * 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19)', [s for s in range(1, 53) if f(5, s, 1)])
print('20)', [s for s in range(1, 53) if not f(5, s, 1) and f(5, s, 3)])
print('21)', [s for s in range(1, 53) if not f(5, s, 2) and f(5, s, 4)])"""


"""def f(s1, s2, m):  # неудачная игра all -> any
    if s1 + s2 >= 77: return m % 2 == 0
    if m == 0: return 0
    h = [f(s1 + 1, s2, m - 1), f(s1 * 2, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1, s2 * 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19)', [s for s in range(1, 70) if f(7, s, 2)])  # all -> any
print('20)', [s for s in range(1, 70) if not f(7, s, 1) and f(7, s, 3)])
print('21)', [s for s in range(1, 70) if not f(7, s, 2) and f(7, s, 4)])"""


"""def f(s1, s2, m):  # вычитание
    if s1 + s2 <= 20: return m % 2 == 0
    if m == 0: return 0
    h = [f(s1 - 1, s2, m - 1), f(s1 // 2 + s1 % 2, s2, m - 1),
         f(s1, s2 - 1, m - 1), f(s1, s2 // 2 + s2 % 2, m - 1)
         ]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19)', [s for s in range(11, 100) if f(10, s, 2)])
print('20)', [s for s in range(11, 100) if not f(10, s, 1) and f(10, s, 3)])
print('21)', [s for s in range(11, 100) if not f(10, s, 2) and f(10, s, 4)])"""



