"""s = open('24.txt').readline()
s = s.replace('KEGE', 'KEG EGE')
print(max(len(x) for x in s.split()))
"""


'''s = open('24.txt').readline()
while 'PPP' in s:
    s = s.replace('PPP', 'PP PP')
print(max(len(x) for x in s.split()))
'''


"""s = open('24.txt').readline() # максимальное кличсетво пар ZX или ZY
s = s.replace('ZX', '*').replace('ZY', '*').replace('X', ' ').replace('Y', ' ').replace('Z', ' ')
print(max(len(x) for x in s.split()))"""


"""s = open('24.txt').readline()  # максимальная строка в которой не более трех букв A
s = s.split('A')
ans = []
for i in range(len(s) - 3):
    c = s[i] + 'A' + s[i + 1] + 'A' + s[i + 2] + 'A' + s[i + 3]
    # c = 'A'.join(s[i:i + 4]
    ans.append(c)
print(max(len(x) for x in ans))"""


"""s = open('24.txt').readline()  # мин строка в которой не более трех букв A
s = s.split('A')
ans = []
for i in range(len(s) - 3):
    c = 'A' + s[i + 1] + 'A' + s[i + 2] + 'A'
    # c = 'A' + 'A'.join(s[i + 1:i + 3] + 'A'
    ans.append(c)
print(max(len(x) for x in ans))"""


"""s = open('24.txt').readline()  # динамический метод
m = [0] * len(s)
for i in range(len(s)):
    if s[i] in 'ACDF':
        m[i] = m[i - 1] + 1
print(max(m))"""


"""s = open('24.txt').readline()  # динамический метод (различные соседнии буквы)
m = [1] * len(s)
for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        m[i] = m[i - 1] + 1
print(max(m))"""


"""s = open('24.txt').readline()  # динамический метод (убывание)
m = [1] * len(s)
for i in range(1, len(s)):
    if s[i - 1] >= s[i]:
        m[i] = m[i - 1] + 1
print(max(m))"""


"""s = open('24.txt').readline()  # динамический метод (нет PPP)
m = [2] * len(s)
for i in range(2, len(s)):
    if s[i - 2] + s[i - 1] + s[i] != 'PPP':
        m[i] = m[i - 1] + 1
print(max(m))"""


"""s = open('24.txt').readline()  # динамический метод (кол-во AA CC)
m = [0] * len(s)
for i in range(1, len(s)):
    if s[i - 1] + s[i] == 'ZX' or s[i - 1] + s[i] == 'ZY':
        m[i] = m[i - 2] + 1
print(max(m))"""


"""s = open('24.txt').readline()  # метод двух указателей (максимум)
l = 0
m = 0
k = 0
for r in range(len(s)):
    if s[r] == '.': k += 1
    while k > 1:
        if s[l] == '.': k -= 1
        l += 1
    m = max(m, r - l + 1)
print(m)"""


"""s = open('24.txt').readline()  # метод двух указателей (минимум)
l = 0
m = 1000000
kz = 0
for r in range(len(s)):
    if s[r] == 'Z': kz += 1
    while kz >= 120:
        if s[l] == 'Z': kz -= 1
        l += 1
        if kz == 120: m = min(m, r - l + 1)
print(m)"""


"""s = open('24_13715.txt').readline().strip()  # метод двух указателей (пары)
l = 0
m = 0
k = 0

for r in range(1, len(s)):
    if s[r - 1] + s[r] == 'AB': k += 1
    while k > 50:
        if s[l] + s[l + 1] == 'AB': k -= 1
        l += 1
    if k == 50:
        m = max(m, r - l + 1)
print(m)
"""

"""s = open('24_12476.txt').readline().strip()
l = 0
m = 0
k = 0

for r in range(1, len(s)):
    if r >= 3 and (s[r-2] + s[r-1] + s[r] == 'ORO' or s[r-2] + s[r-1] + s[r] == 'ROR'):
        l = r - 1
        k = 0
    if s[r-1] + s[r] == 'RO': k += 1
    while k > 21:
        if s[l] + s[l + 1] == 'RO': k -= 1
        l += 1
    if k == 21:
        m = max(m, r - l + 1)
print(m)"""


"""s = open('24_279.txt').readline().strip()

while 'JBOSSJBOSSJ' in s: s = s.replace('JBOSSJBOSSJ', 'JBOSSJ JBOSSJ')
print(s.count('BOSS') - s.count('JBOSS') - s.count('BOSSJ') + s.count('JBOSSJ'))"""


s = open('24_2509.txt').readline().strip()  # частота встреч
d = {x: s.count(x) for x in sorted(set(s))}

m = max(d.values())
for elem in d:
    if d[elem] == m:
        print(elem, d[elem])