"""step = 0
while True:
    a = []
    x = 36 ** 17 - 6 ** step + 71
    while x > 0:
        a = [x % 6] + a
        x = x // 6
    if sum(a) == 61:
        print(step)
        break
    else:
        a = []
        step += 1"""

"""x = 5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875
a = []
while x > 0:
    a = [x % 6] + a
    x = x // 6
print(a.count(5) - a.count(0))"""

"""for x in range(1, 100000):
    if (2 * x + 1) * (x + 3) == 3 * x ** 2 + x + 3:
        print(x)
        break"""

"""count = 0
for n in range(0, 10000):
    a5 = []
    a2 = []
    a16 = []
    x5 = n
    x2 = n
    x16 = n
    while x5 > 0:
        a5 = [x5 % 5] + a5
        x5 = x5 // 5
    while x2 > 0:
        a2 = [x2 % 2] + a2
        x2 = x2 // 2
    while x16 > 0:
        a16 = [x16 % 16] + a16
        x16 = x16 // 16
    if len(a5) <= 4 and len(a2) >= 5 and a16[-1] == 12:
        count += 1
print(count)"""

for x in '0123456789abcdefghijk':
    if (int(f'125{x}9', 21) + int(f'36599', 21)) % 18 == 0:
        print(x, (int(f'125{x}9', 21) + int(f'36599', 21)) // 18)
