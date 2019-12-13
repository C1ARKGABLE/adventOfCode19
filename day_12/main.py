import numpy as np
from datetime import datetime
import copy
from math import gcd


def lcm(a, b):
    return (a * b) // gcd(a, b)


pos = []
for line in open("input.txt", "r").readlines():
    line = line.strip()[1:-1]
    vals = line.split(", ")
    vals = [int(v[2:]) for v in vals]
    pos.append(vals)


class Moon:
    def __init__(self, name, pos):
        self.name = name
        self.pos = np.array(pos, dtype=int)
        self.vel = np.zeros((3), dtype=int)

    def get_x(self):
        return self.pos[0]

    def get_y(self):
        return self.pos[1]

    def get_z(self):
        return self.pos[2]

    def move(self):
        self.pos += self.vel

    def gravity(self, other):
        # print(other.pos)

        # self 3 other 5
        # self +1 other -1 because 3 < 5

        diff = other.pos - self.pos  # 2
        normal = 1 * (diff > 0) - (diff < 0)

        # print(normal)

        self.vel += normal
        other.vel -= normal

    def energy(self):
        return sum(abs(self.pos)) * sum(abs(self.vel))


class System:
    def __init__(self, moons):
        self.moons = moons

    def summary(self):
        return [f"{m.name} {m.pos = }, {m.vel = }" for m in self.moons]

    def get_coords(self, axis):
        if axis == "x":
            return sum(m.get_x() * 100 ^ i for i, m in enumerate(self.moons))
        elif axis == "y":
            return sum(m.get_y() * 100 ^ i for i, m in enumerate(self.moons))
        elif axis == "z":
            return sum(m.get_z() * 100 ^ i for i, m in enumerate(self.moons))
        else:
            return None

    def energy(self):
        return sum(m.energy() for m in self.moons)

    def step(self):
        temp = self.moons.copy()

        for moon in self.moons:
            temp.remove(moon)
            for moon2 in temp:
                moon.gravity(moon2)

        [m.move() for m in self.moons]
        [print(self.get_coords(i)) for i in ["x","y","z"]]


"""
<x=19, y=-10, z=7>
<x=1, y=2, z=-3>
<x=14, y=-4, z=1>
<x=8, y=7, z=-6>
"""

# print(vels)
planets = ["Io", "Europa", "Ganymede", "Callisto"]

moons = [Moon(planets[i], p) for i, p in enumerate(pos)]

system = System(moons)

# for i in range(1000):
#     print("="*30)
#     print(f"step {i}")
#     system.step()
#     system.summary()

# print(system.energy()) # 6227


# start_state = copy.deepcopy(system)

xs = [system.get_coords("x")]
ys = [system.get_coords("y")]
zs = [system.get_coords("z")]

x_done, y_done, z_done = False, False, False
count = 0

print(xs, ys, zs)
while not (x_done and y_done and z_done):
    # if count % 10000 == 0:
    #     print(count)
    #     print(x_done,y_done,z_done)
    system.step()
    if (x := system.get_coords("x")) in xs: 
        x_done = True
        x_count = count
    if (y := system.get_coords("y")) in ys:
        y_done = True
        y_count = count
    if (z := system.get_coords("z")) in zs:
        z_done = True
        z_count = count

    xs.append(x)
    ys.append(y)
    zs.append(z)

    count += 1

print(xs, ys, zs)
print(x_count, y_count, z_count)
print(lcm(x_count, lcm(y_count, z_count)))


# print(abs(np.array([1,-2,10,-100])) + np.array([2,3,10,2]))
