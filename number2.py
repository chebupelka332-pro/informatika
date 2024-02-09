from itertools import *


def f(x, y, z, w):
    return (x != z) <= ((x or w) == y)


for a in product([0, 1], repeat=5):
    table = [(0, a[0], 0, a[1]), (a[2], a[3], 0, 0), (a[4], 0, 0, 0)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(p)

"""table = [(1, 0, 0, 0), (1, 0, 1, 0), (1, 0, 1, 1), (1, 1, 0, 0)]
for p in permutations('abcd'):
    if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1, 1]:
        print(p)"""


