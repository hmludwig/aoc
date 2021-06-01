import sys
from collections import defaultdict
import numpy as np

f = open(sys.argv[1])
data = f.read().strip().split('\n\n')

tiles = {}
for d in data:
    d = d.splitlines()
    tile_id = d[0].split(' ')
    tile_id = int(tile_id[1].strip(':'))

    tmp = []
    for i in range(1, len(d)):
        tmp.append(list(d[i]))
    tiles[tile_id] = np.array(tmp)

def rotations(tile):
    for _ in range(2):
        for _ in range(4):
            yield tile
            tile = np.rot90(tile)
        tile = np.flip(tile, 0)

tiles_degree = defaultdict(lambda: 0)
for key1 in tiles:
    for rotation1 in rotations(tiles[key1]):
        for key2 in tiles:
            if key1 != key2:
                for rotation2 in rotations(tiles[key2]):
                    if np.all(rotation1[0, :] == rotation2[0, :]):
                        tiles_degree[key1] += 1
                        break
                    if np.all(rotation1[-1, :] == rotation2[-1, :]):
                        tiles_degree[key1] += 1
                        break
                    if np.all(rotation1[:, 0] == rotation2[:, 0]):
                        tiles_degree[key1] += 1
                        break
                    if np.all(rotation1[:, -1] == rotation2[:, -1]):
                        tiles_degree[key1] += 1
                        break
lower = min(list(tiles_degree.values()))
result1 = 1
for key in tiles_degree:
    if tiles_degree[key] == lower:
        result1 *= key

print(f'Part1: {result1}')
