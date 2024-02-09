"""for n in range(1000):
    a = str(bin(n))[2:]
    a = a + a[-1]
    for _ in range(2):
        if a.count('1') % 2 == 0:
            a += '0'
        else:
            a += '1'
    a = int(a, 2)
    if a > 90:
        print(n, a)"""


"""for n in range(200):
    a = bin(n)[2:].zfill(8)
    a = a.replace('1', '2').replace('0', '1').replace('2', '0')
    a = int(a, 2) + 1
    print(n, a)"""


"""def cc(x):
    a = []
    while x > 0:
        a = [str(x % 3)] + a
        x //= 3
    return ''.join(a)


for n in range(100):
    r = cc(n)
    r += str(n % 3)
    print(n, int(r, 3))"""

