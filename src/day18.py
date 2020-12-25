import sys

f = open(sys.argv[1])
data = f.read().strip().splitlines()

sum1 = 0
for d in data:
    sum1 += eval(d)

print(f'Part 1: {sum1}')
