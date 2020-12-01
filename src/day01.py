f = open("../input/input01")
data = f.read().split()
data = [int(i) for i in data]

no_solution1 = True
no_solution2 = True

for i in range(len(data)):
    for j in range(len(data)):
        for k in range(len(data)):
            if no_solution1 and data[i] + data[j] == 2020:
                print(f"Solution 1: {data[i] * data[j]}")
                solution1 = False
            if no_solution2 and data[i] + data[j] + data[k] == 2020:
                print(f"Solution 2: {data[i] * data[j] * data[k]}")
                solution2 = False
