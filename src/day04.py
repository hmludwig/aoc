import sys

f = open(sys.argv[1])
data = f.read().split('\n\n')
data = [x.replace('\n', ' ') for x in data]


required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

cnt1 = 0
cnt2 = 0

for d in data:
    passport = d.replace(' ', ':').split(':')
    print(passport)
    if all(i in passport for i in required_fields):
        cnt1 += 1
        


print(f'Part 1: {cnt1}')
print(f'Part 2: {cnt2}')
