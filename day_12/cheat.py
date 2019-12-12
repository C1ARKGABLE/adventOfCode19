"""
1. Simulate every moon in a time step (e.g on iteration of a loop)
2. Update VELOCITY by applying GRAVITY
3. Update POSITION by applying VELOCITY
"""

from copy import deepcopy


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a*b)//gcd(a, b)


def tick():
    """
    A single tick amounts to a new calculation of positions and velocities for all the moons.
    """
    for i in range(len(Mpos)):
        for j in range(len(Mpos)):
            for p in Mpos[i]:
                if Mpos[i][p] < Mpos[j][p]:
                    Mvel[i][p] += 1
                elif Mpos[i][p] > Mpos[j][p]:
                    Mvel[i][p] -= 1

    # Update the x,y,z position of each moon based on its x,y,z velocity.
    for i in range(len(Mpos)):
        for k in Mpos[i]:
            Mpos[i][k] += Mvel[i][k]


Mpos = []
Mvel = []

for line in open("input.txt", "r").readlines():
    line = line.strip()
    line = line[1:-1]
    line = line.split(", ")
    moon = {}
    for e in line:
        k, v = e.split("=")
        moon[k] = int(v)
    Mpos.append(moon)
    Mvel.append({'x': 0, 'y': 0, 'z': 0})

# Make copies of the stating positions and velocities (for Part 2)
start_Mpos = deepcopy(Mpos)
start_Mvel = deepcopy(Mvel)


# For Part 1 we just need to run 1000 ticks and then calculate some stuff. Fairly straightforward once you have a
# feel for what the question is asking.
part_1 = 0
for _ in range(1000):
    tick()

for i in range(len(Mpos)):
    pot = 0  # Potential energy. Sum of absolute values of moon's co-ordinates.
    kin = 0  # Kinetic energy. Sum of absolute values of its velocity coordinates
    for k in Mpos[i]:
        pot += abs(Mpos[i][k])
        kin += abs(Mvel[i][k])
    part_1 += (pot * kin)

print(part_1)