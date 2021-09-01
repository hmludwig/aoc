import sys

f = open(sys.argv[1])
cups1 = list(map(int, list(f.read().strip())))
cups2 = cups1.copy()

for i in range(100):
    current_cup = cups1[0]
    pick_up = cups1[1:4]
    destination = current_cup - 1 if current_cup - 1 >= min(cups1) else max(
        cups1)
    while destination in pick_up:
        destination -= 1
        if destination < min(cups1):
            destination = max(cups1)
    destination_index = cups1.index(destination)
    tmp = []
    if destination_index == 4:
        tmp.append(destination)
        tmp += pick_up
        tmp += cups1[5:]
        tmp.append(current_cup)
        cups1 = tmp
    else:
        tmp += cups1[4:destination_index + 1]
        tmp += pick_up
        tmp += cups1[destination_index + 1:]
        tmp.append(current_cup)
        cups1 = tmp

solution1 = ''
index_one = cups1.index(1)
solution1 = solution1.join(
    list(map(str, cups1[index_one + 1:] + cups1[:index_one])))

print(f'Solution 1: {solution1}')
