"""f = open('26.txt')  # таймлайн

k = int(f.readline())
n = int(f.readline())
a = []
for i in range(n):
    start, end = map(int, f.readline().split())
a.sort()

# Время окончания хранения багажа в ячейках
camera = [0] * k
count = last = 0

for i in range(n):
    start, end = a[i]
    for j in range(k):
        if camera[j] < start:
            camera[j] = end
            count += 1
            last = j + 1
            break

print(count, last)"""


"""f = open('26.txt')  # таймлайн, но приходится ждать своей очереди
M, N = map(int, f.readline().split())
a = []
for i in range(N):
    start, r = map(int, f.readline().split())
    a.append([start, start + r, r])
    
a.sort(key=lambda x: x[0])

bank = [0] * M
bankc = [0] * M
last = 0
for i in range(N):
    start, end, r = a[i]
    for j in range(M):
        if bank[j] <= start:
            bank[j] = end
            if bank[j] <= 1440:
                bankc[j] += 1
                last = bank[j]
            break
    else:
        m = min(bank)
        for j in range(M):
            if bank[j] == m:
                if bank[j] <= 1440:
                    bankc[j] += 1
                    last = bank[j]
                bank[j] = bank[j] + r
                break

print(max(bankc), last)"""


"""f = open('26.txt')  # упаковка файлов
s, n = map(int, f.readline().split())
a = [int(x) for x in f]
a.sort()

k = 0
s1 = 0
last = 0

for i in range(n):
    if s1 + a[i] <= s:
        s1 += a[i]
        k += 1
        a[i] = 0
        last = a[i]

for i in range(n):
    if a[i] != 0 and s1 - last + a[i] <= s:
        s1 = s1 - last + a[i]
        last = a[i]
print(k, last)"""


"""f = open('26.txt')  # упоковка файлов короткий вариант
s, n = map(int, f.readline().split())
a = [int(x) for x in f]
a.sort()
b = []

while sum(b) + a[0] <= s:
    b.append(a.pop(0))

for i in range(len(a)):
    if sum(b) - b[-1] + a[i] <= s:
        b[-1] = a[i]
print(len(b), b[-1])"""


"""f = open('26.txt')  # отбор чисел
n, m = map(int, f.readline().split())
a = [int(x) for x in f]
b = []
for i in range(n):
    if 180 <= a[i] <= 200:
        b.append(a[i])
        a[i] = 0

a = sorted([x for x in a if x != 0])

m = m - sum(b)
c = []
while sum(c) + a[0] <= m:
    c.append(a.pop(0))
c.sort(reverse=True)

for i in range(len(c)):
    for j in range(len(a)):
        if a[j] > c[i] and sum(c) - c[i] + a[j] <= m:
            c[i], a[j] = a[j], c[i]
print(len(b) + len(c), sum(b) + sum(c))"""


"""f = open('26.txt')  # быстрый поиск
n = int(f.readline())
a = [int(x) for x in f]
b = set(a)
ans = []
for i in range(n):
    for j in range(i + 1, n):
        if (a[i] + a[j]) % 2 == 0:
            aver = (a[i] + a[j]) // 2
            if aver in b:
                ans.append(aver)

print(len(ans), max(ans))"""


"""from bisect import *


f = open('26.txt')  # бинарный поиск
n = int(f.readline())
a = [int(x) for x in f]
a.sort()
ans = []
for i in range(n):
    for j in range(i + 1, n):
        aver = (a[i] + a[j]) // 2
        count = bisect_left(a, aver)
        if count % 100 == 0:
            ans.append(count)

print(len(ans), max(ans))"""
