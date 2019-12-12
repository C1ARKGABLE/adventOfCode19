import numpy as np
import math

with open("input.txt", "r") as file:
    parts = [list(line.strip()) for line in file.readlines()]
    grid = np.array(parts) == "#"

# print(grid)

in_view = {}

rows = grid.shape[0]
cols = grid.shape[1]


it = np.nditer(grid, flags=["f_index", "multi_index"])


def count_in_view(grid, center, rows, cols):
    ratios = set()
    for i in range(0, rows):
        for j in range(0, cols):
            if grid[i, j] and (i, j) != center:
                dx, dy = i - center[0], j - center[1]
                g = abs(math.gcd(dx, dy))
                reduce = (dx // g, dy // g)
                ratios.add(reduce)

    return ratios


while not it.finished:
    if it[0]:
        center = it.multi_index
        inFOV = count_in_view(grid, center, rows, cols)

        in_view[it.index] = {"loc":center,"len": len(inFOV), "ast": inFOV}

    else:
        pass

    it.iternext()

# print(in_view)

# Small
"""
.7..7
.....
67775
....7
...87
"""
station = max(in_view, key=(lambda key: in_view[key]["len"]))
print(f"Part 1: {in_view[station]['len']}")


destroyed = [(math.atan2(dy, dx), (dx, dy)) for dx, dy in in_view[station]["ast"]]
destroyed.sort(reverse=True)



x,y = in_view[station]["loc"] + destroyed[199][1]

while not grid[x,y]:
    x, y = x + dx, y + dy

print(f"Part 2: {y*100+x}")

