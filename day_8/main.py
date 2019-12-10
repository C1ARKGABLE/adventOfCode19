import numpy as np
from PIL import Image

with open("input.txt", "r") as input_file:
    INPUT_STRING = input_file.read().strip()

n = 6
m = 25


def part1():
    indices = list(range(0, len(INPUT_STRING), n * m))
    parts = [list(INPUT_STRING[i:j]) for i, j in zip(indices, indices[1:] + [None])]

    a = np.array(parts, dtype=int)

    minZeros = a[np.argmin(np.sum(a == 0, axis=1))]

    unique, counts = np.unique(minZeros, return_counts=True)
    counts_dict = dict(zip(unique, counts))

    print(counts_dict[1] * counts_dict[2])


indices = list(range(0, len(INPUT_STRING), n * m))
parts = [
    np.reshape(np.array(list(INPUT_STRING[i:j]), dtype=int), (n, m))
    for i, j in zip(indices, indices[1:] + [None])
]

img = np.zeros((n, m))

for part in parts[::-1]:
    img = np.logical_or(np.logical_and(img, (part == 2)), (part < 1))

final = Image.fromarray(255 * img)


final.show()

