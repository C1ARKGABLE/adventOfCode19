
# This recursively solves the problem for day 1, part 2 
# using Python 3.8's walrus operator.

def fuel_cost(load_mass):
    '''
    Calculates the mass of fuel needed to lift a given load, including fuel mass to lift the calculated fuel mass.
    '''
    if (fuel_mass := (load_mass//3)-2) > 0:
        return fuel_mass + fuel_cost(fuel_mass)
    else:
        return 0
        

total_fuel_mass = 0
for load_mass in open("reqs.csv"):
    # Sum the fuel costs for each load mass to get the total fuel mass
    total_fuel_mass += fuel_cost(int(load_mass))
    
print(total_fuel_mass)
