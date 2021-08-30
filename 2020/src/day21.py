import sys
from collections import defaultdict


f = open(sys.argv[1])
data = f.read().strip().splitlines()
data = [x.split('(contains ') for x in data]
data = [(sorted(x.split()), y.replace(')','').replace(',','').split()) for x,y in data]

ingredients = defaultdict(lambda: 0)
for _, y in data:
    for x in y:
        ingredients[x] += 1

ingredients = sorted(ingredients.items(), key=lambda k_v: k_v[1], reverse=True)

dangerous_ingredients = []

for key, value in ingredients:
    tmp = []
    for x, y in data:
        if key in y:
            tmp.append(x)
    common = list(set.intersection(*map(set, tmp)))
    if common:
        dangerous_ingredients.append((common[0], key))
    for x, y in data:
        if common:
            if common[0] in x:
                x.remove(common[0])

solution1 = 0
for x, y in data:
    solution1 += len(x)

dangerous_ingredients =  sorted(dangerous_ingredients, key=lambda x: x[1])

solution2 = ''
for x,_ in dangerous_ingredients:
    solution2 += x + ','

print(f'Solution 1: {solution1}')
print(f'Solution 2: {solution2[:-1]}')
