from itertools import product, permutations

count = 1
x = [''.join(z) for z in product('аимря', repeat=4)]
for elem in x:
    print(count, elem)
    count += 1
