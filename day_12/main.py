import numpy as np

pos = []
for line in open("input.txt", "r").readlines():
    line = line.strip()[1:-1]
    vals = line.split(", ")
    vals = [int(v[2:]) for v in vals]
    pos.append(vals)


class Moon:
    def __init__(self, name, pos):
        self.name = name
        self.pos = np.array(pos)
        self.vel = np.zeros((3))

    def move(self):
        self.pos += self.vel

    def gravity(self, other):

        diff =  other.pos - self.pos
        normal = 1 * (diff > 0) - (diff < 0)

        self.vel += normal
        #other.vel -= normal

    def energy(self):
        return sum(abs(self.pos)) * sum(abs(self.vel))

class System:

    def __init__(self,moons):
        self.moons = moons
    def energy(self):
        return sum(m.energy() for m in self.moons)
    def step(self):
        temp = self.moons.copy()

        for moon in temp:
            for moon2 in self.moons:
                if not moon == moon2:
                    moon.gravity(moon2)



"""
<x=19, y=-10, z=7>
<x=1, y=2, z=-3>
<x=14, y=-4, z=1>
<x=8, y=7, z=-6>
"""

# print(vels)
planets = ["Io", "Europa", "Ganymede", "Callisto"]

motion = {}

moons = [Moon(planets[i], p) for i, p in enumerate(pos)]

system = System(moons)

for i in range(1000):
    system.step()

print(system.energy())

# def gravity(motion, pts):

#     for source in pts:
#         pts.remove(source)
#         for dest in pts:

#             diff = motion[dest]["pos"] - motion[source]["pos"]

#             # Sprint(1*(diff > 0) - (diff < 0))

#             motion[dest]["vel"] -= 1 * (diff > 0) - (diff < 0)
#             motion[source]["vel"] += 1 * (diff > 0) - (diff < 0)

#     return motion


# def move(motion, planets):
#     for planet in planets:
#         motion[planet]["pos"] += motion[planet]["vel"]

#     return motion


# def energy(motion, planets):
#     total = 0
#     for planet in planets:
#         total += sum(abs(motion[planet]["pos"])) * sum(abs(motion[planet]["vel"]))
#     return total


# for i in range(1000):
#     motion = gravity(motion, planets.copy())
#     motion = move(motion, planets)

# print(energy(motion, planets))
# # print(motion)


# print(np.array([3, 4, 5]) - np.array([1, 2, 3]))

