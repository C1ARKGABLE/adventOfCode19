from pprint import pprint
import math

raw_lines = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL""".split("\n")
# with in_file as open("input.txt"):
#     raw_lines = in_file.readlines()

recipe = {}
for line in raw_lines:
    print(line)
    reactants, product = line.split("=>")    
    reactants = reactants.split(",")
    amt_prod, product = product.strip().split(" ")
    
    final = []

    for reactant in reactants:
        amt_react,reactant = reactant.strip().split(" ")
        final.append((reactant,int(amt_react)int(amt_prod)))

    recipe[product.strip()] = final


def get_dependants(recipe, mult=1,product="FUEL"):
    reactants = recipe[product]
    if reactants[0][0] == "ORE":
        return reactants[0][1]*mult
    else:
        return sum(get_dependants(recipe,mult=reactant[1],product=reactant[0]) for reactant in reactants)*mult



pprint(recipe)
print(get_dependants(recipe))
