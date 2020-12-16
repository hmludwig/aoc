import sys

f = open(sys.argv[1])
data = f.read().strip().splitlines()
data = [d for d in data if d.strip() != '']

rules = dict() 
rules_section = True
my_ticket = None
tickets = list()

for i, d in enumerate(data):
    if d == 'your ticket:':
        rules_section = False
        my_ticket = [int(x) for x in data[i+1].split(',')]
    elif d == 'nearby tickets:':
        for k in range(i+1, len(data)):
            tickets.append([int(x) for x in data[k].split(',')])
        break
    elif rules_section:
        tmp = d.split(': ')
        rule_name = tmp[0]
        rule_range = [x.split('-') for x in tmp[1].split(' or ')]
        rules[rule_name] = [(int(x[0]), int(x[1])) for x in rule_range]


