# количество сочетаний = n(n-1)/m!, где n-количество чисел,
# а m-как их нудно взять(пары, тройки и т.д.)

# количество пар элементов последовательности с четной суммой
f = open('27.txt')
n = int(f.readline())
k_chet = k_nechet = 0
for i in range(n):
    x = int(f.readline())
    if x % 2 == 0:
        k_chet += 1
    else:
        k_nechet += 1

print(k_chet * (k_chet - 1) / 2 + k_nechet * (k_nechet - 1) / 2)


# количество пар элементов, произведение которых кратно 11
f = open('27.txt')
n = int(f.readline())
k11 = k = 0
for i in range(n):
    x = int(f.readline())
    if x % 11 == 0:
        k11 += 1
    else:
        k += 1

print(k11 * (k11 - 1) / 2 + k11 * k)


# количество пар элементов, произведение которых кратно 26
f = open('27.txt')
n = int(f.readline())
k26 = k13 = k2 = 0  # непересекающиеся группы
for i in range(n):
    x = int(f.readline())
    if x % 26 == 0:
        k26 += 1
    elif x % 13 == 0:
        k13 += 1
    elif x % 2 == 0:
        k2 += 1
    else:
        k += 1

print(k26*(k26-1)/ 2 + k26*(n - k26) + k2 * k13)


# количество пар элементов, произведение которых кратно 17 и сумма четна
f = open('27.txt')
n = int(f.readline())
k17_1 = k17_0 = k_1 = k_0 = 0  # непересекающиеся группы
for i in range(n):
    x = int(f.readline())
    if x % 17 == 0 and x % 2 == 0: k17_0 += 1
    if x % 17 == 0 and x % 2 != 0: k17_1 += 1
    if x % 17 != 0 and x % 2 == 0: k_0 += 1
    if x % 17 != 0 and x % 2 != 0: k_1 += 1

print(k17_0*(k17_0-1)/2 + k17_1*(k17_1-1)/2 + k17_0*k_0 + k17_1*k_1)


# количество пар элементов, сумма которых кратна 100
f = open('27.txt')
n = int(f.readline())
k = [0] * 100
for i in range(n):
    x = int(f.readline())
    k[x % 100] += 1

count = k[0] * (k[0] - 1) / 2 + k[50] * (k[50] - 1) / 2
for i in range(1, 49 + 1):
    count += k[i] * k[100 - i]

print(count)


# максимальные\минимальные четные суммы пары
f = open('27.txt')
n = int(f.readline())
a0 = []
a1 = []
for _ in range(n):
    x = int(f.readline())
    if x % 2 == 0:
        a0.append(x)
    else:
        a1.append(x)
a0.sort()
a1.sort()
print(max(a0[-1] + a0[-2], a1[-1] + a1[-2]), min(a0[0] + a0[1], a1[0] + a1[1]))


# максимальные\минимальные произведения кратные 23
f = open('27.txt')
n = int(f.readline())
a23 = []
a = []
for _ in range(n):
    x = int(f.readline())
    if x % 23 == 0:
        a23.append(x)
    else:
        a.append(x)
a.sort()
a23.sort()
print(max(a23[-1] + a[-1], a23[-1] + a23[-2]), min(a23[0] + a[0], a23[0] + a23[1]))


# координатная полскость (треугольники)
f = open('27.txt')
n = int(f.readline())
k1 = k2 = k3 = k4 = 0
for i in range(n):
    x, y = map(int, f.readline().split())
    if x > 0 and y > 0: k1 += 1
    elif x < 0 and y > 0: k2 += 1
    elif x < 0 and y < 0: k3 += 1
    elif x > 0 and y < 0: k4 += 1
print(k2 * (k2 - 1) // 2 * k1 + k2 * k1 * (k1 - 1) // 2 +
      k3 * k4 * (k4 - 1) // 2 + k4 * k3 * (k3 - 1) // 2)
