import sys

f = open(sys.argv[1])
data = f.read().split()

count1 = 0
count2 = 0
for i in range(0, len(data), 3):
    minmax = data[i].split('-')
    minimum = int(minmax[0])
    maximum = int(minmax[1])
    search_char = data[i + 1][0]
    search_string = data[i + 2]
    if minimum <= search_string.count(
            search_char) and maximum >= search_string.count(search_char):
        count1 += 1
    if (search_string[minimum - 1] == search_char) ^ (search_string[maximum - 1]
                                                      == search_char):
        count2 += 1

print(f'Part 1: {count1}')
print(f'Part 2: {count2}')
