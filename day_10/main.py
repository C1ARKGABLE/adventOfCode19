import numpy as np

with open("small.txt","r") as file:
    parts = [list(line.strip()) for line in file.readlines()]
    grid = np.array(parts)







# Small
"""
.7..7
.....
67775
....7
...87
"""

print(grid)


