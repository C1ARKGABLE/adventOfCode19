import sys
import math


orbit_dict = {orbiter: target for (target, orbiter) in [line.strip().split(")") for line in open("orbit.csv")]}

def get_distance_to(orbiter, to):
    if orbiter != to:
        return get_distance_to(orbit_dict[orbiter], to) + 1
    else:
        return 0

def get_orbits(orbiter, to):
    while orbiter != to:
        orbiter = orbit_dict[orbiter]
        yield orbiter




print(sum(get_distance_to(orbiter, 'COM') for orbiter in orbit_dict))



fst_cmn_orb = next(orbit for orbit in get_orbits('YOU', 'COM') if orbit in get_orbits('SAN', 'COM'))

print(len(list(get_orbits('YOU', fst_cmn_orb))) + len(list(get_orbits('SAN', fst_cmn_orb))) - 2) #part 2
