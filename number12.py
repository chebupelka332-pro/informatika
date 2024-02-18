"""k = 0
for i in range(1, 36):
    s = '1' * i
    while '25' in s:
        s = s.replace('25', '9', 1)
        s = s.replace('333', '1', 1)
    if s == '131':
        k += 1
print(k)"""

"""s = '1' * 50
while '111' in s:
    s = s.replace('111', '33', 1)
    s = s.replace('333', '1', 1)
print(s)"""

"""s = '>' + '1' * 10 + '2' * 20 + '3' * 30
while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '2>', 1)
    if '>3' in s:
        s = s.replace('>3', '1>', 1)
print(sum(int(x) for x in s[:-1]))"""

"""for i in range(81, 100):
    s = '1' * i
    k = len(s)
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('2222', '1', 1)
    print(s, k)"""

s = '03'
while '01' in s or '02' in s or '03' in s:
    s = s.replace('01', '2302', 1)
    s = s.replace('02', '10', 1)
    s = s.replace('03', '201', 1)
print(s)
