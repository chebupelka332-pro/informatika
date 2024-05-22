# количество пар, произведение которых кратно 7
f = open('27.txt')
n = int(f.readline())
count = 0
k = 0  # количество ВСЕХ предыдущих чисел
k7 = 0  # количество предыдущих чисел, кратных 7
for i in range(n):
    x = int(f.readline())
    if x % 7 == 0: count += k
    elif x % 7 != 0: count += k7

    k += 1
    if x % 7 == 0: k7 += 1

print(count)


# количество пар, произведение которых кратно 15
f = open('27.txt')
n = int(f.readline())
count = 0
k = 0  # количество ВСЕХ предыдущих чисел
k15 = k5 = k3 = 0  # количество предыдущих чисел, кратных 15
for i in range(n):
    x = int(f.readline())
    if x % 15 == 0: count += k
    elif x % 5 == 0: count += k3
    elif x % 3 == 0: count += k5
    else: count += k15

    k += 1
    if x % 15 == 0: k15 += 1
    elif x % 5 == 0: k5 += 1
    elif x % 3 == 0: k3 += 1

print(count)


# количество пар, сумма которых кратна 127
f = open('27.txt')
n = int(f.readline())
count = 0
k = [0] * 127
for i in range(n):
    x = int(f.readline())
    ost = 0 if x % 127 == 0 else 127 - x % 127
    count += k[ost]
    k[x % 127] += 1

print(count)


# максимальную суммы пары, кратную 107
f = open('27.txt')
n = int(f.readline())
mx = -10 ** 20
k = [-10 ** 20] * 107
for i in range(n):
    x = int(f.readline())
    ost = 0 if x % 107 == 0 else 107 - x % 107
    mx = max(x + k[ost], mx)

    k[x % 107] = max(x, k[x % 107])

print(mx)


# максимальную суммы пары, кратную 350 и первый элемент пары больше второго
f = open('27.txt')
n = int(f.readline())
mx = -10 ** 20
k = [-10 * 20] * 350
for i in range(n):
    x = int(f.readline())
    ost = 0 if x % 350 == 0 else 305 - x % 350
    if k[ost] > x:
        mx = max(mx, k[ost] + x)

    k[x % 350] = max(x, k[x % 350])

print(mx)


# пары элементов с расстоянием не менее 8 и разностью кратной 999
f = open('27.txt')
n = int(f.readline())
q = [int(f.readline()) for _ in range(7)]  # очередь
count = 0
k = [0] * 999
for i in range(n - 7):
    x = int(f.readline())
    count += k[x % 999]

    k[q[0] % 999] += 1
    q.append(x)
    q.pop(0)

print(count)


# суммы пары кратна 25 и расстояние между элементами пары больше k (без очереди)
n = 1000
k = 100
a = [int(x) for x in open('27.txt')]

k25 = [0] * 25
count = 0
for i in range(k, n):
    ost = a[i - k] % 25
    k25[ost] += 1

    ost2 = 0 if a[i] % 25 == 0 else 25 - a[i] % 25
    count += k25[ost2]
print(count)


# максимальная сумма пары кратна 101 и расстояние между элементами пары больше k (без очереди)
n = 1000
k = 100
a = [int(x) for x in open('27.txt')]

m = [-10 ** 20] * 101
mx = -10 ** 20
for i in range(k, n):
    ost = a[i - k] % 101
    m[ost] = max(m[ost], a[i - k])

    ost2 = 0 if a[i] % 101 == 0 else 101 - a[i] % 101
    mx = max(mx, a[i] + m[ost2])
print(mx)


# суммы пары кратна 17 и расстояние между элементами пары меньше k (без очереди)
n = 1000
k = 100
a = [int(x) for x in open('27.txt')]

k17 = [0] * 17
count = 0
for i in range(1, n):
    ost = a[i - k] % 17
    k17[ost] += 1

    if i > k:
        ost = a[i - (k + 1)] % 17
        k17[ost] -= 1

    ost2 = 0 if a[i] % 17 == 0 else 17 - a[i] % 17
    count += k17[ost2]
print(count)


