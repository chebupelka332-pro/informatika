"""a = [int(x) for x in open('17_2013.txt')]
ans = []
for i in range(len(a)):
    if (a[i] % 10 == 2 or a[i] % 10 == 7) and a[i] % 3 == 0 and a[i] % 11 == 0:
        ans.append(a[i])
print(len(ans), min(ans))"""


"""a = [int(x) for x in open('17_2016.txt')]
ans = []
for i in range(len(a)):
    if a[i] % 13 == 7 and a[i] % 7 != 0 and a[i] % 11 != 0:
        ans.append(a[i])
print(max(ans) - min(ans), len(ans))"""


"""a = [int(x) for x in open('17_2017.txt')]
ans = []
for i in range(len(a)):
    if a[i] % 16 == 11 and a[i] % 7 == 0 and a[i] % 6 != 0 and a[i] % 13 != 0 and a[i] % 19 != 0:
        ans.append(a[i])
print(sum(ans), len(ans))"""


"""a = [int(x) for x in open('17_1993.txt')]
ans = []
for i in range(len(a) - 1):
    if (a[i] + a[i + 1]) % 3 == 0 and (a[i] + a[i + 1]) % 6 != 0 and abs(a[i] * a[i + 1]) % 10 == 8:
        ans.append(a[i] + a[i + 1])
print(len(ans), max(ans))"""


"""a = [int(x) for x in open('17_2402.txt')]
ans = []
for i in range(len(a) - 2):
    if (abs(a[i]) % 3 == 2) + (abs(a[i + 1]) % 3 == 2) + (abs(a[i + 2]) % 3 == 2) >= 1:
        ans.append(min(a[i], a[i + 1], a[i + 2]))
print(len(ans), sum(ans))"""


"""a = [int(x) for x in open('17_2002.txt')]
ans = []
for i in range(len(a) - 3):
    if a[i] > a[i + 1] > a[i + 2] > a[i + 3] and a[i] - a[i + 3] > 1000:
        ans.append(a[i] + a[i + 1] + a[i + 2] + a[i + 3])
print(len(ans), min(ans))"""


"""a = [int(x) for x in open('17_2310.txt')]
ans1 = []
ans2 = []

for i in range(len(a)):
    if a[i] % 11 == 0:
        ans1.append(a[i])
    if a[i] % 17 == 0:
        ans2.append(a[i])

if len(ans1) > len(ans2):
    print(len(ans1), min(ans1))
else:
    print(len(ans2), max(ans2))"""


a = [int(x) for x in open('17_2399.txt')]
m = sum([int(i) for x in a if x % 35 == 0 for i in str(x)])
ans = []

for i in range(len(a) - 1):
    if (a[i] > m and a[i + 1] <= m and hex(a[i + 1])[-2:] == 'ef') or \
            (a[i + 1] > m and a[i] <= m and hex(a[i])[-2:] == 'ef'):
        ans.append(a[i] + a[i + 1])
print(len(ans), min(ans))
